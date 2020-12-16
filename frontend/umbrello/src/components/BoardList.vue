<template>
    <v-card
        elevation="5"
        block
        min-height="200"
        min-width="100"
        class="ma-5">
        <v-container class="blue lighten-6">
            <header>{{listName}}</header>
        </v-container>
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
export default {
    props: ['listName', 'listid']
}
</script>
