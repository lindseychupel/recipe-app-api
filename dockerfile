# Imagem base
FROM python:3.9-alpine3.13

# Autor / mantenedor
LABEL maintainer="lindseychupel"

# Variável de ambiente para não bufferizar a saída do Python
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Instala as dependências
RUN apk add --no-cache postgresql-dev gcc musl-dev
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.dev.txt

# Copia a aplicação para dentro do container
COPY ./app /app

# Cria um usuário para rodar a aplicação (opcional, mais seguro)
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

# Expõe a porta da aplicação
EXPOSE 8000

# Comando padrão ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
