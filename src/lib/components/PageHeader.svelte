<script lang="ts">
  let { title, description }: { title: string; description: string } = $props();
</script>

<div class="page-header">
  <h1>{title}</h1>
  <p>{description}</p>
</div>
