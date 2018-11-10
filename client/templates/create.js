var html = require('choo/html')

module.exports = function() {
	return html`
		<div>
			<form id="create">
				I like to go <input id="activityname" name="activityname" type="text">
				at <input id="lat" name="lat" type="text"> <input id="lng" name="lng" type="text"> 
				when <input id="weathercondition" name="weathercondition" type="text">...
			</form>
		</div>
	`
}
