<template>
<div>
  confirmed you wanna delete <AlertDisplayView :alert="alert">?

    <button>ye boi</button>
    <button>nah son</button>
</div>
</template>

<script>
import AlertDisplayView from './AlertDisplayView.vue'

export default {
  name: 'DeleteAlert',
  components: {
    AlertDisplayView
  }
}
</script>
