## Video apresentando projeto:

  

*EM BREVE*

  

## Motivação:

  

Desenvolver um projeto que apresente algumas camadas de segurança/privacidade.

* Páginas com restrições
* Arquivos de mídia com restrições
* Verificação constante de segurança ( Chave de Segurança nas tabelas do Banco de Dados )

  

Todas as restrições/segurança é baseada nas **Views** do projeto e não nos templates.

**O foco principal é o desenvolvimento Backend do projeto, focando principalmente nas views**

  
  

## Sobre do Projeto:

  **Projeto foi desenvolvido com o intuito de melhorar/desenvolver minhas habilidades Backend.**
  O projeto funciona através do sistema de segurança dele, sem ele a ideia principal, de ter um armazenamento virtual onde apenas o criador de tal conteúdo terá acessado, se perde.

De inicio, o projeto foi desenvolvido em 3 Aplicações:
1. USERS
2. PAGES
3. FORUM

### USERS
Essa aplicação vai cuidar especialmente das funções do usuário, sendo mais específico, é nela que será armazenado a questão de segurança e também a customização das funções de usuário.

### PAGES
Aqui ficará armazenado apenas as rotas URL, aplicação bem simples e sem muita alteração a ser feita nela.

### FORUM
Essa aplicação será responsável por todo nosso projeto praticamente, é nela que se encontra nossos **Mixins**, **Models**, e algumas funções extras.
Nela também faremos algumas verificações de segurança.
**Informando também que:** *As verificações de segurança foram todas feitas através dos views, os templates não são responsáveis por nenhum tipo de validação de segurança*



### Segurança

A segurança do projeto foi feita através de:
* LoginRequiredMixin 
* UserPassesTestMixin

Classes responsáveis:
* CheckBaseView
* CheckDetailView
* media_access

Funcionamento delas é bem simples, ao criar a conta é gerado para o usuário uma SECRETKEY , cada tabela do Banco de Dados e URL acessada pelo usuário é feito através de SECRETKEY, o sistema apenas faz verificações para ver se o acesso que o usuário está fazendo é o mesmo que sua key.

#### SecretKey

É uma chave de acesso de **40 digitos** gerada aleatoriamente e única, tem a mesma função que o ID do usuário.
Cada item da tabela no Banco de Dados possui uma **autor_key** , que quando é feito a criação do item desejado, a chave de usuário é salva nessa tabela.
**Outra opção**: Uma outra opção era apenas usar o **ForeignKey** e relacionar com o banco de dados do usuário, ou até mesmo salvar apenas o ID dele, porém, eu acredito que ficaria muito previsível essas chaves de acesso, *já que a intenção é de que apenas o próprio usuário tenha acesso a sua chave*.

**Caso o acesso seja inválido, ele apenas retorna a página inicial**

## Planejamentos:

#### TEMPLATES

- forum_categoria.html -> Responsável pela página inicial do fórum

- forum_subcategoria.html -> Responsável por exibir conteúdo dentro da subcategoria

- forum_topico.html -> Responsável por exibir conteúdo do tópico

- forum_form.html -> Responsável pelo formulário

  

* Recebera uma <tipo> onde mostrará um formulário pra cada tipo: Adicionar, Editar e Deletar.

* 0 Adicionar

* 1 Editar

* 2 Deletar

  

#### SEGURANÇA

  

Cada item do Banco de Dados receberá a securitKey do usuário, essa será a identificação do mesmo. Basicamente é checado toda vez que o usuário acessa algo se essa key é igual a do usuário logado atualmente, caso não seja, ele apenas retorna a página inicial, impedindo que o usuário visualize, edite e delete itens de outros usuários.

  

#### URL

  

Cada rota URL terá tanto a SecuretKey do usuário quando a ID do item que ele está acessando. Essa ID serve para acessar o item e realizar a verificação de segurança.


## Atualizações

Data | Atualização | Versão
:--------- | :------: | -------:
21/04/2023 | Iniciado projeto Django | V0.0
21/04/2023 | Adicionado UserCustom | V0.1
21/04/2023 | Adicionado uma SecretKey ao usuário | V0.1.1
21/04/2023 | Adicionado Models do fórum | V0.2
21/04/2023 | Adicionado rotas de templates e arquivos estáticos | v0.2.1
21/04/2023 | Adicionado Markdown e templatetags | v0.2.2
21/04/2023 | Adicionado Templates ( Vazios ) | V0.2.3
21/04/2023 | Adicionado SecretKey a todos os Models para identificação ( Cada Models será identificado por sua SecretKey, apenas o usuário que tem a mesma secrekey poderá acessar e administra-lo ) | v0.2.3
21/04/2023 | Adicionado Classe que checa se usuário está logado e se o parâmetro recebido através da URL tem a mesma secretkey que o usuário | v0.2.4
22/04/2023 | Adicionado get_sucess_url aos Models | v0.2.5
22/04/2023 | Adicionado form_valid aos Views | v0.2.6
22/04/2023 | Fixado problema na Segurança url_objkey | v0.2.7
22/04/2023 | Adicionado Views e Templates ( Vazios ) | v0.3
22/04/2023 | Adicionado Redirect para Login/Forum | v0.3.1
22/04/2023 | Views Finalizada e alteração na hora de chegar a SecretKey, quaisquer alteração retornar para página inicial | v0.4
22/04/2023 | Fixado get_absolute_url nos Models | v0.4.1
24/04/2023 | Templates desenvolvidos | v1.0
24/04/2023 | Fixado bug AttributeError para AnonymousUser | v1.1
24/04/2023 | Adicionado segurança a acessar Mídia | v1.2
24/04/2023 | Adicionado funções de Arquivos ao tópico | v1.3
25/04/2023 | Adicionado Versão Alpha do projeto | v2.0
28/04/2023 | Deploy do Projeto | v3.0 - Alpha
28/04/2023 | Fixado Bug de segurança nas categorias | v3.1 - Alpha
28/04/2023 | Adicionado Azure POSTGRESQL | v3.2 - Alpha
28/04/2023 | Fixado erro de Deploy | v3.3 - Alpha
30/04/2023 | Optimização do código | v3.4 - Alpha
30/04/2023 | Adicionado opção de voltar para subcategoria a partir do tópico | v3.5 - Alpha
  

## Bugs e erros:

  

Erro | Atualização | Fixado
:--------- | :------: | -------:
url_objkey | Falha lógica/Segurança | Fixado em 22/04/2023
get_absolute_url | Função errada nos Models | Fixado em 22/04/2023
AttributeError | Django apontava erro de atributo para AnonymousUser | Fixado em 24/04/2023
Violação de Segurança | Era capaz dos outros usuários ver todas as categorias criadas | Fixado em 28/10/2023

  
  

## Próximos Updates:

- Adicionar UserCustom[X] ( V 0.1 ) - Concluído
- Adicionar Models[X] ( V 0.2 ) - Concluído
- Adicionar Templates[X] ( V 0.3 ) - Concluído
- Adicionar Views[X] ( V 0.4 ) - Concluído
- Desenvolver FrontEnd [X] ( v1.0 ) - Concluído
  * Desenvolver forum_categoria.html [X]
  * Desenvolver forum_subcategoria.html [X]
  * Desenvolver forum_topico.html [X]
  * Desenvolver forum_forum.html [X]
- Sistema de grupos [ ] - Em Breve
  * Fazer com que usuários consigam permitir que outros usuários possam acessar
  suas postagens