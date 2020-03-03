<template>
  display alertList here with all forms filled in as appropriate for list
</template>
<script>
export default () {
  name: 'AlertEdit',
  created() {
    // TODO: get the alert from the server
    /**
      get the alert id from the router if any
        if not logged in or no id or whatever, just default to CreateAlert view
      send the id to server
      get back the alert
      put alert in data
      prepopulate the form
      handle saving appropriately
    **/
  },
  methods: {},
  data () {
    return {
      alert: {}
    }
  },
}
</script>
