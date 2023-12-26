<template>
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
    errorMsg.value = "";
    props.setError("Błąd połączenia z serwerem");
  }
});

const props = defineProps<{
  handleNextStep: (nextStep: string) => void;
  setError: (msg: string) => void;
}>();
</script>
