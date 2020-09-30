import Vue from 'vue'
import Vuex from 'vuex'
// import { postService } from "@/services";
import { Meme } from '../types'

Vue.use(Vuex)
export const store = Vue.observable({
  current: {} as Meme,
  saved: {} as Meme[]
})
export const savedStore = {
  getters: {
    saved: () => store.saved
  },
  mutations: {

  }
}
export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
