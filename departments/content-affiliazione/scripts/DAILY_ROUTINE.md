# Routine giornaliera (eseguita dallo scheduled task)

Questa è la checklist che l'agente segue ad ogni esecuzione giornaliera.

1. **Sincronizza il progetto**
   - Se `~/income-project` esiste già in questo ambiente: `cd ~/income-project && git pull`.
   - Altrimenti: `git clone <REPO_URL> ~/income-project && cd ~/income-project`.

2. **Scegli il prossimo articolo**
   - Apri `data/content-calendar.csv`.
   - Prendi la prima riga con `status=planned` (ordine di `priority`).

3. **Scrivi l'articolo**
   - Crea un file in `content/articles/<slug>.md` seguendo lo stesso formato/tono degli articoli esistenti (front matter con title/date/type/slug/description, poi corpo in markdown, uso di `{{affiliate:slug}}` per i link, disclosure finale).
   - Lunghezza indicativa: 500-900 parole, contenuto pratico e onesto (non riempitivo).
   - Se il topic richiede dati aggiornati (prezzi, funzionalità di un tool), fai una ricerca web veloce prima di scrivere per evitare affermazioni sbagliate.

4. **Aggiorna il calendario**
   - Cambia `status` della riga da `planned` a `published` in `data/content-calendar.csv`.

5. **Ricostruisci il sito**
   - `python3 scripts/build_site.py`

6. **Aggiorna il log giornaliero**
   - Aggiungi una nuova sezione in `logs/daily-log.md` (in cima, ordine cronologico inverso) con: data, articolo pubblicato, parole scritte, totale articoli cumulativo, eventuali blocchi/decisioni prese, prossimi passi.

7. **Commit e push**
   - `git add -A && git commit -m "Articolo: <titolo>" && git push`
   - Se il push fallisce per credenziali mancanti, annotalo chiaramente nel log e fermati: non inventare risultati.

8. **Controlli periodici (non tutti i giorni)**
   - Una volta alla settimana: controlla se ci sono almeno 10 articoli pubblicati → se sì, ricorda nel log che è il momento di fare domanda per Google AdSense e per i programmi di affiliazione (vedi `data/affiliate-programs.md`).
   - Se Search Console è collegata: controlla impressioni/click e riportali nel log.
   - Se in `data/affiliate-links.json` sono stati aggiunti link reali che prima erano placeholder: verifica che compaiano correttamente nel sito costruito.

## Regole importanti

- Non riportare mai numeri di guadagno finti. Finché non ci sono account affiliati/AdSense attivi, il log deve dire esplicitamente "nessun guadagno reale ancora, siamo in fase di costruzione contenuti".
- Non pubblicare un articolo se non sei ragionevolmente sicuro che le informazioni sui tool siano corrette (prezzi, funzionalità): meglio verificare con una ricerca veloce.
- Se il calendario editoriale (`content-calendar.csv`) si esaurisce (tutte le righe `published`), aggiungi 10 nuove righe `planned` con nuovi topic coerenti con la nicchia, prima di fermarti.
