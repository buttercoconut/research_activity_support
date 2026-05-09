<template>
  <div>
    <h2>Project List</h2>
    <ul>
      <li v-for="project in projects" :key="project.id">
        <strong>{{ project.title }}</strong> - {{ project.description }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Project {
  id: number
  title: string
  description?: string
  start_date: string
  end_date?: string
  budget: number
}

const projects = ref<Project[]>([])

const fetchProjects = async () => {
  try {
    const { data } = await axios.get<Project[]>('http://localhost:8000/projects/')
    projects.value = data
  } catch (e) {
    console.error('Failed to fetch projects', e)
  }
}

onMounted(() => {
  fetchProjects()
})
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 0.5rem;
}
</style>
