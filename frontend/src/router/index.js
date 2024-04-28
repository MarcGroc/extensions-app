import { createRouter, createWebHistory } from 'vue-router';
import brand from '@/assets/brand/brand.js';


const routes = [
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('../views/pages/404.vue')
    },
    {
        path: '/',
        name: 'Home',
        meta: {
            title: brand.projectName,
            description: brand.description,
            url: brand.url,
            facebook: brand.facebook,
            twitter: brand.twitter,
            instagram: brand.instagram,
            tiktok: brand.tiktok,

        },
        component: () => import('../views/Home.vue'),
    },
    {
        path: '/coming-soon',
        name: 'ComingSoon',
        component: () => import('../views/pages/ComingSoon.vue'),
    },
    {
        path: '/privacy',
        name: 'PrivacyPolicy',
        component: () => import('../views/pages/PrivacyPolicy.vue'),
    },{
        path: '/terms',
        name: 'TermsOfUse',
        component: () => import('../views/pages/Terms.vue'),
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/pages/Login.vue'),
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('../views/pages/Register.vue'),
    },
    {
        path: '/contact'
        , name: 'Contact'
        , component: () => import('../views/pages/Contact.vue')
    }
];

const router = createRouter({
    history: createWebHistory(import.meta.env.VITE_BASE_URL),
    routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.projectName || 'DjaVue - Template';
  next();
});

export default router;
