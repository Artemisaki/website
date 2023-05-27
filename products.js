const api = "http://127.0.0.1:5000";
window.onload = () => {
    // BEGIN CODE HERE
        document.querySelector('.save-button').addEventListener('click',productFormOnSubmit);
        document.querySelector('.search-button').addEventListener('click', searchButtonOnClick);
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    console.log("and here")
    let searchInput = document.querySelector('#inputId').value;



     fetch(`${api}/search?name=${searchInput}`)
        .then(response => response.json())
        .then(data => {
            let resultsTable = document.querySelector('.Results-table');
            resultsTable.innerHTML = `
                <thead>
                    <tr>
                      <th class="text_input"> ID</th>
                      <th class="text_input">Name</th>
                      <th class="text_input">Production Year</th>
                      <th class="text_input">Price</th>
                      <th class="text_input">Color</th>
                      <th class="text_input">Size</th>
                    </tr>
                </thead>
              `;
            data.forEach(product => {
                resultsTable.innerHTML += `
                <tr>
                  <td>${product.id}</td>
                  <td>${product.Name}</td>
                  <td>${product.ProductionYear}</td>
                  <td>${product.Price}</td>
                  <td>${product.Color}</td>
                  <td>${product.Size}</td>
                </tr>`;
            });
        });
    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    alert("ok")
     event.preventDefault();
        let dataSend = {
            name: document.getElementById("fname").value ,
            productionYear: parseInt(document.getElementById("fyear").value),
            price: parseFloat(document.getElementById("fprice").value),
            color: parseInt(document.getElementById("fcolor").value),
            size: parseInt(document.getElementById("fsize").value)
             };
    console.log(dataSend)
     fetch(`${api}/add-product`,{
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataSend)
    })
    .then(response => response.json())
    .then(data => {py
        alert(data.message);

        inputs.forEach(input => input.value = '');
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // END CODE HERE
}