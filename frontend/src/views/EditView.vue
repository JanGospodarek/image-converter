<template>
  <div class="w-screen h-screen flex items-center justify-center">
    <TitleStep
      v-if="step === 'hello'"
      :handleNextStep="handleNextStep"
      :setError="setErrorMsg"
    />

    <UploadPhotoStep
      v-if="step === 'upload'"
      :handleNextStep="handleNextStep"
    />

    <EditPhotoStep v-if="step === 'edit'" :setError="setErrorMsg" />

    <ErrorAlert v-if="errorMsg" :errorMsg="errorMsg" :timeout="delay" />
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
// eslint-disable-next-line
// @ts-ignore
import EditPhotoStep from "../components/edit/EditPhotoStep.vue";
// eslint-disable-next-line
// @ts-ignore
import ErrorAlert from "../components/error/ErrorAlert.vue";
import { ErrorProps } from "../components/error/ErrorPropsTypes";
const step = ref<string>("hello");
const handleNextStep = (nextStep: string) => {
  step.value = nextStep;
};
const errorMsg = ref<string | null>(null);
const delay = ref<boolean>(false);

const setErrorMsg = (msg: string | null) => (errorMsg.value = msg);
</script>
