<template>

	<div class="flex flex-col h-screen max-h-screen">
		<div class="z-10 flex justify-center realtive bg-[#094183] bg-unimelb-logo bg-no-repeat pl-8 pr-8 px-4 pt-4 pb-24">
			<!-- button -->
      <div class="z-10 absolute top-8 right-36 gap-y-24 gap-x16">
        <van-button class="z-999 bg-white" @click="updateData" type="default">Update Data</van-button>
      </div>
      
			<div class="z-10 absolute top-8 right-8 gap-y-24 gap-x16">
				<van-button class="z-999 bg-white" @click="goHomePage" type="default">Home Page</van-button>
			</div>
		</div>
		<div class="grid grid-cols-2 flex justify-center pt-8 pl-16 pr-16">
      <div class="z-999 h-screen">
				<v-chart class="z-999 chart justify-center h-1/3" :option="option1Hist" />
				<v-chart class="z-999 chart justify-center h-1/3" :option="option2Hist" />
        <v-chart class="z-999 chart justify-center h-1/3" :option="option3Hist" />
			</div>
			<div class="z-999 h-screen">
				<v-chart class="z-999 chart justify-center h-1/3" :option="option1" />
				<v-chart class="z-999 chart justify-center h-1/3" :option="option2" />
        <v-chart class="z-999 chart justify-center h-1/3" :option="option3" />
			</div>
		</div>
    </div>
</template>

<script>
/*
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
*/

import { use } from "echarts/core";
import axios from "axios"
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart from "vue-echarts";

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);


export default({
  name: "HelloWorld",
  components: {
    VChart
  },
  data() {
    return {
      info: null,
      option1: {
        title: {
          text: "Transportation Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [
          {
            name: "Transportation Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 0, name: "Positive Sentiment" },
              { value: 0, name: "Negative Sentiment" },
              { value: 0, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      },
      option2: {
        title: {
          text: "Health Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [
          {
            name: "Health Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 0, name: "Positive Sentiment" },
              { value: 0, name: "Negative Sentiment" },
              { value: 0, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      },
      option3: {
        title: {
          text: "Housing Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [{
            name: "Housing Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 0, name: "Positive Sentiment" },
              { value: 0, name: "Negative Sentiment" },
              { value: 0, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      },
      option1Hist: {
        title: {
          text: "History Transportation Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [
          {
            name: "History Transportation Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 16974, name: "Positive Sentiment" },
              { value: 10142, name: "Negative Sentiment" },
              { value: 17637, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      },
      option2Hist: {
        title: {
          text: "History Health Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [
          {
            name: "History Health Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 1519, name: "Positive Sentiment" },
              { value: 859, name: "Negative Sentiment" },
              { value: 1425, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      },
      option3Hist: {
        title: {
          text: "History Housing Sector",
          left: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"]
        },
        series: [{
            name: "History Housing Sector",
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            data: [
              { value: 15640, name: "Positive Sentiment" },
              { value: 8140, name: "Negative Sentiment" },
              { value: 16347, name: "Neutral Sentiment" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      }
    }
  },
	methods: {
    updateInfo () {
      axios.get('/test_db')
            .then(response => (this.info = response.data))
            .catch(function (error) { 
              console.log(error);
            });
    },
    async updateData () {
      await this.updateInfo();
      this.option1.series[0].data[0].value = this.info[1][1];
      this.option1.series[0].data[1].value = this.info[1][-1];
      this.option1.series[0].data[2].value = this.info[1][0];
      this.option2.series[0].data[0].value = this.info[0][1];
      this.option2.series[0].data[1].value = this.info[0][-1];
      this.option2.series[0].data[2].value = this.info[0][0];
      this.option3.series[0].data[0].value = this.info[2][1];
      this.option3.series[0].data[1].value = this.info[2][-1];
      this.option3.series[0].data[2].value = this.info[2][0];
    },
    goHomePage () {
        this.$router.push('/');
    },
  },
  async created() {
    await axios.get('/test_db')
            .then(response => {
              this.option1.series[0].data[0].value = response.data[1][1];
              this.option1.series[0].data[1].value = response.data[1][-1];
              this.option1.series[0].data[2].value = response.data[1][0];
              this.option2.series[0].data[0].value = response.data[0][1];
              this.option2.series[0].data[1].value = response.data[0][-1];
              this.option2.series[0].data[2].value = response.data[0][0];
              this.option3.series[0].data[0].value = response.data[2][1];
              this.option3.series[0].data[1].value = response.data[2][-1];
              this.option3.series[0].data[2].value = response.data[2][0];
              this.info = response.data;
            })
            .catch(function (error) { 
              console.log(error);
    });
  }
});
</script>
