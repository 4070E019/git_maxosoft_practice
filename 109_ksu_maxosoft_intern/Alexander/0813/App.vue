<template>

  <div id="app" class="container">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading">Users</h3>
    
<div>
     <Multiselect
      v-model="value"
      placeholder="Select your  engine"
      label="name"
      trackBy="name"
      :options="options"
      :searchable="true"
    >
      <template v-slot:singleLabel="{ value }">
        <div class="multiselect-single-label">
          <img height="26" style="margin: 0 6px 0 0;" :src="value.icon"> {{ value.name }}
        </div>
      </template>

      <template v-slot:option="{ option }">
        <img height="22" style="margin: 0 6px 0 0;" :src="option.icon">{{ option.name }}
      </template>
    </Multiselect>
  </div>

        <thead>
          <tr>
        
          
          </tr>
        </thead>
        <tbody>
          <tr v-for="products in info" v-bind:key="products">
             
             <input
                type="checkbox"
                value="eat"
                v-model="data"
            >
              <h3 class="card-title" style="margin-left:90%," >id:{{ products.id }}    weight:{{ products.weight }} </h3> 
 
   </tr>
  </tbody>
   
  <table class=" table-bordered"  style= " height: 500px; width:500px; text-align:center;" >
      <thead>
   <tr><td rowspan="2">下載</td><td>產出</td></tr>
<tr><td>GG</td></tr>
         
   
      </thead>
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