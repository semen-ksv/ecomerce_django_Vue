<template>

<!--            <div class="col s12 m6 l4">-->
<!--                <div class="card blue-grey product-card">-->
<!--                    <div class="card-content white-text">-->
<!--&lt;!&ndash;                        <a href=""  class="card-title white-text" @click="goTo(slug)">{{title}}</a>&ndash;&gt;-->

<!--                        <router-link-->
<!--                        :to ="{name: 'Single', params: {slug: slug}}"-->

<!--                        >-->
<!--                            <a href=""  class="card-title white-text" >{{title}}</a>-->
<!--                        </router-link>-->

<!--                        <p class="currency-line">-->
<!--                            <span>{{price}}</span>-->
<!--                        </p>-->
<!--                    </div>-->
<!--                </div>-->
<!--            </div>-->
<!--            <div class="row">-->
    <div class="col s12 m3 product-card">
      <div class="card ">
        <div class="card-image">
          <img src="../assets/images/def_prod.jpeg">

<!--          <span class="card-title">Card Title</span>-->
          <a class="btn-floating halfway-fab waves-effect waves-light red"><i class="material-icons">add</i></a>
        </div>
        <div class="card-content">
            <span class="card-title">
            <router-link
                    :to ="{name: 'Single', params: {slug: slug}}"
            >
                <a href=""  class="card-title black-text" ><span>{{title}}</span></a>
            </router-link>
            </span>
             <p class="currency-line">
                <span>Price: {{price}}</span>
            </p>
          <p>I am a very simple card. I am good at containing small bits of information. I am convenient because I require little markup to use effectively.</p>
        </div>
      </div>
    </div>
<!--  </div>-->

</template>

<script>
    export default {
        name: "ProductItem",
        props: ['title', 'price', 'slug'],
        methods: {
            goTo(slug) {
                this.$router.push({name: "Single", params: {slug: slug}})
            }
        }
    }
</script>

<style scoped>

</style>