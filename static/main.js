/*
        main.js is the javscript that is served to the index.html main page of the app.
*/


// server root url
var url = "http://localhost:5000"

// add event listeners:

// eventListener for zipcode form submit
document.getElementById("zipForm").addEventListener("submit", (event)=>{
    // prevent form submit event from "firing" so we stay on page, code will handle
    event.preventDefault();

    // data to send to server
    var payload = {
        zip: event.target.zip.value,
        tags: event.target.tags.value
    }
console.log('POST 2')
    // fetch POST request -- send payload and receive data in callback/promise
    fetch(url + "/receiver", {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)

    }).then((data)=>{
    // callback/promise to receive data from server and update map coords
        
        return data.json()})
        .then((data)=>{
            console.log(data)
            myMap({
                data
                //lat: data.tweets[0].latitude,
               // lng: data.tweets[0].longitude
            })
        })})
    