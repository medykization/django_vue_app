<template>
  <div id='board-card'>
    <v-hover v-slot="{ hover }">
      <v-card
        @click="testClick"
        outlined
        block
        shaped
        :elevation="hover ? 16 : 2"
        :class="{ 'on-hover': hover }"
        min-height="140"
        class="ma-5">
        <v-container class="blue lighten-3"></v-container>
        <v-card-title>{{boardName}}</v-card-title>
        <v-card-subtitle>{{boardid}}</v-card-subtitle>
        </v-card>
    </v-hover>
  </div>
</template>
<script>
export default {
    props: ['boardName', 'boardid'],
    methods: {
      testClick () {
        var boardURL = '/board/'
        boardURL = boardURL.concat(this.boardid, '/', this.boardName)
        console.log('boardid: ' + this.boardid)
        console.log('URL: ' + boardURL)
        this.$router.push({ path: boardURL })
      }
    }
}
</script>
