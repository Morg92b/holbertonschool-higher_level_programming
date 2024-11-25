const header = document.querySelector('header');
const red_header = document.getElementById('red_header');
red_header.addEventListener('click', function() {
  header.classList.add('red');
});