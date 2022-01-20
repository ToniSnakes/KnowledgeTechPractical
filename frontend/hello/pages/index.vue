<template>
  <div class="bg-gray-100 h-screen">
    <div class="container mx-auto flex flex-col items-center py-12 sm:py-24 h-screen  z-index-10 justify-center">
      <div class="w-11/12 sm:w-2/3 mb-5 sm:mb-10">
        <h1
          class="
            text-2xl
            sm:text-3xl
            md:text-4xl
            lg:text-5xl
            xl:text-6xl
            text-center text-gray-800
            font-extrabold
            leading-tight
          "
        >
          Welcome to the 
          <span class="text-indigo-700">survey</span>
          of your dreams
        </h1>
        <p
          class="
            mt-5
            sm:mt-10
            text-gray-600
            font-normal
            text-center text-lg
            sm:text-lg
          "
        >
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nam assumenda reiciendis totam.
        </p>
      </div>
      <div class="flex justify-center items-center">
        <nuxt-link
          to="/survey"
          class="
            focus:outline-none
            bg-indigo-700
            transition
            duration-150
            ease-in-out
            hover:bg-indigo-600
            rounded
            text-white
            px-4
            sm:px-10
            py-2
            sm:py-4
            text-sm
            uppercase
          "
        >
          Get Started
        </nuxt-link>
      </div>
    </div>
    <img
      :src="require('@/static/illustration.png')"
      class="illustration"
      alt="illustration"
    />
  </div>
</template>

<script>
export default {
  name: 'CentreAlignedSimple',
  methods: {
    // Function to toggle header menu in mobile view.
    toggleMenu(flag) {
      let value = document.getElementById('menu')
      if (flag) {
        value.classList.remove('hidden')
      } else {
        value.classList.add('hidden')
      }
    },
  },
}
</script>
<style>
.z-index-10 *{
  z-index: 1000 !important;
}
img.illustration {
  position: fixed;
  right: -50px;
  bottom: -80px;
  z-index: 1;
  width: 500px;
}
</style>