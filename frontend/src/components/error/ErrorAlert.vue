<template>
  <div
    v-if="errorMsg != null"
    className="alert alert-error absolute right-0 left-0 bottom-16 ml-auto mr-auto h-16  w-1/2"
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
    <span>{{ props.errorMsg }}</span>
  </div>
</template>

<script lang="ts" setup>
import { ref, defineProps, onMounted, watchEffect } from "vue";
import { ErrorProps } from "./ErrorPropsTypes";
const errorMsg = ref<string | null>(null);
watchEffect(() => {
  if (props.errorMsg) {
    errorMsg.value = props.errorMsg;
  }
});

const props = defineProps<ErrorProps>();
</script>
./ErrorPropsTypes
