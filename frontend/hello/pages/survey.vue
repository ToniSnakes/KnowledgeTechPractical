<template>
<div>
  <TextQuestion :questionProp="question"/>
</div>
</template>

<script>
export default {
  data() {
    return {
      question: "Please wait..."
    };
  }
}
</script>
