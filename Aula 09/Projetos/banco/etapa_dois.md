# Etapa 02 - Criando a Base de Dados do Projeto
Nesta etapa, você irá configurar o banco de dados do seu projeto Django e criar um usuário administrador para acessar a interface de administração.

### Entendendo as Migrações do Django
As migrations (migrações) no Django são a forma como o framework lida com as alterações no seu modelo de banco de dados. Em vez de escrever SQL manualmente, você define seus modelos Python (classes que representam tabelas no banco de dados), e o Django gera automaticamente os arquivos de migração que contêm as instruções para criar, modificar ou excluir tabelas e campos no seu banco de dados.

Quando você executa makemigrations, o Django inspeciona suas classes de modelo e compara-as com o estado atual das migrações. Se ele detectar alguma alteração (como a criação de um novo modelo ou a adição de um campo), ele gera um novo arquivo de migração.

Quando você executa migrate, o Django pega todos os arquivos de migração pendentes (tanto os seus quanto os dos aplicativos internos do Django, como autenticação e administração) e os aplica ao seu banco de dados, criando ou modificando as tabelas conforme necessário.

### Gerando Arquivos de Migração:
Este comando prepara o Django para criar as tabelas necessárias para os aplicativos padrão (como autenticação, administração) e para o seu próprio aplicativo banco.

```
python manage.py makemigrations
```
Você verá uma saída indicando os arquivos de migração que foram criados ou detectados.

### Aplicando as Migrações ao Banco de Dados:
Agora, execute o comando para aplicar essas migrações. Isso criará as tabelas no seu banco de dados (por padrão, o Django usa SQLite para desenvolvimento, que é um arquivo simples no diretório do seu projeto).
```
python manage.py migrate
```
Este comando irá criar as tabelas para os módulos internos do Django e para o seu aplicativo banco.

### Criando o Usuário Administrador (Superuser)
Para acessar a interface de administração do Django, você precisará de um usuário com privilégios de superusuário.

### Criar Superusuário:
Execute o seguinte comando no terminal:
```
python manage.py createsuperuser
```
### Preencha os Campos Solicitados:
O terminal irá solicitar algumas informações. Preencha conforme as instruções:

- **Username (leave blank to use 'seu_nome_de_usuario'):** Digite admin e pressione Enter.

- **Email address:** Pressione Enter para deixar vazio.

- **Password:** Digite senac@123 e pressione Enter. A senha não aparecerá na tela por segurança.

- **Password (again):** Digite senac@123 novamente e pressione Enter.

Você verá uma mensagem de sucesso como "Superuser created successfully."

### Iniciar o Projeto e Acessar o Painel Administrativo
Agora que o banco de dados está configurado e o superusuário criado, você pode iniciar o servidor e acessar a interface de administração.

Iniciar a Aplicação:
```
python manage.py runserver
```
### Acessar o Painel Administrativo:
No seu navegador, acesse a seguinte URL:

http://127.0.0.1:8000/admin/

Você será redirecionado para a página de login do painel administrativo do Django.

### Fazer Login:
Utilize o nome de usuário (admin) e a senha (senac@123) que você criou anteriormente para fazer login.

**Parabéns!** Você acessou com sucesso o painel administrativo do Django, onde poderá gerenciar os modelos do seu projeto, usuários e outras configurações.