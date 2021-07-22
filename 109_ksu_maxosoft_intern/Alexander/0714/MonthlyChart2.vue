<script>
import { defineComponent } from 'vue'
import {Doughnut} from 'vue3-chart-v2'



export default defineComponent({
  name: 'MonthlyChart',
  extends: Doughnut,

  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
      datasets: [
        {
          label: '甲班',
          backgroundColor: '#f87979',
          data: [42, 50, 6, 35, 42, 57, 36, 45, 23, 6, 72, 51]
        },
         {
          label: '乙班 ',
          backgroundColor: 'blue',
          data: [23, 35, 67, 7, 23, 75, 2, 32, 41, 23, 4, 65]
        },
        {
          label: '丙班 ',
          backgroundColor: 'green',
          data: [32, 75, 42, 32, 21, 39, 54, 48, 3, 8, 9, 45]
        }
      ]
    })
  }
})
</script>
<style>

</style>