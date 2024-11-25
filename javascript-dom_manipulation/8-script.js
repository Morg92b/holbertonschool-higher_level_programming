window.onload = function () {
    const values = fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    values.then(response => response.json()).then(data => {
        document.getElementById('hello').innerHTML = data.hello;
    });
};