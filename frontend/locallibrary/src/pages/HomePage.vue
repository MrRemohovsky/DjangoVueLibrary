<script setup>
import { ref, onMounted } from 'vue';
import axios from "axios";
const numBooks = ref(0);
const numInstances = ref(0);
const numInstancesAvailable = ref(0);
const numAuthors = ref(0);
const numVisits = ref(0);

onMounted( () => {
  axios.defaults.withCredentials = true;
  axios.get('http://localhost:8000/catalog/api/library-stats/')
  .then(response => {
    const data = response.data;
    numBooks.value = data.num_books;
    numInstances.value = data.num_instances;
    numInstancesAvailable.value = data.num_instances_available;
    numAuthors.value = data.num_authors;
    numVisits.value = data.num_visits;
  })
});


</script>

<template>
  <div class="home">
    <h1>Local Library</h1>

    <p>The library has the following record counts:</p>
    <ul>
      <li><strong>Books:</strong> {{ numBooks }}</li>
      <li><strong>Copies:</strong> {{ numInstances }}</li>
      <li><strong>Copies available:</strong> {{ numInstancesAvailable }}</li>
      <li><strong>Authors:</strong> {{ numAuthors }}</li>
    </ul>

    <p>
      You have visited this page {{ numVisits }}
      <span v-if="numVisits === 1">time</span>
      <span v-else>times</span>
    </p>
  </div>
</template>

<style scoped>
.home {
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
}

ul {
  list-style-type: none;
}

strong {
  font-weight: bold;
}
</style>
