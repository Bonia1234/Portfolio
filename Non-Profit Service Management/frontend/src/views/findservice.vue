<!-- This view shows a list of services. Users can search for services and click on a service to be redirected to another component that displays the service's details -->
<template>
  <main>
    <!-- Page header -->
    <div>
      <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
        Find Services
      </h1>
    </div>

    <!-- Search fields and buttons -->
    <div class="px-10 pt-20">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
        <h2 class="text-2xl font-bold">Search Service By</h2>
        <!-- Dropdown to choose search criteria -->
        <div class="flex flex-col">
          <select
            class="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            v-model="searchBy">
            <option value="Service Name">Service Name</option>
            <option value="Service Description">Service Description</option>
          </select>
        </div>

        <!-- Input fields for search -->
        <div class="flex flex-col" v-if="searchBy === 'Service Name'">
          <label class="block">
            <input type="text"
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              v-model="name" @keyup.enter="handleSubmitForm" placeholder="Enter service name" />
          </label>
        </div>
        <div class="flex flex-col" v-if="searchBy === 'Service Description'">
          <label class="block">
            <input type="text"
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              v-model="description" @keyup.enter="handleSubmitForm" placeholder="Enter service description" />
          </label>
        </div>
      </div>

      <!-- Buttons for search and clearing search -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
        <div></div>
        <div></div>
        <div class="mt-5 grid-cols-2">
          <button class="mr-10 border border-red-700 bg-white text-red-700 rounded" @click="loadData" type="submit">
            Clear Search
          </button>
          <confirmation class="bg-red-700 text-white rounded" @ChildModalsubmit="handleSubmitForm" type="submit">
            Search Service
          </confirmation>
        </div>
      </div>
    </div>

    <hr class="mt-10 mb-10" />

    <!-- Displaying the list of services -->
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
      <div class="ml-10">
        <h2 class="text-2xl font-bold">List of Services</h2>
        <h3 class="italic">Click table row to view service details</h3>
      </div>
      <div class="flex flex-col col-span-2">
        <table class="min-w-full shadow-md rounded">
          <thead class="bg-gray-50 text-xl">
            <tr>
              <th class="p-4 text-left" style="width: 25%;">Service Name</th>
              <th class="p-4 text-left" style="width: 75%;">Service Description</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-300">
            <tr
              v-for="service in services"
              :key="service._id"
              class="cursor-pointer"
              :class="{ 'hoverRow': hoverId === service._id }"
              @mouseenter="hoverId = service._id"
              @mouseleave="hoverId = null"
              @click="$router.push({ name: 'servicedetails', params: { id: service._id } })"
            >
              <td class="p-4 text-left">{{ service.name }}</td>
              <td class="p-4 text-left text-sm">{{ service.description }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getServices, searchServices } from '../api/api';
import { useToast } from 'vue-toastification';

import confirmation from '../components/confirmation.vue';

// Set up toast for notifications
const toast = useToast();

// Variables for the services, search criteria, and input fields
const services = ref(null);
const searchBy = ref('');
const name = ref('');
const description = ref('');
const hoverId = ref(null);

// Load initial data when component mounts
async function loadData() {
  // Clear input fields
  searchBy.value = '';
  name.value = '';
  description.value = '';

  try {
    const response = await getServices();
    services.value = response;
  } catch (error) {
    toast.error('Error loading services');
  }
};

// Function to handle the search form submission
async function handleSubmitForm () {
  console.log('running search')
  try {
    let response;
    // Search by service name
    if (searchBy.value === 'Service Name' && name.value) {
      response = await searchServices({ searchBy: 'name', name: name.value });
    }
    // Search by service description
    else if (searchBy.value === 'Service Description' && description.value) {
      response = await searchServices({ searchBy: 'description', description: description.value });
    }

    if (response) {
      services.value = response;
    }
  } catch (error) {
    toast.error('Error searching services');
  }
};

// Load data on component mount
onMounted(() =>  {
  loadData()
})
</script>
