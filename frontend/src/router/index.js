import { createRouter, createWebHistory } from 'vue-router'
import ProjectList from '@/views/ProjectList.vue'

const routes = [
  { path: '/', name: 'Home', component: ProjectList },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
