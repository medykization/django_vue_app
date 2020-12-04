<template>
  <v-container fill-height fluid>
    <v-row align="center">
      <v-col>
          <v-flex xs12 sm6 offset-sm3 class="text-xs-center pt-16 white--text">
            <h1>See You soon</h1>
          </v-flex>
          <v-flex xs12 sm6 offset-sm3 mt-3>
            <blockquote class="blockquote text-xs-center white--text">
            Thanks for using Umbrello app.
            </blockquote>
          </v-flex>
          <v-flex xs12 sm6 offset-sm3 class="text-xs-center" my-5>
            <v-btn color="primary" to="/login">Sign In</v-btn>
            <v-btn to="/register">Sign Up</v-btn>
          </v-flex>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    created () {
      this.$store.dispatch('logoutUser')
        .then(() => {
          this.$router.push({ name: 'home' })
        })
    }
  }
</script>
