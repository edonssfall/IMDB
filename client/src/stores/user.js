import {defineStore} from 'pinia'
import {apiFetch} from "../utils/api";

export const useUserStore = defineStore('user', {
    state: () => {
        return {user: null}
    },

    getters: {
        getUserName(state) {
            if (state.user) {
                if (state.user.first_name === null && state.user.last_name === null) {
                    return state.user.email
                }
                return `${state.user.first_name} ${state.user.last_name}`
            }
        },
        getUserId(state) {
            return state.user ? state.user.id : null;
        },
        UserIsStaff(state) {
            return state.user ? state.user.is_staff : false
        }
    },

    actions: {
        logOut() {
            this.user = null
            localStorage.removeItem('userToken')
        },
        async fetchUser() {
            const response = await apiFetch(
                '/api/auth/current-user/',
                {method: 'GET'}
            )
            if (response.status === 200) {
                this.user = await response.json()
            }
            return
        }
    }
})