let waypoints = [];
let directionsService, directionsRenderer;

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: { lat: -23.5505, lng: -46.6333 },
  });

  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer({ map });

  map.addListener("click", (e) => {
    waypoints.push({ location: e.latLng, stopover: true });
    calcularRota();
  });
}

function calcularRota() {
  if (waypoints.length < 2) return;

  directionsService.route({
    origin: waypoints[0].location,
    destination: waypoints[waypoints.length - 1].location,
    waypoints: waypoints.slice(1, -1),
    travelMode: google.maps.TravelMode.DRIVING,
  }, (result, status) => {
    if (status === "OK") directionsRenderer.setDirections(result);
  });
}

document.getElementById("enviar-rota")?.addEventListener("click", () => {
  const rota = waypoints.map(p => ({
    lat: p.location.lat(),
    lng: p.location.lng()
  }));

  fetch("/enviar_rota", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(rota)
  }).then(() => alert("Rota enviada para o capacete!"));
});