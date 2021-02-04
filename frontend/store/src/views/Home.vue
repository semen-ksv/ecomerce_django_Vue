<template>
    <div>
        <div class="page-title">
            <h3>Products</h3>

<!--            <button class="btn waves-effect waves-light btn-small" >-->
<!--                <i class="material-icons">refresh</i>-->
<!--            </button>-->
<!--            <a class="waves-effect waves-light btn-large" href="#">Wave</a>-->
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
    // import Sidebar from "../components/Sidebar";
    import ProductItem from "../components/ProductItem";

    export default {
        name: "Home",
        data() {
            return {
                productList: [],
            }
        },
        components: {
            ProductItem,
        },
        created() {
            this.loadListProduct()

        },
        methods: {
            async loadListProduct() {
                this.productList = await fetch(
                    `${this.$store.getters.getServerUrl}/store/product/`,
                    {method: 'get',}
                ).then(response => response.json())
            },
            goTo(slug) {
                this.$router.push({name: "Single", params: {slug: slug}})
            }
        },
    }
</script>

