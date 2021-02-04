<template>

  <div>
    <div class="page-title">
      <h3>Add new product</h3>
    </div>

    <form class="form">
<!--      <div class="input-field" >-->
<!--        <select>-->
<!--          <option-->
<!--          >name cat</option>-->
<!--        </select>-->
<!--        <label>Выберите категорию</label>-->
<!--      </div>-->

<!--      <p>-->
<!--        <label>-->
<!--          <input-->
<!--              class="with-gap"-->
<!--              name="type"-->
<!--              type="radio"-->
<!--              value="income"-->
<!--          />-->
<!--          <span>Доход</span>-->
<!--        </label>-->
<!--      </p>-->

<!--      <p>-->
<!--        <label>-->
<!--          <input-->
<!--              class="with-gap"-->
<!--              name="type"-->
<!--              type="radio"-->
<!--              value="outcome"-->
<!--          />-->
<!--          <span>Расход</span>-->
<!--        </label>-->
<!--      </p>-->

      <div class="input-field">
        <input
            id="title"
            type="text"
        >
        <label for="title">Title</label>
<!--        <span class="helper-text invalid">amount пароль</span>-->
      </div>
          <!-- Dropdown Trigger -->
  <a class='dropdown-trigger btn' href='#' data-target='dropdown1' ref="dropdown2">Select category!</a>

  <!-- Dropdown Structure -->
  <ul  id='dropdown1' class='dropdown-content'>
    <li v-for="category in categories" :key="category.slug"><a href="#">{{category.title}}</a></li>

  </ul>
      <div class="input-field">
        <input
            id="description"
            type="text"
        >
        <label for="description">Description</label>
<!--        <span-->
<!--              class="helper-text invalid">description пароль</span>-->
      </div>
        <div class="input-field">
        <input
            id="price"
            type="number"
        >
        <label for="price">Peice</label>
<!--        <span-->
<!--              class="helper-text invalid">description пароль</span>-->
      </div>

              <p>
        <label>
          <input
              class="with-gap"
              name="type"
              type="checkbox"
              value="income"
          />
          <span>Is active</span>
        </label>
      </p>

      <button class="btn waves-effect waves-light" type="submit" @click.prevent="">
        Create
        <i class="material-icons right">send</i>
      </button>
    </form>
  </div>


</template>

<script>
    import M from "materialize-css";

    export default {
        name: "AddProduct",
        data () {
            return {
                categories: []
            }
        },
        created() {
            this.categories = this.$store.getters.getCategoryList
            console.log(this.categories)
        },
        mounted() {
            this.dropdown = M.Dropdown.init(this.$refs.dropdown2,
                    {
                      constrainWidth:false
                    })
        },

    }
</script>

<style scoped>

</style>