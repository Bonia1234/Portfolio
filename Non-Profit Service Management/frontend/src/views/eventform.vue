<template>
  <!-- While changing the file the template section remains the same-->
  <main>
    <!--Main page title-->
    <div>
      <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">
        Create New Event
      </h1>
    </div>
    <div class="px-10 py-20">
      <form @submit.prevent>
        <!--Form containor for uploaded information-->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
          <h2 class="text-2xl font-bold">Event Details</h2>
          <div class="flex flex-col">
            <label class="block">
              <!-- Event Details section area-->
              <span class="text-gray-700">Event Name</span>
              <span style="color: #ff0000">*</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.name" />
            </label>
            <span v-if="v$.name.$error" class="text-red-500">
              Event Name is required
            </span>
          </div>
          <!-- Creating event while adding the title-->
          <div class="flex flex-col">
            <label class="block">
               <!-- Creating event while adding the date-->
              <span class="text-gray-700">Date</span>
              <span style="color: #ff0000">*</span>
              <input
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.date" type="date" />
            </label>
            <!-- Error messages for incorrect date inputs-->
            <span v-if="v$.date.$error" class="text-red-500">
              <span v-if="v$.date.required.$invalid">Event Date is required</span>
              <span v-else-if="!v$.date.required.$invalid && v$.date.validDate.$invalid">
                Event Date must be a valid date
              </span>
              <span
                v-else-if="!v$.date.required.$invalid && !v$.date.validDate.$invalid && v$.date.notBeforeToday.$invalid">
                New Event Date cannot be in the past.
              </span>
            </span>
            <!-- Adding space to maintain layout outline-->
          </div>
          <div></div>
          <div></div>
          <div class="flex col-span-2 flex-col">
            <label class="block">
              <!-- Labeling the event details description area-->
              <span class="text-gray-700">Description</span>
              <!-- Textarea input bound to event.description using v-model -->
              <textarea
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                rows="2" v-model="event.description"></textarea>
            </label>
          </div>
        </div>
        <!-- This section is for services offered at events-->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10 mt-10">
          <h2 class="text-2xl font-bold">Services Offered at Event</h2>
          <div class="flex flex-col grid-cols-3">
            <div>
              <!-- Conditional rendering if there are active services -->
              <ul v-if="activeServices.length" class="space-y-2">
                 <!-- Loop through active services to display checkboxes -->
                <li v-for="service in activeServices" :key="service._id" :data-service-id="service._id"
                  class="rounded-lg border border-gray-300 p-2 hover:bg-gray-100 transition-colors relative">
                  <label class="block w-full h-full">
                    <!-- Checkbox for each service, bound to event.services array using v-model -->
                    <input type="checkbox" :id="service._id" :value="service._id"
                      :checked="event.services.includes(service._id)" v-model="event.services"
                      class="rounded border-gray-300 text-indigo-600 shadow-sm focus:border-indigo-300 focus:ring focus:ring-offset-0 focus:ring-indigo-200 focus:ring-opacity-50 mr-2">
                      <!-- Display the name of the service -->
                    <span class="font-medium">{{ service.name }}</span>
                  </label>
                </li>
              </ul>
              <!-- Message displayed if no services are available -->
              <p v-else class="text-gray-600">No Active Services Available</p>
            </div>
          </div>
        </div>
         <!-- Address input section -->
        <div class="mt-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
          <h2 class="text-2xl font-bold">Address</h2>
          <div class="flex flex-col">
            <label class="block">
              <!-- Address Line 1 Input Field -->
              <span class="text-gray-700">Address Line 1</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.address.line1" />
            </label>
          </div>
          <div class="flex flex-col">
            <label class="block">
              <!-- Address Line 2 Input Field -->
              <span class="text-gray-700">Address Line 2</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.address.line2" />
            </label>
          </div>
          <!-- City Input Field -->
          <div class="flex flex-col">
            <label class="block">
              <span class="text-gray-700">City</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.address.city" />
            </label>
          </div>
          <div></div>
          <!-- Input County Field -->
          <div class="flex flex-col">
            <label class="block">
              <span class="text-gray-700">County</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.address.county" />
            </label>
          </div>
          <!-- Input Zipcode Field -->
          <div class="flex flex-col">
            <label class="block">
              <span class="text-gray-700">Zip Code</span>
              <input type="text"
                class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
                v-model="event.address.zip" />
            </label>
          </div>
        </div>
<!-- Submit Button Section -->
        <div class="mt-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
          <div></div>
          <!-- Submit button to add the event -->
          <div class="flex justify-between mr-20">
            <confirmation class="bg-red-700 text-white rounded" type="submit"
              @ChildModalsubmit = "handleSubmitForm">
              Add New Event
            </confirmation>
          </div>
        </div>
      </form>
    </div>
  </main>
</template>
<!-- We start using composition API using the script setup function-->
<script setup>
import { ref, computed, onMounted } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import { getServices, createEvent } from '../api/api'
import { useToast } from 'vue-toastification'


import confirmation from '../components/confirmation.vue'

import { useRouter } from 'vue-router'
const router = useRouter()

// The webpage will recieve toast notifications
const toast = useToast()

// Using reactive we are defining reactive data with composition API
const event = ref({
  name: null,
  description: null,
  date: null,
  services: [],
  address: {
    line1: null,
    line2: null,
    city: null,
    county: null,
    zip: null
  },
  attendees: []
})

const activeServices = ref([])


const validDate = (value) => {
      const date = new Date(value)
      return !isNaN(date)
    }

// prevents form submission if new event has a date before the current date
const notBeforeToday = (value) => {
      const today = new Date()
      return value >= today.toISOString().split('T')[0]
    }
    
const validations = computed(() =>({
    // validations
    name: { required },
    date: {
      required,
      validDate,
      notBeforeToday
    },
      
    
  })) 

  
// Register Vuelidate
const v$ = useVuelidate(validations, event);



// The data will load on to the onmounted function
onMounted(async () => {
  try {
    const response = await getServices()
    activeServices.value = response.filter(item => item.status === "Active")
  } catch (error) {
    toast.error(error)
  }
})

// This section will handle the method to handle the submission form
async function  handleSubmitForm() {
  v$.value.$validate()

  if (v$.value.$error) {
    toast.error('Please fix input field errors')
    return
  }
  

  try {
    const response = await createEvent(event.value);
    router.push('/findevents')
    toast.success(response)
    
  } catch (error) {
    toast.error('Error creating new event:', error)
  }
}
</script>
