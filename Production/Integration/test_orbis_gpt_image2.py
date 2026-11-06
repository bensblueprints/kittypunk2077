"""Offline checks: payload, route, image decoding, and credential-free downloads."""
import base64, io, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import orbis_gpt_image2 as client

class ClientTests(unittest.TestCase):
    def test_native_payload(self):
        png = b'\x89PNG\r\n\x1a\nexample'
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(client, 'ROOT', Path(directory)), patch.object(client, 'request', return_value={'data':[{'b64_json':base64.b64encode(png).decode()}]}) as request:
                receipt = client.generate(client.MINIMAL_PROMPT, Path(directory)/'out')
                request.assert_called_once_with('/v1/images/generations', {'model':'gpt-image-2','prompt':client.MINIMAL_PROMPT,'n':1})
                self.assertEqual(Path(receipt['images'][0]['path']).read_bytes(), png)
                self.assertEqual(receipt['status'], 'images_saved')

    def test_url_download_has_no_headers(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(client.urllib.request, 'urlopen', return_value=io.BytesIO(b'GIF89a')) as open_url:
            saved = client.save_images({'data':[{'url':'https://example.com/image'}]}, directory, 'test')
            open_url.assert_called_once_with('https://example.com/image', timeout=120)
            self.assertTrue(saved[0]['path'].endswith('.gif'))

    def test_reject_missing_empty_and_bad_base64(self):
        with tempfile.TemporaryDirectory() as directory:
            for result in ({'data':[]}, {'data':[{}]}, {'data':[{'b64_json':'%%%%'}]}):
                with self.assertRaises(Exception): client.save_images(result, directory, 'test')

    def test_signatures_and_wrong_route(self):
        self.assertEqual(client.extension(b'\xff\xd8\xff123'), 'jpg')
        self.assertEqual(client.extension(b'RIFF1234WEBPtest'), 'webp')
        self.assertEqual(client.extension(b'unknown'), 'bin')
        with patch.object(client, 'request', return_value={'data':[{'id':'other'}]}):
            with self.assertRaises(RuntimeError): client.check()

if __name__ == '__main__': unittest.main()
