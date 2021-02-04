<template>
    <div>
        <div class="page-title">
            <h3>Product in category {{title}}</h3>

            <button class="btn waves-effect waves-light btn-small" >
                <i class="material-icons">refresh</i>
            </button>
        </div>

        <div class="row">
            <ProductItem
                    v-for="product in productList" :key="product.slug"
                    v-bind:title="product.title"
                    v-bind:price="product.price"
                    v-bind:slug="product.slug"
            />
        </div>

    </div>
</template>

<script>
    import ProductItem from "../components/ProductItem";

    export default {
        name: "Category",
        props: ['slug', 'title'],
        data() {
            return {
                productList: [],
            }
        },
        components: {
            ProductItem,
        },
        created() {
            this.loadListProduct(this.slug)

        },
        async beforeRouteUpdate (to, from, next) {
            this.loadListProduct(to.params['slug'])
            // this.productList = to.params.productList
            next()
        },


        methods: {
            async loadListProduct(slug) {
                this.productList = await fetch(
                    `${this.$store.getters.getServerUrl}/store/category/${slug}`,
                    {method: 'get',}
                ).then(response => response.json())

            },

        },
    }
</script>