<template>
  <div id="app">
      <component :is="layout">

      </component>
  </div>
</template>

<script>


import EmptyLayout from "./layouts/EmptyLayout";
import MainLayout from "./layouts/MainLayout";
export default {
  name: 'App',
  components: {
      // Footer,
      // Nav,
      EmptyLayout,
      MainLayout,
  },
    computed: {
      layout() {
            return (this.$route.meta.layout || 'empty') + '-layout'
      }
    },
    async mounted() {
      if (!Object.keys(this.$store.getters.info).length) {
          await this.$store.dispatch('getCurrentUser')
      }
    }
}
</script>

<style>
    @import "assets/css/style.css";
    @import "~materialize-css/dist/css/materialize.min.css";
</style>
