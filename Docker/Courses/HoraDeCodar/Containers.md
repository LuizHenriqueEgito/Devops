# O que são Containers:
- Containers são um `pacote de código que pode executar uma ação` por exemplo uma aplicação Python, Node.js, PHP etc
- Containers utilizam `imagens` para serem executados
- Multiplos containers podem rodar juntos, p.e: um para PHP e utro para MySQL

# Containers x Imagens
- `Imagem` e `Container` são recursos fundamentais do Docker
- Imagem é o `Projeto` que será executado pelo container, todas as instruções estarão declaradas nela (é a receita do que o container deve fazer)
- Container é o `Docker rodando alguma imagem`, consequentemente executando algum código proposto por ela
- Seguimos o fluxo: Programamos uma `Imagem` e a executamos por meio de um `Container`

# Rodando um Container
- Encontramos imagens no repositório do Docker: `https://hub.docker.com`
- Neste site podemos ver quais imagens existem, por exemplo: Python e aprender como utilizá-las
- Para executar faça:  
```docker run <imagem>```
- Use a flag `-it` de iterativo p.e:  
```docker run -t ubuntu``` pronto agora você consegue mexer em uma maquina ubuntu pelo seu docker.
- Use: ```docker ps``` para listar todos os containers que estão rodando.

# Como verificar containers executados
- Os comandos:  
```docker ps``` ou ```docker container ls``` exibe quais containers estão sendo executados no momento.
- Utilizando a flag `-a`, temos também todos os containers já executados na máquina:  
```docker ps -a```  
```docker container ls -a```

# Container x VM
- Container é uma aplicação que serve para um determinado fim, não possui sistema operacional, seu tamanho é de alguns MBs
- VM possui OS próprio, tamanho de GBs, pode executar diversas funções ao mesmo tempo
- Containers gastam menos recursos para serem executados (por serem mais especificos)

# Rodando Container em Backgroud (detached)
- Quando iniciamos um container que `persiste`, ele fica fica ocupando o terminal
- Podemos executa-lo utilizando a flag -d `(detached)`
- `docker run -d nginx`  # precisamos aprender a expor uma porta

# Expondo Portas
- Os containers docker não tem conexão com nada de fora deles;
- Para expor portas use a `flag -p` p.e: `-p 80:80`, dessa forma teremos a porta 80 acessivel para o container;
- `docker run -d -p 80:80 nginx`

# Parando Containers
- Para parar um container fazemos: `docker stop <id ou nome>`
- Para se certificar que o container não está mais "ligado" faça `docker ps`

# Reiniciando Containers
- Para voltar a rodar um container podemos usar: `docker start <id>`
- OBS: `docker run <imagem>` sempre cria um novo container
- Caso necessite usar um antigo use `docker start <id>`

# Definando nomes para um Container
- Definimos o nome de um container usando a flag `--name`
- Se não definimos um nome ele vem aleatoriamente
- Por exemplo: `docker run --name <nome_desejado> nginx`
- Para para-lo: `docker stop <nome_desejado>`
- Para voltar a roda-lo: `docker start <nome_desejado>`

# Acessando Logs de um Container
- Podemos verificar o que aconteceu com um container usando o seguinte comando: `docker logs <id>`
- As ultimas ações realizadas no container, serão **exibidas no terminal**
- Para acompanhar todo novo log use: `docker logs -f <id>` f de **follow**

# Removendo Containers
- Podemos remover um container da nossa máquina com o comando: `docker rm <id ou nome>`
- Se o container estiver rodando ainda, podemos utilizar a flag `-f` **force**, p.e: `docker rm <id ou nome> -f`
- O container removido não é mais listado com o comando: `docker ps -a`
