# Build (Constroi a imagem)
```bash
docker build -t app-messages .
```
# Cria o volume
```bash
docker volume create messages-volume
```
# Roda o container
```bash
docker run -it --name app -v messages-volume:/data app-messages
```
# Rodar novamente
```bash
docker start -i app
```