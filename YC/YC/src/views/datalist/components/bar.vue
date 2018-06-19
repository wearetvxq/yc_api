<template>
    <div style="width:100%;height:100%;" id="bar"></div>
</template>

<script>
import echarts from 'echarts';
export default {
    name: 'visiteVolume',
    data () {
        return {
            //
        };
    },
    mounted () {
        this.$nextTick(() => {
            let visiteVolume = echarts.init(document.getElementById('bar'));

            const option = {
              color:['#87cefa'],
              xAxis: {
                  type: 'category',
                  data: ['城区', '开发区', '当阳市', '五峰县', '兴山县', '夷陵区', '远安县','枝江市','长阳县','秭归','全市']
              },
              yAxis: {
                  type: 'value'
              },
              series: [{
                  data: [120, 200, 150, 80, 70, 110, 130, 60, 75, 50, 380],
                  type: 'bar',
                  barWidth:'50%'
              }]
            };
            visiteVolume.setOption(option);
            // window.addEventListener('resize', function () {
            //     visiteVolume.resize();
            // });
        });
    }
};
</script>
