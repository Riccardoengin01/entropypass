![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

# EntropyPass 🔐  
🌐 Generatore di Password Sicure + Calcolo Entropia  
🔐 Secure Password Generator + Entropy Estimator

---

## 🇮🇹 Introduzione

**EntropyPass** è uno script Python da riga di comando (CLI) che:

- genera password sicure in base alle preferenze dell’utente  
- calcola l’entropia stimata (in bit) per valutarne la robustezza  
- sfrutta il modulo `secrets`, raccomandato per la generazione crittografica  
- consente di specificare la lunghezza da 8 a 64 caratteri (anche interattivamente)

👤 Utile per sysadmin, sviluppatori, ingegneri della sicurezza informatica o chiunque voglia password robuste.

---

## 🇬🇧 Introduction

**EntropyPass** is a Python command-line (CLI) script that:

- generates strong passwords based on user-selected preferences  
- computes the estimated entropy (in bits) to evaluate strength  
- uses Python’s `secrets` module for cryptographically secure randomness  
- allows selecting a password length between 8 and 64 (also interactively)

👤 Useful for sysadmins, developers, cybersecurity engineers, or anyone needing strong passwords.

---

## ▶️ 🇮🇹 Esecuzione / 🇬🇧 Run

```bash
# con argomento lunghezza
python entropypass.py -l 20

# interattivo (ENTER = default 16)
python entropypass.py
```

---

## ⚙️ 🇮🇹 Opzioni disponibili / 🇬🇧 Available options

| Opzione / Option | 🇮🇹 Descrizione                    | 🇬🇧 Description                     |
|------------------|------------------------------------|------------------------------------|
| `-l`             | Lunghezza della password (8–64)    | Password length (8–64)             |
| `--digits`       | Includi numeri (0–9)               | Include digits (0–9)               |
| `--symbols`      | Includi simboli (!@#…)             | Include symbols (!@#…)             |
| `--no-upper`     | Escludi lettere maiuscole          | Exclude uppercase letters          |
| `--no-lower`     | Escludi lettere minuscole          | Exclude lowercase letters          |
| `--no-digits`    | Escludi numeri                     | Exclude digits                     |
| `--no-symbols`   | Escludi simboli                    | Exclude symbols                    |

---

## 🔐 🇮🇹 Entropia e sicurezza / 🇬🇧 Entropy & security

| Length | Charset | Entropy (bit) | 🇮🇹 Sicurezza stimata          | 🇬🇧 Estimated security        |
|-------:|:-------:|--------------:|-------------------------------|------------------------------|
| 8      | 26      | 37.6 bit      | Crackabile in < 1 s           | Crackable in < 1 s           |
| 8      | 62      | 47.6 bit      | Pochi secondi                 | Few seconds                  |
| 12     | 70      | 71.6 bit      | Sufficiente per uso base      | Safe for casual use          |
| 16     | 70      | 95.5 bit      | Alta sicurezza                | Highly secure                |
| 20     | 70      | 119.4 bit     | Livello “militare”            | Military-grade protection    |

> 💡 Stime basate su attacchi brute-force a 10 miliardi di tentativi/sec.

---

## 📄 Esempio di output

```txt
🔐  Password: hB9@GskPqT$w7cZ1
🧮  Entropia stimata: 95.5 bit (len=16, charset=70 chars)
```

---

## 👤 Autore / Author

**Riccardo Righini**  
🔗 <https://github.com/Riccardoengin01>  
📝 Licensed under the **MIT License**

Made with ❤️ in Italy 🇮🇹