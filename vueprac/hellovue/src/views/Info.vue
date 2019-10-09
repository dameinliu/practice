<template>
  <div>
    Hello Info! <br>
    <button type="button" @click="add">添加</button>
    <demo1></demo1>
  </div>
</template>

<script>
import store from '@/store'
import demo1 from '@/components/demo1.vue';

export default {
  name: 'info',
  store,
  data: {

  },
  methods: {
  	add() {
  		console.log('Add Event from Info!')
  		store.commit('increase')
  	}
  },
  components: {
    demo1,
  },
};
</script>
