# 🗳️ Polling Application API

RESTful API per la creazione, partecipazione e gestione di sondaggi online.

---

## ✅ Funzionalità principali

- Autenticazione con **JWT** (accesso + refresh token)
- Registrazione nuovi utenti
- Creazione e gestione sondaggi
- Votazione protetta con autenticazione via token
- Statistiche in tempo reale sui voti
- Client HTML minimale incluso (`index.html`)
- Permessi differenziati per utenti anonimi e autenticati
- Utente personalizzato (`CustomUser`)
- Due app Django: autenticazione utenti e gestione sondaggi
- Due relazioni tra modelli
- Almeno una view class-based generica (`ListCreateAPIView`)
- Permessi differenziati per due gruppi di utenti

---

## 🧱 Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- SimpleJWT
- Bootstrap 5 (solo lato client)
- SQLite (pre-popolato)

---

## 🔗 Endpoint API Principali

> Il client HTML comunica con i seguenti endpoint REST tramite `fetch()` e token JWT:

| Metodo | Endpoint                     | Descrizione                          |
|--------|------------------------------|--------------------------------------|
| POST   | `/api/token/`                | Login e generazione token JWT        |
| POST   | `/api/register/`             | Registrazione nuovo utente           |
| GET    | `/api/polls/`                | Elenco dei sondaggi                  |
| GET    | `/api/polls/<id>/`           | Dettagli e opzioni del sondaggio     |
| POST   | `/api/polls/<id>/vote/`      | Invia voto (autenticazione richiesta)|
| GET    | `/api/polls/<id>/results/`   | Visualizzazione risultati del sondaggio |

---

## 🖥️ Client REST minimale

✔️ Il file `index.html` implementa un **client HTML standalone** che interagisce con le API tramite `fetch()`:
- login JWT e logout
- registrazione utente
- caricamento dei sondaggi
- selezione e invio del voto con autenticazione
- visualizzazione dei risultati

✔️ Nessun template Django viene utilizzato nella logica client. Le richieste avvengono solo via REST API.

✔️ Le chiamate protette includono l’header `Authorization: Bearer <token>`.

---

## 📦 Database precaricato

Il progetto include un file `db.sqlite3` con dati dimostrativi:
- 2 utenti di test (es. admin e utente base)
- sondaggi e opzioni
- voti già registrati

---

## 🚀 Installazione locale

1. **Clona il progetto**
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

2. **Crea e attiva un ambiente virtuale**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate   # Windows
   ```

3. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia il server di sviluppo**
   ```bash
   python manage.py runserver
   ```

5. **Apri il client HTML**
   - Apri il file `index.html` con un browser
   - Accedi con un utente valido o registrane uno nuovo

---

## 🌍 Deploy online (in fase di preparazione)

🔧 Il progetto sarà distribuito tramite [Railway](https://railway.app).  
🔗 Il link sarà pubblicato qui appena disponibile.

---

## 📄 Licenza

Questo progetto è rilasciato per scopi formativi e dimostrativi.