//import axios from 'axios';

document.addEventListener("DOMContentLoaded", ()=>{
axios.get('https://api.thecatapi.com/v1/images/search?size=full')
.then(function (response) {
// handle success
	const imageData = response.data[0];
	const imageUrl = imageData.url;
	const node = document.createElement("img");
	node.src = imageUrl;
	let div_node = document.querySelector("#imgbox");
	div_node.append(node)
})
.catch(function (error) {
// handle error
console.log(error);
})
.finally(function () {
// always executed
});
})
