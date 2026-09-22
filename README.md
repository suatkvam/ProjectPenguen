# ProjectPenguen — Zemin360 Hackathon (GİRVAK)

Kurum-kişi/girişim iş birliklerinde ilerleyişin şeffaf takip edilememesi problemine
(Zemin360 Hackathon problemi #6) odaklanan bir platform.

## Proje Özeti

Taraflar bir proje/iş birliği başlattıktan sonra (her iki tarafın da "projeye başla"
butonuna basmasıyla) süreç günlük feedback/flag akışıyla kaydediliyor ve milestone'lar
bu akışa göre tamamlanıyor. İş bittiğinde taraflar birbirini değerlendiriyor ve bu
feedback'ler herkes tarafından görülebiliyor.

## Yapı

```
.
├── backend/    # FastAPI — veri modeli, skor motoru, API
├── frontend/   # React (Vite) — UI
└── docker-compose.yml
```

## Kurulum

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

- Backend: http://localhost:8000 (health check: `/health`)
- Frontend: http://localhost:3000
- Postgres: localhost:5432

## Ekip / Rol Dağılımı

| Kişi | Alan |
|---|---|
|Arif Suat Kıvam| Backend / Veri Modeli & Skor Motoru |
| Uğur | Backend / API & İş Mantığı |
| Alexandra | Frontend / UI & Demo |

## Branch'ler

- `master` — tam proje (backend + frontend)
- `backend` — sadece backend
- `frontend` — sadece frontend
