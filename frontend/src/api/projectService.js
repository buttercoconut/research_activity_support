import apiClient from './apiClient'

export const fetchProjects = async () => {
  const response = await apiClient.get('/projects/')
  return response.data
}

export const createProject = async (project) => {
  const response = await apiClient.post('/projects/', project)
  return response.data
}
