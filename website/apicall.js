let table = document.getElementById("table");

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
    create_table(data);
  }) 
  .catch(error => { 
    // Handle any errors here 
    console.error(error); // Example: Logging the error to the console 
  });

function create_table(data) {
  const TABLE_HEADERS = ["Name", "Position", "Ranking", "Commited To"];
  let row = table.insertRow(0);
  // Create header
  for (let i = 0; i < TABLE_HEADERS.length; i++) {
    let th = document.createElement("th");
    th.textContent = TABLE_HEADERS[i];
    row.append(th); 
  }
  


  for (let i = 0; i < 2000; i++) {
    let row = table.insertRow(i + 1);
    let name = row.insertCell(0);
    let position = row.insertCell(1);
    let ranking = row.insertCell(2);
    let college = row.insertCell(3);

    name.textContent = `${data[i].name}`;
    position.textContent = `${data[i].position}`;
    ranking.textContent = `${data[i].ranking}`;
    college.textContent = `${data[i].school}`;
  }
}