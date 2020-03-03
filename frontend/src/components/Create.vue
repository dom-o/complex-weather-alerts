<template>
<div>
  <AlertForm
    :alert_prefill="{email: prefilled_email}"
    @alert-form-submit="processForm($event)"
  />
</div>
</template>

<script>
import { mapState } from 'vuex'
import AlertForm from './AlertForm.vue'
// import axios from 'axios'

export default {
  components: {
    AlertForm
  },
  computed: {
    ...mapState({
      prefilled_email: state => state.user.email
    }),
  },
  watch: {},
  methods: {
    processForm (data) {
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
          longitude: data.longitude,
          latitude: data.latitude,
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
    // axios.post('http://127.0.0.1:8000/alerts', transformedData)
      // .then(response => {
      //   console.log(response)
      //   router.push({name:'created', params: {id: response.id}})
      // })
      // .catch(error => { console.log(error) })
    },
  },
  data () {
    return {}
  },
  name: 'Create'
}
</script>
