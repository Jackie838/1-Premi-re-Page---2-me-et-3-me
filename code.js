function toto()
{
    fetch("http://127.0.0.1:5000/test/34")
    .then(response => response.json())
    .then(json => titi(json))
    .catch(error => alert("Erreur : " + error));

}

function titi(json)
{
    var contenu = document.querySelector('.intro');
	contenu.innerHTML = json.id;
}
