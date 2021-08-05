<template>

  <div id="app" class="container">
   
    
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading">Users</h3>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">code</th>
            <th scope="col">rate </th>
            <th scope="col">description</th>
            <th scope="col">rate_float</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="country in info" v-bind:key="country">
            <td>{{ country.code }}</td>
            <td>{{ country.rate }}</td>
            <td>{{ country.description}}</td>
              <td>{{ country.rate_float}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
    import axios from "axios";
    
    export default {
      name: 'app',
      data () {
        return {
          loading: false,
         info: null,
         errored: false,
        }
      },
      mounted () {
        this.loading = true;
        axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response.data.bpi))
       .catch(error => console.log(error))
      .finally(() => this.loading = false)
      }
    }
    </script>

    <style>
#app {
  text-align: center;
  margin-top: 50px;
}
.heading {
  margin-bottom: 30px;
}
</style>