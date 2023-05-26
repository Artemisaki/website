const api = "http://127.0.0.1:5000";
window.onload = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    console.log("here")
    var xml = new XMLHttpRequest();
    xml.open('POST',"/app.py",true);
    xml.setRequestHeader("Content-type","application/json");
    var dataReply = this.responseText //αυτό που παίρνουμε
    xml.send(productFormOnSubmit)
    dataSend = JSON.stringify({ // αυτο που στελνουμε
    'name' : document.getElementById("fname").value ,
    'productionYear' : document.getElementById("fyear").value,
    'price' : document.getElementById("fprice").value,
    'color' : document.getElementById("fcolor").value,
    'size' : document.getElementById("fsize").value
    });
    console.log(dataSend)
    // END CODE HERE
}