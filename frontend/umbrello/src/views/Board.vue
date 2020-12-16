<template>
    <div fluid fill-height>
    <!-- <header>{{ $route.params.name }}</header> -->
    <v-container class="my-5">
      <v-layout row class="mt-5">
        <v-flex v-for="list in boardLists" :key="list.id">
            <BoardList :listName="list.name" :listid="list.id"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import BoardList from '../components/BoardList.vue'
import { getAPI } from '../api/axios-base'
export default {
    components: { BoardList },
    data () {
    return {
      boardLists: []
    }
  },
    created () {
        getAPI.post('/boards/lists', { id: this.$route.params.id }, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }) // proof that your access token is still valid; if not the
        // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            console.log('GetAPI successfully got the lists')
            console.log(response.data)
            this.boardLists = response.data
            // this.$store.state.APIData = response.data // store the response data in store
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          })
    }
}
</script>
