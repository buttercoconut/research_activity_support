<template>
  <div>
    <h2>Project List</h2>
    <ul>
      <li v-for="project in projects" :key="project.id">
        <strong>{{ project.title }}</strong> (PI ID: {{ project.pi_id }})
        <p>{{ project.description }}</p>
        <small>Budget: {{ project.budget }} | Start: {{ formatDate(project.start_date) }}</small>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Project {
  id: number;
  title: string;
  description?: string;
  start_date: string;
  end_date?: string;
  pi_id: number;
  budget: number;
}

const projects = ref<Project[]>([]);

const fetchProjects = async () => {
  try {
    const response = await axios.get<Project[]>('http://localhost:8000/projects/');
    projects.value = response.data;
  } catch (err) {
    console.error(err);
  }
};

const formatDate = (dateStr: string) => {
  const d = new Date(dateStr);
  return d.toLocaleDateString();
};

onMounted(() => {
  fetchProjects();
});
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  border-bottom: 1px solid #ccc;
  padding: 8px 0;
}
</style>
