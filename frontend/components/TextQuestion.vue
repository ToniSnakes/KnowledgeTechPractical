<template>
  <div
    class="
      bg-gray-100
      min-h-screen
      w-100
      items-center
      flex
      justify-center
      content-center
    "
  >
    <div class="container mx-auto px-4 w-100 sm:w-10/12 md:w-8/12 z-index-10">
      <nuxt-link class="home-button" to="/">Home</nuxt-link>
      <div class="flex justify-between content-center">
        <h1 class="text-2xl mt-4 leading-7 font-bold uppercase">
          Test Chooser
        </h1>

        <button
          @click="sidebar = !sidebar"
          class="
            inline-block
            bg-indigo-200
            rounded-lg
            px-4
            py-2
            text-sm
            font-semibold
            uppercase
            text-indigo
            mb-2
          "
        >
          Trace
        </button>
      </div>
      <vue-tailwind-modal
        :showing="showModal"
        @close="showModal = false"
        :showClose="true"
        :backgroundClose="true"
        v-if="!!qDict"
        style="z-index: 2000 !important"
      >
        <h3 class="text-xl leading-7 font-bold capitalize">More info</h3>
        <p>{{qDict.info}}</p>
      </vue-tailwind-modal>

      <div class="container mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-5 gap-6">
          <div :class="sidebar ? 'col-span-3' : 'col-span-5'">
            <div
              class="rounded-lg overflow-hidden shadow-lg bg-white mt-4 mb-32"
            >
              <div class="px-6 py-4">
                <p class="text-gray-700 text-xl">
                  {{ question }}

                  <a
                    class="link-button"
                    v-if="!!question && questionName != 'solved'"
                    @click="showModal = true"
                    >More Info</a
                  >
                </p>

                <div v-if="questionName != 'solved'">
                  <div
                    v-for="answerOption in answerOptions"
                    :key="answerOption"
                    class="flex items-center mr-4 my-2"
                  >
                    <input
                      type="radio"
                      name="radio"
                      v-model="answer"
                      :value="answerOption"
                    />
                    <label class="ml-4 capitalize"> {{ answerOption }}</label>
                  </div>
                </div>
                <div v-if="questionName == 'solved'">
                  <span style="white-space: pre-wrap">{{ description }}</span>
                  <span style="white-space: pre-wrap; background-color: lightgray;">{{r}}</span>
                </div>
              </div>
              <div class="px-6 pt-4 pb-2">
                <span v-if="questionName == 'solved'">
                  <button
                    @click.prevent="reset"
                    class="
                      inline-block
                      bg-pink-100
                      rounded-lg
                      px-8
                      py-5
                      text-sm
                      font-semibold
                      uppercase
                      text-grey-700
                      mr-2
                      mb-2
                    "
                  >
                    Reset
                  </button>

                  <button
                    @click.prevent="undo"
                    class="
                      inline-block
                      bg-pink-100
                      rounded-lg
                      px-8
                      py-5
                      text-sm
                      font-semibold
                      uppercase
                      text-grey-700
                      mr-2
                      mb-2
                    "
                  >
                    Undo
                  </button>
                </span>
                <span v-else>
                  <button
                    @click.prevent="formSubmit"
                    class="
                      inline-block
                      bg-indigo-500
                      rounded-lg
                      px-8
                      py-5
                      text-sm
                      font-semibold
                      uppercase
                      text-white
                      mr-2
                      mb-2
                    "
                  >
                    Submit
                  </button>

                  <button
                    @click.prevent="reset"
                    class="
                      inline-block
                      bg-pink-100
                      rounded-lg
                      px-8
                      py-5
                      text-sm
                      font-semibold
                      uppercase
                      text-grey-700
                      mr-2
                      mb-2
                    "
                  >
                    Reset
                  </button>

                  <button
                    @click.prevent="undo"
                    class="
                      inline-block
                      bg-pink-100
                      rounded-lg
                      px-8
                      py-5
                      text-sm
                      font-semibold
                      uppercase
                      text-grey-700
                      mr-2
                      mb-2
                    "
                  >
                    Undo
                  </button>
                </span>
              </div>
            </div>
          </div>
          <div class="col-span-2" v-show="sidebar" style="overflow-y: scroll;">
            <div
              class="
                rounded-lg
                overflow-hidden
                shadow-lg
                bg-white
                mt-4
                mb-32
                p-4
              "
            >
              <div v-if="qDict.trace && qDict.trace.rules" style="height: 200 px;">
                <div v-for="(item, i) in qDict.trace.rules" :key="i">
                  <h4 class="font-bold">Facts</h4>
                  <ul>
                    <li
                      v-for="(it, index) in Object.keys(showFacts(i))"
                      :key="index"
                    >
                      <strong>{{ it }}:</strong> {{ showFacts(i)[it] }}
                    </li>
                  </ul>

                  <h4 class="font-bold mt-2">Rules</h4>
                  <ul>
                    <li
                      v-for="(i, index) in Object.keys(showRules(i))"
                      :key="index"
                    >
                      <span
                        >[
                        <li
                          v-for="(j, index) in Object.keys(item[i].premises)"
                          :key="index"
                        >
                          <strong>{{ j }}</strong
                          >: {{ item[i].premises[j] || '--' }}
                        </li>
                        ]
                      </span>
                      => [
                      <span v-if="item[i].conclusion">
                        <li
                          v-for="(j, index) in Object.keys(item[i].conclusion)"
                          :key="index"
                        >
                          {{ j }}: {{ index }}
                        </li>
                      </span>

                      ]
                    </li>
                  </ul>
                  <br />
                </div>
              </div>
            </div>
          </div>
        </div>
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
import VueTailwindModal from 'vue-tailwind-modal'
import Alert from './Alert.vue'
export default {
  props: ['questionProp'],
  data() {
    return {
      answer: '',
      renderTextInput: true,
      posts: [],
      question: this.questionProp,
      questionName: '',
      description: '',
      r: 'hey',
      renderForm: true,
      baseUrl: process.env.BASE_URL || 'http://localhost:5000',
      answerOptions: [],
      message: '',
      showModal: false,
      qDict: {},
      no: 0,
      sidebar: false,
    }
  },
  computed: {
    rules() {
      let premises = []
      let conclusion = []
      this.qDict.trace.rules.forEach((item) => {
        premises.push(item[0].premises)
        conclusion.push(item[0].conclusion)
      })
      return { premises, conclusion }
    },
  },
  created() {
    this.fetchQuestion()
  },
  methods: {
    showFacts(i) {
      return this.qDict.trace.facts[i]
    },
    showRules(i) {
      return this.qDict.trace.rules[i]
    },
    async fetchQuestion() {
      try {
        const url = `${this.baseUrl}/nextQuestion`
        console.log(url)
        console.log(this.baseUrl)
        const qDict = await this.$axios.$get(url)
        this.handleQDict(qDict)
      } catch (error) {
        console.log('error', error)
      }
    },
    async postAnswer() {
      const url = `${this.baseUrl}/answer/${this.questionName}/${this.answer}`
      console.log(url)
      const qDict = await this.$axios.$post(url)
      this.handleQDict(qDict)
    },
    async undo() {
      const url = `${this.baseUrl}/undo`
      console.log(url)
      const qDict = await this.$axios.$post(url)
      this.handleQDict(qDict)
      this.renderForm = true
    },
    async reset() {
      const url = `${this.baseUrl}/reset`
      console.log(url)
      const qDict = await this.$axios.$post(url)
      this.handleQDict(qDict)
      this.renderForm = true
    },
    handleQDict(qDict) {
      console.log('qDict', qDict)
      this.qDict = qDict
      this.question = qDict.question
      this.questionName = qDict.name
      this.no += 1
      if (qDict.name == 'solved') {
        this.renderForm = false
        this.description = qDict.description
        this.r = qDict.r
        this.message = "You've solved this question. Go to the next question"
      } else {
        this.answerOptions = qDict.answers
      }
    },
    reloadForm() {
      this.answer = ''
    },
    formSubmit() {
      console.log('form submitted')
      console.log(this.answer)
      if (this.answer == '') {
        console.log('no input')
        this.reloadForm()
        this.message = 'Please specify a value'
        this.question = `${this.question}` // extremely jank
      } else {
        this.postAnswer()
        this.reloadForm()
      }
    },

    nextQuestion() {},
  },
  components: { Alert, VueTailwindModal },
}
</script>

<style>
.z-index-10 {
  z-index: 1000 !important;
}
img.illustration {
  position: fixed;
  right: -50px;
  bottom: -80px;
  z-index: 1;
  width: 500px;
}
.bg-smoke-800 {
  background: rgb(0, 0, 0, 60%);
}
.fixed.inset-0.w-full.h-screen.flex.items-center.justify-center.bg-smoke-dark {
  background: rgb(0, 0, 0, 70%) !important;
}

.home-button:hover {
  color: rgb(0 97 255);
  text-decoration: underline;
}
.link-button {
  color: rgb(0 97 255);
}
.link-button:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>