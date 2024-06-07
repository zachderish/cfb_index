const select = document.getElementById("rec-yrs");
const table = document.createElement("table");

const FIRST_YEAR = 2000;
const LAST_YEAR = 2025;
for (let i = FIRST_YEAR; i < LAST_YEAR; i++) {
  let option = document.createElement("option");
  option.text = `${i}`;
  select.add(option);
}

select.addEventListener("change", function() {
  console.log(select.value)
  fetch(`http://ec2-54-89-177-134.compute-1.amazonaws.com/recruiting/year=${select.value}`) 
  .then(response => { 
    if (response.ok) { 
        return response.json(); // Parse the response data as JSON 
    } else { 
        throw new Error('API request failed'); 
    } 
  }) 
  .then(data => { 
    // Process the response data here 
    create_player_table(data);
  }) 
  .catch(error => { 
    // Handle any errors here 
    console.error(error); // Example: Logging the error to the console 
  });
});

function create_player_table(data) {
  console.log(data[0])
  const TABLE_HEADERS = ["Name", "Position","Height", "Weight", "Stars", "Ranking", "Committed To"];

  table.innerHTML = "";
  document.body.appendChild(table);

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
    college.textContent = `${data[i].committedTo}`;
  }
}