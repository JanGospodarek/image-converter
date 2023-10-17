import { Store, createStore } from "vuex";
import { InjectionKey } from "vue";

export interface State {
  id: string;
}

export const key: InjectionKey<Store<State>> = Symbol();

export default createStore<State>({
  state: {
    id: "",
  },
  getters: {},
  mutations: {
    setId(state, payload: string) {
      state.id = payload;
    },
  },
  actions: {},
  modules: {},
});
