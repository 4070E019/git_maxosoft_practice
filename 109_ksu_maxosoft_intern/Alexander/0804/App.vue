<template>
    <div id="app" >
        
        {{ info }}
      </div>

    </template>

<script>
    import axios from "axios";
    
    export default {
      name: 'app',
      data () {
        return {
          loading: false,
         info: null
        }
      },
      mounted () {
        this.loading = true;
        axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))
      }
    }
    </script>