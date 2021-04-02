import './../scss/main.scss';
import 'bootstrap/dist/js/bootstrap.bundle';

document.querySelector('#menu-toggle').addEventListener('click', (e) => {
  e.preventDefault();
  document.querySelector('#wrapper').classList.toggle('toggled');
});
