const button = document.getElementById('update_header');
const header = document.querySelector('header'); 
button.addEventListener('click', function() {
  header.innerText = 'New Header!!!';
});