/* eslint-disable */
export default {

    actions: {
        async login({dispatch, commit, getters}, {username, password}) {
            try {
                let status = 0
                const resp = await fetch(
                    `${getters.getServerUrl}/auth/token/login`,
                    {
                        method: 'post',
                        headers: {
                            "Content-type": "application/json",
                        },
                        body: JSON.stringify({
                            username: username, password: password
                        })
                    }
                ).then(function (response) {
                    status = response.status
                    return response.json()
                }).then(json => json)

                const token = await resp
                localStorage.setItem('token', token["auth_token"])
                // commit('setToken', token["auth_token"])
                return status

                } catch (error) {
                    console.log('Request failed', error)
                }

            // .then((json,status) => console.log(json ["auth_token"], status))

    },
    async register({dispatch, commit, getters}, {email, username, password}) {
        try {

            return await fetch(
                `${getters.getServerUrl}/auth/users/`,
                {
                    method: 'post',
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify({
                        email: email, password: password, username: username
                    })
                }
            ).then(function (response) {
                return response.status
            })

        } catch (error) {
            console.log('Request failed', error)
        }
    },
    async logout({getters, commit}) {
        try {
            await fetch(
                `${getters.getServerUrl}/auth/token/logout/`,
                {
                    method: 'post',
                    headers: {
                        "Content-type": "application/json",
                        "Authorization": `Token ${getters.token}`
                    },
                }
            )
            localStorage.removeItem('token')
            // await commit('clearToken')
            await commit('clearInfo')

        } catch (error) {
            console.log('Request failed', error)
        }
    }
}
}