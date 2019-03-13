<template>
  <div>
    <select v-model="selectedCond" >
      <option v-for="(option, optionName) in condieFilter.options" :key="optionName" :value="option">
        {{ option.title }}
      </option>
    </select>
    {{ selectedCond.description }}
    is
    <template v-if="selectedCond.type==='string'">
      <input type="text" id="selectedText">
    </template>
    <template v-else-if="selectedCond.enum">
      <select>
        <option v-for="item in selectedCond.enum" :key="item" :value="item">{{item}}</option>
      </select>
    </template>
    <template v-else-if="selectedCond.type==='number'">
      <select v-model="selectedNum">
        <option :key="'exactly'" :value="'exactly'">exactly</option>
        <option :key="'between'" :value="'between'">between</option>
        <option :key="'more than'" :value="'more than'">more than</option>
        <option :key="'less than'" :value="'less than'">less than</option>
      </select>
      <input id="selectedNum1" type="number">
      <template v-if="selectedNum==='between'">
        and <input type="number" id="selectedNum2">
      </template>
    </template>
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
  data () {
    return {
      selectedCond: {},
      selectedNum: ''
    }
  }
}
</script>
