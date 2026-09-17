---
title: Come pubblicare il sito su GitHub (upload manuale)
updated: 2026-09-17
---

# Quando sei al computer, in 5 minuti

1. Scarica ed estrai lo zip del progetto che Claude ti ha mandato in chat (`automazione-progetto.zip`).
2. Vai su **github.com/Craisy0/Automazione**
3. Clicca **Add file** (in alto a destra, sopra la lista file) → **Upload files**
4. Trascina dentro la pagina TUTTI i file e le cartelle estratte dallo zip (mantieni la struttura: `docs/`, `company/`, `departments/`, `README.md`, ecc. — trascinando l'intera cartella estratta funziona su Chrome/Edge desktop)
5. In fondo alla pagina scrivi un messaggio di commit tipo "Primo caricamento" e clicca **Commit changes**
6. Vai su **Settings** (del repository) → **Pages** (menu a sinistra) → in "Source" scegli branch **main**, cartella **/docs** → **Save**
7. Dopo 1-2 minuti il sito sarà live su: **https://craisy0.github.io/Automazione/**

## Dopo il primo caricamento

Mandami un messaggio quando è online: aggiorno l'URL reale nel sito (per la sitemap SEO) e ti preparo i prossimi aggiornamenti da caricare, finché non troviamo un modo per farlo automaticamente (es. collegando un computer a questa chat, vedi `company/ORG.md`).

## Se qualcosa va storto

Se GitHub segnala conflitti o file duplicati, è probabile che tu abbia inizializzato il repository con un README durante la creazione — in quel caso cancella quel file dal repo prima di ricaricare tutto, oppure dimmelo e ti aiuto a risolvere.
