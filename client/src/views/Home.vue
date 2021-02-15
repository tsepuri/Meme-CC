<template>
  <div class="home">
    <ScreenLoading :pageName="'memecc'" :isLoading='state.isLoading'/>
    <main v-if='!state.isLoading'>
    Meme-CC is under construction, but you can search for posts now! Check out MemeGG in the meantime.
        <SearchBar @searched="onSearch"/>
    <div v-if="state.searched" id="search-results">
      <li v-for="(post, index) in state.searchData" :key="index">
        <Card :info="post" :infoDisabled="false"/>
        </li>
      </div>
    </main>
  </div>
</template>

<script>
// @ is an alias to /src

import ScreenLoading from '@/components/ScreenLoading.vue'
import SearchBar from '@/components/SearchBar.vue'
import Card from '@/components/Card.vue'
import { postService } from '../services'
import { defineComponent, reactive, onMounted } from '@vue/composition-api';;
export default defineComponent({
  name: 'Home',
  components: {
    ScreenLoading,
    SearchBar,
    Card
  },
  setup () {
    const state = reactive({
      searched: false,
      isLoading: true,
      searchData: []
    })
    const onSearch = async(term) => {
      state.searched = false;
      state.searchData = await postService.getMatchingText(term);
      console.log(state.searchData);
      state.searched = true
    }
    onMounted(
      () => {
        setTimeout(() => {
      state.isLoading = false
    }, 100)
      }
    )
    return { state, onSearch }
  }

})
</script>
<style scoped>
a{
  text-decoration: none;
  color: #fff;
}
</style>
