<template>
  <div class="sidebar">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/author-list">All authors</router-link></li>
      <li><router-link to="/book-list">All books</router-link></li>
      <hr>
      <li v-if="isAuthenticated">
        <p>User: {{ username }}</p>
        <router-link to="/borrower">Borrowed Books</router-link>
        <p></p>
          <div v-if="isLibraryWorker">
            <hr>
            <p>Staff</p>
            <router-link to="/all_borrower">All Borrowed Books</router-link>
          </div>
        <p></p>
        <button @click="logout">Logout</button>
      </li>

      <li v-if="!isAuthenticated">
        <router-link to="/register">Register</router-link>
      </li>
      <li v-if="!isAuthenticated">
        <router-link to="/login">Login</router-link>
      </li>
      <li v-if="!isAuthenticated">
        <router-link to="/reset_password_page">Reset Password</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  name: 'SideBar',
  setup() {
    const isAuthenticated = ref(localStorage.getItem('access_token') !== null);
    const username = ref(localStorage.getItem('username'));
    const isLibraryWorker = ref(false);
    const router = useRouter();

    const refreshAccessToken = async () => {
      const refresh_token = localStorage.getItem('refresh_token');
      if (!refresh_token) {
        throw new Error('No refresh token found');
      }

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refresh_token,
        });

        const newAccessToken = response.data.access;
        localStorage.setItem('access_token', newAccessToken);

        return newAccessToken;
      } catch (error) {
        throw new Error('Unable to refresh token');
      }
    };

    const fetchUserGroups = async () => {
      if (!isAuthenticated.value) return;

      try {
        let accessToken = localStorage.getItem('access_token');

        if (!accessToken) {
          throw new Error('No access token');
        }

        try {
          const response = await axios.get('http://127.0.0.1:8000/api/accounts/user_info/', {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          });
          const groups = response.data.groups || [];
          isLibraryWorker.value = groups.includes('LibraryWorkers');
        } catch (error) {
          if (error.response && error.response.status === 401) {
            console.log('Токен истёк, пробуем обновить...');
            accessToken = await refreshAccessToken();
            const response = await axios.get('http://127.0.0.1:8000/api/accounts/user_info/', {
              headers: {
                Authorization: `Bearer ${accessToken}`,
              },
            });
            const groups = response.data.groups || [];
            isLibraryWorker.value = groups.includes('LibraryWorkers');
          } else {
            console.error('Ошибка при загрузке групп пользователя:', error);
            logout();
          }
        }
      } catch (error) {
        console.error('Ошибка при загрузке групп пользователя:', error);
      }
    };

    const logout = async () => {
      try {
        await axios.post('http://127.0.0.1:8000/api/accounts/logout/', {}, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });

        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('username');

        isAuthenticated.value = false;
        isLibraryWorker.value = false;

        router.push('/');
      } catch (error) {
        console.error('Ошибка при выходе', error);
      }
    };

    const checkTokenValidity = () => {
      setInterval(async () => {
        const accessToken = localStorage.getItem('access_token');
        if (accessToken) {
          try {
            await axios.get('http://127.0.0.1:8000/api/accounts/user_info/', {
              headers: {
                Authorization: `Bearer ${accessToken}`,
              },
            });
          } catch (error) {
            if (error.response && error.response.status === 401) {
              console.log('Токен истёк, пробуем обновить...');
              try {
                await refreshAccessToken();
                console.log('Токен обновлён');
              } catch (e) {
                console.error('Ошибка обновления токена', e);
                logout();
              }
            }
          }
        }
      }, 60000);
    };

    onMounted(() => {
      fetchUserGroups();
      checkTokenValidity();
    });

    window.addEventListener('storage', () => {
      isAuthenticated.value = localStorage.getItem('access_token') !== null;
      username.value = localStorage.getItem('username');
      fetchUserGroups();
    });

    return {
      isAuthenticated,
      username,
      isLibraryWorker,
      logout,
    };
  },
};
</script>


<style scoped>
.sidebar {
  width: 200px;
  padding: 20px;
  background-color: #f8f9fa;
}

button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 8px 16px;
  cursor: pointer;
}

button:hover {
  background-color: #d32f2f;
}
</style>
