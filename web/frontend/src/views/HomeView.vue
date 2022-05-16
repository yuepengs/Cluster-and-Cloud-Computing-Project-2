<template>
  <div class="flex flex-col h-screen max-h-screen">
    <!-- header -->
    <div class="z-10 flex justify-center realtive bg-[#094183] bg-unimelb-logo bg-no-repeat pl-8 pr-8 px-4 pt-4 pb-24">
      <!-- lga info -->
      <div class="absolute
        flex
        flex-col
        lg:flex-row
        bg-white
        gap-y-8
        gap-x-8
        px-4
        pt-4
        pb-3
        rounded-md"
      >
        <!-- flex item #1 -->
        <div class="flex flex-col">
            <h3 class="text-xs mb-1 uppercase">LGA Name</h3>
            <span class="text-xl" id="lganame"></span>
        </div>
        <!-- flex item #2 -->
        <div class="flex flex-col">
            <h3 class="text-xs mb-1 uppercase">Positive Sentiment</h3>
            <span class="text-xl" id="positive_count"></span>
        </div>
        <!-- flex item #2 -->
        <div class="flex flex-col">
            <h3 class="text-xs mb-1 uppercase">Negative Sentiment</h3>
            <span class="text-xl" id="negative_count"></span>
        </div>
        <!-- flex item #3 -->
        <div class="flex flex-col">
            <h3 class="text-xs mb-1 uppercase">Tweet Total Number</h3>
            <span class="text-xl" id="total_count"></span>
        </div>
      </div>
      <!-- button -->
      <div class="absolute top-8 right-8 gap-y-16 gap-x-16">
        <van-button class="z-999 bg-white" @click="goGraphPage" type="default">Graph Page</van-button>
      </div>
    </div>
    <!-- Map Content -->
    <div id="mapid" class="h-full z-10">
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

import leaflet from "leaflet"
import polygonJs from "../assets/map.json"
import { onMounted } from "vue"

export default {
  name: 'HomeView',
  setup() {
    let mymap;
    let whiteLayer = leaflet.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png', {
        maxZoom: 25,
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });
    let darkLayer = leaflet.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
        maxZoom: 20,
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });
    let satLayer = leaflet.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
        maxZoom: 20,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });
    let baseMaps = {
        "White Layer": whiteLayer,
        "Dark Layer": darkLayer,
        "Satellite Layer": satLayer,
    };
    function highlightFeature(e) {
      var layer = e.target;
      layer.setStyle({
        weight: 4,
        color: "#666",
        dashArray: "",
        fillOpacity: 0.7
      })
      layer.bindPopup(
            "<ol><li><b>Local Government Area:          </b>" + layer.feature.properties.vic_lga__3 + 
            "</li><li><b>Positive Tweet Density:        </b>" + layer.feature.properties.senti_pos_dens +
            "</li><li><b>Negative Tweet Density:        </b>" + layer.feature.properties.senti_neg_dens +
            "</li><li><b>Tweet Total Number:            </b>" + layer.feature.properties.total_tweets + 
            "</li><li><b>Rent Median:                   </b>" + layer.feature.properties.rent_median + 
            "</li><li><b>Lower Income Number:           </b>" + layer.feature.properties.low_income_card + 
            "</li></ol>")

      // show info on header
      document.getElementById("lganame").innerHTML = layer.feature.properties.vic_lga__3;
      document.getElementById("positive_count").innerHTML = layer.feature.properties.senti_pos_count;
      document.getElementById("negative_count").innerHTML = layer.feature.properties.senti_neg_count;
      document.getElementById("total_count").innerHTML = layer.feature.properties.total_tweets;
    }
    function resetNegHighlight(e){
      negativeLayer.resetStyle(e.target);
    }
    function resetPosHighlight(e){
      positiveLayer.resetStyle(e.target);
    }
    function resetRentHighlight(e){
      rentLayer.resetStyle(e.target);
    }
    function resetIncomeHighlight(e){
      incomeLayer.resetStyle(e.target);
    }
    function getPosColor(d) {
      return  d > 0.50  ? '#800026' :
              d > 0.47  ? '#BD0026' :
              d > 0.43  ? '#E31A1C' :
              d > 0.40  ? '#FC4E2A' :
              d > 0.35  ? '#FD8D3C' :
              d > 0.30  ? '#FEB24C' :
              d > 0.25  ? '#FED976' :
                          '#FFEDA0';
    }
    function getNegColor(d) {
      return  d > 0.40  ? '#800026' :
              d > 0.37  ? '#BD0026' :
              d > 0.33  ? '#E31A1C' :
              d > 0.30  ? '#FC4E2A' :
              d > 0.25  ? '#FD8D3C' :
              d > 0.20  ? '#FEB24C' :
              d > 0.15  ? '#FED976' :
                          '#FFEDA0';
    }
    function getRentColor(d) {
      return  d > 500  ? '#800026' :
              d > 460  ? '#BD0026' :
              d > 420  ? '#E31A1C' :
              d > 400  ? '#FC4E2A' :
              d > 380  ? '#FD8D3C' :
              d > 360  ? '#FEB24C' :
              d > 340  ? '#FED976' :
                          '#FFEDA0';
    }
    function getIncomeColor(d) {
      return  d > 7000  ? '#800026' :
              d > 6000  ? '#BD0026' :
              d > 5000  ? '#E31A1C' :
              d > 4000  ? '#FC4E2A' :
              d > 3000  ? '#FD8D3C' :
              d > 2000  ? '#FEB24C' :
              d > 1000  ? '#FED976' :
                          '#FFEDA0';
    }
    function styleNeg(feature) {
        return {
            fillColor: getNegColor(feature.properties.senti_neg_dens),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.4
        };
    }
    function stylePos(feature) {
        return {
            fillColor: getPosColor(feature.properties.senti_pos_dens),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.4
        };
    }
    function styleRent(feature) {
        return {
            fillColor: getRentColor(feature.properties.rent_median),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.4
        };
    }
    function styleIncome(feature) {
        return {
            fillColor: getIncomeColor(feature.properties.low_income_card),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.4
        };
    }
    function onNegEachFeature(feature, layer) {
      layer.on({
          mouseover: highlightFeature,
          mouseout: resetNegHighlight,
          click: highlightFeature
        }
      )
    }
    function onPosEachFeature(feature, layer) {
      layer.on({
          mouseover: highlightFeature,
          mouseout: resetPosHighlight,
          click: highlightFeature
        }
      )
    }
    function onRentEachFeature(feature, layer) {
      layer.on({
          mouseover: highlightFeature,
          mouseout: resetRentHighlight,
          click: highlightFeature
        }
      )
    }
    function onIncomeEachFeature(feature, layer) {
      layer.on({
          mouseover: highlightFeature,
          mouseout: resetIncomeHighlight,
          click: highlightFeature
        }
      )
    }
    let negativeLayer = leaflet.geoJSON(polygonJs, {
        onEachFeature: onNegEachFeature, 
        style: styleNeg
    })
    let positiveLayer = leaflet.geoJSON(polygonJs, {
        onEachFeature: onPosEachFeature,
        style: stylePos
    })
    let rentLayer = leaflet.geoJSON(polygonJs, {
      onEachFeature: onRentEachFeature,
      style: styleRent
    })
    let incomeLayer = leaflet.geoJSON(polygonJs, {
      onEachFeature: onIncomeEachFeature,
      style: styleIncome
    })
    let overlayMaps = {
      "Positive Sentiment" : positiveLayer,
      "Nagetive Sentiment" : negativeLayer,
      "Rent" : rentLayer,
      "Lower Income" : incomeLayer,
    };

    onMounted(() => {
      mymap = leaflet.map('mapid');
      mymap.setView([-37.9536, 145.2631], 9);
      whiteLayer.addTo(mymap);
      positiveLayer.addTo(mymap);
      leaflet.control.layers(baseMaps, overlayMaps, {
        collapsed: false
      }).addTo(mymap);
    })
  },
  methods: {
    goGraphPage () {
      this.$router.push('graph');
    }
  }
}
</script>