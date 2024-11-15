<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios";

const bookList = ref([]);

onMounted( () => {
  axios.defaults.withCredentials = true;
  axios.get('http://localhost:8000/catalog/api/book-list/')
  .then(response => {
    bookList.value = response.data;
  })
});
</script>

<template>
  <div>
    <h1>Book List</h1>
      <li v-for="book in bookList" :key="book.id">
        <a :href="book.absolute_url">{{ book.title }}</a>
      </li>
  </div>
</template>

<style scoped>
h1 {
  color: #333;
  font-size: 2rem;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}

a {
  text-decoration: none;
  color: #2a9d8f;
}

a:hover {
  text-decoration: underline;
}
</style>
