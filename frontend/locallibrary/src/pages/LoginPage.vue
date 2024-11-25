<template>
  <div>
    <h1>Вход</h1>
    <form @submit.prevent="loginUser">
      <div>
        <label for="username">Имя пользователя</label>
        <input v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input v-model="password" id="password" type="password" required/>
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import {ref} from 'vue';
import {useRouter} from 'vue-router';
import axios from "axios";
export default {
  name: 'LoginPage',
  setup() {
    const username = ref('');
    const password = ref('');
    const errorMessage = ref(null);
    const router = useRouter();

    // Функция для авторизации пользователя
    const loginUser = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
          username: username.value,
          password: password.value,
        });

        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);

        // Обновляем состояние isAuthenticated в localStorage
        window.dispatchEvent(new Event('storage'));

        alert('Авторизация успешна!');
        router.push('/');
      } catch (error) {
        if (error.response && error.response.data) {
          errorMessage.value = error.response.data.detail || 'Ошибка авторизации';
        } else {
          errorMessage.value = 'Сетевая ошибка. Попробуйте ещё раз.';
        }
      }
    };

    return {
      username,
      password,
      errorMessage,
      loginUser,
    };
  },
};
</script>

<style scoped>
.error {
  color: red;
  margin-top: 10px;
}
</style>
