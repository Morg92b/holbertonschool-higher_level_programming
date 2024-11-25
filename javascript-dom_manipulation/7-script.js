const titleName = fetch('https://swapi-api.hbtn.io/api/films/?format=json');
titleName.then(response => response.json()).then(data => {
    document.getElementById('list_movies').innerHTML = data.results.map(movie => `<li>${movie.title}</li>`).join('');
});