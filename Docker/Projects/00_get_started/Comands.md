# Passo a passo
1. Construção do código python `app.py`;
2. Construção do `dockerfile` que usa o código python;
3. Construção da `imagem docker`:
```bash
docker build -t 00_get_started .
```
4. Para ver a `imagem` criada:
```bash
docker images
# ou já achando ela diretamente
docker images | grep 00_get_started
```
5. Rodando a imagem no formato `interativo (it)`:
```bash
# -i: mantém o input aberto
# -t: terminal interativo
docker run -it 00_get_started
```
