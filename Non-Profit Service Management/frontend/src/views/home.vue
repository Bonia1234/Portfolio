<!-- This is the home view - which shows a dashboard -->
<template>
  <main>
    <div>
      <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
        Dashboard
      </h1>
      <br />
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
        <div class="ml-10"></div>
        <div class="flex flex-col col-span-2">
          <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
              Events Attendance
          </h1>
      
          <div v-if="!data.recentEvents.length" class="flex justify-center mt-10">No events found.</div>
          <table v-if="data.recentEvents.length" class="min-w-full shadow-md rounded">
            <thead class="bg-gray-50 text-xl">
              <tr class="p-4 text-left">
                <th class="p-4 text-left">Event Name</th>
                <th class="p-4 text-left">Event Date</th>
                <th class="p-4 text-left">Number of Attendees</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-300"> 
              <tr
                @click="editEvent(event._id)"
                v-for="event in data.recentEvents"
                :key="event._id"
              >
                <td class="p-2 text-left">{{ event.name }}</td>
                <td class="p-2 text-left">{{ formatDate(event.date) }}</td>
                <td class="p-2 text-left">{{ event.attendees.length }}</td>
              </tr>
            </tbody>
          </table>
          
          <div v-if="data.recentEvents.length">
            <barChart
              v-if="!data.loading && !data.error"
              :label="data.labels"
              :chart-data="data.chartData"
            ></barChart>

            <!-- Start of loading animation -->
            <div class="mt-40" v-if="data.loading">
              <p
                class="text-6xl font-bold text-center text-gray-500 animate-pulse"
              >
                Loading...
              </p>
            </div>
            <!-- End of loading animation -->

            <!-- Start of error alert -->
            <div class="mt-12 bg-red-50" v-if="data.error">
              <h3 class="px-4 py-1 text-4xl font-bold text-white bg-red-800">
                {{ data.error.title }}
              </h3>
              <p class="p-4 text-lg font-bold text-red-900">
                {{ data.error.message }}
              </p>
            </div>
            <!-- End of error alert -->
          </div>
        </div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
        <div class="ml-10"></div>
        <div class="flex flex-col col-span-2">
          <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
              Clients by Zip Code
          </h1>
          
          <div v-if="!data.zips.length" class="flex justify-center mt-10">No clients found.</div>
          <table v-if="data.zips.length" class="min-w-full shadow-md rounded">
            <thead class="bg-gray-50 text-xl">
              <tr class="p-4 text-left">
                <th class="p-4 text-left">Zip Number</th>
                <th class="p-4 text-left">Client Count</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-300">
              <tr
                v-for="zip in data.zips"
                :key="zip._id"
              >
                <td class="p-2 text-left">{{ zip._id }}</td>
                <td class="p-2 text-left">{{ zip.count }}</td>
              </tr>
            </tbody>
          </table>
          <div v-if="data.zips.length" class="flex justify-center mt-10">
            <ZipChart
              v-if="!data.zipLoading && !data.zipError"
              :label="data.zipLabels"
              :chart-data="data.zipChartData"
            ></ZipChart>

            <!-- Start of loading animation -->
            <div class="mt-40" v-if="data.zipLoading">
              <p
                class="text-6xl font-bold text-center text-gray-500 animate-pulse"
              >
                Loading...
              </p>
            </div>
            <!-- End of loading animation -->

            <!-- Start of error alert -->
            <div class="mt-12 bg-red-50" v-if="data.zipError">
              <h3 class="px-4 py-1 text-4xl font-bold text-white bg-red-800">
                {{ data.zipError.title }}
              </h3>
              <p class="p-4 text-lg font-bold text-red-900">
                {{ data.zipError.message }}
              </p>
            </div>
            <!-- End of error alert -->
          </div>
        </div>
      </div>
    </div> 
  </main>
 
</template>

<script setup>
// importing ref for reactivity and onMounted to run code as the component is mounted to the DOM
import { ref, onMounted } from 'vue'
// importing barChart and ZipChart for the dashboard
import barChart from '../components/barChart.vue'
import ZipChart from '../components/donutZipChart.vue'
// importing functions to get chart data using the API
import { getAttendance, getClientsByZipCode } from '../api/api'

// making the data for the dashboard reactive and accessible to the template
const data = ref({
  recentEvents: [],
  zips: [],
  labels: ['event1', 'event2', 'event3', 'event4', 'event5'],
  chartData: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
  zipLabels: [],
  zipChartData: [],
  loading: false,
  error: null,
  zipLoading: false,
  zipError: null
});

// getting chart data when the SFC is mounted to the DOM
onMounted(() => {
  getAttendanceData();
  getZipData();
});


async function getAttendanceData() {
  try {
    data.value.error = null
    data.value.loading = true
    
    const attendance = await getAttendance();
    data.value.recentEvents = attendance;
    data.value.labels = attendance.map(
      (item) => `${item.name} (${formatDate(item.date)})`
    )
    data.value.chartData = attendance.map((item) => item.attendees.length)
  } catch (err) {
    if (err.response) {
      // client received an error response (5xx, 4xx)
      data.value.error = {
        title: 'Server Response',
        message: err.message
      }
    } else if (err.request) {
      // client never received a response, or request never left
      data.value.error = {
        title: 'Unable to Reach Server',
        message: err.message
      }
    } else {
      // There's probably an error in your code
      data.value.error = {
        title: 'Application Error',
        message: err.message
      }
    }
  }
  data.value.loading = false
}

async function getZipData() {
  try {
    data.value.zipError = null
    data.value.zipLoading = true
    
    const zipdata = await getClientsByZipCode();
    data.value.zips = zipdata;
    data.value.zipLabels = zipdata.map((item) => item._id)
    data.value.zipChartData = zipdata.map((item) => item.count)
  } catch (err) {
    if (err.response) {
      // client received an error response (5xx, 4xx)
      data.value.zipError = {
        title: 'Server Response',
        message: err.message
      }
    } else if (err.request) {
      // client never received a response, or request never left
      data.value.zipError = {
        title: 'Unable to Reach Server',
        message: err.message
      }
    } else {
      // There's probably an error in your code
      data.value.zipError = {
        title: 'Application Error',
        message: err.message
      }
    }
  }
  data.value.zipLoading = false
}

// method called to format the event date
function formatDate(date) {
  const isoDate = new Date(date);
  const year = isoDate.getUTCFullYear();
  const month = String(isoDate.getUTCMonth() + 1).padStart(2, '0');
  const day = String(isoDate.getUTCDate()).padStart(2, '0');
  return `${month}/${day}/${year}`;
}
</script>
