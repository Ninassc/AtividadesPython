# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Nina Sepúlveda
- Turma: 3A2

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
Essas classes ficam na pasta Models.
Caminho : `Aula12 - Alunos/models`

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
O banco criado é `streamflix.db`. A configuração está em `app.py`, na variável `SQLALCHEMY_DATABASE_URI`.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
Existem as classes `ModeloBase` (`models/base.py`), `FilmeFavorito` (`models/filme_favorito.py`) e `HistoricoBusca` (`models/historico_busca.py`).

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
`FilmeFavorito` e `HistoricoBusca` herdam de `ModeloBase`. Elas recebem automaticamente os campos `id`, `data_criacao` e `data_atualizacao`.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
O `__tablename__` é `"filmes_favoritos"`. Ele define explicitamente o nome da tabela no banco, independentemente do nome da classe.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
A coluna é `tmdb_id`. Ela possui `nullable=False` e `unique=True`.

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
O método verifica se o filme já existe usando `buscar_por_tmdb`. Se existir, retorna `None`. Caso contrário cria um objeto, adiciona à sessão, faz `commit` e retorna o favorito criado.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
Está em `models/historico_busca.py`. Classe `HistoricoBusca`, método `ultimas()`.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
O projeto salva apenas alguns campos da API. Exemplos: `tmdb_id`, `titulo`, `poster_path`, `nota` e `ano`.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
Além de `db`, são exportados `ModeloBase`, `FilmeFavorito` e `HistoricoBusca`. Isso permite importar diretamente `from models import FilmeFavorito`, deixando o código mais organizado.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
Existem 3 Blueprints: `dashboard_bp` (sem `url_prefix`), `filmes_bp` (`/filmes`) e `favoritos_bp` (`/favoritos`).

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
A rota está em `controllers/filmes_controller.py`. A função é `populares()`.

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
Antes do `render_template`, ela chama `api.filmes_populares()` que busca a lista de filmes populares e `FilmeFavorito.listar()` que lista os filmes já favoritados. A partir dessa lista, é criado um conjunto (ids_fav) contendo apenas os IDs dos filmes.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
O registro é feito em `controllers/filmes_controller.py`, usando `HistoricoBusca.registrar(termo, len(filmes))` na linha 54.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
O método HTTP é `POST`. Exemplo: `/favoritos/adicionar/550`.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
Se `api.detalhe(filme_id)` retornar `None`, o usuário é redirecionado para `/filmes/populares`.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
Os Blueprints são registrados em `app.py` com `app.register_blueprint(dashboard_bp)`, `app.register_blueprint(filmes_bp)` e `app.register_blueprint(favoritos_bp)`.

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
O controller é `dashboard_controller.py`. Ele envia `populares`, `melhores`, `total_favoritos`, `historico` e `modo_demo`.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
`services/tmdb_api.py` é uma camada de serviço (Service), mais parecida com uma Model. Os controllers utilizam essa classe para buscar dados da API TMDB.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
O termo pode vir de `request.args` (GET) ou `request.form` (POST). `request.args` lê parâmetros da URL e `request.form` lê dados enviados pelo formulário.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
Os templates ficam em `views/templates/`.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
O template base é `views/templates/layout.html`. Os outros utilizam `{% extends "layout.html" %}`.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
O menu possui links para Home, Filmes Populares, Melhores Filmes, Buscar e Favoritos, usando url_for('dashboard.index'), url_for('filmes.populares'), url_for('filmes.melhores'), url_for('filmes.buscar'), url_for('favoritos.listar')

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
O arquivo é `views/templates/filmes/detalhe.html`. A variável `streaming` vem do controller `detalhe()`, através de `api.streaming(filme_id)`.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
`_card.html` é um componente reutilizável. Ele é incluído com `{% include "filmes/_card.html" %}`.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
A View verifica a variável `favorito`, enviada pelo controller que antes busca o id em buscar favoritos. Se ela existir, mostra o botão Remover; caso contrário, Salvar.

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
O CSS fica em `views/static`. O `layout.html` o carrega usando `url_for('static', filename='...')`.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
O loop é `{% for favorito in favoritos %}`. São exibidos campos como título, nota e ano.

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
`{% if modo_demo %}` verifica se a aplicação está em modo demonstração. Essa variável é disponibilizada para todos os templates pelo `context_processor` em `app.py`.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
Fluxo: o usuário clica em **Salvar favorito** na View (`filmes/detalhe.html`), o formulário envia um `POST` para `controllers/favoritos_controller.py`, que chama `FilmeFavorito.adicionar()` em `models/filme_favorito.py`. Depois o controller faz `redirect` para a página anterior ou para a lista de favoritos.

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
