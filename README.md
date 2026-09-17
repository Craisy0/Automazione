# AUTOSOSTENTAMENTO — azienda a sotto-reparti

Progetto per costruire un flusso di entrate ricorrenti, gestito come una piccola azienda: un manager (Claude) coordina più reparti (sotto-agenti), ognuno responsabile di un canale di guadagno diverso, a costo zero finché non ci sono segnali reali.

## Struttura

- `company/ORG.md` — organigramma, ruoli, KPI, regole di premio/penalità, gestione budget
- `company/scoreboard.csv` — punteggio/attività giornaliera per reparto
- `company/daily-reports/YYYY-MM-DD.md` — report giornaliero
- `company/DAILY_MANAGER_ROUTINE.md` — cosa fa il manager ogni giorno
- `company/accounts-todo-consolidato.md` — tutti gli account da creare, in ordine di urgenza
- `departments/content-affiliazione/` — blog SoloStack (tool AI/automazione per freelance), affiliazioni + ads
- `departments/prodotti-digitali/` — template/guide/checklist venduti su Gumroad
- `departments/print-on-demand/` — planner/design venduti su Amazon KDP/Redbubble

## Stato attuale

Vedi l'ultimo file in `company/daily-reports/`.

## Deploy del sito (reparto content-affiliazione)

Il sito statico viene generato in `docs/` alla radice del repo, così GitHub Pages può servirlo direttamente:
Settings del repo → Pages → Source: branch principale, cartella `/docs`.
