<template>
    <Nav/>
    <form class="card auth-card"
          @submit.prevent="submitHandler"
    >
        <div class="card-content">
            <span class="card-title center">Please Login</span>
            <div class="input-field">
                <input
                        id="username"
                        type="text"
                        class="validate"
                        v-model="username"
                >
                <label for="username">User name</label>
                <p v-if="errMessage"></p>
                <small class="helper-text red-text invalid right-align">{{errMessage}}</small>
            </div>
            <div class="input-field">
                <input
                        id="password"
                        type="password"
                        class="validate"
                        v-model="password"
                >
                <label for="password">Password</label>
                <small v-if="errMassagePass" class="helper-text invalid red-text right-align">{{errMassagePass}}</small>
            </div>

        </div>
        <div class="card-action">
            <div>
                <button
                        class="btn waves-effect waves-orange auth-submit"
                        type="submit"
                >
                    Войти
                    <i class="material-icons right">send</i>
                </button>
            </div>

            <p class="center">
                Нет аккаунта?
                <router-link
                        :to="{name:'Register'}"><a href="">Зарегистрироваться</a>
                </router-link>
            </p>
        </div>
    </form>
</template>

<script>
    import Nav from "../components/Nav";

    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
                errMessage: null,
                errMassagePass: null
            }
        },
        components: {
            Nav
        },
        methods: {
            // validateEmail(email) {
            //     const re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
            //     return re.test(String(email).toLowerCase());
            // },

            async submitHandler() {
                this.errMessage = null
                this.errMassagePass = null

                if (this.username === '' || this.password === '') {
                    this.errMessage = 'Please fill out all fields.'
                    return
                }
                // else if (!this.validateEmail(this.username)) {
                //     this.errMessage = 'Email is not valid.'
                //     return
                // }
                // this.goToHome()

                let loginFormData = {
                    username: this.username,
                    password: this.password,
                }
                // try {
                //     this.$store.dispatch('login', loginFormData)
                //     await this.$router.push({name: "Home"})
                // } catch (e) {
                //     console.log(e)
                // }
                const res = await this.$store.dispatch('login', loginFormData)
                console.log(res)
                if (res === 200) {
                    await this.$store.dispatch('getCurrentUser')
                    await this.$router.push({name: "Home"})
                } else {
                    this.$message(`Your credentials are wrong`)
                    this.$message(`Try again`)
                }



            }
        }
    }
</script>

<style scoped>

</style>