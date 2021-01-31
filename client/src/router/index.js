import Vue from 'vue';
import Router from 'vue-router';
import Timezone from '../components/Timezone.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Timezone',
      component: Timezone,
    },
  ],
});
