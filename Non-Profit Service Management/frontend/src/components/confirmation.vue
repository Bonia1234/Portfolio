<script setup>

// imported useSlots to access the slot value in script
import { ref, useSlots } from 'vue'

const props = defineProps({
  disabled : Boolean
})

// Used to determine whether modal shows or not (changes depending on what is clicked (CRUD button, close button, submit button, cancel button))
const toggle_modal = ref(false)


// useSlots declaration
const slots = useSlots();


// Grabbing the default slot value from parent (found by console logging slots.default() and finding the correct index and property to include)
const slotValue = slots.default()[0].children;


// Removes white space at the end of the slot value (wanted '?'' attached to the end of the slot value w/o whitespace) because slot value seems to have white space at the end
function remove_white_space() {
  return slotValue.trim() + '?'
}


</script>




<template>

<!-- CRUD BUTTON -->
<!-- '$attrs.class' used to directly inherit parent's default class style of its CRUD button -->
<button @click = "toggle_modal = true" :class = "$attrs.class" :disabled = "disabled">  <slot/>   </button>

  

  <!-- MODAL POPUP-->
  <div>
    <div id="myModal" class= "modal" v-if="toggle_modal" style = "display:block" >

      <!-- CONTENT in the Modal Popup -->
      <div class="modal-content">


        <!-- CLOSE BUTTON in the Modal Popup -->
        <!-- When clicked, Modal Popup will close (toggle_modal = "false") -->
        <p @click ="toggle_modal = false" class = "close">  &times;   </p>
        <p class = "font-bold text-2xl"> Please Confirm </p>
        <br>
          <!-- 'remove_white_space()' takes the parent slot value, trim the whitespace, and attaches '?' at the end -->
          Are you sure you want to <br>
          <b> {{remove_white_space()}} </b>
        
        <br><br>



        <!-- SUBMIT BUTTON in the Modal Popup -->
        <!-- Parent will listen to the 'ChildModalsubmit' emit identifier and send different CRUD functions to it -->
        <!-- When clicked, Modal Popup will close (toggle_modal = "false") -->
        <button @click = "$emit('ChildModalsubmit'); toggle_modal = false"  class="bg-green-700 disabled:opacity-50 text-white rounded" type = "submit"> Submit </button>
      

        <!-- CANCEL BUTTON in the Modal Popup -->
        <!-- When clicked, Modal Popup will close (toggle_modal = "false") -->
        <button @click = "toggle_modal = false" class="bg-red-700 disabled:opacity-50 text-white rounded ml-1"> Cancel </button>
      </div>

    </div>
  </div>

</template>





<style scoped>

/* Background of the Modal Popup */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /*Stay in place */
  z-index: 1; /*Sit on top */
  padding-top: 10%;  /* Box location */
  

  /* Aligns background to the farthest left and top of screen */
  left: 0;
  top: 0;

  /* Full width and height of the screen to be in dark color */
  width: 100%; 
  height: 100%; 
  overflow: auto; /* Enable scroll if needed */

  /* Background of the screen goes black if the modal pops up */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}



/* Modal Popup/Modal content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 20%;
  text-align: center;
  border-radius: 15px;
}



/* Close button of Modal Popup */
.close {
  color: #aaaaaa;
  float: right; /* Floating the 'x' close button to the right of the Modal Popup */ 
  margin: -26px -14px; /* Making the 'x' close button go to the top right as much as possible */
  font-size: 28px;
  font-weight: bold;  
}

/* Mouse interaction of Close Button */
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

</style>


<!-- REFERENCES -->
<!-- Modal template used - https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal -->
<!-- useSlots - https://vuejs.org/api/composition-api-helpers -->
<!-- slot default - https://vuejs.org/guide/components/slots.html -->
<!-- $attrs.class - https://stackoverflow.com/questions/69939912/how-to-pass-class-attribute-to-child-component-element/77641371#77641371 -->
<!-- .trim - https://vuejs.org/guide/essentials/forms.html#trim -->