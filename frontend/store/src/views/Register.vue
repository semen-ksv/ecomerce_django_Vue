<template>
    <Nav/>
    <form class="card auth-card" @submit.prevent="submitHandler">
        <div class="card-content">
            <span class="card-title center">Register new User</span>
            <div class="input-field">
                <input
                        id="email"
                        type="text"
                        v-model="email"
                >
                <label for="email">Email</label>
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
                <label for="password">Пароль</label>
                <small v-if="errMassagePass" class="helper-text invalid red-text right-align">{{errMassagePass}}</small>
            </div>
            <div class="input-field">
                <input
                        id="confirm_password"
                        type="password"
                        class="validate"
                        v-model="confirm_password"
                >
                <label for="confirm_password">Confirm password</label>
<!--                <small class="helper-text invalid">Password</small>-->
            </div>
            <div class="input-field">
                <input
                        id="name"
                        type="text"
                        class="validate"
                        v-model="name"
                >
                <label for="name">Имя</label>
<!--                <small class="helper-text invalid">Name</small>-->
            </div>
            <p>
                <label>
                    <input type="checkbox" v-model="confirm_checkbox"/>
                    <span>С правилами согласен</span>
                    <br>
                    <small v-if="errMassageCheck"
                           class="helper-text invalid red-text right-align">{{errMassageCheck}}</small>
                </label>
            </p>
        </div>
        <div class="card-action">
            <div>
                <button
                        class="btn waves-effect waves-light auth-submit"
                        type="submit"
                >
                    Зарегистрироваться
                    <i class="material-icons right">send</i>
                </button>
            </div>

            <p class="center">
                Уже есть аккаунт?
                <router-link
                        :to="{name:'Login'}">
                    <a href="/">Войти!</a>
                </router-link>
            </p>
        </div>
    </form>
</template>

<script>
    import Nav from "../components/Nav";

    export default {
        name: "Register",
        data() {
            return {
                email: '',
                password: '',
                confirm_password: '',
                name: '',
                confirm_checkbox: false,
                errMessage: null,
                errMassagePass: null,
                errMassageCheck: null
            }
        },
        components: {
            Nav
        },
        methods: {
            validateEmail(email) {
                const re = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
                return re.test(String(email).toLowerCase());
            },
            goToHome() {
                this.$router.push({name: "Home"})
            },
            async submitHandler() {
                this.errMessage = null
                this.errMassagePass = null
                this.errMassageCheck = null

                if (this.email === '' || this.password === '' || this.name === '' || this.confirm_password === '') {
                    this.errMessage = 'Please fill out all fields.'
                    return
                } else if (!this.validateEmail(this.email)) {
                    this.errMessage = 'Email is not valid.'
                    return
                } else if (this.password.length < 6 || this.confirm_password.length < 6) {
                    this.errMassagePass = 'Password is short. Please input password no less 6 symbols.'
                    return
                } else if (this.password !== this.confirm_password) {
                    this.errMassagePass = 'Password not much.'
                    return
                } else if (!this.confirm_checkbox) {
                    this.errMassageCheck = 'Please select confirm familiarization.'
                    return
                }

                let registerData = {
                    email: this.email,
                    password: this.password,
                    username: this.name
                }

                const res = await this.$store.dispatch('register', registerData)
                if (res === 201) {
                    this.$message(`You was successfully registered.\n`)
                    this.$message(`Please login.`)
                    await this.$router.push({name: "Login"})
                }else {
                    this.$error(`Something gone wrong`)
                    this.$message(`Try again`)
                }


                this.$emit('login-submit', registerData)
                this.email = ''
                this.name = ''
                this.password = ''
                this.confirm_password = ''
                this.confirm_checkbox = false
            }
        }
    }
</script>

<style scoped>

</style>