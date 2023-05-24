## Minha API CRUD em Django

### Passo a passo da criação da mesma
#### 1. Criar a .venv do projeto:
#### py -m venv myenv
#### entrar na .venv .\.venv\Scripts .\activate

#### instalar django e djangorestframework
#### criar o pip feeze e criar o arquivo de requirements.txt

#### criar o projeto e o app
#### django-admin startproject core ., python manage.py startapp CRUD

#### add a aplicacao criada a settings em installed apps
#### migrar o projeto python manage.py makemigrations e depois migrate

#### criar um superuser
#### proteger a secrete key com: str(os.getenv('SECRET_KEY'))
