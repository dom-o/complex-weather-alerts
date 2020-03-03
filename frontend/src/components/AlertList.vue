/* eslint-disable */
<template>
<div>
  <h1>{{ user.name }}'s alerts</h1>
  <router-link to='/create'>new alert</router-link>
  <router-link to='/unsub/all'>unsubscribe all</router-link>
  <router-link to='/delete/all'>delete all</router-link>
  <ul>
    <li v-for="alert in alerts">
      <AlertDisplay
        :alert="alert"
      />
    </li>
  </ul>
</div>
</template>
<script>
import AlertDisplay from './AlertDisplay.vue'

export default {
  name: 'AlertList',
  components: {
    AlertDisplay,
  },
  methods: {
  },
  data () {
    return {
      user: {name: 'young oldman'},
      alerts: [
        {
          activityName: 'CLIMB',
          recipient: {
            email: 'a@a.com'
          },
          latitude: 69.420,
          longitude: -8.309,
          filters: [{
            weather_option: 'apparentTemperature', number: 60, compare_option: 'more', range: null
          }],
          monday: false, tuesday: false, wednesday: true, thursday: false, friday: true, saturday: false, sunday: false,
          advance_notice: 1
        },
        {
          activityName: 'run',
          recipient: {
            email: '0@run.com'
          },
          latitude: -44.09,
          longitude: -1.64,
          filters: [
            { weather_option: 'windSpeed', number: 0.85, compare_option: 'exactly', range: null },
          ],
          monday: false, tuesday: false, wednesday: false, thursday: true, friday: true, saturday: false, sunday: true,
          advance_notice: 7
        },
        {
          activityName: 'parachute',
          recipient: {
            email: '1@parachute.com'
          },
          latitude: 16.41,
          longitude: -143.2,
          filters: [
            { weather_option: 'temperatureLow', number: 0.61, compare_option: 'exactly', range: null }, { weather_option: 'temperatureLowTime', number: 0.27, compare_option: 'more', range: null },
          ],
          monday: false, tuesday: true, wednesday: true, thursday: true, friday: true, saturday: false, sunday: true,
          advance_notice: 4
        },
        {
          activityName: 'cave',
          recipient: {
            email: '2@cave.com'
          },
          latitude: 79.05,
          longitude: 19.03,
          filters: [
            { weather_option: 'windBearing', number: 0.22, compare_option: 'between', range: null },
          ],
          monday: false, tuesday: true, wednesday: true, thursday: false, friday: false, saturday: true, sunday: false,
          advance_notice: 7
        },
        {
          activityName: 'scuba',
          recipient: {
            email: '3@scuba.com'
          },
          latitude: -68.24,
          longitude: -60.23,
          filters: [
            { weather_option: 'nearestStormDistance', number: 0.63, compare_option: 'less', range: null },
          ],
          monday: false, tuesday: true, wednesday: false, thursday: false, friday: false, saturday: false, sunday: true,
          advance_notice: 4
        },
        {
          activityName: 'picnic',
          recipient: {
            email: '4@picnic.com'
          },
          latitude: -23.92,
          longitude: 137.78,
          filters: [
            { weather_option: 'temperatureHigh', number: 0.41, compare_option: 'more', range: null },
          ],
          monday: false, tuesday: true, wednesday: false, thursday: true, friday: true, saturday: false, sunday: false,
          advance_notice: 4
        },
        {
          activityName: 'skiing',
          recipient: {
            email: '5@skiing.com'
          },
          latitude: 26.49,
          longitude: -119.31,
          filters: [
            { weather_option: 'uvIndex', number: 0.04, compare_option: 'between', range: null },
          ],
          monday: true, tuesday: true, wednesday: true, thursday: true, friday: false, saturday: false, sunday: false,
          advance_notice: 4
        },
      ]
    }
  },
}
</script>
