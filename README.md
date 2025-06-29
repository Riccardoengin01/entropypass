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
python entropypass.py -l 20 --symbols
```

---

## ⚙️ 🇮🇹 Opzioni disponibili / 🇬🇧 Available options

| Opzione / Option | 🇮🇹 Descrizione                  | 🇬🇧 Description                    |
|------------------|----------------------------------|------------------------------------|
| `-l`             | Lunghezza della password         | Password length                    |
| `--digits`       | Includi numeri (0–9)             | Include digits (0–9)               |
| `--symbols`      | Includi simboli (!@#...)         | Include symbols (!@#...)           |
| `--no-upper`     | Escludi lettere maiuscole        | Exclude uppercase letters          |
| `--no-lower`     | Escludi lettere minuscole        | Exclude lowercase letters          |
| `--no-digits`    | Escludi numeri                   | Exclude digits                     |
| `--no-symbols`   | Escludi simboli                  | Exclude symbols                    |

---

📄 Esempio di output / [Example output](examples/example_output.txt)

---

## 👤 Autore / Author

**Riccardo Righini**  
🔗 [GitHub](https://github.com/Riccardoengin01)  
📝 Licensed under the MIT License  

Made with ❤️ in Italy 🇮🇹
