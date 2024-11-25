import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
});

api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      await refreshAccessToken();

      return api(originalRequest);
    }

    return Promise.reject(error);
  }
);

const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem('refresh_token');
  if (!refreshToken) return;

  try {
    const response = await api.post('accounts/token/refresh/', {
      refresh: refreshToken,
    });

    localStorage.setItem('access_token', response.data.access);
  } catch (error) {
    console.error('Token refresh failed', error);
    logout();
  }
};

const logout = () => {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  window.location.href = '/'; // Перенаправляем на главную страницу
};

const setAuthHeader = () => {
  const token = localStorage.getItem('access_token');
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  }
};

export { api, setAuthHeader, logout };
