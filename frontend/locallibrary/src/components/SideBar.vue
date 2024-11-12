<template>
  <div class="sidebar">
    <ul>
      <li><router-link to="/">Home</router-link></li>

    </ul>
  </div>
</template>

<script>
export default {
  name: 'SideBar'
};
</script>

<style scoped>
.sidebar {
  width: 200px;
  padding: 20px;
  background-color: #f8f9fa;
}
</style>
