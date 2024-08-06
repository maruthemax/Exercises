console.log("Let's get this party started!");

// document.getElementById('searchForm').addEventListener('submit', async function(event) {
//     event.preventDefault();
//     const searchTerm = document.getElementById('searchTerm').value;
//     const apiKey = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
//     const url = `http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${apiKey}`;

//     try {
//       const response = await axios.get(url);
//       console.log(response.data);
//     } catch (error) {
//       console.error('Error fetching data:', error);
//     }
//   });

//   document.getElementById('searchForm').addEventListener('submit', async function(event) {
//     event.preventDefault();
//     const searchTerm = document.getElementById('searchTerm').value;
//     const apiKey = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
//     const url = `http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${apiKey}`;

//     try {
//       const response = await axios.get(url);
//       const gifs = response.data.data;
//       const gifContainer = document.getElementById('gifContainer');
//       gifs.forEach(gif => {
//         const img = document.createElement('img');
//         img.src = gif.images.fixed_height.url;
//         gifContainer.appendChild(img);
//       });
//     } catch (error) {
//       console.error('Error fetching data:', error);
//     }
//   });

  // document.getElementById('searchForm').addEventListener('submit', async function(event) {
  //   event.preventDefault();
  //   const searchTerm = document.getElementById('searchTerm').value;
  //   const apiKey = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
  //   const url = `http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${apiKey}`;

  //   try {
  //     const response = await axios.get(url);
  //     const gifs = response.data.data;
  //     const gifContainer = document.getElementById('gifContainer');
  //     gifs.forEach(gif => {
  //       const img = document.createElement('img');
  //       img.src = gif.images.fixed_height.url;
  //       gifContainer.appendChild(img);
  //     });
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // });

  // document.getElementById('removeGifs').addEventListener('click', function() {
  //   const gifContainer = document.getElementById('gifContainer');
  //   gifContainer.innerHTML = '';
  // });

  // document.getElementById('searchForm').addEventListener('submit', async function(event) {
  //   event.preventDefault();
  //   const searchTerm = document.getElementById('searchTerm').value.trim();
  //   if (!searchTerm) {
  //     alert('Please enter a search term.');
  //     return;
  //   }
  //   const apiKey = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
  //   const url = `http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${apiKey}`;
  
  //   try {
  //     const response = await axios.get(url);
  //     const gifs = response.data.data;
  //     console.log(gifs); // Log the response data to ensure it's what you expect
  //     const gifContainer = document.getElementById('gifContainer');
  //     gifContainer.innerHTML = ''; // Clear previous GIFs
  
  //     if (gifs.length > 0) {
  //       let $newCol = $("<form>", { class: "col-md-4 col-12 mb-4" });
  //       const img = document.createElement('img');
  //       img.src = gifs[0].images.fixed_height.url; // Display only the first GIF
  //       gifContainer.appendChild(img);
  //     } else {
  //       alert('No GIFs found for this search term.');
  //     }
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // });
  
  // document.getElementById('removeGifs').addEventListener('click', function() {
  //   const gifContainer = document.getElementById('gifContainer');
  //   gifContainer.innerHTML = '';
  // });

  console.log("Let's get this party started!");

const $gifArea = $("#gifContainer");
const $searchInput = $("#searchTerm");

/* use ajax result to add a gif */
function addGif(res) {
  let numResults = res.data.length;
  if (numResults) {
    let randomIdx = Math.floor(Math.random() * numResults);
    let $newCol = $("<div>", { class: "col-md-4 col-12 mb-4" });
    let $newGif = $("<img>", {
      src: res.data[randomIdx].images.original.url,
      class: "w-100"
    });
    $newCol.append($newGif);
    $gifArea.append($newCol);
  }
}

/* handle form submission: clear search box & make ajax call */
$("#searchForm").on("submit", async function(evt) {
  evt.preventDefault();

  let searchTerm = $searchInput.val().trim();
  if (!searchTerm) {
    alert('Please enter a search term.');
    return;
  }
  $searchInput.val("");

  try {
    const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
      params: {
        q: searchTerm,
        api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
      }
    });
    addGif(response.data);
  } catch (error) {
    console.error('Error fetching data:', error);
    alert('Failed to fetch GIFs. Please try again later.');
  }
});

/* remove gif */
$("#removeGifs").on("click", function() {
  $gifArea.empty();
});
