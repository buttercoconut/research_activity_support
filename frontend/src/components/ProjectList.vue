<template>
  <div class="project-list">
    <h2>연구 프로젝트 목록</h2>
    <ul>
      <li v-for="project in projects" :key="project.id">
        <router-link :to="{ name: 'ProjectView', params: { id: project.id } }">
          {{ project.title }} ({{ project.start_date }} ~ {{ project.end_date }})
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const projects = ref([])

const fetchProjects = async () => {
  try {
    const response = await axios.get('/api/projects')
    projects.value = response.data
  } catch (error) {
    console.error('프로젝트 목록 가져오기 실패', error)
  }
}

onMounted(() => {
  fetchProjects()
})
</script>

<style scoped>
.project-list {
  padding: 1rem;
}
.project-list ul {
  list-style: none;
  padding: 0;
}
.project-list li {
  margin-bottom: 0.5rem;
}
</style>
