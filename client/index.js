var choo = require('choo');
var html = require('choo/html');

var main = require('./templates/main.js')
var create = require('./templates/create.js')

var app = choo()

app.route('/', main)
app.route('/create', create)

app.mount('div')
