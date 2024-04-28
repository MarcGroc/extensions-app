<template>
    <div class="error404">
        <div class="page-404-content">
            <div class="container">
                <div class="row full-height">
                    <div class="col-md-12 text-center">
                        <div class="error-image section-space--mb_50">
                            <img class="img-fluid" src="../../assets/img/other/page-404-image.png" alt="Image Not Found">
                        </div>
                        <h1 class="error-404-title font-weight--light text-white">{{ text["404_text"] }}</h1>
                        <div class="error-buttons section-space--mt_50">
                            <router-link class="ht-btn ht-btn-md" to="/">
                                 <span class="button-icon mr-2">
                                    <i class="fa fa-home"></i>
                                </span>
                                <span class="button-text">{{ text["404_back"] }}</span>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import textData from '../../assets/text.json';
    export default {
        name: 'NotFound',
        data () {
            return {
                text: textData.header
            }
        }
    }
</script>
