<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link> 
      <router-link to="/memegg">MemeGG</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
body{
  background-color: #555;
  color: #fff;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#nav {
  padding: 5px 30px;

  a {
    text-decoration: none;
    font-weight: bold;
    color: #7aade0;
    padding: 4px;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
