var express = require('express')
var app = express()
var bodyParser = require('body-parser')

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}))


app.use(express.static('EarthxHack2018'));

app.post('/receiver', (req,res)=>{
    var zipcode = req.body.zip
    var category = req.body.hashtag
    console.log(req.body)
    console.log("zip: " + zipcode + ";  category: " + category)

    dummy = [{
        tweet: "People are all trashy or they are not",
        lat: 37.2343,
        long: -115.8067
    }]

    res.send(JSON.stringify(dummy))
})


var port = process.argv[2] || 5000

app.listen(port);
console.log("Server on port " + port)