FROM python:3.12-slim

WORKDIR /app

COPY app.py .

# cria o diretório do volume
RUN mkdir /data

VOLUME /data

CMD ["python", "app.py"]