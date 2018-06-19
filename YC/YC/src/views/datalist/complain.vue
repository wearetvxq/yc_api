<template>
    <div class="home">
        <Row>
            <Row class="Top">
              <Tabs type="card" @on-click="handleTab" >
                  <TabPane label="24小时投诉日报">
                      <complaintwentyfour v-if="tab0"></complaintwentyfour>
                  </TabPane>
                  <TabPane label="投诉8小时日报">
                      <complaineigtht v-if="tab1"></complaineigtht>
                  </TabPane>

                  <!-- <TabPane label="接单及时率">
                     <take-order></take-order>
                  </TabPane> -->

                  <TabPane label="首次联系用户及时率" >
                    <contactuser v-if="tab2"></contactuser>
                  </TabPane>
                  <TabPane label="投诉处理时长TOP20">
                    <toptwenty v-if="tab3"></toptwenty>
                  </TabPane>
                  <TabPane label="超时未回复">
                    <unanswered v-if="tab4"></unanswered>
                  </TabPane>
                  <TabPane label="高频小区统计" >
                    <highfrequentlyarea v-if="tab5"></highfrequentlyarea>
                  </TabPane>

                  <TabPane label="投诉回访满意度">
                    <visitedsatisfation v-if="tab6"></visitedsatisfation>
                  </TabPane>

                  <!-- <TabPane label="故障处理及时率通报">
                      <timely-rate v-if="tab7"></timely-rate >
                  </TabPane> -->
                   <TabPane label="高频故障网元TOP20">
                      <highfrequently v-if="tab7"></highfrequently>
                  </TabPane>
              </Tabs>
            </Row>
      </Row>
    </div>
</template>
<script>
    import complaintwentyfour from './complain-listPage/twentyfour.vue'
    import complaineigtht from './complain-listPage/eight.vue'
    // import takeOrder from './complain-listPage/order.vue'
    import timelyrate from './complain-listPage/timely.vue'
    import highfrequently from './complain-listPage/highfrequently.vue'
    import contactuser from './complain-listPage/contact.vue'
    import toptwenty from './complain-listPage/top.vue'
    import unanswered from './complain-listPage/Unanswered.vue'
    import highfrequentlyarea from './complain-listPage/higharea.vue'
    import visitedsatisfation from './complain-listPage/visited.vue'

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
         complaintwentyfour,
         complaineigtht,
         // takeOrder,
         timelyrate,
         highfrequently,
         contactuser,
         toptwenty,
         unanswered,
         highfrequentlyarea,
         visitedsatisfation
       }
    }
</script>
<style>
  .ivu-tabs.ivu-tabs-card>.ivu-tabs-bar .ivu-tabs-nav-container{
    font-size: 12px;
  }

</style>
