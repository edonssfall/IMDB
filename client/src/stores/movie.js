import {defineStore} from "pinia";

export const useMovieStore = defineStore('movie', {
    state: () => {
        return{
            movies: null,
            movie: [],
            rec_movies: null,
            showNext: false,
            showPrevious: false,
            currentPage: 1,
            total_pages: null,
            isLoading: false,
        }
    },
    getters: {
        getMovieDetails(state) {
            if (state.movie) {
                return state.movie ? state.movie: []
            }
        }
    },
    actions: {
        async loadNext() {
            this.currentPage += 1
            await this.MoviesList()
        },
        async loadPrevious() {
            this.currentPage -= 1
            await this.MoviesList()
        },
        async MoviesList() {
            this.isLoading = true
            const response = await fetch(`api/imdb/movies/?page=${this.currentPage}`)
            if (response.status === 200) {
                const data = await response.json()
                this.movies = data.results
            }
            this.isLoading = false
            return this.movies
        },
        async MovieDetails(movie_slug) {
            this.isLoading = true
            const response = await fetch(`api/imdb/title/${movie_slug}`)
            if (response.status === 200) {
                this.movie = await response.json()
            }
        },
        async MovieRec() {
            let movie_genres = this.movie.genres
            let request_genres = ''
            for (const item of movie_genres) {
                request_genres += '&genres=' + item
            }
            const response = await fetch(`api/imdb/?title=${this.movie.imdb_id}${request_genres}`)
            if (response.status === 200) {
                const data = await response.json()
                this.rec_movies = data.results
                this.isLoading = false
                return this.rec_movies
            } else {
                return 404
            }
        }
    }
})
