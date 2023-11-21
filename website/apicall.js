let table = document.getElementById("table");
let year = document.getElementById("year")
let yearString = year.innerText.split(" ")[0]
console.log(yearString)

fetch(`http://127.0.0.1:5000/recruiting/year=${yearString}`) 
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
  const TABLE_HEADERS = ["Name", "Position","Height", "Weight", "Stars", "Ranking", "Commited To"];
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
    let height = row.insertCell(2);
    let weight = row.insertCell(3);
    let stars = row.insertCell(4);
    let ranking = row.insertCell(5);
    let college = row.insertCell(6);

    name.textContent = `${data[i].name}`;
    position.textContent = `${data[i].position}`; 
    height.textContent = `${data[i].height}`;
    weight.textContent = `${data[i].weight}`;
    stars.textContent = `${data[i].stars}`;
    ranking.textContent = `${data[i].ranking}`;
    college.textContent = `${data[i].school}`;
  }
}