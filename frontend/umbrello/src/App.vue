<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-toolbar flat color="primary">
        <router-link to="/">
        <v-toolbar-title class="white--text">Umbrello.</v-toolbar-title>
        </router-link>
        <v-spacer></v-spacer>
        <v-btn v-if="accessToken==null" to="/login">
          Sign In
        </v-btn>
        <v-btn v-if="accessToken==null" to="/register">
          Sign Up
        </v-btn>
        <v-btn v-if="accessToken!=null" to="/downloads">
          Boards
        </v-btn>
        <v-btn v-if="accessToken!=null" to="/logout">
          Sign Out
        </v-btn>
      </v-toolbar>
    </v-app-bar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: 'App',
    computed: mapState(['accessToken'])
  }
</script>
