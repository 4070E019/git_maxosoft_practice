<template>

    <div class="row">
     <div class="col-6 col-md-4">
    <div class="card border-dark">
       <div class="card-header">
        Bar
        </div>
       
       
       
        <div class="card-body">
        <bar :data="data" :option="option"> </bar>
          <p class="card-text">
            Some quick example text to build on the card title and make up the bulk of the
            card's content.
          </p>
          <button class="btn-primary" >Read more</button>
        </div>
      </div>
    </div>

 <div class="col-6 col-md-4">
    <div class="card border-dark">
       <div class="card-header">
        Doughnut
        </div>
       
       
       
        <div class="card-body">
        <Doughnut :data="data" :option="option"> </Doughnut>
          <p class="card-text">
            Some quick example text to build on the card title and make up the bulk of the
            card's content.
          </p>
          <button class="btn-primary" >Read more</button>
        </div>
      </div>
      </div>
  </div>

      
</template>

<script>
import bar from './bar.vue';
import Doughnut from './Doughnut.vue';


export default{
       name:'info',
       props:[
           'data',
           'option'
       ],
       components:{
           bar,
         Doughnut
       }
}
</script>