<template lang="html">
       <div class="home_main">
          <Row>
              <Col span="14">
                <Row>
                  <Col span="8">
                      <Row>
                        <Row>
                          <Col>
                              <Card>
                                  <p slot="title" class="card-title">
                                      <Icon type="android-map"></Icon>
                                      处理及时率
                                  </p>
                                  <div class="data-source-row">
                                      <user-flow></user-flow>
                                  </div>
                              </Card>
                           </Col>
                        </Row>
                        <Row>
                          <Col>
                              <Card>
                                  <p slot="title" class="card-title">
                                      <Icon type="android-map"></Icon>
                                      平均处理时长
                                  </p>
                                  <div class="data-source-row">
                                      <home-flows></home-flows>
                                  </div>
                              </Card>
                          </Col>
                        </Row>
                      </Row>
                      <Row>

                      </Row>
                  </Col>
                  <Col span="16">
                      <Row>
                          <Col>
                            <Card>
                                <p slot="title" class="card-title">
                                    <Icon type="ios-pulse-strong"></Icon>
                                     宜昌市移动用户地图
                                </p>
                                <div class="map">
                                     <home-map :city-data="cityData"></home-map>
                                </div>
                            </Card>
                          </Col>
                      </Row>
                  </Col>
                </Row>
                <Row>
                  <Col :style="{marginTop: '-12px'}">
                     <Card>
                         <p slot="title" class="card-title">
                             <Icon type="android-map"></Icon>
                             家宽用户结构
                         </p>
                         <div class="data-bar1">
                            <visite-volume></visite-volume>
                         </div>
                     </Card>
                 </Col>
                </Row>
              </Col>
              <Col span="10">
                  <Row>
                    <Col>
                      <Card >
                          <p slot="title" class="card-title">
                              <Icon type="android-wifi"></Icon>
                              各县区投诉单量
                          </p>
                          <div class="data-line">
                               <home-lines></home-lines>
                          </div>
                      </Card>
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      <Card >
                          <p slot="title" class="card-title">
                              <Icon type="android-wifi"></Icon>
                              各县区故障单量
                          </p>
                          <div class="data-line">
                               <home-line></home-line>
                          </div>
                      </Card>
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      <Card >
                          <p slot="title" class="card-title">
                              <Icon type="android-wifi"></Icon>
                              投诉分析统计
                          </p>
                          <div class="data-line1">
                              <Bar></Bar>
                          </div>
                      </Card>
                    </Col>
                  </Row>
              </Col>
          </Row>
       </div>
</template>

<script>
import cityData from './map-data/get-city-value.js';
import userFlow from './components/flow.vue';
import homeFlows from './components/flows.vue';
import Bar from './components/bar.vue';
import homeLine from './components/line.vue';
import homeLines from './components/linetwo.vue';
import homeMap from './components/map.vue';
import visiteVolume from './components/visiteVolume.vue';
export default {
  data() {
    return {
          data:[],
          cityData: cityData,
    }
  },
  methods: {

  },
  created() {

  },
  mounted() {

  },
  components: {
    userFlow,
    homeFlows,
    homeMap,
    homeLine,
    homeLines,
    visiteVolume,
    Bar
  }
}
</script>

<style lang="scss" scoped>

.data-bar1{

    height: 335px;
}
.data-line{
  height: 220px;
}
.data-line1{
  height: 335px;
}
.data-source-row{
  height: 222px;

}
.map{
  height: 537px;
  margin-left: 30px;
}

</style>
