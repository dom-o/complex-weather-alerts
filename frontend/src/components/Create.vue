<template>
<div>
  <form>
    I like to go <input id="activityname" name="activityname" type="text">
    at <input id="lat" name="lat" type="text"> <input id="lon" name="lon" type="text">
    when the <CondieFilterContainer/>
    I'm free
      <input type="checkbox" id="mondaySelect" name="daysFree"><label for="mondaySelect">Monday</label>
      <input type="checkbox" id="tuesdaySelect" name="daysFree"><label for="tuesdaySelect">Tuesday</label>
      <input type="checkbox" id="wednesdaySelect" name="daysFree"><label for="wednesdaySelect">Wednesday</label>
      <input type="checkbox" id="thursdaySelect" name="daysFree"><label for="thursdaySelect">Thursday</label>
      <input type="checkbox" id="fridaySelect" name="daysFree"><label for="fridaySelect">Friday</label>
      <input type="checkbox" id="saturdaySelect" name="daysFree"><label for="saturdaySelect">Saturday</label>
      <input type="checkbox" id="sundaySelect" name="daysFree"><label for="sundaySelect">Sunday</label>
    I wanna know about good condies
      <select id="advanceNotice">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
      </select>
    days in advance
    Reach me at <input type="email" id="email" required>
    <input type="submit" value="Go">
  </form>
</div>
</template>

<script>
import CondieFilterContainer from './CondieFilterContainer.vue'

export default {
  components: {CondieFilterContainer},
  methods: {
  },
  name: 'Create'
}
</script>
