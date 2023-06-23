const gifZone = document.querySelector('#gifZone');

async function getRandomGif(e){
    e.preventDefault();
try{
    const apiKey = 'yQpIWqK2q8y8GLcjsIvH1BhuZVyLVhSm';
    const gifSearch = document.querySelector('#gifSearch');
    const search = gifSearch.value;
    const limit = 25;
    const offset = 0;
    const rating = '';
    const lang = 'en';

    const res = await axios.get('http://api.giphy.com/v1/gifs/search', {
        params: {
            api_key: apiKey,
            q: search,
            limit: limit,
            offset: offset,
            rating: rating,
            lang: lang

        }
    });
    const gifData = res.data.data;
    const randomIndex = Math.floor(Math.random() * gifData.length);
    const randomGifUrl = gifData[randomIndex].images.original.url;
   

    const newGif = document.createElement('IMG');
    newGif.src = randomGifUrl;
    gifZone.append(newGif);

  
    console.log(res.data);
    
   
  

} catch (e){

}
};

const submitBtn = document.querySelector('#submitBtn');
submitBtn.addEventListener('click', getRandomGif);

const removeBtn = document.querySelector('#removeBtn');
removeBtn.addEventListener('click', function(){
    const gifImages = gifZone.querySelectorAll('IMG');

    gifImages.forEach(function (image){
        image.remove()
    });
})