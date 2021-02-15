<template>
    <div class="searchbar-container">
        <input class = "searchbar" v-model="state.term" type="text" placeholder="Type anything..."/>
        <button type="submit" class="button" @click="$emit('searched', state.term)">Search</button>
    </div>
</template>
<script>
import { defineComponent, reactive } from '@vue/composition-api'
export default defineComponent({
    name:'SearchBar',
    setup(){
        const state = reactive({
            term: ""
        })
        return { state }     
    }
})
</script>
<style scoped>
    .searchbar {
       color: #000; 
       padding: 0.5rem;
       margin: 0.25rem;
       border-radius: 2rem;
       border: 1px solid #444;
    }
</style>