<template>
   <div class = "card">
       <div class="card-header">
        Bar
        </div>
        <div class="card-body">
            <bar :data="data" :option="option"> </bar>
      </div>
     </div>
</template>

<script>
import bar from './bar.vue';


export default{
       name:'info',
       props:[
           'data',
           'option'
       ],
       components:{
           bar
       }
}
</script>