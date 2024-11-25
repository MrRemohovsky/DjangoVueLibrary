<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const password2 = ref('');
const errorMessage = ref(null);

const router = useRouter();

onMounted(() => {
  axios.defaults.withCredentials = true;

  const registerUser = async () => {
    if (password.value !== password2.value) {
      errorMessage.value = 'Пароли не совпадают!';
      return;
    }

    try {
      await axios.post('http://127.0.0.1:8000/api/accounts/register/', {
        username: username.value,
        email: email.value,
        password: password.value,
      });
      alert('Регистрация успешна!');

      router.push('/login');
    } catch (error) {
      if (error.response && error.response.data) {
        errorMessage.value = error.response.data.detail || 'Ошибка регистрации';
      } else {
        errorMessage.value = 'Сетевая ошибка. Попробуйте ещё раз.';
      }
    }
  };

  const form = document.querySelector('form');
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    registerUser();
  });
});
</script>

<template>
  <div>
    <h1>Регистрация</h1>
    <form>
      <div>
        <label for="username">Имя пользователя</label>
        <input v-model="username" id="username" required />
      </div>
      <div>
        <label for="email">Email</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <div>
        <label for="password2">Повторите пароль</label>
        <input v-model="password2" id="password2" type="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<style scoped>
.error {
  color: red;
  margin-top: 10px;
}
</style>
