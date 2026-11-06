const box=document.querySelector('#lightbox');
document.querySelectorAll('[data-full]').forEach(button=>button.addEventListener('click',()=>{document.querySelector('#lightbox-image').src=button.dataset.full;document.querySelector('#lightbox-title').textContent=button.dataset.title;box.showModal();}));
document.querySelector('#close-lightbox')?.addEventListener('click',()=>box.close());
box?.addEventListener('click',e=>{if(e.target===box)box.close();});
