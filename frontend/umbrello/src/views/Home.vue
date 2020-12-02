<template>
  <v-container fluid fill-height class="bg">
  <v-container fluid>
    <v-layout row align-center>
      <v-flex xs12 sm6 offset-sm3 class="text-xs-center pt-16">
        <h1>Welcome to Umbrello</h1>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 mt-3>
        <blockquote class="blockquote text-xs-center">
        The Umbrello app helps you collaborate<br>
        and get more done.
        </blockquote>
      </v-flex>
      <v-flex xs12 sm6 offset-sm3 class="text-xs-center" my-5>
        <v-btn color="primary" to="/login">Sign In</v-btn>
        <v-btn to="/register">Sign Up</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
  </v-container>
</template>
<script>
export default {
  // name: "Home"
}
</script>
<style scoped>
  .bg {
    /*
    background: url('https://i.imgur.com/7WuLRWF.jpg') no-repeat center center;
    */
    background-size: cover;
  }
</style>
