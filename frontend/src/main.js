import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { Field, Form, ErrorMessage, defineRule, configure } from 'vee-validate';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import '../src/assets/css/fontawesome-all.min.css'
import 'animate.css/animate.min.css'
import '../src/assets/scss/style.scss'
import 'swiper/css';
import 'swiper/css/effect-fade';

const app = createApp(App);

app.component('Field', Field);
app.component('Form', Form);
app.component('ErrorMessage', ErrorMessage);

app.use(router);


app.mount("#app");
