<template>
<v-container fill-height>
    <v-row justify="center" align="center">
        <v-col cols="12" sm="3">
          <v-card
            elevation="10"
            align-center
            outlined
            block
            shaped
          >
            <v-flex xs12 sm6 offset-sm3 class="text-xs-center" mt-5>
              <h1>Sign In</h1>
            </v-flex>
            <v-flex xs12 sm6 offset-sm3 mt-3>
              <form>
                  <v-flex>
                    <v-text-field
                      name="username"
                      label="Username"
                      id="username"
                      type="username"
                      v-model="username"
                      required></v-text-field>
                  </v-flex>
                  <v-flex>
                    <v-text-field
                      name="password"
                      label="Password"
                      id="password"
                      type="password"
                      v-model="password"
                      required></v-text-field>
                  </v-flex>
                  <v-flex class="text-xs-center" my-5>
                    <v-btn @click="loginUser()" color="primary" type="button">Sign In</v-btn>
                  </v-flex>
              </form>
            </v-flex>
          </v-card>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        wrongCred: false // activates appropriate message if set to true
      }
    },
    methods: {
      loginUser () { // call loginUSer action
        this.$store.dispatch('loginUser', {
          username: this.username,
          password: this.password
        })
            .then(() => {
              this.wrongCred = false
              this.$router.push({ name: 'dashboard' })
            })
          .catch(err => {
            console.log(err)
            this.wrongCred = true // if the credentials were wrong set wrongCred to true
          })
        }
      }
  }
</script>
