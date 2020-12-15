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
              <h1>Sign Up</h1>
            </v-flex>
            <v-flex xs12 sm6 offset-sm3 mt-3>
              <form>
                <v-layout column>
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
                      name="email"
                      label="Email"
                      id="email"
                      type="email"
                      v-model="email"
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
                  <v-flex>
                    <v-text-field
                      name="confirmPassword"
                      label="Confirm Password"
                      id="confirmPassword"
                      type="password"
                      v-model="confirmed_password"
                      required
                      ></v-text-field>
                  </v-flex>
                  <v-flex class="text-xs-center" my-5>
                    <v-btn @click="registerUser()" color="primary" type="button">Sign Up</v-btn>
                  </v-flex>
                </v-layout>
              </form>
            </v-flex>
          </v-card>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
  export default {
    name: 'register',
    data () {
      return {
        email: '',
        username: '',
        password: '',
        confirmed_password: ''
      }
    },
    methods: {
      registerUser () {
        this.$store.dispatch('registerUser', {
          email: this.email,
          username: this.username,
          password: this.password,
          confirmed_password: this.confirmed_password
        }).then(() => {
          this.$router.push({ name: 'login' })
        })
      }
    }
  }
</script>
