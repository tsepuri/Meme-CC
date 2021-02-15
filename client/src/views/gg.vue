<template>
  <div>
    <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
    <h3 class="score">Score: {{state.score}}</h3>
    <h3 class="score">High Score: {{state.highscore}}</h3>
    <div v-if="posts[0].file_name" :key=state.componentKey>

    <li v-for="(post, index) in posts"  :key="index">
      <h3 class = "likes" v-if="index%2==0 | state.found">
      Likes: {{posts[index].likes}}
      </h3>
      <div class="likes" v-if="index%2==1 && !state.found">
        <button class="higher button" @click="answeredHigher(true)"><i class="fas fa-arrow-up"></i> HIGHER </button>
        <button class="lower button" @click="answeredHigher(false)"><i class="fas fa-arrow-down"></i> LOWER</button>
        </div>
      <Card :info="posts[index]" :infoDisabled="index%2==1" class="main-card"/>
    </li>
      <Infobox v-if="state.found" @close-box="toggleAnswerbox">{{state.message}}<br></Infobox>
    </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import Infobox from '../components/Infobox.vue'
import Card from '../components/Card.vue'
import getCookies from '../services/cookieUtil'
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
    interface MemeGGType {
      componentKey: number,
      isHigher: boolean,
      reveal: boolean,
      score: number,
      found: boolean,
      message: string,
      answerBox: boolean,
      threshold: number,
      highscore: string
    }
    const state = reactive({
      componentKey: 0,
      isHigher : true,
      reveal: false,
      score: 0,
      found: false,
      message: "Wrong",
      answerBox: false,
      threshold: computed<number>(() => Math.max(10000 - (2000* state.score/3), 5)),
      highscore: '0'
    }) as MemeGGType
    onMounted(
      async () => {
        state.highscore = getCookies().highscore;
        if (state.highscore === undefined) {
            state.highscore = '0';
            console.log(state.highscore);
            document.cookie = `highscore=0;path=/;`;
            console.log(document.cookie);
        }
        posts.value = await postService.getRandomAmount(2);
        state.isHigher = posts?.value[1]?.likes > posts.value[0].likes;
      }
    );
    console.log(posts)
    //@ts-ignore
    const loadNew = async () => {
      try {
        if(posts.value && posts.value[1]){
          posts.value[0] = posts.value[1]
        while(Math.abs(posts.value[0].likes - posts.value[1].likes) < state.threshold){
          const result = await postService.getRandomAmount(1);
          posts.value[1] = await result[0]
        }
        state.isHigher = posts.value[1].likes > posts.value[0].likes
        }
        state.found = false;

        state.componentKey += 1;
      }
      catch{
          console.log("error")
      }
    };
    const toggleAnswerbox = () => {
      state.answerBox = !state.answerBox;
      loadNew();
    }
    const answeredHigher = (higher:boolean) => {
      if(higher == state.isHigher){
        state.message = "Correct! You earned a point"
        state.score += 1
        if (state.score > +state.highscore) {
          state.highscore = state.score+"";
          document.cookie = `highscore=${state.score};path=/;`;
          console.log(state.highscore);
        }
      }
      else{
        state.message = "Wrong. :( Your final score was "+state.score+"."
        state.score = 0

      }
      state.found = true
      state.answerBox = true;
    }
    return {
      posts, state, loadNew, answeredHigher, toggleAnswerbox
    };
  }
});
</script>

<style>
li{
  display: inline-block;
  padding: 0 0.5rem;
}
.score{
  margin: 0.2rem;
}
.likes{
  font-size: 25px;
  align-items: center;
  margin: 0.2rem;
}

.higher{
  background-color: rgb(84, 235, 84);
  margin: 0.2rem;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
}
.higher:hover{
  background-color: lightgreen;
}
.lower{
  background-color: rgb(236, 69, 69);
  margin: 0.2rem;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
}
.lower:hover{
  background-color: lightcoral;
}
</style>

