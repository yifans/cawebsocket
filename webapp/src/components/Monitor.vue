<template>
  <div class="monitor">
    <h1 id='page-title'>Monitor PVs via websocket</h1>
    <Table :columns="columns1" :data="data1"></Table>
  </div>
</template>

<script>
export default {
  name: 'monitor',
  data () {
    return {
      columns1: [
        {
          title: 'PV Name',
          key: 'pv'
        },
        {
          title: 'Value',
          key: 'value'
        }
      ],
      data1: []
    }
  },
  mounted: function () {
    var vm = this
    var pvlist = ['RNG:BEAM:CURR',
      'RNG:BEAM:LIFE',
      'RNG:ENG',
      'RNG:OPER:MODE',
      'RNG:OPER:STAT'
    ]
    var ws = new WebSocket('ws://localhost:7890/')
    ws.onopen = function () {
      ws.send(pvlist)
    }
    ws.onmessage = function (event) {
      var rec = JSON.parse(event.data)
      var flag = false // 缺省表中没有该元素
      for (var i in vm.data1) {
        if (vm.data1[i].pv === rec.pvname) {
          vm.data1[i].value = rec.value
          flag = true
          break
        }
      }
      if (flag === false) {
        var item = {
          pv: rec.pvname,
          value: rec.value
        }
        vm.data1.push(item)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#page-title {
  font-size: 3em;
}
</style>
