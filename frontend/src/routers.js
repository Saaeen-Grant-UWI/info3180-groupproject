import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import Register from '@/views/Register.vue'
import Login from '@/views/Login.vue'
import Logout from '@/views/Logout.vue'
import UserProfile from '@/views/UserProfile.vue'
import NewProfile from '@/views/NewProfile.vue'
import ProfileDetails from '@/views/ProfileDetails.vue'
import FavouritesReport from '@/views/FavouritesReport.vue'
import { name } from "@vue/eslint-config-prettier/skip-formatting";


const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: HomePage
  // },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/users/:user_id',
    name: 'UserProfile',
    component: UserProfile,
    props: true
  },
  {
    path: '/profiles/new',
    name: 'NewProfile',
    component: NewProfile
  },
  {
    path: '/profiles/:profile_id',
    name: 'ProfileDetails',
    component: ProfileDetails,
    props: true
  },
  {
    path: '/profiles/favourites',
    name: 'FavouritesReport',
    component: FavouritesReport
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
