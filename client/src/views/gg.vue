<template>
  <div :class="{overlay:state.infobox}">
    <h3>Score: {{state.score}}</h3>
    <div v-if="posts[0].file_name" :key=state.componentKey>

    <li v-for="(post, index) in posts"  :key="index">
      <h3 class = "likes" v-if="index%2==0 | state.found">
      Likes: {{posts[index].likes}}
      </h3>
      <div class="likes" v-if="index%2==1 && !state.found">
        <button class="higher button" @click="answeredHigher(true)">Higher</button>
        <button class="lower button" @click="answeredHigher(false)">Lower</button>
        </div>
      <Card :info="posts[index]" :infoDisabled="index%2==1" @add-overlay="toggleInfobox" @close-box="toggleInfobox"/>
    </li>
      <Infobox v-if="state.found && state.infobox" @close-box="toggleAnswerbox">{{state.message}}<br></Infobox>
    </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import Infobox from '@/components/Infobox.vue'
import Card from '@/components/Card.vue'
import { postService } from '../services'
import { Meme } from '../types'
import { ref, defineComponent, onMounted, reactive, computed } from '@vue/composition-api';;
export default defineComponent({
  name: 'MemeGG',
  components: {
    Card, Infobox
  },
  data(){
    return{
      posts_now : []
    }
  },
  setup(){
    const posts = ref<Meme[]>(null);
    const state = reactive({
      infobox: false,
      componentKey: 0,
      isHigher : true,
      reveal: false,
      score: 0,
      found: false,
      message: "Wrong",
      answerBox: false
    })
    onMounted(
      async () => {
        posts.value = await postService.getRandomAmount(2)
        state.isHigher = posts?.value[1]?.likes > posts.value[0].likes
      }
    );
    console.log(posts)
    //@ts-ignore
    const loadNew = async () => {
      try {
        if(posts.value && posts.value[1]){
          posts.value[0] = posts.value[1]
        const result = await postService.getRandomAmount(1);
        posts.value[1] = await result[0]
        state.isHigher = posts?.value[1]?.likes > posts.value[0].likes
        }
        state.found = false;

        state.componentKey += 1;
      }
      catch{
          console.log("error")
      }
    };
    const toggleInfobox = () => {
      state.infobox = !state.infobox
      //state.componentKey+=1;
    };
    const toggleAnswerbox = () => {
      state.infobox = !state.infobox;
      state.answerBox = !state.answerBox;
      loadNew();
    }
    const answeredHigher = (higher:boolean) => {
      if(higher == state.isHigher){
        state.message = "Correct! You earned a point"
        state.score += 1
      }
      else{
        state.message = "Wrong. :( Your final score was "+state.score+"."
        state.score = 0

      }
      state.found = true
      state.infobox = true;
      state.answerBox = true;
    }
    return {
      posts, state, loadNew, toggleInfobox, answeredHigher, toggleAnswerbox
    };
  }
});
</script>>

<style scoped>
li{
  display: inline-block;
  padding: 2rem;
}
.likes{
  font-size: 25px;
  align-items: center;
}
.overlay:not(.infobox){
  opacity: 0.7;
}
.higher{
  background-color: lightgreen;
  margin: 2px;
}
.higher:hover{
  background-color: rgb(161, 238, 161);
}
.lower{
  background-color: lightcoral;
  margin: 2px;
}
.lower:hover{
  background-color: rgb(240, 150, 150);
}
</style>

