<template lang="html">
     <div class="assembly">
         <Row>
            <Row class="Top">
                <Tabs type="card" @on-click="handleTab" >
                  <TabPane label="入库明细">
                      <assembly-bound v-if="tab0"></assembly-bound>
                  </TabPane>
                  <TabPane label="装维人员申领明细">
                      <assembly-apply v-if="tab1"></assembly-apply>
                  </TabPane>
                  <TabPane label="装机使用明细">
                      <assembly-instruction v-if="tab2"></assembly-instruction>
                  </TabPane>
                  <TabPane label="维护使用明细">
                      <assembly-maintance v-if="tab3"></assembly-maintance>
                  </TabPane>
                  <TabPane label="报废明细表">
                      <assembly-abolish v-if="tab4"></assembly-abolish>
                  </TabPane>
                  <TabPane label="返修明细">
                      <assembly-repair v-if="tab5"></assembly-repair>
                  </TabPane>
                </Tabs>
            </Row>
         </Row>
     </div>
</template>

<script>
import assemblyBound from './AssemblyDetail/inbound.vue'
import assemblyApply from './AssemblyDetail/apply.vue'
import assemblyInstruction from './AssemblyDetail/instruction.vue'
import assemblyMaintance from './AssemblyDetail/maintance.vue'
import assemblyAbolish from './AssemblyDetail/abolish.vue'
import assemblyRepair from './AssemblyDetail/repair.vue'

export default {
     data(){
       return{
         tab0:true,
         tab1:false,
         tab2:false,
         tab3:false,
         tab4:false,
         tab5:false
       }
     },
     methods:{
       handleTab(name) {
          this['tab' + name] = true
       }
     },
     components:{
        assemblyBound,
        assemblyApply,
        assemblyInstruction,
        assemblyMaintance,
        assemblyAbolish,
        assemblyRepair
     }
}
</script>

<style lang="scss" scoped>

</style>
