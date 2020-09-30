<template>
  <div class="card center">
    <img :src="`http://localhost:5000/api/file/${filename}`">
    <br>
    <button :disabled="infoDisabled" class="info_button button" @click="$emit('add-overlay'); infobox = true "><i class="fas fa-info-circle"></i> Info</button>
    <Infobox v-if="infobox" @close-box="infobox=false; $emit('close-box');">
      Title: {{details.title}}<br>
    Created on {{details.created_at.substring(details.created_at.indexOf(",")+1, details.created_at.indexOf(":")-3)}}<br>
    Author: {{details.author}}<br>
    <a class="info" :href="details.shortlink">Source</a>
    <br>
    </Infobox>
  </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "@vue/composition-api";
import { Meme } from "../types";
import Infobox from "@/components/Infobox.vue"
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
    background: #ddd;
    align-items: center;
    width: 24rem;
    height: 25rem;
    padding: 3rem 1rem;
  }
  img{
    height: 23rem;
    max-width: 24rem;
  }
  .center{
    align-items: center;
  }
  .info_button{
    background: #fff;
    font-size: 16px;
    margin-top: 1rem;

  }
  .info_button:hover{
    background: #eee;
    transition: ease;
  }
</style>
