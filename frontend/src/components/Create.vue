<template>
<div>
  <form>
    I like to go <input id="activityname" name="activityname" type="text">
    at <input id="lat" name="lat" type="text" required> <input id="lon" name="lon" type="text" required>
    when the <CondieFilterContainer/>
    I'm free
      <input type="checkbox" id="anyday" v-model="allSelected"><label for="anyday">Anytime</label>
      <input type="checkbox" id="monday" value="Monday" v-model="days"><label for="monday">Monday</label>
      <input type="checkbox" id="tuesday" value="Tuesday" v-model="days"><label for="tuesday">Tuesday</label>
      <input type="checkbox" id="wednesday" value="Wednesday" v-model="days"><label for="wednesday">Wednesday</label>
      <input type="checkbox" id="thursday" value="Thursday" v-model="days"><label for="thursday">Thursday</label>
      <input type="checkbox" id="friday" value="Friday" v-model="days"><label for="friday">Friday</label>
      <input type="checkbox" id="saturday" value="Saturday" v-model="days"><label for="saturday">Saturday</label>
      <input type="checkbox" id="sunday" value="Sunday" v-model="days"><label for="sunday">Sunday</label>
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
  watch: {
    allSelected: function(val) {
      if(val) {
        this.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      }
    }
  },
  methods: {},
  data () {
    return {
      allSelected: false,
      days: []
    }
  },
  name: 'Create'
}
</script>
