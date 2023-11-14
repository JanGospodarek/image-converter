<template>
  <div class="w-screen h-screen flex items-center justify-center">
    <!-- <TitleStep v-if="step === 'hello'" :handleNextStep="handleNextStep" />

    <UploadPhotoStep
      v-if="step === 'upload'"
      :handleNextStep="handleNextStep"
    /> -->
    <!-- <EditPhotoStep v-if="step === 'edit'" /> -->
    <EditPhotoStep />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
// eslint-disable-next-line
// @ts-ignore
import TitleStep from "../components/edit/TitleStep.vue";
// eslint-disable-next-line
// @ts-ignore
import UploadPhotoStep from "../components/edit/UploadPhotoStep.vue";
import EditPhotoStep from "../components/edit/EditPhotoStep.vue";

const step = ref<string>("hello");
const handleNextStep = (nextStep: string) => {
  step.value = nextStep;
};
</script>
