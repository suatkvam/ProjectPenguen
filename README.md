# Frontend — Zemin360 (ProjectPenguen)

React (Vite) tabanlı frontend. UI, dashboard ve demo akışını içerir.

## Stack

- React
- Vite
- ESLint
- Docker

## Kurulum

### Docker ile çalıştırma (önerilen)

Proje kökünden:
```bash
docker compose up --build
```
http://localhost:3000 adresinde açılır.

### Lokal çalıştırma (Docker olmadan)

```bash
npm install
npm run dev
```

## Yapı

```
frontend/
├── public/
├── src/
├── index.html
├── vite.config.js
├── package.json
└── Dockerfile
```

## Sorumluluk Alanları

- Profil oluşturma ekranı (Kurum/Kişi)
- Bağlantı/node görselleştirme
- Dashboard (ilerleme durumu, kurum/birey görünümü)
- Popup/bildirim UI, milestone/flag ekranları, feedback ekranı
- Demo verisi + sunum akışı

## Not

Proje `create-react-app` yerine Vite ile kuruldu (CRA artık deprecated).