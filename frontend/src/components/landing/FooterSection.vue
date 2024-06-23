<template>
  <div class="footer-area-wrapper">
    <div class="footer-copyright-area ebook-footer section-space--pb_120">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="ebook-social-group__list mb-20 text-center">
              <ul class="list ht-social-networks large-icon">
                <li class="item">
                  <a :href="brand.facebook" target="_blank" class="social-link">
                    <i class="fab fa-facebook social-link-icon"></i
                  ></a>
                </li>
                <li class="item">
                  <a :href="brand.twitter" target="_blank" class="social-link">
                    <i class="fab fa-twitter social-link-icon"></i
                  ></a>
                </li>
                <li class="item">
                  <a
                    :href="brand.instagram"
                    target="_blank"
                    class="social-link"
                  >
                    <i class="fab fa-instagram social-link-icon"></i
                  ></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="row aling-items-center">
          <div class="col-md-12">
            <div class="horizontal-list text-center">
              <ul>
                <li>
                  <span class="copyright-text">
                    &copy; {{ currentYear }} <b>{{ brand.projectName }}</b>
                  </span>
                </li>
                <li>
                  <a
                    href="/privacy"
                    class="hover-style-link hover-style-link--sub-color"
                    >{{ text.privacy }}</a
                  >
                </li>
                <li>
                  <a
                    href="/terms"
                    class="hover-style-link hover-style-link--sub-color"
                    >{{ text.terms }}</a
                  >
                </li>
                <li>
                  <a
                    href="/contact"
                    class="hover-style-link hover-style-link--sub-color"
                    >{{ text.contact }}</a
                  >
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import textData from "../../assets/text_landing_pl.json";
import brand from "@/assets/brand/brand.js";

const currentYear = new Date().getFullYear();

export default {
  name: "FooterBottom",
  data() {
    return {
      text: textData.footer,
      brand,
      currentYear,
    };
  },
};
</script>
