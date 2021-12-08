<template>
  <div class="relative flex items-top justify-center min-h-screen bg-gray-100 sm:items-center sm:pt-0">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.1.2/dist/tailwind.min.css" rel="stylesheet">
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
      <div class="mt-8 bg-white overflow-hidden shadow sm:rounded-lg p-6">
        <h2 class="text-2xl leading-7 font-semibold">
          Statistics Picker
        </h2>
        <p class="mt-3 text-gray-600">
          {{ question }}
        </p>
        <form id="signup-form" class="mt-4 text-gray-800 border-t border-dashed" v-if="renderForm">
          <!-- name -->
          <div class="field">
            <label class="label">Answer:</label><br>
            <!-- <input type="text" class="input" name="name" v-model="answer" placeholder="yes/no" v-if="renderTextInput"><br> reference -->
            <div v-for="answerOption in answerOptions" :key="answerOption">
              <!-- <RadioOption :answerOption="answerOption" @update="radioOption(answerOption)"/> -->
              <input type="radio" name="radio" v-model="answer" :value="answerOption">{{ answerOption }}<br>
            </div>
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
      renderForm: true,
      baseUrl: process.env.BASE_URL || 'http://localhost:5000',
      answerOptions: []
    };
  },
  created() {
    this.fetchQuestion()
  },
  methods: {
    async fetchQuestion() {
      const url = `${this.baseUrl}/nextQuestion`
      console.log(url)
      console.log(process.env.baseUrl)
      const qDict = await this.$axios.$get(url)
      this.handleQDict(qDict)
    },
    async postAnswer(){
      const url = `${this.baseUrl}/answer/${this.questionName}/${this.answer}`
      console.log(url)
      const qDict = await this.$axios.$post(url)
      this.handleQDict(qDict)
    },
    async reset(){
      const url = `${this.baseUrl}/reset`
      console.log(url)
      const qDict = await this.$axios.$post(url)
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
      else {
        this.answerOptions = qDict.answers
      }
    },
    reloadForm(){
      //this.renderTextInput = false;
      this.answer = ""

      /*this.$nextTick(() => {    // keep as reference if we need it again
        this.renderTextInput = true;
      })*/
    },
    formSubmit() {
      console.log('form submitted')
      console.log(this.answer)
      if (this.answer == "") {
        console.log("no input")
        this.reloadForm()
        this.question = `${this.question}\nPlease specify a value` // extremely jank
      }
      else {
        this.postAnswer()
        this.reloadForm()
      }
    }
  }
}
</script>