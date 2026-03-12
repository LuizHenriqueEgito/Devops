# O que são Imagens
- Imagens são originadas de arquivos que **programamos** para que o docker crie uma estrutura que execute determinada ações em containers
- Ela contém informações como:
    - Imagens base
    - Diretório base
    - Comandos a serem executados
    - Porta da aplicação
    - etc
- Ao rodar um container baseado na imagem, as instruções serão executadas em camadas

# Como escolher uma Imagem
- Podemos fazer o download das imagens em: `https://hub.docker.com`
- Porém qualquer um pode subir imagens nesse site e isso é perigoso então tome cuidado
- Use imagens oficiais (Veja a quantidade de downloads e o número de estrelas)

# Criando uma Imagem
- Para criar uma imagem é preciso de um arquivo `Dockerfile`
- Este arquivo precisa de algumas instruções para poder ser executado
    - `FROM:` imagem base
    - `WORKDIR:` diretório da aplicação
    - `EXPOSE:` porta da aplicação
    - `COPY:` quais arquivos precisam ser copiados
- Veja um exemplo de criaçãod e imagem em Node.sj:  
```
FROM node

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]
```
- Para ver suas imagens faça: `docker image ls`

# Executando a Imagem Criada
- Primeiro faça o build da imagem
- `docker build <diretório da imagem>`
- Depois é possivel rodar o comando `docker run <imagem>` para executa-lá com o id que é criado após o build
- Cada camada é uma linha do seu Dockerfile
- OBS: `docker run -d -p <porta exposta no navegador:porta expondo na imagem> <id>`

# Alterando a nossa imagem
- 

# Camadas das imagens
- As imagens do Docker são divididas em **camadas** (layers)
- Cada instrução no Dockerfile representa uma layer
- quando algo é atualizado apenas as layers depois da linha atualizada são refeitas (o resto permanece em cache, tornando o build mais rápido)

# Fazendo o Download de Imagens
- Podemos fazer o download de alguma imagem do hub e deixá-la disponivel em nosso ambiente
- Use o comando: `docker pull <imagem>`
- Desta maneira, caso se use em outro container, a imagem já estará pronta para ser utilizada
```
docker pull python
docker run -it python
```

# Comandos no Docker (use help)
- Todo comando no docker tem acesso a uma flag `--help`
- `docker run --help` irá te lembrar o que se pode fazer

# Multiplas aplicações no mesmo container
- Podemos inicializar vários containers com a mesma imagem
- As aplicações funcionarão em paralelo

# Alterando o nome da Imagem e Tag
- podemos nomear a imagem que criamos
- vamos utilizar o comando `docker tag <nome>`
- Também podemos modificar a tag, que seria como uma versão da imagem, semelhante ao git
- Para inserir a tag utilizamos: `docker tag <nome>:<tag>`
```
docker images
docker tag <id> minhaimagem:minhatag
```
- Para nomear uma imagem no build faça: `docker build -t minha_imagem:minha_tag .` Em resumo use a flag `-t`

# Reiniciando um Container iterativo
- Use a flag `-i`:
```
docker start -i sua_imagem
```

# Removendo Imagens
- Assim como nos conainers, podemos remover imagens com o comando: `docker rmi <imagem>`
- Se o container estiver utilizando a imagem podemos utilizar a flag `-f` para forçar sua exclusão: `docker rmi -f <id ou nome da imagem>`

# Removendo Imagens e Containers
- `docker system prune` removemos imagens, containers e networks que não são utilizados
- Removendo um container após a sua utilização, após ele rodar:
```
docker run --rm <container>
```
- Economizamos memoria no computador e deixamos o ambiente mais organizado

# Copiando arquivos entre Containers
- Para copiar arquivos entre containers utilizamos o comand: `docker cp`
- Pode ser utilizado para copiar um arquivo de um diretório para um container ou de um container para um diretório determinado
- Com o container rodando faça: `docker cp minha_imagem:/arquivo/que_quero.py ./pasta_onde_sera_colado/`

# Verificando informações de processamento de um Container
- Para verificar dados de execução de um continer utilizamos: `docker top <container>`
- Dessa forma temos um raio-x do nosso container
- Para verificar diversas informações como: `id, data de criação, imagem e etc`:
```
docker inspect <container>
```
- Dessa forma podemos entender como o container está configurado
- para verificar os processos que estão sendo executados em um continer, usamos o comando: `docker stats`
