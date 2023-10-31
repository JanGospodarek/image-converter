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
          :class="`file-input w-full max-w-xs ${extError && 'bg-error'}`"
          @change="handleFileInputChange($event)"
        />
        <button
          :class="`btn btn-square btn-success btn-outline ml-4  ${
            (!active || loading) && 'btn-disabled'
          }`"
          @click="uploadImage()"
        >
          <span
            className="loading loading-dots loading-lg"
            v-if="loading"
          ></span>

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
          :disabled="!activeBtn"
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
    <Transition name="fade">
      <div
        class="absolute top-0 left-0 z-20 w-full h-full bg-black rounded-xl shadow-xl bg-opacity-60 flex flex-col justify-center items-center"
        v-if="status == 'error'"
      >
        <img src="../../assets/error.png" alt="" width="80" />
        <p class="text-white">{{ errorMsg }}</p>
      </div>
    </Transition>
  </div>
</template>
<script lang="ts" setup>
import { defineProps, ref, onMounted } from "vue";
import { useStore } from "vuex";
import { key } from "../../store";

import convertBase64 from "../../hooks/convertToBase";
import SendButton from "../../assets/sendButton.vue";
import PrevArrow from "../../assets/prevArrow.vue";
import NextArrow from "../../assets/nextArrow.vue";
const store = useStore(key);

const file = ref<HTMLInputElement | null>(null);
const loading = ref<boolean>(false);
const status = ref<"ok" | "error" | null>(null);
const activeBtn = ref<boolean>(false);
const extError = ref<boolean>(false);
const errorMsg = ref<string | null>(null);
const active = ref<boolean>(false);
const acceptableExts = ["png", "jpg", "jpeg"];

const handleFileInputChange = (e: Event) => {
  if (!file.value?.files) return;

  const ext = file.value.files[0].name.split(".").pop() as string;

  if (!acceptableExts.includes(ext)) {
    const target = e.target as HTMLInputElement;
    target.value = "";
    active.value = false;
    extError.value = true;
  } else {
    active.value = true;
    extError.value = false;
  }
};

const uploadImage = async () => {
  if (!file.value?.files || file.value.files[0] == undefined) return;
  loading.value = true;
  try {
    const base64 = await convertBase64(file.value.files[0]);
    const res = await fetch("http://127.0.0.1:8000/upload_image", {
      method: "POST",
      body: JSON.stringify({ image64: base64, id: store.state.id }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();
    loading.value = false;
    if (res.status == 200) {
      status.value = "ok";
      activeBtn.value = true;
    } else {
      throw new Error(data.message);
    }
  } catch (error) {
    status.value = "error";
    errorMsg.value = error as string;
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
