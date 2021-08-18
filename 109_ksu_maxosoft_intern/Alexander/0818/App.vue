<template>

  <div id="app" class="container">
 
 </div>
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading">Users</h3>


 <select v-model="selected">
    <option selected>下載</option>
    <option>產出</option>
    <option>GG</option>
  </select>
  <span> 資料區域(請選擇):</span>
<input type="text" v-model="searchTerm" />
<br><br>
        
      <!-- 注意下面 input 對應的都是 v-model="checkedNames"  -->
  

      <div class="faq-body">
        <div v-for="(products, index) in filterByTerm" :key="products" class="faq-question">
          <input type="checkbox" v-model="checkedNames" :value="products" :td="index" />
          <label class="card-title" style="margin-left" >{{ index }}.{{ products.id }}    weight:{{ products.weight }} </label> 
      
        </div>
      </div>
 <br><br>
   
   
  <table class=" table-bordered"  style= " height: 500px; width:500px; text-align:center;"  >
      <thead>
        
{{ checkedNames}}





   <tr><td rowspan="2"> <button v-on:click="up(113)">下載</button></td>




   <td><button type="button" >產出</button></td></tr>
<tr><td><button type="button">GG</button></td></tr>
         
   
      </thead>
      </table>


       <div class="col-md-6 text-right">
         <h2>
      Total: <span class="price-content">{{ total_price }}</span>
    </h2>
           
    </div>
   </div>
</template>

<script>
import _ from "lodash";
    import axios from "axios";
    
    export default {
      name: 'app',
       components: {
  },
      data () {
        return {
          checkedNames:[],
         
          loading: true,
         info: null,
         errored: false,
         searchTerm:"",
        
           methods:{
            up:function(){
            console.log()
            }
        }
         
        }
      },
      mounted () {
        this.loading = true;
        axios
        .get('https://yjserp.maxosoft.com/api/final_demo')
      .then(response => (this.info = response.data.products))
       .catch(error => console.log(error))
      .finally(() => this.loading = false)
      },
    
    computed: {
    filterByTerm() {
      return this.info.filter(products=> {
        return products.id.toLowerCase().includes(this.searchTerm);
      });
    },
    
      total_price: function () {
      return _.reduce(
        this.checkedNames,
        function (memo, products) {
          return memo + products.weight;
        },
        0
      );
    },
  },
    
    
    }
    </script>

    <style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.heading {
  margin-bottom: 30px;
}
 .faq-body {
    width: auto;
    height: 400px;
    background: #fff;
    overflow: scroll;
    border: 5px solid #8F4586;
    border-radius: 10px;
  }
  .faq-body::-webkit-scrollbar {
    width: 20px;
  }
  .faq-body::-webkit-scrollbar-thumb {
    background-color: #8F4586;
    border: 5px solid #fff;
    border-radius: 10rem;
  }
  .faq-body::-webkit-scrollbar-track {
    position: absolute;
    right: -3rem;
    top: -50rem;
    background: transparent;
  }
  .faq-question {
    padding: 20px;
    border-bottom: 1px solid #000;
    line-height: 1.3;
    color: #15191b;
    font-size: 1.3rem;
  }
</style>
