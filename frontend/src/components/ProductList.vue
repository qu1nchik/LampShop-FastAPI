<template>
  <!-- while loading -->
  <div v-if="products.length === 0">
    Загрузка...
  </div>
  <!-- when received -->
  <div class="products-grid" v-else>
    <div v-for="p in products" :key="p.id" class="product-card">
      <img :src="'https://placehold.co/300x200'"class="product-image">
      <div class="product-info">
        <div class="product-title">{{ p.name }}</div>
        <div class="product-price">{{ p.price }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import {ref, onMounted}from 'vue'

  const products = ref([])

  onMounted(async () => {
    try {
      const responce = await fetch('/api/products')
      if (!responce.ok) throw new Error('Ошибка Загрузки')
      products.value = await responce.json()
    }
    catch (err) {
      console.error(err)
      products.value = []
    }
  })
</script>
