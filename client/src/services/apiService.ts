import axios from 'axios'
const api = axios.create({
  baseURL: 'http://localhost:5000/api',
  withCredentials: false
});
api.interceptors.request.use(config => {
  return config;
})
api.interceptors.response.use(
  res => {
    if("Error" in res.data){
      throw new Error(res.data);
    }
    return res.data;
  }
)
export default api;
