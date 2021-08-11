<template>

  <div id="app" class="container">
   
    
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading">Users</h3>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">id</th>
            <th scope="col">weight </th>
          
          </tr>
        </thead>
        <tbody>
          <tr v-for="products in info" v-bind:key="products">
            <td>{{ products.id }}</td>
            <td>{{ products.weight }}</td>
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
        .get('https://yjserp.maxosoft.com/api/final_demo')
      .then(response => (this.info = response.data.products))
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