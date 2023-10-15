<template>
  <div
    class="flex items-center justify-center relative w-[600px] rounded-xl shadow-xl h-[250px]"
  >
    <div
      class="flex flex-col items-center absolute top-0 left-0 z-0 w-full p-6"
    >
      <p class="text-5xl font-extrabold p-6">Dodaj nowe zdjęcie</p>
      <div class="flex justify-center">
        <input
          type="file"
          ref="file"
          name="file"
          class="file-input w-full max-w-xs"
          @change="handleFileInputChange()"
        />
        <button
          :class="`btn btn-square btn-success btn-outline  ${
            (!active || loading) && 'btn-disabled'
          }`"
          @click="uploadImage()"
        >
          <LoadingSpinner v-if="loading" />

          <SendButton v-if="!loading" />
        </button>
      </div>
      <div class="flex mt-6 w-full justify-between">
        <button
          class="btn btn-accent btn-outline"
          @click="props.handleNextStep('hello')"
        >
          <PrevArrow />
          Wróć
        </button>
        <button
          class="btn btn-accent btn-outline"
          @click="props.handleNextStep('upload')"
        >
          Dalej
          <NextArrow />
        </button>
      </div>
    </div>
    <Transition name="fade">
      <div
        class="absolute top-0 left-0 z-20 w-full h-full bg-black rounded-xl shadow-xl bg-opacity-60 flex justify-center items-center"
        v-if="status == 'ok'"
      >
        <img src="../../assets/checked.png" alt="" width="80" />
      </div>
    </Transition>
  </div>
</template>
<script lang="ts" setup>
import { defineProps, ref } from "vue";
import convertBase64 from "../../hooks/convertToBase";
import SendButton from "../../assets/sendButton.vue";
import LoadingSpinner from "../../assets/loadingSpinner.vue";
import PrevArrow from "../../assets/prevArrow.vue";
import NextArrow from "../../assets/nextArrow.vue";
const file = ref<HTMLInputElement | null>(null);
const loading = ref<boolean>(false);
const status = ref<"ok" | "error" | null>(null);
const active = ref<boolean>(false);

const handleFileInputChange = () => {
  if (file.value?.files && file.value.files[0] !== undefined)
    active.value = true;
};

const uploadImage = async () => {
  if (!file.value?.files || file.value.files[0] == undefined) return;
  loading.value = true;
  const base64 = await convertBase64(file.value.files[0]);
  const res = await fetch("http://127.0.0.1:8000/upload_image", {
    method: "POST",
    body: JSON.stringify({ image64: base64 }),
    headers: { "Content-Type": "application/json" },
  });
  const data = await res.json();
  loading.value = false;
  if (res.status == 200) {
    // handle ok
    status.value = "ok";
    console.log(data);
  } else {
    // handle error
  }
  setTimeout(() => {
    status.value = null;
  }, 2000);
};
const props = defineProps<{
  handleNextStep: (nextStep: string) => void;
}>();
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
