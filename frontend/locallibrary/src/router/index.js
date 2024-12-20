import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "@/pages/HomePage.vue";
import BookList from "@/pages/BookList.vue";
import AuthorList from "@/pages/AuthorList.vue";
import BookDetail from "@/pages/BookDetail.vue";
import AuthorDetail from "@/pages/AuthorDetail.vue";
import RegisterPage from "@/pages/RegisterPage.vue";
import LoginPage from "@/pages/LoginPage.vue";
import BorrowerPage from "@/pages/BorrowerPage.vue";
import AllBorrowerPage from "@/pages/AllBorrowerPage.vue";
import ResetPasswordPage from "@/pages/ResetPasswordPage.vue";
import ResetPasswordConfirmPage from "@/pages/ResetPasswordConfirmPage.vue";

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
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/borrower',
    name: 'BorrowerPage',
    component: BorrowerPage
  },
  {
    path: '/all_borrower',
    name: 'AllBorrowerPage',
    component: AllBorrowerPage
  },
  {
    path: '/reset_password_page',
    name: 'ResetPasswordPage',
    component: ResetPasswordPage
  },
  {
    path: '/reset_password_confirm_page/:token',
    name: 'ResetPasswordConfirmPage',
    component: ResetPasswordConfirmPage,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
