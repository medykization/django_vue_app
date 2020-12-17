<template>
    <v-card
        elevation="5"
        block
        min-height="200"
        min-width="80"
        class="ma-4">
        <v-card-title class="grey lighten-5">
            <h5>{{listName}}</h5>
            <v-spacer></v-spacer>
            <v-menu bottom left>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                light
                icon
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>

            <v-list>
            <v-list-item link>
                <v-list-item-title>
                        Add card...
                </v-list-item-title>
              </v-list-item>
              <v-list-item link>
                <v-list-item-title>
                    <v-list-item-action>
                        <modal v-show="isModalVisible" :listid="variableAtParent"/>
                    </v-list-item-action>
                </v-list-item-title>
              </v-list-item>
            <v-list-item
                link
                @click="archivizeList">
                <v-list-item-title>
                        Archivize list
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-card-title>
        <v-card
        outlined
        min-height="55"
        elevation="7"
        color="white"
        block
        class="ma-2 pa-3"
        min-width="100">
            <v-card-subtitle>Test karty</v-card-subtitle>
        </v-card>
        <v-card-actions>
          <v-btn
            color="blue lighten-1"
            text
          >
          + Add new card
          </v-btn>
        </v-card-actions>
    </v-card>
</template>
<script>
import modal from '../components/ListEditModal.vue'
import { getAPI } from '../api/axios-base'
export default {
    components: {
      modal
    },
    props: ['listName', 'listid'],
    data () {
      return {
        isModalVisible: true,
        variableAtParent: this.listid
      }
    },
    methods: {
        archivizeList () {
        console.log({ name: this.listid })
        getAPI.put('/boards/archive/list',
          { id: this.listid },
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
