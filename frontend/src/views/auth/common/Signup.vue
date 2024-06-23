<template>
  <form @submit.prevent="onSubmit" class="space-y-4">
    <Textinput
      label="Full name"
      type="text"
      placeholder="Full Name"
      name="name"
      v-model="name"
      :error="nameError"
      classInput="h-[48px]"
    />
    <Textinput
      label="Email"
      type="email"
      placeholder="Type your email"
      name="emil"
      v-model="email"
      :error="emailError"
      classInput="h-[48px]"
    />
    <Textinput
      label="Password"
      type="password"
      placeholder="8+ characters, 1 capital letter "
      name="password"
      v-model="password"
      :error="passwordError"
      hasicon
      classInput="h-[48px]"
    />
    <Textinput
      label="Confirm Password"
      type="password"
      placeholder="Confirm your password"
      name="confirmPassword"
      v-model="confirmPassword"
      :error="confirmPasswordError"
      hasicon
      classInput="h-[48px]"
    />

    <label class="cursor-pointer flex items-start">
      <input
        type="checkbox"
        class="hidden"
        @change="() => (checkbox = !checkbox)"
      />
      <span
        class="h-4 w-4 border rounded inline-flex mr-3 relative flex-none top-1 transition-all duration-150"
        :class="
          checkbox
            ? 'ring-2 ring-black-500 dark:ring-offset-slate-600 dark:ring-slate-900  dark:bg-slate-900 ring-offset-2 bg-slate-900'
            : 'bg-slate-100 dark:bg-slate-600 border-slate-100 dark:border-slate-600 '
        "
      >
        <img
          src="@/assets/images/icon/ck-white.svg"
          alt=""
          class="h-[10px] w-[10px] block m-auto"
          v-if="checkbox"
        />
      </span>
      <span class="text-slate-500 dark:text-slate-400 text-sm leading-6"
        >You accept our Terms and Conditions and Privacy Policy</span
      >
    </label>

    <button type="submit" class="btn btn-dark block w-full text-center">
      Create an account
    </button>
  </form>
</template>
<script>
import Textinput from "@/components/Textinput";
import { useField, useForm } from "vee-validate";
import * as yup from "yup";

import { inject } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import axios from "@/plugins/axios";
export default {
  components: {
    Textinput,
  },
  data() {
    return {
      checkbox: false,
    };
  },
  setup() {
    // Define a validation schema
    const schema = yup.object({
      name: yup.string().required("Name is required"),
      email: yup.string().required(" Email is required").email(),
      password: yup.string().required("Password is  required").min(8),
      confirmPassword: yup
        .string()
        .required("Please confirm your password")
        .oneOf([yup.ref("password")], "Passwords must match"),
      acceptTerms: yup.boolean().oneOf([true], "You must accept the terms"),
    });
    const swal = inject("$swal");
    const toast = useToast();
    const router = useRouter();

    // Create a form context with the validation schema

    const { handleSubmit } = useForm({
      validationSchema: schema,
    });
    // No need to define rules for fields

    const { value: name, errorMessage: nameError } = useField("name");
    const { value: email, errorMessage: emailError } = useField("email");
    const { value: password, errorMessage: passwordError } =
      useField("password");
    const { value: confirmPassword, errorMessage: confirmPasswordError } =
      useField("confirmPassword");
    const { value: acceptTerms } = useField("acceptTerms");

    const onSubmit = handleSubmit(async (values) => {
      const { name, email, password } = values;
      const formData = {
        username: name,
        email,
        password1: password,
        password2: password,
      };
      try {
        const response = await axios.post(
          "api/dj-rest-auth/registration/",
          formData
        );
        if (response.status === 201) {
          toast.success(
            "Account created successfully, confirmation email  has been sent",
            { timeout: 2000 }
          );
          await router.push("/login");
        }
      } catch (error) {
        // use sweetalert 2
        swal.fire({
          title: "Somthing went wrong!",
          text: "Please try another email",
          icon: "error",
          confirmButtonText: "Ok",
        });
      }
    });

    return {
      name,
      email,
      password,
      confirmPassword,
      acceptTerms,
      emailError,
      nameError,
      passwordError,
      confirmPasswordError,
      onSubmit,
    };
  },
};
</script>
<style lang="scss"></style>
