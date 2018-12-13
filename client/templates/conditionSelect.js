var html = require('choo/html')
var datapointSchema = require('../../datapoint.json')

/*
*	get options from schema
*	for every option in schema
*		create option item
*			<option title=DESCRIPTION>NAME</option>
*		label for dropdown = DESCRIPTION, change when option changes
*/

module.exports = function (entry) {
	var description = entry[1].description
	var name = entry[0]
	
	return html`
		<option id="${name}" title="${description}">${name}</option>
	`
}
