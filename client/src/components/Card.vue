<template>
  <div class="card center">
   <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
    <img :src="`http://localhost:5000/api/file/${filename}`">
    <h4 class="title">{{details.title}}</h4>
    <button :disabled="infoDisabled" class="info_button button" @click="infobox = true "><i class="fas fa-info-circle"></i> Info</button>
    <Infobox v-if="infobox" @close-box="infobox=false">
      Title: {{details.title}}<br>
    Created on {{details.created_at.substring(details.created_at.indexOf(",")+1, details.created_at.indexOf(":")-3)}}<br>
    Author: {{details.author}}<br>
    <a class="info" :href="details.shortlink"><i :class="'fab fa-'+details.source.toLowerCase()"/> Source</a>
    <br>
    </Infobox>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "@vue/composition-api";
import { Meme } from "../types";
import Infobox from "./Infobox.vue"
export default defineComponent(
  {
    name: 'Card',
    components:{
      Infobox
    },
    props: {
    info: Object as () => Meme,
    infoDisabled: Boolean
  },
    setup(props){
      let filename = "test"
      const details = ref<Meme>(null)
      const infoDisabled = props.infoDisabled
      let infobox = false
      if(props.info && props.info.file_name){
        filename = props.info.file_name;
        details.value = props.info;
      }
      return{
        filename, infobox, details, infoDisabled
      }
    }

  },
)

</script>
<style scoped>
  .card{
    background: #222;
    align-items: center;
    width: 47vw;
    height: 75vh;
    padding: 0.5rem;
    margin: 0;
    color: #fff;
  }
  img{
    height: 63vh;
    min-width: 25vw;
    max-width: 45vw;
  }
  .title{
    margin: 0.1rem;
  }
  /* For mobile phones: */
  @media only screen and (max-width: 768px) {
  
    .card{
      width: 87vw;
      height: 36vh;
    }
    img{
      height: 25vh;
      max-width: 80vw;
    }
}
  .info_button{
    background: #fff;
    font-size: 16px;
    margin: 0.2rem;
    margin-bottom: 0.4rem;
  }
  .info_button:hover{
    background: #eee;
    transition: ease;
  }
</style>
