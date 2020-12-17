<template>
  <div fluid fill-height>
    <v-container class="my-5">
      <v-layout row class="mt-5">
        <v-flex v-for="mod in APIData" :key="mod.id" xs8 md4 lg2>
          <BoardCard :boardName="mod.name" :boardid="mod.id"/>
        </v-flex>
        <v-flex xs8 md4 lg2>
          <v-card
          outlined
          block
          elevation="5"
          min-height="140"
          class="ma-5">
            <v-container class="blue lighten-5"></v-container>
            <v-card-title>New Board</v-card-title>
            <v-card-actions>
              <modal v-show="isModalVisible"/>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import BoardCard from '../components/BoardCard.vue'
  import { getAPI } from '../api/axios-base'
  import modal from '../components/BoardAddModal.vue'
  import { mapState } from 'vuex'
  export default {
    components: {
      BoardCard,
      modal
    },
    name: 'app',
    data () {
      return {
        isModalVisible: true
      }
    },
    onIdle () { // dispatch logoutUser if no activity detected
      this.$store.dispatch('logoutUser')
        .then(response => {
          this.$router.push('/login')
        })
    },
    computed: mapState(['APIData']), // get APIData from store.state.
    created () {
        getAPI.get('/boards', {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }) // proof that your access token is still valid; if not the
        // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            console.log('GetAPI successfully got the boards')
            this.$store.state.APIData = response.data // store the response data in store
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          })
    }
  }
</script>
