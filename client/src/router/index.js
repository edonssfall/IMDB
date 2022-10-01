import {createRouter, createWebHistory} from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from "../views/RegisterView.vue";
import MoviesView from "../views/MoviesView.vue";
import PersonView from "../views/PersonView.vue";
import HomeView from "../views/HomeView.vue";
import MovieDetailsView from "../views/MovieDetailsView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView
        },
        {
            path: '/movies',
            name: 'movies',
            component: MoviesView
        },
        {
            path: '/persons',
            name: 'person',
            component: PersonView
        },
        {
            path: '/:movie_slug',
            name: 'movie_details',
            component: MovieDetailsView
        }
    ]
})

export default router
