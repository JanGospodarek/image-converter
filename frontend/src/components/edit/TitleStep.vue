<template>
  <div class="w-screen h-screen relative">
    <div
      class="absolute h-screen w-screen top-0 left-0 flex flex-col items-center justify-center"
    >
      <p class="text-6xl font-extrabold p-6">Podążaj za kolejnymi krokami</p>

      <button
        :class="`btn  btn-outline mx-auto ${
          errorMsg ? 'btn-error' : 'btn-accent'
        }`"
        :disabled="errorMsg != null"
        @click="props.handleNextStep('upload')"
      >
        Dalej
        <NextArrow />
      </button>
    </div>
    <div
      className="alert alert-error absolute right-0 left-0 bottom-16 ml-auto mr-auto h-16  w-1/2"
      v-if="errorMsg"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="stroke-current shrink-0 h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
      <span>{{ errorMsg }}</span>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineProps, onMounted, ref } from "vue";
import NextArrow from "../../assets/nextArrow.vue";
import store from "../../store";
const errorMsg = ref<string | null>(null);

onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/init", {
      method: "GET",
    });

    if (!res.ok) throw new Error("Błąd połączenia z serwerem");

    const data = await res.json();

    if (res.status == 200) store.commit("setId", data.id);
  } catch (error) {
    errorMsg.value = "Błąd połączenia z serwerem";
    console.log(error);
  }
});

const props = defineProps<{
  handleNextStep: (nextStep: string) => void;
}>();
</script>
