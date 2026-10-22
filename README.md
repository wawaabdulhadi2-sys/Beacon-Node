# 🚏 Smart Bus Stop Kiosk — Rapid Penang @ USM

> **Submission for Sime Darby Property University Hackathon 2026: Township of Tomorrow**

An interactive proof-of-concept digital kiosk prototype designed for modern smart townships, featuring real-time Rapid Penang bus tracking, live seat availability metrics, and dynamic route ETAs along real road networks in Penang.

---

## 📌 Project Overview

Urban public transit often suffers from unpredictable arrival times and a lack of real-time crowd transparency at bus stops. The **Smart Bus Stop Kiosk** provides transit commuters with live telemetry, real-time GPS tracking along real road networks, and transparent seat occupancy indicators—promoting public transit usage in next-generation smart townships.

### Key Features
* 🗺️ **Live Map & Real Road Routing:** Displays real driving routes powered by OSRM and Leaflet.js mapping along Jalan Sultan Azlan Shah towards the USM Main Gate.
* ⏱️ **Dynamic Arrival ETAs:** Calculates real-time arrival counts and distances as the bus approaches the stop.
* 🪑 **Seat Occupancy Telemetry:** Tracks actual seating metrics based on standard Rapid Penang single-deck bus capacity (35 seats).
* 📱 **Smart Township Kiosk UI:** Designed with a dark-mode, high-contrast dashboard for public display terminals.

---

## 🛠️ Tech Stack & Dependencies

* **Frontend:** HTML5, CSS3, JavaScript (ES6)
* **Mapping Engine:** [Leaflet.js](https://leafletjs.com/)
* **Map Tiles:** [OpenStreetMap France](https://openstreetmap.fr/)
* **Routing API:** [OSRM (Open Source Routing Machine API)](http://project-osrm.org/)

---

## 🚀 How to Run Locally

No complex build setups or package installations are required.

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)
   cd YOUR-REPOSITORY-NAME
