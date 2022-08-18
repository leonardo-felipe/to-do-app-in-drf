# ToDo List API

Estrutura da API

/admin     - Admin

/tasks     - Tasks 
 
## Principais tecnologias utilizadas
 
* Python version 3.10.6
* Django==3.2.10
* djangorestframework==3.13.1
 
## Instruções para instalar e rodar o projeto
 
* Instalar Python 3.10.6
>    https://www.python.org/downloads/

* Clonar o repositório com git clone
>  git clone git@github.com:leonardo-felipe/todo.git

* Ir até a pasta do projeto

* Criar Virutalenv
* Para Linux/Mac:
> python3 -m venv venv
* Para Windows
> python -m venv venv

* Ativar a virtual env no Linux:
> source venv/bin/activate
* Ativar a virtual env no Windows:
> venv\Scripts\activate

* Instalar dependências
> pip install -r requirements.txt

* Migrações
> python manage.py makemigrations

> python manage.py migrate


* Rodar o projeto
> python manage.py runserver

* Crie um super usuário para o Django Admin
> python manage.py createsuperuser

  
## Autor
 
* **Leonardo Oliveira**: @leonardo-felipe (https://github.com/leonardo-felipe)
