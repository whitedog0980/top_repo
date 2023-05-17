import axios from axios.js

axios.get("https://api.thecatapi.com/v1/images/search?size=full")
  .then(response => {
    const imageData = response.data[0];
    const imageUrl = imageData.url;
    console.log(imageUrl);
  })
  .catch(error => {
    console.error(error);
  });
