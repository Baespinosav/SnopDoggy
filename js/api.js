const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
    
	if (this.readyState === this.DONE) {
        const data = JSON.parse(this.response);
        const HTMLResponse = document.querySelector("#Raza");

        const tpl = data.map((user) => `<li>${user.name}</li>`);
        HTMLResponse.innerHTML = `<ul>${tpl}</ul>`
		console.log(data);
	}
});

xhr.open("GET", "https://razas-de-perros.p.rapidapi.com/TypeOfBreeds");
xhr.setRequestHeader("X-RapidAPI-Host", "razas-de-perros.p.rapidapi.com");
xhr.setRequestHeader("X-RapidAPI-Key", "ae053577b9msh2a876e057ddc8aep12383fjsn3abfecc930ee");



xhr.send(data);

