<template>
  <div>
    <select v-model="selected">
      <option v-for="(option, optionName) in condieFilter.options" :key="optionName" :value="option.description">
        {{ option.title }}
      </option>
    </select>
    {{ selected }}
  </div>
</template>

<script>
export default {
  name: 'CondieFilter',
  props: {
    condieFilter: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      selected:'',
    }
  },
}
</script>
