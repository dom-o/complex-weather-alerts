var html = require('choo/html')
var conditionSelect = require('./conditionSelect.js')


module.exports = function(state, emit) {
	return html`
		<div>
			<form id="create">
				I like to go <input id="activityname" name="activityname" type="text">
				at <input id="lat" name="lat" type="text"> <input id="lng" name="lng" type="text"> 
				when <select>
					${Object.entries(state.fields).map(conditionSelect)}
				</select>					
				<button>more conditions</button>
			</form>
		</div>
	`
}

