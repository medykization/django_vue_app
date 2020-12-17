<template>
  <div id='board-card'>
    <v-hover v-slot="{ hover }">
      <v-card
        outlined
        block
        shaped
        :elevation="hover ? 16 : 2"
        :class="{ 'on-hover': hover }"
        min-height="140"
        class="ma-5">
        <v-container class="blue lighten-3"></v-container>
        <v-card-title>{{boardName}}</v-card-title>
        <v-card-subtitle>SubTitle</v-card-subtitle>
        <v-card-text>Text Text Text Text Text</v-card-text>
        </v-card>
    </v-hover>
  </div>
</template>
<script>
export default {
    props: ['boardName']
}
</script>
