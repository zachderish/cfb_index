let text = document.getElementById("text");

fetch('http://localhost:5000/recruiting') 
  .then(response => { 
    if (response.ok) { 
      return response.json(); // Parse the response data as JSON 
    } else { 
      throw new Error('API request failed'); 
    } 
  }) 
  .then(data => { 
    // Process the response data here 
    text.innerHTML(data); // Example: Logging the data to the console 
  }) 
  .catch(error => { 
    // Handle any errors here 
    console.error(error); // Example: Logging the error to the console 
  });