<template>


  <div class="app-main-layout">

    <Nav @clickSidebar="isOpen = !isOpen"/>
    <Sidebar v-bind:value="isOpen"/>


    <main class="app-content" :class="{full: !isOpen}">
      <div class="app-page">
      <router-view/>

      </div>
      </main>

    <div class="fixed-action-btn">
      <router-link
      :to="{name:'AddProduct'}">
        <a class="btn-floating btn-large blue" href="#">
        <i class="large material-icons">add</i>
      </a></router-link>
    </div>

    <Footer/>

</div>



</template>

<script>
  import Nav from "../components/Nav";
  import Sidebar from "../components/Sidebar";
  import Footer from "../components/Footer";
    export default {
        name: "MainLayout",
        data: () => ({
                 isOpen: true
                }
        ),
        components: {
          Nav,
          Sidebar,
          Footer
        }
    }
</script>

<style scoped>

</style>