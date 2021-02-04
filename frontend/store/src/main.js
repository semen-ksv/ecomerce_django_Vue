import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // <---
import store from "./store"
import messagePlugin from './utils/message.plugin'
import dateFilter from "./filters/date.filters"
import 'materialize-css/dist/js/materialize.min'
// import M from "materialize-css";


const app = createApp(App)
app.config.globalProperties.$filters = {dateFilter}
// app.config.globalProperties.$message = function (html) {
//             M.toast({html})
//             console.log(html)
//         }
app.use(router).use(store).use(messagePlugin)
app.mount('#app')
