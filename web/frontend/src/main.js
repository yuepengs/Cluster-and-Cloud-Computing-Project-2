/*
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
*/

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import { Button } from "vant"
import ECharts from "vue-echarts";
import "echarts/lib/chart/pie";
import 'vant/es/button/style/index';

createApp(App).use(ECharts).use(Button).use(router).mount('#app')