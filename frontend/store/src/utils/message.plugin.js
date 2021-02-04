import M from 'materialize-css'

export default {
    install(app) {
        app.config.globalProperties.$message = function (html) {
            M.toast({html})
            console.log(html)
        }
        app.config.globalProperties.$error = function (html) {
            M.toast({html: `Error: ${html}`})
        }
    }

}