import { createRouter, createWebHistory } from 'vue-router'
import RaceList from '../views/RaceList.vue'
import RaceDetail from '../views/RaceDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: RaceList },
        { path: '/race/:id', name: 'race-detail', component: RaceDetail },
    ]
})

export default router
