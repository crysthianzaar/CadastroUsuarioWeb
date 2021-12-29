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
  
  
   [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/1ba2ece2b373d108bb7f?action=collection%2Fimport)
 </div>
 
