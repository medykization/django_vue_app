<script>
  import { getAPI } from '../api/axios-base'
  export default {
    data: () => ({
      dialog: false,
      name: ''
    }),
    methods: {
      addBoard () {
      console.log({ name: this.name })
      getAPI.post('/boards/add',
        { name: this.name },
        { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` }
      })
      .then(response => {
          console.log('GetAPI successfully added the board')
          window.location.reload()
          // this.$store.state.APIData = response.data // store the response data in store
        })
        .catch(err => { // refresh token expired or some other error status
          console.log(err)
        })
      }
    }
  }
</script>
<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Add
        </v-btn>
      </template>
      <v-card>
        <v-card-text>
          <v-container>
              <v-col cols="12">
                 <v-text-field
                  label="Name of new board"
                  type="text"
                  name="Name"
                  id="Name"
                  v-model="name"
                  required
                ></v-text-field>
              </v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            type="button"
            @click="addBoard"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
