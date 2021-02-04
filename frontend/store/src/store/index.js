import { createStore } from 'vuex'
import auth from "./auth";
import user_info from "./user_info";

const store = createStore({
  state () {
    return {
        backendUrl: "http://127.0.0.1:8000",
        categoryStoreList: []
    }
  },
  actions() {
    return {
      setCateList (context, payload) {
    context.commit('getCategoryList', payload);
    }
    }
  },
  modules: {
    auth,
    user_info
  },
  mutations: {
    setCategoryList(state, categories) {
      state.categoryStoreList = categories
    }
  },
  getters: {
        getServerUrl: state => {
          return state.backendUrl
    },
            getCategoryList: state => {
          return state.categoryStoreList
    },

  },
})

export default store