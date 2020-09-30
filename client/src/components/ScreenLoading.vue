<template>
  <div :class="{ loader: true, fadeout: !isLoading }">
    <p>{{pageName}}</p>
  </div>
</template>
<script>
export default {
  name: 'ScreenLoading',
  props: {
    isLoading: Boolean,
    pageName: String
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Gloria+Hallelujah&display=swap');
.loader{
  background-color: #222;
  bottom: 0;
  top: 0;
  right: 0;
  color: #eee;
  display: block;
  font-family: 'Gloria Hallelujah', cursive;
  font-size: 50px;
  left: 0;
  overflow: hidden;
  padding-top: 10vh;
  position: fixed;
  text-align: center;
}
.fadeout {
  animation: fadeout 2s forwards;
}
@keyframes fadeout {
  to {
    opacity : 0;
    visibility: hidden;
  }
}
</style>
