# Use uma imagem base do Python 3
FROM python:3

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# Instale as dependências do seu aplicativo
RUN pip install --upgrade pip
RUN pip install requests Flask flask_mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]
