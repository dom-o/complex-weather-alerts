<template>
<div>
  <form @submit.prevent="processForm">
    I like to go <input v-model="activity" type="text">
    at <input v-model.number="latitude" type="number" step="any" min="-90" max="90" required> <input v-model.number="longitude" type="number" step="any" min="-180" max="180" required>
    when the <template v-for="filter in filters">
      <select :key="filter.id+'selectedOption'" v-model="filter.selectedOption" >
        <option v-for="(option, optionName) in filterOptions" :key="optionName" :value="option">
          {{ option.title }}
        </option>
      </select>
      {{ filter.selectedOption.description }}
      is
      <template v-if="filter.selectedOption.type==='string'">
        <input :key="filter.id+'string'" type="text" v-model="filter.selectData.string">
      </template>
      <template v-else-if="filter.selectedOption.enum">
        <select :key="filter.id+'enum'" v-model="filter.selectData.enum">
          <option v-for="item in filter.selectedOption.enum" :key="item" :value="item">{{item}}</option>
        </select>
      </template>
      <template v-else-if="filter.selectedOption.type==='number'">
        <select :key="filter.id+'compareOption'" v-model="filter.selectData.number.compareOption">
          <option :key="'exactly'" :value="'exactly'">exactly</option>
          <option :key="'between'" :value="'between'">between</option>
          <option :key="'more'" :value="'more'">more than</option>
          <option :key="'less'" :value="'less'">less than</option>
        </select>
        <input :key="filter.id+'num'" type="number" step="any" :min="filter.selectedOption.minimum" :max="filter.selectedOption.maximum" v-model.number="filter.selectData.number.num">
        <template v-if="filter.selectData.number.compareOption==='between'">
          and <input :key="filter.id+'range'" type="number" step="any" :min="filter.selectedOption.minimum" :max="filter.selectedOption.maximum" v-model.number="filter.selectData.number.range">
        </template>
      </template>
      <button type="button" @click="removeFilter(filter.id)">remove this condition</button>
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
      console.log(this.$data)
    },
    removeFilter (id) {
      var index = this.filters.findIndex((element) => { return element.id === id })
      console.log(index)
      this.filters.splice(index, 1)
    },
    newFilter () {
      this.filters.push({
        id: ++nextFilterId,
        selectedOption: {},
        selectData: {
          string: '',
          enum: '',
          number: {
            compareOption: '',
            num: '',
            range: ''
          }
        }
      })
    }
  },
  data () {
    return {
      activity: '',
      latitude: '',
      longitude: '',
      filterOptions: datapointSchema.properties,
      filters: [{
        id: nextFilterId,
        selectedOption: datapointSchema.properties.apparentTemperature,
        selectData: {
          string: '',
          enum: '',
          number: {
            compareOption: 'more',
            num: 60,
            range: ''
          }
        }
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
