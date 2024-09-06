<script setup lang="ts">
//import Pong from './components/Pong.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <!-- code: make a dark themed one simple page ui, with round borders -->

    <!-- code: make a title for the page. The goal is to predict if infos inside text (or url) are fake or true -->

    <!-- code: make an input field in the middle of the page, long, round borders. placeholder : "paste text or url" -->

    <!-- code: when submitting the input field, send the text to /api/predict. it will respond with this object: {real: bool, confidence: float}. real is if info is real or not, confidence is in percent, how much it is confident. -->

    <!-- code: print if it is true or not and the confidence. -->

    <!-- code: remove everything that is not related to this app. -->
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
    <Pong />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
