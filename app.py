from flask import Flask, render_template, request, flash, redirect, url_for, session
import requests
import code

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        renavam = request.form.get('renavam')
        if len(renavam) != 9 or not renavam.isdigit():
            flash('Número de Renavam incorreto, renavam contém 9 dígitos')
            return redirect(url_for('index'))
        # Salvar o valor do RENAVAM na sessão
        session['renavam'] = renavam
        flash(f'Renavam: {renavam} salvo com sucesso.')
        return redirect(url_for('obter_dados'))  # Redireciona para a função obter_dados
    return render_template('index.html')


@app.route('/obter_dados')


def obter_dados():     
    renavam = session.get('renavam')  # Recupera o renavam da sessão
    if not renavam:
        flash('Nenhum Renavam encontrado.')
        return redirect(url_for('index'))

    url = f'https://buscar-renavam-ipva-digital.fazenda.mg.gov.br/api/extrato-debito/renavam/{renavam}/'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        dict_deb = {}
        for ano_deb in dados['extratoDebitos']:
            pago = True
            for parcela in ano_deb['parcelas']:
                if parcela['estaPago'] != True:
                    pago = False
                    break
            dict_deb[f'{ano_deb['anoExercicio']}'] = pago
    else:
        dados = {'error': 'Não foi possível obter os dados'}

    def ver_pag(valor):
        if dict_deb[f'{valor}'] == True:
            return 'Pago'
        else:
            return 'Não Pago'

    # code.interact(local=locals())
    return render_template('dados.html', dados=dados, ver_pag=ver_pag)


if __name__ == '__main__':
    app.run(debug=True)