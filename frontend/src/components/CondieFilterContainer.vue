<template>
  <div>
    <CondieFilter
      v-for="condieFilter in condieFilters"
      :key="condieFilter.id"
      :condieFilter="condieFilter"
    />
    <button type="button" @click="newCondieFilter">more conditions</button>
  </div>
</template>

<script>
import datapointSchema from '@/assets/datapoint.json'
import CondieFilter from './CondieFilter.vue'
import Vue from 'vue'

let nextCondieFilterId = 1

export default {
  name: 'CondieFilterContainer',
  components: {CondieFilter},
  methods: {
    newCondieFilter () {
      this.condieFilters.push({
        id: nextCondieFilterId++,
        options: datapointSchema.properties
      })
    }
  },
  data: function () {
    return {
      condieFilters: [
        {
          id: nextCondieFilterId++,
          options: datapointSchema.properties
        }
      ]
    }
  }
}
</script>
