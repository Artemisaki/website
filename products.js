const api = "http://127.0.0.1:5000";
window.onload = () => {
    // BEGIN CODE HERE
   //$.ajax({url:"app.py"})
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    console.log("here")
    //xml.open('POST',"/app.py",true);
    var xml = new XMLHttpRequest();
    xml.open('POST',"/app.py",true);
    xml.setRequestHeader("Content-type","application/json");
    dataSend = JSON.stringify({
        'name' : document.getElementById("fname").value ,
        'productionYear' : document.getElementById("fyear").value,
         'price' : document.getElementById("fprice").value,
         'color' : document.getElementById("fcolor").value,
         'size' : document.getElementById("fsize").value
         });
    $.ajax({
        url:'/add-product',
        method: "POST",
        data : dataSend
    })

    xml.unload=function()
    {
        var dataReply = JSON.parse(this.responseText) //αυτό που παίρνουμε
    }
    xml.send(dataSend)
    console.log(dataSend)
    // END CODE HERE
}