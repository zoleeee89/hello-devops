# Hello DevOps – Python + Flask

Egyszerű "Hello World" típusú webalkalmazás Flaskkel, DevOps beadandóhoz.

Az alkalmazás HTTP-n elérhető, és egy egyszerű szöveget ad vissza a `http://localhost:8080` címen.

## Követelmények

- Python 3.10+ (ajánlott 3.12)
- pip
- (opcionális) Docker
- Git

## Projekt felépítése

- `app.py` – Flask alkalmazás
- `requirements.txt` – Python függőségek
- `Dockerfile` – Docker image buildhez
- `.github/workflows/ci.yml` – GitHub Actions CI pipeline

---

## Build és futtatás (lokálisan)

1. Virtuális környezet létrehozása (opcionális, de ajánlott):

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate

Ez a sor a feature/update-message branch-en lett hozzáadva.