const charName = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
charName.then(response => response.json()).then(data => {
  document.getElementById('character').innerHTML = data.name;
});