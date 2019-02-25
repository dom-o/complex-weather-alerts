<template>
  <div>
    <select v-model="selected">
      <option v-for="(option, optionName) in datapointSchema.properties" :key="optionName" :value="option.description">
        {{ option.title }}
      </option>
    </select>
    {{ selected }}
</div>

</template>

<script>
import datapointSchema from '@/assets/datapoint.json'
export default {
  name: 'ConditionSelect',
  created () {
    this.datapointSchema = datapointSchema
  },
  data() {
    return {
      selected:'',
    }
  },
}
</script>
