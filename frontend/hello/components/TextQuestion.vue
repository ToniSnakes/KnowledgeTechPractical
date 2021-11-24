<!-- Please remove this file from your project -->
<template>
  <div class="relative flex items-top justify-center min-h-screen bg-gray-100 sm:items-center sm:pt-0">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.1.2/dist/tailwind.min.css" rel="stylesheet">
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
      <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
        <h2 class="text-2xl leading-7 font-semibold">
          Hello Routes!
        </h2>
        <p class="mt-3 text-gray-600">
          {{ question }}
        </p>
        <!-- <input class="mt-4 text-gray-800 border-t border-dashed" v-model="message" placeholder="yes/no">
        <button v-on:click="counter += 1">Send</button> -->
        <form id="signup-form" class="mt-4 text-gray-800 border-t border-dashed" v-if="renderForm">
          <!-- name -->
          <div class="field">
            <label class="label">Answer</label>
            <input type="text" class="input" name="name" v-model="answer" placeholder="yes/no" v-if="renderTextInput">
          </div>

          <!-- submit button -->
          <div class="field has-text-right mt-4">
            <button @click.prevent="formSubmit" type="submit" class="button is-danger">Submit</button>
          </div>
        </form>
        <div class="field has-text-right mt-4 border-dashed">
          <button @click.prevent="reset" type="submit" class="button is-danger">Reset</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [ 'questionProp' ],
  data() {
    return {
      answer: "",
      renderTextInput: true,
      posts: [],
      question: this.questionProp,
      questionName: "",
      renderForm: true
    };
  },
  created() {
    this.fetchQuestion()
  },
  methods: {
    async fetchQuestion() {
      const qDict = await this.$axios.$get('http://localhost:5000/nextQuestion')
      this.handleQDict(qDict)
    },
    async postAnswer(){
      const qDict = await this.$axios.$post(`http://localhost:5000/answer/${this.questionName}/${this.answer}`)
      this.handleQDict(qDict)
    },
    async reset(){
      const qDict = await this.$axios.$post('http://localhost:5000/reset')
      this.handleQDict(qDict)
      this.renderForm = true
    },
    handleQDict(qDict){
      console.log(qDict)
      this.question = qDict.question
      this.questionName = qDict.name
      if (qDict.name == "solved") {
        this.renderForm = false
      }
    },
    reloadForm(newQ){
      this.renderTextInput = false;
      this.answer = ""

      this.$nextTick(() => {
        this.renderTextInput = true;
      })
    },
    formSubmit() {
      console.log('form submitted')
      console.log(this.answer)
      if (this.answer != "yes" && this.answer != "no") {
        console.log("wrong input")
        this.reloadForm()
        this.question = `${this.question}\nPlease only use yes/no` // extremely jank
      }
      else {
        this.postAnswer()
        this.reloadForm()
      }
    }
  }
}
</script>