/*
        main.js is the javscript that is served to the index.html main page of the app.
*/

var url = "http://localhost:5000"

var zipForm = document.getElementById("zipForm");
console.log(zipForm)
zipForm.addEventListener("submit", (event)=>{
    event.preventDefault();

    console.log(event.target.zip.value);

    var payload = {
        zip: event.target.zip.value
    }
    console.log(payload)

    fetch(url + "/receiver", {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    }).then((data)=>{
        return data.json()})
        .then((data)=>{
            console.log(data)
            myMap({
                lat: data[0].lat,
                lng: data[0].long
            })
        })})
    