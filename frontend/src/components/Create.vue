<template>
<div>
  <form>
    I like to go <input id="activityname" name="activityname" type="text">
    at <input id="lat" name="lat" type="text"> <input id="lon" name="lon" type="text">
    when the <ConditionSelect/> <ConditionFilter/>
    <button>more conditions</button>
  </form>
</div>
</template>

<script>
import ConditionSelect from './ConditionSelect.vue'

export default {
  components: {ConditionSelect},
  name: 'Create'
}
</script>
