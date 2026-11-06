<script setup>
	import { ref } from 'vue'

  var text_received_from_server = ref("Nothing")
  
  async function ClickMeButton() {
    // Data
    var response = await fetch("https://rs-vjezbe-vjezbe1-zadatak2.onrender.com/button")
    
    // Data to json
    var json_file = await response.json()
    
    // Set the title of the json file to the text
    text_received_from_server.value = json_file.title
  }
</script>

<template>
  <h1>
    A big button!
  </h1>
  <p>
    Siguran je za kliknuti... valjda.
  </p>
  <button @click="ClickMeButton">
    CLICK ME!
  </button>
  <p>
   {{ text_received_from_server }}
  </p>
</template>