# README.md para o Projeto de Acesso à API do Detran de MG <img src='https://github.com/andref-tech/andref-tech/blob/main/Python-programming-logo-on-transparent-background-PNG.png' width='70'>

## Descrição do Projeto

Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Flask. O objetivo é acessar a API do Detran de Minas Gerais (MG) para coletar dados de um veículo através do número do RENAVAM. A aplicação permite que o usuário insira o RENAVAM e visualize informações detalhadas sobre o veículo e seu proprietário, incluindo débitos pendentes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento da aplicação.
- **Flask**: Framework web para Python que facilita a criação de aplicações web.
- **HTML/CSS**: Para a construção da interface do usuário.
- **Bootstrap**: Framework CSS para estilização e responsividade da interface.
- **Requests**: Biblioteca para fazer requisições HTTP à API do Detran.

## Estrutura do Projeto

```
/projeto-detran
│
├── app.py
├── /templates
│   ├── index.html
│   └── dados.html
└── README.md
```

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/andref-tech/projeto-detran.git
   cd projeto-detran
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install Flask requests
   ```

## Configuração

- **Chave Secreta**: No arquivo `app.py`, altere a linha `app.secret_key = 'sua_chave_secreta_aqui'` para definir uma chave secreta para a sessão.

## Como Usar

1. **Inicie a aplicação**:
   ```bash
   python app.py
   ```

2. **Acesse a aplicação**: Abra o navegador e vá para `http://127.0.0.1:5000/`.

3. **Insira o RENAVAM**: Digite o número do RENAVAM (deve conter 9 dígitos) e clique em "Continuar".

4. **Visualize os dados**: Após a validação do RENAVAM, você será redirecionado para uma página que exibirá os dados do veículo e do proprietário, incluindo informações sobre débitos.

## Exemplo de Uso

- **RENAVAM Válido**: Insira um RENAVAM válido para visualizar os dados do veículo.
- **RENAVAM Inválido**: Se o RENAVAM não for válido, uma mensagem de erro será exibida.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um "issue" ou enviar um "pull request".

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.


Sinta-se à vontade para personalizar este README conforme necessário para atender às suas necessidades específicas!
