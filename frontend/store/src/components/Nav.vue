<template>
<nav class="navbar blue-grey lighten-1">
      <div class="nav-wrapper">
        <div class="navbar-left">
          <a href="#" @click.prevent="$emit('clickSidebar')">
            <i class="material-icons black-text">dehaze</i>
          </a>
          <span class="black-text" @click="goToHome"><a class="nav-logo" href="" style="color:#585353">My STORE</a></span>


        </div>

        <ul class="right hide-on-small-and-down">
          <li><span class="black-text" >{{ $filters.dateFilter(date) }}</span></li>
          <li class="cart_icon" @click="goToCart">
          <router-link
          :to="{name:'Cart'}"
          >

            <i class="material-icons medium">shopping_cart</i>


          </router-link>
          </li>

          <li v-if="username">
            <a
                class="dropdown-trigger black-text drop-name"
                href="#"
                data-target="dropdown"
                ref="dropdown"
            >
              {{username}}
              <i class="material-icons right">arrow_drop_down</i>
            </a>

            <ul id='dropdown' class='dropdown-content'>
              <li>
                <router-link :to="{name: 'Profile'}" class="black-text">
                  <i class="material-icons">account_circle</i>Профиль
                </router-link>
              </li>
              <li class="divider" tabindex="-1"></li>
              <li>
                <a href="#" class="black-text" @click.prevent="logout">
                  <i class="material-icons">assignment_return</i>Выйти
                </a>
              </li>
            </ul>
          </li>
          <li v-else>
            <router-link
            :to="{name: 'Login'}">
              LOGIN
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
<!--     <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About<outer-link> |-->

</template>

<script>
  import M from 'materialize-css'
  import messages from "../utils/messages";
    export default {
        name: "Nav",
        data: () =>({
          dropdown: null,
          date: new Date(),
          // username: null
        }),
        methods: {
          logout() {
            this.$store.dispatch('logout')
            this.$message(messages['logout'])
            this.$message(`Please login `)
            this.$router.push({name: "Login"})

          },
          goToHome() {
                this.$router.push({name: "Home"})
            },
          goToCart() {
                this.$router.push({name: "Cart"})
            },
        },
      computed: {
          username() {
            return this.$store.getters.info.username
          }
      },
        mounted() {
            this.dropdown = M.Dropdown.init(this.$refs.dropdown,
                    {
                      constrainWidth:false
                    })
        },
      onBeforeUnmount() {
          if (this.dropdown && this.dropdown.destroy) {
            this.dropdown.destroy()
          }
      }
    }
</script>

<style scoped>

</style>