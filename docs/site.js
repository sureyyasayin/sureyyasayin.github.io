// Süreyya Sayın — kişisel site. Dış kaynak yok, çerez yok.
(function () {
  "use strict";

  // WhatsApp numarası: boş bırakılırsa düğme gizli kalır.
  // Örnek biçim (ülke kodu, başında + ve 0 olmadan): "905xxxxxxxxx"
  var WHATSAPP_NO = "";

  // E-posta, spam botları HTML'de bulamasın diye parçalardan birleştirilir.
  var eposta = ["sureyya", "sayin"].join(".") + String.fromCharCode(64) + ["gmail", "com"].join(".");

  document.querySelectorAll(".js-eposta").forEach(function (a) {
    a.href = "mailto:" + eposta;
  });
  document.querySelectorAll(".js-eposta-metin").forEach(function (el) {
    var a = document.createElement("a");
    a.href = "mailto:" + eposta;
    a.textContent = eposta;
    el.replaceChildren(a);
  });

  if (WHATSAPP_NO) {
    document.querySelectorAll(".js-whatsapp").forEach(function (a) {
      a.href = "https://wa.me/" + WHATSAPP_NO;
      a.target = "_blank";
      a.rel = "noopener";
      a.hidden = false;
    });
  }

  // Tema: sistem tercihi varsayılan; düğmeyle seçilen bu cihazda hatırlanır.
  var kok = document.documentElement;
  function kayitliTema() {
    try { return localStorage.getItem("tema"); } catch (e) { return null; }
  }
  var t = kayitliTema();
  if (t === "dark" || t === "light") kok.dataset.theme = t;

  var temaDugme = document.querySelector(".tema-dugme");
  if (temaDugme) {
    temaDugme.addEventListener("click", function () {
      var simdiKoyu = kok.dataset.theme
        ? kok.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      var yeni = simdiKoyu ? "light" : "dark";
      kok.dataset.theme = yeni;
      try { localStorage.setItem("tema", yeni); } catch (e) { /* özel pencere */ }
    });
  }

  // Mobil menü
  var menuDugme = document.querySelector(".menu-dugme");
  var menu = document.getElementById("menu");
  if (menuDugme && menu) {
    function kapat() {
      menu.classList.remove("acik");
      menuDugme.setAttribute("aria-expanded", "false");
    }
    menuDugme.addEventListener("click", function () {
      var acik = menu.classList.toggle("acik");
      menuDugme.setAttribute("aria-expanded", String(acik));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) kapat();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") kapat();
    });
  }
})();
