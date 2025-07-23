<template>
  <div class="images">
    <div class="block">
      <el-image
        style="width: 300px; height: 300px"
        :src="url1"
      />
<!--      <el-image-->
<!--        style="width: 300px; height: 100px"-->
<!--        :src="url2"-->
<!--      />-->
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import localImage from '@/assets/ff.png'

export default {
  name: 'Dashboard',
  data() {
    return {
      url1: localImage
      // url1: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.askququ.com%2Fuploads%2Fallimg%2F161103%2F1_161103000823_1.jpg&refer=http%3A%2F%2Fwww.askququ.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1671551929&t=5004d6bccc38525300b9a9c196091de1',
      // url2: 'https://img2.baidu.com/it/u=616788594,529779786&fm=253&fmt=auto&app=138&f=JPEG?w=1658&h=500'
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.images{
  margin: 20px;
}
.demonstration{
  margin-right: 20px;
}
.el-row{
  margin-top: 20px;
}
</style>
