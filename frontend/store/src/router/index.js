import {createWebHistory, createRouter} from "vue-router";
import Home from "@/views/Home.vue";


const routes = [
    {
        path: "/",
        name: "Home",
        meta: {layout: 'main'},
        component: Home,
    },
    {
        path: "/login",
        name: "Login",
        meta: {layout: 'empty'},
        component: () => import('../views/Login'),
    },
        {
        path: "/register",
        name: "Register",
        meta: {layout: 'empty'},
        component: () => import('../views/Register'),
    },
        {
        path: "/profile",
        name: "Profile",
        meta: {layout: 'main'},
        component: () => import('../views/Profile'),
    },
    {
        path: "/category/:slug",
        name: "Category",
        component: () => import('../views/Category'),
        meta: {layout: 'main'},
        props: true

    },
    {
        path: "/add_product",
        name: "AddProduct",
        component: () => import('../views/AddProduct'),
        meta: {layout: 'main'},
        props: true

    },
    {
        path: "/product/:slug",
        name: "Single",
        component: () => import('../views/Single'),
        meta: {layout: 'main'},
        props: true

    },
    {
        path: "/cart",
        name: "Cart",
        component: () => import('../views/Cart'),
        meta: {layout: 'main'},
        props: true

    },
    {
        path: "/about",
        name: "About",
        component: () => import('../views/About'),
        meta: {layout: 'main'},
    },
    {
        path: "/:catchAll(.*)",
        component: () => import('../views/NotFound'),
        meta: {layout: 'main'},
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;