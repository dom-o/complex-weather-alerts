<template>
<div>
  <form>
    I like to go <input id="activity" name="activity" v-model="activity" type="text">
    at <input id="lat" name="lat" v-model="latitude" type="text"> <input id="lon" name="lon" v-model="longitude" type="text">
    when the <CondieFilterContainer/>
    I'm free
      <input type="checkbox" id="monday" value="Monday" v-model="checkedDays"><label for="monday">Monday</label>
      <input type="checkbox" id="tuesday" value="Tuesday" v-model="checkedDays"><label for="tuesday">Tuesday</label>
      <input type="checkbox" id="wednesday" value="Wednesday" v-model="checkedDays"><label for="wednesday">Wednesday</label>
      <input type="checkbox" id="thursday" value="Thursday" v-model="checkedDays"><label for="thursday">Thursday</label>
      <input type="checkbox" id="friday" value="Friday" v-model="checkedDays"><label for="friday">Friday</label>
      <input type="checkbox" id="saturday" value="Saturday" v-model="checkedDays"><label for="saturday">Saturday</label>
      <input type="checkbox" id="sunday" value="Sunday" v-model="checkedDays"><label for="sunday">Sunday</label>
    I wanna know about good condies
      <select id="advanceNotice" v-model.number="advanceNotice">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
      </select>
    days in advance
    Reach me at <input type="email" id="email" v-model="email" required>
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
  data () {
    return {
      activity: '',
      latitude: '',
      longitude: '',
      checkedDays: [],
      advanceNotice: '',
      email: ''
    }
  },
  name: 'Create'
}
</script>
