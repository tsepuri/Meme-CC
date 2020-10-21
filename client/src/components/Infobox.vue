<template>
  <div class="infobox" v-if="!closeBox">
    <div class="content">
    <slot>
    </slot>

    <button class="close button" @click="$emit('close-box')">Close</button>
    </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "@vue/composition-api";
import { Meme } from "../types";
import Infobox from "@/components/Infobox.vue"
export default defineComponent(
  {
    name: 'Infobox',
    setup(props){
      let closeBox = false
    }

  },
)

</script>
<style scoped>
  .infobox {
    background-color: rgba(3, 3, 3, 0.7);
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    position: fixed;
    z-index: 1;
  }
   .infobox .content{
    position: fixed;
    background-color: #fff;
    padding:3rem;
    font-size: 25px;
    z-index: 2;
    top: 50%;
    left: 50%;
    max-width: 20rem;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
    color: #000;
    opacity: 1!important;
  }
  .info{
    text-decoration: none;
    color: #222;
  }
  .info:hover{
    color: #555;
  }
  .close{
    background-color: rgb(233, 41, 41);
    padding: 1rem;
    margin-top: 3px;
    border: none;
    border-radius: 15px;
    color: #fff;
  }
  .close:hover{
    background-color: rgb(238, 85, 85);
    transition: 200ms;
  }

</style>

