CHALLENGE 5 - PERFORMANCE

- lo scopo di questa challenge è creare un file excel contenente le classifiche di 20 campionati di calcio entro un certo limite di tempo 
- i dati per creare il file possono essere ottenuti tramite chiamate API verso https://www.thesportsdb.com/
- per superare la challenge il file excel deve contenere tutti i dati corretti divisi in 20 sheet (uno per lega) e poter essere eseguito entro un secondo

- esempio di URL corretta per chiamata API: https://www.thesportsdb.com/api/v1/json/2/lookuptable.php?l=4328&s=2021-2022
- librerie Python suggerite: asyncio, pandas, json, requests, openpyxl