import { defineStore } from 'pinia'

export const useProjectStore = defineStore('project', {
  state: () => ({
    projects: []
  }),
  actions: {
    setProjects(projects) {
      this.projects = projects
    }
  }
})
