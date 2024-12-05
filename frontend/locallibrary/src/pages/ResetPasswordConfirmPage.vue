<template>
  <div>
    <h1>Введите новый пароль</h1>
    <form @submit.prevent="changePassword">
      <div>
        <label for="password">Новый пароль</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <div>
        <label for="confirmPassword">Подтвердите новый пароль</label>
        <input v-model="confirmPassword" id="confirmPassword" type="password" required />
      </div>
      <button type="submit">Сменить пароль</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from "axios";
import { useRoute } from 'vue-router';

export default {
  name: 'ResetPasswordConfirmPage',
  setup() {
    const password = ref('');
    const confirmPassword = ref('');
    const errorMessage = ref(null);
    const successMessage = ref(null);
    const route = useRoute();
    const token = route.params.token;

    const changePassword = async () => {
      if (password.value !== confirmPassword.value) {
        errorMessage.value = 'Пароли не совпадают';
        successMessage.value = null;
        return;
      }
      try {
        await axios.post(
          `http://127.0.0.1:8000/api/accounts/reset_password_confirm/${token}/`,
          { new_password: password.value }
        );

        successMessage.value = 'Пароль успешно изменён';
        errorMessage.value = null;
        password.value = '';
        confirmPassword.value = '';
      } catch (error) {
        if (error.response && error.response.data) {
          errorMessage.value = error.response.data.detail || 'Ошибка при смене пароля';
        } else {
          errorMessage.value = 'Сетевая ошибка. Попробуйте ещё раз.';
        }
        successMessage.value = null;
      }
    };

    return {
      password,
      confirmPassword,
      errorMessage,
      successMessage,
      changePassword,
    };
  },
};
</script>

<style scoped>
.error {
  color: red;
  margin-top: 10px;
}
.success {
  color: green;
  margin-top: 10px;
}
</style>
