import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    //hay que hacer una pagina de bienvenidos
    {
      path: '/Registro',
      name: 'registro',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Registro.vue')
    },
    {
      path: '/Inicio',
      name: 'inicio',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Login.vue')
    },
    {
      path: '/Recuperar',
      name: 'recuperar',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Recuperar.vue')
    },
    {
      path: '/Perfil',
      name: 'perfil',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/perfil.vue')
    },
    {
      path: '/homepage',
      name: 'homepage',
      component: () => import('../views/homepage.vue')
    }
  ]
})

export default router
