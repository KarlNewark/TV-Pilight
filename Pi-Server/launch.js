var Blinkt = require('node-blinkt'),
	leds = new Blinkt();

leds.setup();

var express = require('express')
var app = express()
var bodyParser = require('body-parser');
//app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/', function (req, res) {
  res.send('TV-Light')
  leds.setAllPixels(req.body.red, req.body.green, req.body.blue, 1.0)
  leds.sendUpdate();
  leds.sendUpdate();
})

app.listen(3000)

