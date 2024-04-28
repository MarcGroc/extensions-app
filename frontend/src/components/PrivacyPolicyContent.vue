<template>
	<section class="section-space--ptb_90">
		<div class="container">
			<div class="mb-4">
				<h5 class="mb-2">1.</h5>
				<p>{{text.intro}}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">2.</h5>
				<p>{{text.dataCollection}}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">3.</h5>
				<p>{{text.legalBasis}}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">4.</h5>
				<p>{{text.dataRecipients}}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">5.</h5>
				<p>{{text.dataRetention}}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">6.</h5>
				<p>{{text.userRights }}</p>
			</div>
			<div class="mb-4">
				<h5 class="mb-2">7.</h5>
				<p>{{text.consentWithdrawal}}</p>
			</div>
			<div class="">
				<h5 class="mb-2">8.</h5>
				<p>{{text.complaints}}</p>
			</div><div class="">
				<h5 class="mb-2">9.</h5>
				<p>{{text.notice}}</p>
			</div>
		</div>
	</section>
</template>

<script>
    import textData from '../assets/text.json'
    export default {
        name: 'PrivacyPolicyContent',
      data() {
        return {
          text:textData.privacy
        }
      }
    }
</script>
