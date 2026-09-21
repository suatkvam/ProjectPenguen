# Backend — Zemin360 (ProjectPenguen)

FastAPI tabanlı backend. Veri modeli, güvenilirlik skor motoru ve API/iş mantığını içerir.

## Stack

- Python 3.12
- FastAPI + Uvicorn
- SQLAlchemy + Postgres
- Docker

## Kurulum

```bash
cp .env.example .env
```

`.env` içinde `DATABASE_URL` değerini kendi ortamına göre ayarla (varsayılan
`docker-compose.yml` ile uyumludur).

### Docker ile çalıştırma (önerilen)

Proje kökünden:
```bash
docker compose up --build
```

### Lokal çalıştırma (Docker olmadan)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Yapı

```
backend/
├── app/
│   └── main.py     # FastAPI giriş noktası
├── requirements.txt
├── Dockerfile
└── .env.example
```

## Sorumluluk Alanları

- Node, bağlantı, event stream veri modeli
- Güvenilirlik puanı hesaplama (+/- puan, başlangıç puanı, referans bonusu, karşılıklı feedback)
- Bağlantı kurma akışı, milestone + flag sistemi (CRUD, günlük log)
- Bildirim/popup sistemi (24 saat pencere — milestone/flag hatırlatmaları)
- İş bitişi onay akışı + feedback kaydı

## Health Check

```
GET /health → {"status": "ok"}
```