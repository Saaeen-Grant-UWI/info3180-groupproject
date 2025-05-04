import axios from 'axios';

const api = axios.create({

  isDevelopment : process.env.NODE_ENV === 'development',
  baseURL : isDevelopment ? "http://localhost:5000/api" : "https://info3180-groupproject.onrender.com/api",
});



// Add a request interceptor to include the JWT token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('jwt_token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
