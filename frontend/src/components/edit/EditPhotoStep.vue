<template>
  <div class="w-[900px] rounded-xl shadow-xl h-[600px] grid grid-cols-5">
    <div class="h-[500px] bg-base-300 my-auto col-span-3 ml-4"></div>
    <div class="px-4 pb-8 grid grid-rows-2 col-span-2">
      <div class="flex flex-col items-center">
        <input
          type="text"
          placeholder="Image title"
          className=" text-3xl rounded-xl px-2 mt-10 "
          maxlength="15"
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
        <div class="rounded-xl border-2 p-3 mt-4 mx-auto">
          <p class="text-xl text-center pb-1">Filtr</p>
          <div class="flex justify-around gap-4">
            <button class="btn btn-sm btn-outline btn-primary">ascii</button>
            <button class="btn btn-sm btn-outline btn-primary">emoji</button>
          </div>
        </div>
        <button class="btn btn-success mt-10">Wyślij!</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
const tagName = ref<string>("");
const tagInputError = ref<boolean>(false);
const tags = ref<string[]>([]);

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
</script>
