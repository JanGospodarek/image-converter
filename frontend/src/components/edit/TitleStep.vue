<template>
  <div class="flex flex-col">
    <p class="text-6xl font-extrabold p-6">Podążaj za kolejnymi krokami</p>

    <button
      class="btn btn-accent btn-outline mx-auto"
      @click="props.handleNextStep('upload')"
    >
      Dalej
      <NextArrow />
    </button>
  </div>
</template>

<script lang="ts" setup>
import { defineProps } from "vue";
import NextArrow from "../../assets/nextArrow.vue";

const props = defineProps<{
  handleNextStep: (nextStep: string) => void;
}>();
</script>
