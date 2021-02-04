<template>


    <ul class="sidenav app-sidenav" :class="{open: value}">
        <router-link
                :to = "{name:'Home'}"
            >
            <h3 class="side-h1">Home</h3>
        </router-link>

        <h3 class="side-h1">Categories</h3>

      <router-link
              v-for="category in categoryList"
              :key="category.slug"

              active-class="active"

              :to="{ name: 'Category', params: { slug: category.slug, title:category.title }}"
              exact
       >
<!--          TODO: activate sidebar menu with categories-->
        <li>
            <a  href="#" class="waves-effect waves-orange pointer">
                {{category.title}}
            </a>
        </li>
      </router-link>
                <router-link
                :to = "{name:'Cart'}"
            >
            <h3 class="side-h1">Cart</h3>
        </router-link>
                <router-link
                :to = "{name:'About'}"
            >
            <h3 class="side-h1">About</h3>
        </router-link>
    </ul>

</template>

<script>
    export default {
        name: "Sidebar",
        props: ['value'],
        data(){
            return {
                categoryList: []
            }
        },
        components: {

        },
        created() {
            this.loadListCategory()
        },
        methods: {

            async loadListCategory() {

                const categories = await fetch(
                    `${this.$store.getters.getServerUrl}/store/category/`,
                    {method: 'get', }
                ).then(response => response.json()).then(
                    json =>  json
                )
                this.categoryList = categories
                console.log(this.categoryList)
                this.$store.commit('setCategoryList', this.categoryList)
                console.log(this.$store.getters.getCategoryList)

            },
            goTo(slug, title) {
                this.$router.push({ name: "Category", params: {slug: slug, title:title}})

            }
        },
    }
</script>

<style scoped>

</style>