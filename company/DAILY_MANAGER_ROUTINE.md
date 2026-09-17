---
title: Routine giornaliera del Manager
updated: 2026-09-16
---

# Cosa fa il Manager ogni giorno (eseguito dallo scheduled task)

1. **Sincronizza l'azienda**
   - `cd ~/income-project && git pull` (o `git clone <REPO_URL> ~/income-project` se non esiste ancora in questo ambiente).

2. **Assegna il compito del giorno a ciascun reparto attivo**, usando il tool Agent per lanciare un sotto-agente per reparto, in parallelo, con un prompt che include:
   - Il proprio charter (estratto da `company/ORG.md`)
   - Lo stato attuale del proprio backlog/calendario
   - L'istruzione precisa dell'unità di lavoro di oggi (es. "scrivi il prossimo articolo pianificato", "abbozza il prossimo prodotto pianificato")
   - La richiesta di riportare: cosa ha fatto, eventuali blocchi, eventuali segnali reali osservati (mai inventati)

   Reparti attivi e relativa unità di lavoro giornaliera:
   - **content-affiliazione**: segue `departments/content-affiliazione/scripts/DAILY_ROUTINE.md` (1 articolo/giorno)
   - **prodotti-digitali**: 1 prodotto abbozzato/rifinito da `departments/prodotti-digitali/backlog.csv` ogni 2-3 giorni (non serve un prodotto nuovo ogni giorno)
   - **print-on-demand**: 1 idea abbozzata/rifinita da `departments/print-on-demand/backlog.csv` ogni 3-4 giorni

3. **Raccoglie i risultati** di ogni sotto-agente e li verifica (i file sono davvero stati creati/aggiornati? i claim sono coerenti con quanto trovato nei file?).

4. **Aggiorna `company/scoreboard.csv`** con una riga per reparto per la giornata (o l'ultima attività, per i reparti non attivi oggi).

5. **Una volta alla settimana** (ogni 7 esecuzioni), scrive in più un breve confronto tra reparti in `company/daily-reports/` basato sui segnali reali raccolti fino a quel momento, e decide se riallocare priorità (vedi regole in `company/ORG.md`).

6. **Scrive il report del giorno** in `company/daily-reports/YYYY-MM-DD.md`: cosa ha fatto ogni reparto, stato account/segnali reali, prossimi passi, eventuale proposta di spesa dal budget (solo se giustificata da un segnale reale).

7. **Commit e push**: `git add -A && git commit -m "Giornata <data>: <riassunto breve>" && git push`.

8. **Notifica l'utente**: il report va comunicato in chat (riassunto breve) oltre che salvato su file — se questa sessione programmata non ha accesso diretto alla conversazione originale, il riepilogo resta comunque disponibile nel file di report e nel prossimo aggiornamento della sessione principale.

## Regole ferree

- Mai inventare metriche di traffico, vendite o guadagni. Se non ci sono dati reali, scriverlo esplicitamente.
- Mai proporre di spendere il budget senza un segnale reale concreto a supporto.
- Se un reparto non ha nulla di sensato da fare oggi (es. calendario esaurito), il sotto-agente aggiunge nuovi elementi al proprio backlog invece di restare fermo.
