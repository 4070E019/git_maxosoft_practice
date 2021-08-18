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
  <br>
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
   
   
 
 <div class="download">
             <button v-on:click="up(113)">下載</button>
            
             <div v-for="(products,index) in checkedNames" v-bind:key="products" >
            
            
                  <h3>{{ products.weight }}</h3>
  <div @click="deleteTask(index)">
              <span class="fa fa-trash pointer"></span>
            </div>
            </div>
          </div>
      

 <div class="output">
   <button v-on:click="up(113)">產出</button>
          <div v-for="products in checkedNames" v-bind:key="products" >
            
         
          </div>
        </div>
 
      <div class="GG">
        <button v-on:click="up(113)">GG</button>
          <div v-for="products in checkedNames" v-bind:key="products" >
       
         
          </div>
        </div>

       <div class="col-md-6 text-right">
         <h2>
      Total: <span class="price-content" style= "text-align:left">{{ total_price }}</span>
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

    };
  
  
  },
  mounted() {
    this.loading = true;
    axios
      .get("https://yjserp.maxosoft.com/api/final_demo")
      .then((response) => (this.info = response.data.products))
      .then((data) => console.log(data))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      }) //提醒使用者axios 訪問 API有錯誤
      .finally(() => (this.loading = false)); //載入loading
  },
     methods: {
     deleteTask(index) {
      this.checkedNames.splice(index, 1);
    },
    up:function(){
            console.log()
            }
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
    filterByTerm() {
      //filter search
      return this.info.filter((item) => {
        return item.id.toLowerCase().includes(this.filter);
      });
    },

 
};


</script>
<style>
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
  border: 5px solid #8f4586;
  border-radius: 10px;
}
.faq-body::-webkit-scrollbar {
  width: 20px;
}
.faq-body::-webkit-scrollbar-thumb {
  background-color: #8f4586;
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
#left {
  width: 400px;
  height: 700px;
  float: left;
}
#right-up {
  width: 400px;
  height: 350px;
}
#right-down {
  width: 400px;
  height: 350px;
}
.download {
  width: 450px;
  height: 560px;
  background: #fff;
  text-align:left;
 margin-left:20px;
  border: 1px solid #7b7d7f;
}



.output {
  width: 370px;
  height: 280px;
  background: #fff;
margin-left:370px;
margin-top:-560px;
  border: 1px solid #7b7d7f;
    text-align:left;
}


.GG {
  width: 370px;
  height: 280px;
  background: #fff;
margin-left:370px;
  border: 1px solid #7b7d7f;
    text-align:left;
}
.pointer {
  cursor: pointer;
}
</style>