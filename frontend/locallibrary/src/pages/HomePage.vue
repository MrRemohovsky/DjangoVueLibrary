<script setup>
import { ref } from 'vue';

const numBooks = ref(150);
const numInstances = ref(200);
const numInstancesAvailable = ref(120);
const numAuthors = ref(45);
const numVisits = ref(1);
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
