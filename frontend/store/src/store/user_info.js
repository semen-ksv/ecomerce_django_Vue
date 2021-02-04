export default {
    state: {
        info: {

        },
        token: localStorage.getItem('token') || '',
    },

    mutations: {
        setInfo(state, info) {
            state.info = info
        },
        clearInfo(state) {
            state.info = {}
        },
        setToken(state, token) {
            state.token = token
        },
        clearToken(state) {
            state.token = ''
        }
    },
    actions: {

        async getCurrentUser({getters, commit}) {
            if (localStorage.getItem('token')) {
                try {
                    const resp = await fetch(
                        `${getters.getServerUrl}/auth/users/me`,
                        {
                            method: 'get',
                            headers: {
                                "Content-type": "application/json",
                                "Authorization": `Token ${localStorage.getItem('token')}`
                            },
                        }
                    ).then(response => response.json()).then(
                        json => json
                    )
                    const info = await resp
                    commit("setInfo",info)

                } catch (error) {
                    console.log('Request failed', error)
                }
            }
        }
    },
    getters: {
        info: state => state.info,
        token: state => state.token,
    }
}