<template>
  <div class="flex items-center justify-center">
    <div class="flex flex-col items-center rounded-xl shadow-xl p-6">
      <p class="text-5xl font-extrabold p-6">Dodaj nowe zdjęcie</p>
      <div class="flex justify-center">
        <input type="file" class="file-input w-full max-w-xs" />
        <button class="btn btn-square btn-success btn-outline">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            fill="currentColor"
            viewBox="0 0 256 256"
          >
            <path
              d="M227.32,28.68a16,16,0,0,0-15.66-4.08l-.15,0L19.57,82.84a16,16,0,0,0-2.42,29.84l85.62,40.55,40.55,85.62A15.86,15.86,0,0,0,157.74,248q.69,0,1.38-.06a15.88,15.88,0,0,0,14-11.51l58.2-191.94c0-.05,0-.1,0-.15A16,16,0,0,0,227.32,28.68ZM157.83,231.85l-.05.14L118.42,148.9l47.24-47.25a8,8,0,0,0-11.31-11.31L107.1,137.58,24,98.22l.14,0L216,40Z"
            ></path>
          </svg>
        </button>
      </div>
      <div class="flex mt-6 w-full justify-between">
        <button
          class="btn btn-accent btn-outline"
          @click="props.handleNextStep('hello')"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            fill="currentColor"
            viewBox="0 0 256 256"
          >
            <path
              d="M224,128a8,8,0,0,1-8,8H59.31l58.35,58.34a8,8,0,0,1-11.32,11.32l-72-72a8,8,0,0,1,0-11.32l72-72a8,8,0,0,1,11.32,11.32L59.31,120H216A8,8,0,0,1,224,128Z"
            ></path>
          </svg>
          Wróć
        </button>
        <button
          class="btn btn-accent btn-outline"
          @click="props.handleNextStep('upload')"
        >
          Dalej
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            fill="currentColor"
            viewBox="0 0 256 256"
          >
            <path
              d="M221.66,133.66l-72,72a8,8,0,0,1-11.32-11.32L196.69,136H40a8,8,0,0,1,0-16H196.69L138.34,61.66a8,8,0,0,1,11.32-11.32l72,72A8,8,0,0,1,221.66,133.66Z"
            ></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { defineProps } from "vue";

const props = defineProps<{
  handleNextStep: (nextStep: string) => void;
}>();
</script>
