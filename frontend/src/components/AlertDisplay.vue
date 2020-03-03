<template>
<div>
  {{this.alert.activityName}} @ [{{this.alert.latitude}}, {{this.alert.longitude}}]
  <ul>
    <li v-for="filter in this.alert.filters">
        {{filter.weather_option}} {{filter.compare_option}} {{filter.number}}
          <template v-if="filter.compare_option=='between'">
             and {{filter.range}}
          </template>

    </li>
  </ul>
  <router-link :to="{ name: 'edit', params: { alertId: this.alert.id }}">edit alert</router-link>
  <router-link :to="{ name: 'delete', params: { alertId: this.alert.id }}">delete alert</router-link>
  <router-link :to="{ name: 'unsubscribe', params: { alertId: this.alert.id }}">unsubscribe alert</router-link>
</div>
</template>

<script>
export default {
  name: 'AlertDisplay',
  props: {
    alert: Object,
  },
}
</script>
