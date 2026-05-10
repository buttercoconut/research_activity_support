import { createRouter, createWebHistory } from 'vue-router'
import ProjectList from '../components/ProjectList.vue'
import ProjectView from '../views/ProjectView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ProjectList
  },
  {
    path: '/projects/:id',
    name: 'ProjectView',
    component: ProjectView,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
