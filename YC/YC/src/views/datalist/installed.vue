<template>
    <div class="home">
        <Row>
            <Row class="Top">
              <Tabs type="card" @on-click="handleTab">
                  <TabPane label="24小时装机日报">
                      <installedtwentyfour v-if="tab0"></installedtwentyfour>
                  </TabPane>
                  <TabPane label="装机八小时日报">
                      <installeight v-if="tab1"></installeight>
                  </TabPane>
                  <TabPane label="农普及时率统计">
                      <statisticstimely v-if="tab2"></statisticstimely>
                  </TabPane>
                  <TabPane label="接单及时率">
                      <ordertimely v-if="tab3"></ordertimely>
                  </TabPane>
                  <TabPane label="装机时长TOP20">
                       <installtop v-if="tab4"></installtop >
                  </TabPane>
                  <TabPane label="超时未回复">
                       <overtimeunanswered v-if="tab5"></overtimeunanswered>
                  </TabPane>
                  <TabPane label="退单率">
                      <chargeback v-if="tab6"></chargeback>
                  </TabPane>
                  <!-- <TabPane label="装机劳效">暂不做</TabPane>
                  <TabPane label="装机达人Top">暂不做</TabPane> -->
                  <!-- <TabPane label="满意度">
                       <visited-satisfaction></visited-satisfaction>
                  </TabPane> -->
              </Tabs>
            </Row>
      </Row>
    </div>
</template>
<script>
    import installedtwentyfour from './installed-listPage/twentyfour.vue'
    import statisticstimely from './installed-listPage/timely.vue'
    import installeight from './installed-listPage/eight.vue'
    import ordertimely from './installed-listPage/order.vue'
    import installtop  from './installed-listPage/top.vue'
    import overtimeunanswered from './installed-listPage/Unanswered.vue'
    import chargeback from './installed-listPage/chargeBack.vue'
    //import visitedSatisfaction from './installed-listPage/satisfaction.vue'
    export default {
       data() {
         return {
           tab0:true,
           tab1:false,
           tab2:false,
           tab3:false,
           tab4:false,
           tab5:false,
           tab6:false,
           tab7:false
         }
       },
       methods:{
         handleTab(name) {
            this['tab' + name] = true
         }
       },
       components: {
         installedtwentyfour,
         statisticstimely,
         installeight,
         ordertimely,
         installtop,
         overtimeunanswered,
         chargeback
         // visitedSatisfaction
       }
    }
</script>
<style>
  .ivu-tabs.ivu-tabs-card>.ivu-tabs-bar .ivu-tabs-nav-container{
    font-size: 12px;
  }
</style>
