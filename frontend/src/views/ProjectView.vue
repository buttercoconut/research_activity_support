<template>
  <div class="project-view">
    <h2>{{ project.title }}</h2>
    <p><strong>PI:</strong> {{ project.pi_name }}</p>
    <p><strong>기간:</strong> {{ project.start_date }} ~ {{ project.end_date }}</p>
    <p><strong>예산:</strong> {{ project.budget }} 원</p>
    <p><strong>설명:</strong> {{ project.description }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const project = ref({})

const fetchProject = async () => {
  try {
    const response = await axios.get(`/api/projects/${route.params.id}`)
    project.value = response.data
  } catch (error) {
    console.error('프로젝트 상세 가져오기 실패', error)
  }
}

onMounted(() => {
  fetchProject()
})
</script>

<style scoped>
.project-view {
  padding: 1rem;
}
</style>
