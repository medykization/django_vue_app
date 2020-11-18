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
import AuthService from '../../services/AuthService';

let queryResponse;

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
      this.queryResponse = AuthService.login(this.user.usernameInput, this.user.passwordInput)
        .then((response) => {
          console.log(response);
        })
        .catch((e) => {
          console.log(e);
        });
      console.log(queryResponse);
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
