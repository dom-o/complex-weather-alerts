<template>
<div>
  confirmed you wanna unsubscribe [user.email] from <AlertDisplayView :alert="alert">?

    <button>ye boi</button>
    <button>nah son</button>
</div>
</template>

<script>
import AlertDisplayView from './AlertDisplayView.vue'

export default {
  name: 'UnsubscribeFromAlert',
  components: {
    AlertDisplayView
  }
}
</script>
