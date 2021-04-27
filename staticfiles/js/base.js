document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.sidenav');
    let instances = M.Sidenav.init(elems);
    elems = document.querySelectorAll('.dropdown-trigger');
    instances = M.Dropdown.init(elems);
  });