<template>
  <div class="home">
    <ScreenLoading :pageName="'memecc'" :isLoading='isLoading'/>
    <main v-if='!isLoading'>
    Meme-CC is under construction. Check out MemeGG in the meantime.
    </main>
  </div>
</template>

<script>
// @ is an alias to /src

import ScreenLoading from '@/components/ScreenLoading.vue'
export default {
  name: 'Home',
  components: {
    ScreenLoading
  },
  data () {
    return { isLoading: true }
  },
  mounted () {
    setTimeout(() => {
      this.isLoading = false
    }, 100)
  }

}
</script>
