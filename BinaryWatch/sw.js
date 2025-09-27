// Service Worker minimal — obligatoire pour que la PWA soit installable
self.addEventListener("install", event => {
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil(clients.claim());
});

// Ne fait que laisser passer toutes les requêtes
self.addEventListener("fetch", () => {});
