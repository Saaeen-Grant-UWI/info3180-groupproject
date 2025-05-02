<template>
<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
  <div class="container-fluid">
    <router-link to="/" class="navbar-brand">Navbar</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link to="/users/1" class="nav-link">>My Profile</router-link>
          <a class="nav-link" aria-current="page" href="#">My Profile</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Reports</a>
        </li>
      </ul>
      <div class="d-flex" >
        <button type="button" class="btn btn-link" style="text-decoration: none;" >Log In</button>
        <button class="btn btn-warning" >Register</button>
      </div>
    </div>
  </div>
</nav>
</template>

<script>
export default {
   
}
</script>