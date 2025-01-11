<template>
  <div class="w-1/2">
    <canvas class="p-10" ref="zipChart"></canvas>
  </div>
</template>

<script setup>
// import onMounted from Vue to run code when the SFC is mounted to the DOM
import { ref, onMounted } from 'vue'
// importing modules from Chart.js for displaying charts
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

// defining label and chartData props for the SFC
const props = defineProps({
  label: Array,
  chartData: Array,
});

// zipChart variable for the Chart to bind to
const zipChart = ref(null);

// creating a new Chart when the SFC is mounted to the DOM
onMounted(() => {
  new Chart(zipChart.value, {
    type: 'doughnut',
    data: {
      labels: props.label,
      datasets: [
        {
          borderWidth: 1,
          data: props.chartData // Update this line
        }
      ]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        title: {
          display: true,
          text: 'Clients by Zip Code'
        }
      },
      responsive: true,
      maintainAspectRatio: true
    }
  })
});
</script>
