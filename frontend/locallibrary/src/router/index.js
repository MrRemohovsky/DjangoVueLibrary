import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "@/pages/HomePage.vue";
import BookList from "@/pages/BookList.vue";
import AuthorList from "@/pages/AuthorList.vue";
import BookDetail from "@/pages/BookDetail.vue";
import AuthorDetail from "@/pages/AuthorDetail.vue";

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/book-list',
    name: 'BookList',
    component: BookList
  },
  {
    path: '/author-list',
    name: 'AuthorList',
    component: AuthorList
  },
  {
    path: '/book-detail/:pk',
    name: 'BookDetail',
    component: BookDetail
  },
  {
    path: '/author-detail/:pk',
    name: 'AuthorDetail',
    component: AuthorDetail
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
