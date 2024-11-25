const additem = document.getElementById('add_item');
const list = document.querySelector('.my_list');
additem.addEventListener('click', function() {
  const listelem = document.createElement('li');
  listelem.textContent = 'Item';
  list.appendChild(listelem);
});