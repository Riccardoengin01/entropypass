from flask import Flask, render_template, request
# Importiamo le funzioni logiche e le costanti dal nostro script originale
import entropypass

app = Flask(__name__)

# Definiamo la rotta principale, che accetta sia GET (caricamento pagina) che POST (invio form)
@app.route('/', methods=['GET', 'POST'])
def index():
    # Valori di default per il primo caricamento (GET)
    password_data = {
        'pwd': None,
        'ent': None,
        'len': entropypass.DEFAULT_LENGTH,
        'charset_len': None,
        'use_upper': True,
        'use_digits': True,
        'use_symbols': True
    }

    if request.method == 'POST':
        # Se il form è stato inviato, leggiamo i valori
        length = int(request.form.get('length', entropypass.DEFAULT_LENGTH))
        use_upper = 'use_upper' in request.form
        use_digits = 'use_digits' in request.form
        use_symbols = 'use_symbols' in request.form

        # Validiamo la lunghezza per sicurezza
        if not (entropypass.MIN_LENGTH <= length <= entropypass.MAX_LENGTH):
            length = entropypass.DEFAULT_LENGTH # ripristina il default se il valore non è valido

        # Usiamo le funzioni importate per generare la password
        charset = entropypass.build_charset(use_upper, use_digits, use_symbols)
        pwd = entropypass.generate_pwd(length, charset)
        ent = entropypass.entropy(length, len(charset))

        # Aggiorniamo i dati da passare al template
        password_data.update({
            'pwd': pwd,
            'ent': ent,
            'len': length,
            'charset_len': len(charset),
            'use_upper': use_upper,
            'use_digits': use_digits,
            'use_symbols': use_symbols
        })

    # Renderizziamo il template HTML, passando i dati della password
    return render_template('index.html', data=password_data)

if __name__ == '__main__':
    # Avviamo il server di sviluppo di Flask in modalità debug
    app.run(debug=True)