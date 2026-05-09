<template>
  <div class="project-list">
    <h1>Research Projects</h1>
    <button @click="showCreate = true">Create New Project</button>
    <ul>
      <li v-for="p in projects" :key="p.id">
        <strong>{{ p.title }}</strong> - {{ p.budget }} USD
      </li>
    </ul>
    <div v-if="showCreate" class="modal">
      <h2>Create Project</h2>
      <form @submit.prevent="submit">
        <label>Title: <input v-model="newProject.title" required /></label>
        <label>Description: <textarea v-model="newProject.description" /></label>
        <label>Start Date: <input type="date" v-model="newProject.start_date" required /></label>
        <label>End Date: <input type="date" v-model="newProject.end_date" /></label>
        <label>Budget: <input type="number" step="0.01" v-model.number="newProject.budget" required /></label>
        <button type="submit">Save</button>
        <button type="button" @click="showCreate = false">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchProjects, createProject } from '@/api/projectService'

const projects = ref([])
const showCreate = ref(false)
const newProject = ref({
  title: '',
  description: '',
  start_date: '',
  end_date: '',
  budget: 0,
})

const load = async () => {
  projects.value = await fetchProjects()
}

const submit = async () => {
  await createProject(newProject.value)
  showCreate.value = false
  await load()
}

onMounted(load)
</script>

<style scoped>
.project-list { padding: 1rem; }
.modal { background: rgba(0,0,0,0.5); position: fixed; top:0; left:0; right:0; bottom:0; display:flex; align-items:center; justify-content:center; }
.modal form { background:white; padding:1rem; border-radius:4px; }
</style>
