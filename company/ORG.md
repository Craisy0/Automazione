---
title: Organigramma — Azienda AUTOSOSTENTAMENTO
updated: 2026-09-16
---

# Struttura

**Manager (Claude, in questa sessione e nelle esecuzioni programmate giornaliere)**
- Assegna il compito del giorno a ciascun reparto
- Raccoglie i risultati, li verifica (niente numeri finti)
- Aggiorna la scoreboard
- Decide premi/penalità settimanali (più o meno "spazio" al reparto, non denaro reale)
- Scrive il report giornaliero per l'utente
- Propone quando/come usare il budget di 50€ (tenuto in riserva, si spende solo su indicazione esplicita dell'utente)

**Reparti (sotto-agenti), ognuno con una cartella in `departments/`:**

## 1. Content & Affiliazione — `departments/content-affiliazione/`
- **Cosa fa**: blog SoloStack (tool AI/automazione per freelance), 1 articolo/giorno da calendario, monetizzato con affiliazioni software + AdSense futuro.
- **Costo**: zero (hosting gratuito GitHub Pages).
- **Orizzonte realistico**: primi segnali (traffico Search Console) in 4-8 settimane; prime commissioni affiliate solo dopo approvazione ai programmi, plausibile in 2-4 mesi.
- **KPI**: articoli pubblicati, parole scritte, (quando disponibili) impressioni/click da Search Console, click sui link affiliati.

## 2. Prodotti Digitali — `departments/prodotti-digitali/`
- **Cosa fa**: template, guide e checklist scaricabili nella stessa nicchia (produttività/AI per freelance), vendute su Gumroad. Riusa e "impacchetta" contenuti/competenze già sviluppate per il blog.
- **Costo**: zero (Gumroad non ha costi fissi, trattiene una commissione sulle vendite).
- **Orizzonte realistico**: un prodotto può essere online in pochi giorni; le vendite dipendono dal traffico che gli portiamo (blog, eventualmente social) — non è automatico solo perché è online.
- **KPI**: prodotti pubblicati, pagine di vendita scritte, (quando disponibili) visite alla pagina prodotto, vendite.

## 3. Print-on-Demand / Self-Publishing — `departments/print-on-demand/`
- **Cosa fa**: contenuti a basso contenuto testuale ma alto valore percepito (planner, tracker, journal tematici) pubblicati come ebook/libri stampabili su Amazon KDP, oppure design semplici su Redbubble/Printful. Canale di vendita diverso (ricerca su Amazon/marketplace) per non dipendere solo da Google.
- **Costo**: zero (KDP e Printful non hanno costi di ingresso; l'utente stampa/spedisce nulla, è tutto print-on-demand).
- **Orizzonte realistico**: pubblicazione rapida, ma è un mercato molto affollato — trattarlo come esperimento a basso impegno, non come motore principale.
- **KPI**: prodotti pubblicati, (quando disponibili) visualizzazioni, vendite.

# Regole di valutazione (premio/penalità)

Non c'è denaro reale da distribuire tra i reparti: "premiare" un reparto vuol dire dargli più spazio nel calendario giornaliero e più cicli di miglioramento; "penalizzare" vuol dire ridurne la priorità o mettere in pausa quel filone se dopo un periodo ragionevole non mostra **nessun segnale**, nemmeno minimo.

- **Ogni giorno**: si valuta solo l'esecuzione (il compito assegnato è stato completato bene? sì/no + qualità).
- **Ogni settimana** (dal secondo report settimanale in poi, quando iniziano ad esserci dati reali): si confrontano i segnali reali tra reparti (traffico, click, vendite, feedback) e si riallocano gli sforzi verso ciò che mostra trazione, motivando sempre la decisione nel report.
- **Nessun numero è inventato.** Finché un reparto non ha dati reali (perché gli account non sono ancora attivi, es. Search Console/Gumroad/KDP), il report dice esplicitamente "nessun dato ancora disponibile", mai una stima presentata come fatto.
- Un reparto può essere sospeso se dopo ~6-8 settimane di lavoro costante non mostra alcun segnale misurabile, per concentrare gli sforzi su ciò che funziona.

# Budget

50€ tenuti in riserva. Verranno proposti per una spesa specifica (es. dominio personalizzato, un piccolo test ads, un tool a pagamento) solo quando un reparto mostra un segnale reale che giustifica l'investimento — mai spesi "alla cieca". Ogni proposta di spesa verrà presentata esplicitamente all'utente per approvazione, con la spesa fisicamente eseguita da lui (il manager non ha accesso a pagamenti reali).
