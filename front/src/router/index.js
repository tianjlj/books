import { createRouter, createWebHistory } from 'vue-router' 

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'layout',
            component: () => import('../views/layout.vue'),
            children: [
                {
                    path: '/apis',
                    name: 'apis',
                    component: ()=>import('../views/apis/api_info.vue')
                }
            ]
        }
    ]
})

export default router
