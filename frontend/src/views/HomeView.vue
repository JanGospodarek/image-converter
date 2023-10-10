<template>
  <div class="w-screen h-screen flex items-center">
    <div class="my-24 flex items-center rounded-xl shadow-xl w-full mx-6">
      <div class="flex flex-col p-8">
        <p class="text-7xl font-extrabold tracking-wide p-4 text-center">
          Stwórz swoje <br />
          <span>arcydzieło</span>
        </p>
        <button
          class="btn btn-outline btn-primary mx-auto"
          @click="router.push({ name: 'edit' })"
        >
          Zaczynamy!
        </button>
      </div>

      <div></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();
</script>
