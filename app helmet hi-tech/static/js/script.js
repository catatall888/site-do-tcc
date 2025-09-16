// Toggle sidebar with accessible attributes
const sidebar = document.getElementById('sidebar');
const hamburger = document.getElementById('hamburger');

function setSidebar(open){
  if(open){
    sidebar.classList.add('open');
    sidebar.setAttribute('aria-hidden','false');
    hamburger.setAttribute('aria-expanded','true');
  } else {
    sidebar.classList.remove('open');
    sidebar.setAttribute('aria-hidden','true');
    hamburger.setAttribute('aria-expanded','false');
  }
}

hamburger.addEventListener('click', () => {
  setSidebar(!sidebar.classList.contains('open'));
});

// close with Escape
document.addEventListener('keydown', (e) => {
  if(e.key === 'Escape') setSidebar(false);
});

// close sidebar when clicking any link inside it (nice UX for mobile)
sidebar.addEventListener('click', (e) => {
  if(e.target.tagName === 'A') setSidebar(false);
});
