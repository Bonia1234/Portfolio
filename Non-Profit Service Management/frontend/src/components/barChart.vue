<template>
  <div>
    <!-- 'Canvas' HTML element referencing 'AttendanceChart' property -->
    <canvas class="p-10" ref="AttendanceChart"></canvas>
  </div>
</template>




<!-- Converted to COMPOSITION API -->
<!-- Using script setup -->
<!-- Started conversion by commenting out options API script and migrate code into script setup piece by piece by identifying the imports, properties, props, functions -->

<script setup>

// imported ref and onMounted
import { ref, onMounted } from 'vue'
import { Chart, registerables } from 'chart.js'
import { Colors } from 'chart.js';

Chart.register(...registerables)
Chart.register(Colors);


// defining Props and AttendanceChart
// Removed anywhere that includes 'this.' and replaced with .value in the end
const props = defineProps({
    label: {
      type: Array
    },
    chartData: {
      type: Array
    }
})


// 'Canvas' HTML element referencing 'AttendanceChart' property
const AttendanceChart = ref(null)



// Using child props to inherit parent's data when creating a new bar chart
onMounted(async () => {
    await new Chart(AttendanceChart.value, {
      type: 'bar',
      data: {
        labels: props.label,
        datasets: [
          {
            borderWidth: 1,

            // defining legend label 'Number of Clients', which relates to the bar values of the y-axis 
            label: "Number of Clients",
            
            // using parent's hardcoded data for y-axis (representing number of clients)
            data: props.chartData,

            // making bar color red
            backgroundColor: '#C70733',
            
          }
        ]
      },


      options: {
        scales: {
          y: {
            ticks: {
              stepSize: 1,

              // Defining font size for y-axis tick values
              font:{
                size: 15
              }
            },

            // Defining and displaying y-axis title 'Number of Clients'
            title: {
              display: true,
              text: 'Number of Clients',
              // Defining font size for y-axis title 'Number of Clients' 
              font:{
                size: 20
              }
            },
            
          },


          x: {
            ticks: {
              // Defining font size for x-axis tick values
              font:{
                size: 15
              }
            },
            gridLines: {
              display: false
            },

            // Defining and displaying x-axis title 'Events'
            title:{
              display: true,
              text: 'Events',
              
              // Defining font size for x-axis title 'Events' 
              font:{
                size: 20
              }
            }
          }
        },


        plugins: {
          legend: {

            // Displaying legend and positioning it to the bottom
            display: true,
            position: "bottom",
                        
          },
          title: {
            display: true,
            text: 'Attendance Chart',

            // Defining font size for title 'Attendance Chart'
            font:{
              size: 30
            }
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    })
  }) 



</script>


<!-- REFERENCES -->
<!-- onMounted - https://vuejs.org/api/composition-api-lifecycle.html -->
<!-- addressing chart errors, referencing a javascript example - https://www.geeksforgeeks.org/chartjs-failed-to-create-chart-cant-acquire-context-from-the-given-item/ -->
<!-- chart configurations (font, legend, position, title) https://www.chartjs.org/docs/latest/ -->