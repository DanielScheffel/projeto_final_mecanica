# Especifique a imagem base
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /usr/src/app

# Instale as dependências
RUN pip install Django==3.2.7 psycopg2-binary==2.9.9

# Copie o código do aplicativo para o container
COPY . .

# Exponha a porta que o aplicativo usa
EXPOSE 8000

# Defina o comando para iniciar o aplicativo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]