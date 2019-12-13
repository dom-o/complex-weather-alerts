<template>
<div>
  <form @submit.prevent="processForm">
    I like to go <input v-model="activityName" type="text">
    at <input v-model.number="location.latitude" type="number" step="any" min="-90" max="90" required> <input v-model.number="location.longitude" type="number" step="any" min="-180" max="180" required>
    when the <template v-for="filter in filters">
      <select :key="filter.id+'selectedOption'" v-model="filter.selectedOption" >
        <option v-for="(option, optionName) in filterOptions" :key="optionName" :value="option">
          {{ option.title }}
        </option>
      </select>
      {{ filter.selectedOption.description }}
      is
      <template v-if="filter.selectedOption.enum">
        <select :key="filter.id+'enum'" v-model="filter.num">
          <option v-for="(item,index) in filter.selectedOption.enum" :key="item" :value="index">{{item}}</option>
        </select>
      </template>
      <template v-else-if="filter.selectedOption.type==='number'">
        <select :key="filter.id+'compareOption'" v-model="filter.compareOption">
          <option :key="'exactly'" :value="'exactly'">exactly</option>
          <option :key="'between'" :value="'between'">between</option>
          <option :key="'more'" :value="'more'">more than</option>
          <option :key="'less'" :value="'less'">less than</option>
        </select>
        <input :key="filter.id+'num'" type="number" step="any" :min="filter.selectedOption.minimum" :max="filter.selectedOption.maximum" v-model.number="filter.num">
        <template v-if="filter.compareOption==='between'">
          and <input :key="filter.id+'range'" type="number" step="any" :min="filter.selectedOption.minimum" :max="filter.selectedOption.maximum" v-model.number="filter.range">
        </template>
      </template>
      <button :key="'remove'+filter.id" type="button" @click="removeFilter(filter.id)">remove this condition</button>
    </template>
    <button type="button" @click="newFilter">more conditions</button>
    I'm free
      <input type="checkbox" id="anyday" v-model="allSelected"><label for="anyday">Anytime</label>
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
    Reach me at <input type="email" v-model="email" required>
    <input type="submit" value="Go">
  </form>
</div>
</template>

<script>
import datapointSchema from '@/assets/datapoint.json'
import axios from 'axios'

let nextFilterId = 0

export default {
  components: {},
  watch: {
    allSelected: function (val) {
      if (val) {
        this.checkedDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
      }
    }
  },
  methods: {
    processForm () {
      const data = this.$data
      const transformedData = {
        activity_name: data.activityName,
        monday: data.checkedDays.includes('Monday'),
        tuesday: data.checkedDays.includes('Tuesday'),
        wednesday: data.checkedDays.includes('Wednesday'),
        thursday: data.checkedDays.includes('Thursday'),
        friday: data.checkedDays.includes('Friday'),
        saturday: data.checkedDays.includes('Saturday'),
        sunday: data.checkedDays.includes('Sunday'),
        advance_notice: data.advanceNotice,
        recipient: { email: data.email },
        location: {
          longitude: data.location.longitude,
          latitude: data.location.latitude,
          filters: data.filters.map(
            filter => ({
              weather_option: filter.selectedOption.title,
              number: filter.num,
              compare_option: filter.compareOption,
              range: filter.range
            })
          )
        }
      }

      console.log(JSON.stringify(transformedData))
      axios.post('http://127.0.0.1:8000/alerts', transformedData)
        .then(response => { console.log(response) })
        .catch(error => { console.log(error) })
    },
    removeFilter (id) {
      const index = this.filters.findIndex((element) => { return element.id === id })
      console.log(index)
      this.filters.splice(index, 1)
    },
    newFilter () {
      this.filters.push({
        id: ++nextFilterId,
        selectedOption: {},
        compareOption: '',
        num: null,
        range: null
      })
    },
    filterProperties (toFilter, unwanted) {
      return Object.keys(toFilter)
        .filter(key => !unwanted.includes(key))
        .reduce((obj, key) => {
          return {
            ...obj,
            [key]: toFilter[key]
          }
        }, {})
    }
  },
  data () {
    return {
      activityName: '',
      location: {
        latitude: '',
        longitude: ''
      },
      filterOptions: this.filterProperties(datapointSchema.properties, ['icon', 'summary']),
      filters: [{
        id: nextFilterId,
        selectedOption: datapointSchema.properties.apparentTemperature,
        compareOption: 'more',
        num: 60,
        range: null
      }],
      allSelected: false,
      checkedDays: [],
      advanceNotice: '',
      email: ''
    }
  },
  name: 'Create'
}
</script>
