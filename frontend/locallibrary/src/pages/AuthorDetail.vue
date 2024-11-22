<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios";
import {useRoute} from "vue-router";

const author = ref({});
const books = ref([])
const route = useRoute()
onMounted( () => {
  const pk = route.params.pk;
  axios.defaults.withCredentials = true;
  axios.get(`http://localhost:8000/catalog/api/author-detail/${pk}/`)
  .then(response => {
    author.value = response.data
    books.value = response.data.books
  })
});
</script>

<template>
  <div>
    <h1>Author {{ author.first_name }} {{ author.last_name }}</h1>
  </div>
  <div style="margin-left:20px;margin-top:20px">
    <h4>Books</h4>
    <div v-for="book in books" :key="book.id">
      <hr>
      <p>
        <a :href="`/book-detail/${book.id}`">{{ book.title }}</a>
      </p>
      <p>{{ book.summary }}</p>
    </div>
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
