<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios";

const authorList = ref([]);

onMounted( () => {
  axios.defaults.withCredentials = true;
  axios.get('http://localhost:8000/catalog/api/author-list/')
  .then(response => {
    authorList.value = response.data;
  })
});
</script>

<template>
  <div>
  <h1>Author List</h1>
  <ul>
    <li v-for="author in authorList" :key="author.id">
      <a :href="`/author-detail/${author.id}`">{{ author.first_name }} {{ author.last_name }}</a>
    </li>
  </ul>
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
