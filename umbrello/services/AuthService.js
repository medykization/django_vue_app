import http from '../http-common';

class AuthService {
  login(username, password) {
    return http.post('/login', username, password);
  }
}
export default new AuthService();
