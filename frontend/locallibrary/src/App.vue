<template>
  <div id="app">
    <Sidebar />
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from './components/SideBar.vue';

export default {
  name: 'App',
  components: {
    Sidebar
  }
};
</script>

<style scoped>
#app {
  display: flex;
}

.content {
  flex-grow: 1;
  padding: 20px;
}
</style>
