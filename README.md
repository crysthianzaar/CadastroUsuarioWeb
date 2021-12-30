<H1 align=center> Cadastro de Usuário WEB </H1>

<H3 align=center> Veja todas as issues e kanban do projeto em: https://github.com/crysthianzaar/CadastroUsuarioWeb/projects/1 </H3>

---
### Features:
- Modelagem de Dados
-  Enquanto o usuário não estiver “logado”, apresenta uma página que diz "Olá
visitante"
- Se o usuário estiver “logado”, ao invés da página do "Olá Visitante", apresenta
"Olá {NOME_DO_USUARIO}
- Campo de login por email, CPF ou PIS + senha
- Apresenta botão que leva para página de cadastro de usuário
- Botão de logout
- Botão que leva para a página de edição dos dados cadastrais. Nessa
página apresenta um botão de remoção do usuário que o desloga em
seguida.
- Alteração de senha
- Variáveis de ambiente
- API REST completa para manipulação dos usuários
- Autenticação da API via token JWT

---

#### 	Passos para executar a aplicação:
`$ 1: Criar e ativar venv`

`$ 2: pip install -r requirements.txt`

`$ 3: flask db init`

`$ 4: flask db migrate`

`$ 5: flask db upgrade`

`$ 6: flask run`

---
<div align=center>
  
<H2 > Documentação - RestAPI </H2>
<h5> Rota base da API:  http://127.0.0.1:5000/api/v1/{endpoint} </h5>

Endpoint  | Método | Descrição
------------- | ------------- | -------------
/authlogin/  | POST | Recupera token JWT com base no email e senha 
/users/  | GET | Obtem todos os usuários cadastrados no sistema
/user/ | POST | Adiciona um novo usuário
/user/id | GET | Obtem usuário pelo Id
/user/id | PUT | Altera dados de um usuário pelo Id
/user/id | DELETE | Deleta um usuário pelo Id
/enderecos/ |GET | Obtem todos os endereços cadastrados
  
Utilize o Postman para facilitar testes e entender documentação:
  
  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ed7f32afbde1caef0698?action=collection%2Fimport)
 </div>
 
 - Passos para usar a API:

`$ 1: Ter uma conta ativa na aplicação` 

`$ 2: Utilizar o método POST - /authlogin/ para obter o token JWT (Passar email e senha na body da requisição)`

`$ 3: Passe o campo "token" no params de todos os outros endpoints para usar a API` 

Exemplo de JSON para POST / PUT:


```json
{
    "nome": "Crysthian Z",
    "email": "testfdedfzfanote@gmail.com",
    "cpf": "76420480094" ,
    "pis": "06379098643" ,
    "senha": "teste",
    "pais" : "Brasil",
    "estado" : "ES",
    "municipio" : "Vitória",
    "cep" : "29045740",
    "rua" : "Praça Júlio Teixeira da Cruz",
    "numero": "95",
    "complemento" : "Perto da praça"
} 
```
