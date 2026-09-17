# SoloStack — progetto di reddito ricorrente

Blog di recensioni/comparazioni/tutorial su strumenti AI e automazione per freelance, consulenti solo e piccoli team. Monetizzazione tramite affiliazioni software (commissioni ricorrenti 20-60%) e, in seguito, Google AdSense.

## Struttura

- `content/articles/*.md` — articoli sorgente in Markdown (front matter + corpo)
- `content/about.md` — pagina "about"
- `docs/` — sito statico generato (HTML), **cartella pubblicata su GitHub Pages**
- `scripts/build_site.py` — genera `docs/` a partire da `content/`
- `scripts/templates/` — template HTML/CSS
- `scripts/DAILY_ROUTINE.md` — checklist seguita ogni giorno dall'agente automatico
- `data/niche-brief.md` — perché questa nicchia, target, angolo editoriale
- `data/content-calendar.csv` — backlog di 30 articoli pianificati (stato: planned/published)
- `data/affiliate-programs.md` — programmi di affiliazione target e commissioni
- `data/affiliate-links.json` — (da creare) link affiliati reali una volta ottenuti, es. `{"notion": "https://..."}`
- `data/accounts-todo.md` — cosa deve creare l'utente
- `logs/daily-log.md` — log giornaliero di cosa è stato fatto, in ordine cronologico inverso

## Come rigenerare il sito

```
python3 scripts/build_site.py
```

## Deploy su GitHub Pages

1. Crea un repository GitHub (vuoto) e fai push di questo progetto.
2. Nelle impostazioni del repo → Pages → Source: branch `main` (o `master`), cartella `/docs`.
3. Il sito sarà live su `https://<username>.github.io/<repo>` in pochi minuti.
4. Aggiorna `SITE_URL` in `scripts/build_site.py` con l'URL reale e rilancia il build (serve per sitemap.xml corretto).

## Stato attuale

Vedi `logs/daily-log.md` per l'ultimo aggiornamento.
