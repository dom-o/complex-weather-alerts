var choo = require('choo');
var html = require('choo/html');

var main = require('./templates/main.js')
var create = require('./templates/create.js')

var datapointSchema = require('../datapoint.json')


var app = choo()

app.use((state, emitter) => {
	state.fields = datapointSchema.properties
})

app.route('/', main)
app.route('/create', create)

app.mount('div')
