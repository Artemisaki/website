const api = "http://127.0.0.1:5000";
window.onload = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

productFormOnSubmit = () => {
    // BEGIN CODE HERE

    console.log("it works")
    $.ajax({
      type: "POST",
      url: "/add-product",
      data:{"ID":"1400", "name":"Labrini Piiol", "productionYear":"2000", "price":"600", "color":"2", "size":"2"
          }
    })
    // END CODE HERE
}