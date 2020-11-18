<template>
  <div class="submit-form">
    <div>
      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          class="form-control"
          id="username"
          v-model="user.usernameInput"
          required
          name="username"
        />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="user.passwordInput"
          required
          name="password"
        />
      </div>
      <button @click="logme" class="btn btn-success">Sign In</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      user: {
        usernameInput: '',
        passwordInput: '',
      },
    };
  },
  methods: {
    logme() {
      axios.post('http://127.0.0.1:8000/account/login', {
        headers: {
          'Content-type': 'application/json',
        },
        body: {
          username: this.user.usernameInput,
          password: this.user.passwordInput,
        },
      })
        .then((response) => {
          console.log(response);
        }, (error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>
