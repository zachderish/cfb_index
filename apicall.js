let textObj = document.getElementById("text");

fetch('http://127.0.0.1:5000/recruiting/year=2024') 
  .then(response => { 
    if (response.ok) { 
        return response.json(); // Parse the response data as JSON 
    } else { 
        throw new Error('API request failed'); 
    } 
  }) 
  .then(data => { 
    // Process the response data here 
    for (let i = 0; i < 100; i++) {
        textObj.textContent += data[i].name; // Example: Logging the data to the console 
    }
  }) 
  .catch(error => { 
    // Handle any errors here 
    console.error(error); // Example: Logging the error to the console 
  });