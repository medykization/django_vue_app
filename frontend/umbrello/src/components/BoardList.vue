<template>
    <v-card
        elevation="5"
        block
        min-height="200"
        min-width="100"
        class="ma-5">
        <v-card-title class="blue lighten-6">
            <header>{{listName}}</header>
            <v-spacer></v-spacer>
            <v-menu bottom left>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                dark
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
            <v-list-item link>
                <v-list-item-title>
                        Archivize list
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-card-title>
        <v-card
        min-height="55"
        elevation="2"
        color="white"
        outlined
        block
        class="ma-1 pa-3"
        min-width="100">
            <v-card-subtitle>Test karty</v-card-subtitle>
        </v-card>
        <v-menu>
            <v-card-actions>
              <v-btn color="green lighten-1" @click="addCard">Add</v-btn>
            </v-card-actions>
        </v-menu>
    </v-card>
</template>
<script>
import modal from '../components/ListEditModal.vue'
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
    }
}
</script>
