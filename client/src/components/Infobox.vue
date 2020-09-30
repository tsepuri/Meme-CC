<template>
  <div class="infobox" v-if="!closeBox">
    <div class="content">
    <slot>
    </slot>

    <button class="close" @click="$emit('close-box')">Close</button>
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

   .infobox .content{
    position: absolute;
    background-color: #fff;
    padding:3rem;
    font-size: 25px;
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
    cursor:pointer;
    color: #fff;
  }
  .close:hover{
    background-color: rgb(238, 85, 85);
    transition: 200ms;
  }

</style>

