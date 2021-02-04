<template>

    <div  style="border: beige solid 1px; text-align: center">
            <h2>{{product.title}}</h2>
            <p>Category: {{product.category}}</p>
            <div>
                {{product.description}}
            </div>
            <p>Price: <strong>{{product.price}}</strong></p>
        </div>
</template>

<script>
    export default {
        name: "Single",
        props: ['slug'],
        data() {
            return {
                product: {}
            }
        },
        created() {
            this.loadProduct()
        },
        methods: {
            async loadProduct() {
                this.product = await fetch(
                    `${this.$store.getters.getServerUrl}/store/product/${this.slug}`,
                    {method: 'get', }
                ).then(response => response.json())
                console.log(this.product)
            }
        }
    }
</script>

<style scoped>

</style>