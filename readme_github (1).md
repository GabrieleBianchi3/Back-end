# 🗳️ Polling Application – REST API + Client

Questa applicazione è pensata per creare, votare e consultare sondaggi online. È costruita con Django e Django REST Framework, e include anche una pagina HTML molto semplice (senza template Django) che consente di interagire direttamente con le API usando `fetch()` e token JWT.

---

## Funzionalità principali

- Accesso tramite login JWT (token di accesso e refresh)
- Registrazione utente con inserimento automatico nel gruppo "standard"
- Solo chi ha effettuato il login può creare, modificare o cancellare i propri sondaggi
- Ogni utente può esprimere **un solo voto per sondaggio**
- I sondaggi **non possono essere modificati dopo che hanno ricevuto almeno un voto**
- Tutti, anche gli utenti non autenticati, possono vedere i sondaggi e i risultati
- L'interfaccia web (`index.html`) consente login, registrazione, voto e creazione sondaggi
- Gestione separata degli utenti e dei sondaggi in due app Django distinte
- Database SQLite già predisposto con alcuni dati di test

---

## Tipi di utenti previsti

| Tipo utente           | Cosa può fare                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Visitatore**        | Può vedere tutti i sondaggi e i risultati, ma **non può votare né creare sondaggi**                                  |
| **Utente registrato** | Può votare, creare sondaggi, modificarli (solo se è il creatore e non ci sono voti ancora)                           |
| **Admin Django**      | Ha accesso al pannello di amministrazione di Django. Non può registrarsi tramite il sito, ma solo tramite terminale. |

---

## Permessi

- L'accesso al voto e alla creazione è riservato agli utenti autenticati.
- Solo il creatore del sondaggio può modificarlo o eliminarlo.
- I sondaggi con almeno un voto non sono più modificabili.
- Tutti possono leggere i risultati.

---

## Tecnologie usate

- **Backend**: Python 3.11, Django 5.2, Django REST Framework
- **Autenticazione**: SimpleJWT
- **Frontend**: HTML + JavaScript + Bootstrap 5
- **Database**: SQLite (pronto all'uso con dati dimostrativi)

---

## Endpoint principali

| Metodo | Endpoint                   | Descrizione                                               |
| ------ | -------------------------- | --------------------------------------------------------- |
| POST   | `/api/token/`              | Login: restituisce i token                                |
| POST   | `/api/token/refresh/`      | Rinnovo del token di accesso                              |
| POST   | `/api/users/register/`     | Registra un nuovo utente                                  |
| GET    | `/api/users/me/`           | Restituisce i dati dell'utente attualmente autenticato    |
| GET    | `/api/polls/`              | Mostra la lista dei sondaggi disponibili                  |
| POST   | `/api/polls/`              | Crea un nuovo sondaggio (autenticazione necessaria)       |
| GET    | `/api/polls/<id>/`         | Dettaglio di un singolo sondaggio                         |
| PATCH  | `/api/polls/<id>/`         | Modifica sondaggio (solo se sei il creatore e senza voti) |
| DELETE | `/api/polls/<id>/`         | Elimina sondaggio (solo creatore)                         |
| POST   | `/api/polls/<id>/vote/`    | Vota un'opzione (una sola volta per sondaggio)            |
| GET    | `/api/polls/<id>/results/` | Visualizza i risultati                                    |

---

## Interfaccia utente (index.html)

La pagina HTML minimale consente:

- Login e logout
- Registrazione utente
- Creazione e modifica sondaggi (se permesso)
- Voto
- Visualizzazione dei risultati

L’interfaccia è semplice e funziona anche aprendo il file direttamente da browser, senza necessità di un server Django che serva template.

---

## Cosa trovi già nel progetto

- Un database SQLite già pronto con:
  - 2 utenti (incluso un admin Django)
  - Qualche sondaggio con opzioni
  - Voti già registrati

---

## Come avviare il progetto in locale

1. Clona il repository

   ```bash
   git clone <repo-url>
   cd Back-end-main
   ```

2. Crea e attiva un ambiente virtuale

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # oppure .venv\Scripts\activate su Windows
   ```

3. Installa le dipendenze

   ```bash
   pip install -r requirements.txt
   ```

4. Avvia il server Django

   ```bash
   python manage.py runserver
   ```

5. Apri il file `client/index.html` nel browser

---

## Deploy (esempio Railway)

1. Aggiungi le variabili d’ambiente da `.env.example`
2. Usa `Procfile` con Gunicorn
3. Esegui:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

---

## Struttura delle cartelle principali

```
Back-end-main/
│
├── client/                  # Frontend statico HTML/JS
│   └── index.html
│
├── polling_project/         # Configurazione Django
│   ├── settings.py, urls.py, wsgi.py, asgi.py
│
├── polls/                   # App per i sondaggi
│   ├── models.py, views.py, serializers.py, etc.
│
├── users/                   # App per la gestione utenti
│   ├── models.py, views.py, serializers.py, etc.
│
├── db.sqlite3               # Database precaricato
├── manage.py
├── Procfile
├── requirements.txt
└── README.md
```

---

## Licenza

Questo progetto è stato sviluppato a fini formativi ed è liberamente utilizzabile.\
Se lo riusi o lo modifichi, è buona norma citare l’autore.

---

## Autore



---

