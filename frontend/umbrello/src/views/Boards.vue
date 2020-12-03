<template>
  <div fluid fill-height>
    <v-container class="my-5">
      <v-layout row class="mt-5">
        <v-flex v-for="mod in APIData" :key="mod.id" xs8 md4 lg2>
          <v-card
          outlined
          block
          shaped
          elevation="5"
          min-height="140"
          class="ma-5"
          @contextmenu="showBoardMenu">
            <v-container class="blue lighten-4"></v-container>
            <v-card-title>{{mod.name}}</v-card-title>
            <v-card-subtitle>SubTitle</v-card-subtitle>
            <v-card-text>Text Text Text Text Text</v-card-text>
              <v-menu
              v-model="showMenu"
              :position-x="x"
              :position-y="y"
              absolute
              offset-y
              >
              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-card>
        </v-flex>
        <v-flex xs8 md4 lg2>
          <v-card
          outlined
          block
          shaped
          elevation="5"
          min-height="140"
          class="ma-5">
            <v-container class="blue lighten-4"></v-container>
            <form @submit.prevent="addBoard">
              <label for="user">Name of board</label>
              <input type="text" name="Name" id="Name" v-model="name">
              <button type="submit">Add</button>
            </form>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import { getAPI } from '../api/axios-base'
  import { mapState } from 'vuex'
  export default {
    data: () => ({
      showMenu: false,
      x: 0,
      y: 0,
      items: [
        { title: 'Click Me 1' },
        { title: 'Click Me 2' }
      ]
    }),
    name: 'Boards',
    onIdle () { // dispatch logoutUser if no activity detected
      this.$store.dispatch('logoutUser')
        .then(response => {
          this.$router.push('/login')
        })
    },
    computed: mapState(['APIData']), // get APIData from store.state.
    created () {
        getAPI.get('/boards/all', {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }) // proof that your access token is still valid; if not the
        // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            console.log('GetAPI successfully got the boards')
            this.$store.state.APIData = response.data // store the response data in store
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          })
    },
    methods: {
      showBoardMenu (e) {
        e.preventDefault()
        this.showMenu = false
        this.x = e.clientX
        this.y = e.clientY
        this.$nextTick(() => {
          this.showMenu = true
        })
      },
      addBoard () {
        getAPI.post('/boards/add',
          { name: this.name },
          { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` }
        })
        .then(response => {
            console.log('GetAPI successfully added the board')
            // this.$store.state.APIData = response.data // store the response data in store
          })
          .catch(err => { // refresh token expired or some other error status
            console.log(err)
          })
      }
    }
  }
</script>
<style scoped>
  .bg {
    background: url('https://i.imgur.com/C8BYhgw.jpeg') no-repeat center center;
    background-size: fill;
  }
</style>
