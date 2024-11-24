<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios";
import {useRoute} from "vue-router";

const book = ref({});
const route = useRoute()
onMounted( () => {
  const pk = route.params.pk;
  axios.defaults.withCredentials = true;
  axios.get(`http://localhost:8000/catalog/api/book-detail/${pk}/`)
  .then(response => {
    book.value = response.data
    console.log(response)
    console.log(book.value)
 })
});
</script>

<template>
  <div>
    <h1>Title: {{ book.title }}</h1>
    <div>
      <div>
        <hr>
        <p>
          <strong>Authors: </strong>
          <span v-for="(author, index) in book.author" :key="author.id">
          <a :href="`/author-detail/${author.id}`">{{ author.first_name }} {{ author.last_name }}</a>
          <span v-if="index < book.author.length - 1">, </span>
          </span>
        </p>
      </div>
      <hr>
      <p><strong>Summary:</strong> {{ book.summary }}</p>
      <hr>
      <p><strong>ISBN:</strong> {{ book.isbn }}</p>
      <div v-for="genre in book.genre" :key="genre.id">
        <hr>
        <p>
          <strong>Genre:</strong> {{ genre.name }}
        </p>
      </div>
      <hr>
      <p><strong>Language:</strong> {{ book.language }}</p>
    </div>
    <hr>
    <div>
      <h4>Copies:</h4>
      <div style="margin-left:20px;margin-top:20px" v-for="copy in book.instance" :key="copy.id">
        <p>
        {{ copy.status === 'a' ? 'Available' : copy.status === 'm' ? 'Maintenance' : copy.status === 'o' ? 'On loan' : 'Reserved' }}
        </p>
        <p v-if="copy.status === 'o'"><strong>Due to be returned:</strong> {{ copy.due_back }}</p>
        <p class="text-muted"><strong>Id:</strong> {{ copy.id }}</p>
        <hr>
      </div>
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
