var choo = require('choo');
var html = require('choo/html');

var app = choo();

var main = function() {
	return html`<div>complex weather alerts</div>`;
}

app.route('/', main);

app.mount('div');
