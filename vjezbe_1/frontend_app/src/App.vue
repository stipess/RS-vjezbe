<script setup>
	import { ref } from 'vue'

  var text_received_from_server = ref("Don't click the button!")
  var ime = ref("")
  var prezime = ref("")

  async function ClickMeButton() {
    // Data
    console.log("Sending GET request...")
    var response = await fetch("https://rs-vjezbe-vjezbe1-zadatak2.onrender.com/button")

    // Data to json
    var json_file = await response.json()
    console.log("Received response: ", json_file)
    
    // Set the title of the json file to the text
    text_received_from_server.value = json_file.message
    console.log("New text: ", text_received_from_server.message)
  }

  async function AddName(name) {
    
    var response = await fetch(
      "https://rs-vjezbe-vjezbe1-zadatak2.onrender.com/addname",
      {
        method : "POST",
        headers : {
          "Content-Type" : "application/json"
        },
        body : JSON.stringify({
          firstname : ime.value,
          lastname : prezime.value
        })
      }

    
    )

  }
</script>

<template>
  <h1>
    A big button!
  </h1>
  <p>
    {{ text_received_from_server }}
  </p>
  <button @click="ClickMeButton">
    CLICK ME!
  </button>

  <h2>
    Unesite ime i prezime kako bi dodali vaše podatke u našu bazu podataka.
  </h2>
  <form>
    <label>Ime:</label><br>
    <input type="text" id="firstname" name="firstname" v-model="ime"><br>
    <label>Prezime:</label><br>
    <input type="text" id="lastname" name="lastname" v-model="prezime"><br>
    <br>
  </form>
  <button @click="AddName">
      Send
  </button>
</template>