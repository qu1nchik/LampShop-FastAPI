<template>
  <div>
    <header class="header">
      <div class="container">
          <nav class="header__nav">
              <a href="#" class="header__link" data-route="/">LampShop</a>
              <a href="#" class="header__link" data-route="/cart">Корзина</a>
              <a href="#" class="header__link" data-route="/popular">Популярное</a>
          </nav>
      </div>
    </header>

    <main class="main">
      <div class="container" id="app-container">
        <ProductList />
      </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>© LampShop, 2025</p>
        </div>
    </footer>
  </div>
</template>

<script setup>
  import ProductList from "./components/ProductList.vue"
</script>

<style>
  @import '../static/reset.css';
  @import '../static/fonts.css';
  @import '../static/style.css';
</style>
