<template>
  <div class="w-screen h-screen relative flex justify-center items-center">
    <div class="w-[900px] rounded-xl shadow-xl h-[600px] grid grid-cols-5">
      <div class="h-[500px] bg-base-300 my-auto col-span-3 ml-4">
        <img
          :src="imgFilterSrc"
          alt="ddd"
          class="w-full h-full object-contain"
        />
      </div>
      <div class="px-4 pb-8 grid grid-rows-2 col-span-2">
        <div class="flex flex-col items-center">
          <input
            type="text"
            placeholder="Image title"
            className=" text-3xl rounded-xl px-2 mt-10 "
            maxlength="15"
            v-model="imageTitle"
            @input="handleTitleInputChange()"
          />
          <div class="flex justify-center items-center py-4 mt-3">
            <input
              type="text"
              placeholder="Add tag"
              :className="`input
        input-bordered input-sm ${
          tagInputError ? 'animate-pulse input-error ' : 'input-neutral'
        }`"
              maxlength="10"
              v-model="tagName"
              @input="handleTagInputChange()"
            />
            <button class="btn btn-square btn-sm ml-2" @click="handleTagAdd()">
              Add
            </button>
          </div>
          <div
            class="flex flex-wrap gap-2 rounded-xl bg-base-200 w-56 h-32 p-2 border-2 border-base-300 overflow-scroll"
          >
            <div
              className="badge badge-primary hover:badge-error hover:badge-outline badge-outline cursor-pointer"
              v-for="tag in tags"
              :key="tag"
              @click="handleDeleteTag(tag)"
            >
              <span class="text-info mr-1">#</span> {{ tag }}
            </div>
          </div>
        </div>
        <div class="flex flex-col items-center">
          <div class="p-3 mt-4 mx-auto">
            <p class="text-xl text-center pb-1">Filtr</p>
            <div class="flex flex-col">
              <div class="flex flex-col items-center gap-2 mt-2">
                <p>Pixel size ({{ pixelsAmount }})</p>
                <input
                  type="range"
                  min="3"
                  max="30"
                  step="1"
                  class="range range-sm"
                  v-model="pixelsAmount"
                  @input="handleSetFilter('pixel_art')"
                />
              </div>
            </div>
          </div>
          <button class="btn btn-success" @click="handleSubmitEdit">
            Wyślij!
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, defineProps } from "vue";
import { useStore } from "vuex";
import { key } from "../../store";
import { onMounted } from "vue";
const tagName = ref<string>("");
const imageTitle = ref<string>("");
const tagInputError = ref<boolean>(false);
const tags = ref<string[]>([]);
const pixelsAmount = ref<number>(3);
const store = useStore(key);
const imgFilterSrc = ref<string>("");
const submitError = ref<string | null>(null);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/download_image", {
    method: "POST",
    body: JSON.stringify({
      image: store.state.id,
    }),
    headers: { "Content-Type": "application/json" },
  });
  const data = await res.json();
  if (res.status == 200) {
    const imageBase64 = "data:image/png;base64," + data.imageData;
    imgFilterSrc.value = imageBase64;
  }
});
const handleSetFilter = async (filterName: string) => {
  try {
    const res = await fetch("http://127.0.0.1:8000/convert", {
      method: "POST",
      body: JSON.stringify({
        name: store.state.id,
        pixels: pixelsAmount.value,
      }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await res.json();

    if (res.status == 200) {
      const imageBase64 = "data:image/png;base64," + data.imageData;
      imgFilterSrc.value = imageBase64;
      // const res = await fetch("http://127.0.0.1:8000/download_image", {
      //   method: "POST",
      //   body: JSON.stringify({
      //     image: store.state.id,
      //   }),
      //   headers: { "Content-Type": "application/json" },
      // });
      // const data = await res.json();
    }
  } catch (error) {
    console.log(error);
  }
};

const handleTagAdd = () => {
  tagInputError.value = false;

  const tagNameValue = tagName.value;
  if (
    tags.value.includes(tagNameValue) ||
    tags.value.length == 10 ||
    tagName.value === ""
  ) {
    tagInputError.value = true;
    setTimeout(() => (tagInputError.value = false), 2000);
    return;
  }

  tags.value.push(tagNameValue);
  tagName.value = "";
};

const handleDeleteTag = (tagToDelete: string) => {
  const index = tags.value.indexOf(tagToDelete);
  tags.value.splice(index, 1);
};

const handleTagInputChange = () => {
  const format = /[ `!@#$%^&*()+\-=[\]{};':"\\|,.<>/?~]/;
  if (format.test(tagName.value)) {
    const chars = tagName.value.split("");
    chars.pop();
    tagName.value = chars.join("");
  }
};
const handleTitleInputChange = () => {
  if (imageTitle.value.trim() !== "") {
    props.setError(null);
  }
};
const handleSubmitEdit = async () => {
  if (imageTitle.value === "") {
    submitError.value = "Musisz podać tytuł";
    props.setError(submitError.value);
    return;
  }
};
const props = defineProps<{
  // handleNextStep: (nextStep: string) => void;
  setError: (msg: string | null) => void;
}>();
</script>
