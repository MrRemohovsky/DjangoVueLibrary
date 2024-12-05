<template>
  <div>
    <h1>Сброс пароля</h1>
    <form @submit.prevent="resetPassword">
      <div>
        <label for="email">Электронная почта</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <button type="submit">Отправить ссылку для сброса пароля</button>
    </form>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from "axios";

export default {
  name: 'ResetPasswordPage',
  setup() {
    const email = ref('');
    const successMessage = ref(null);
    const errorMessage = ref(null);

    const resetPassword = async () => {
      try {
        await axios.post(
          'http://127.0.0.1:8000/api/accounts/reset_password_request/',
          { email: email.value }
        );
        successMessage.value = 'Ссылка для сброса пароля отправлена на вашу почту.';
        errorMessage.value = null;
        email.value = '';
      } catch (error) {
        if (error.response && error.response.data) {
          errorMessage.value = error.response.data.detail || 'Ошибка при сбросе пароля';
        } else {
          errorMessage.value = 'Сетевая ошибка. Попробуйте ещё раз.';
        }
        successMessage.value = null;
      }
    };

    return {
      email,
      successMessage,
      errorMessage,
      resetPassword,
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
