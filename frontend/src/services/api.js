import axios from 'axios';

const api = axios.create({
  baseURL : "http://localhost:5000/api",
  // baseURL : "https://info3180-groupproject.onrender.com/api",
});


api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token && !config.url.includes('/auth/login') && !config.url.includes('/register')) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, error => {
  return Promise.reject(error)
})

export default api