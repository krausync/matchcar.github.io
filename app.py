from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        duvidas = request.form['duvidas']

        # Adicione os dados à planilha Excel
        dados = pd.DataFrame({
            'Nome': [nome],
            'Email': [email],
            'Telefone': [telefone],
            'Dúvidas': [duvidas]
        })

        dados.to_excel('formulario.xlsx', index=False, header=False, mode='a')

        return redirect(url_for('obrigado'))

    return render_template('formulario.html')

@app.route('/obrigado')
def obrigado():
    return 'Obrigado por enviar o formulário!'

if __name__ == '__main__':
    app.run(debug=True)
