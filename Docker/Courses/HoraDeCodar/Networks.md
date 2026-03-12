# O que são Networks
- Uma forma de gerenciar a conexão do Docker com outras plataformas ou até mesmo entre containers
- Eles são criadas separadas dos containers, como os volumes
- Uma Rede deixa muito mais simples a comunicação entre containers

# Tipos de Conexão
- **Externa**: Conexão com uma API de um servidor remoto
- **Com o Host**: Comunicação com a máquina que está executando o Docker
- **Entre containers**: Comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers

# Tipos de Driver
- **Bridge**: O mais comum e default do Docker, utilizado quando os containers precisam se conectar (na maioria das vezes optmaos por este driver)
- **Host**: Permite a conexão entre um container a maquina que está hosteando o Docker
- **Macvlan**: Permite a conexão a um container por um MAC addess
- **None**: Remove todas as conexões de rede de um container
- **Plugins**: Permite extensões de terceiros para criar outras redes

# Listando Networks
- Para verificar as redes use: `docker networks ls`
- Algumas redes já estão criadas, eles fazem parte da configuração inicial do Docker

# Criando Redes
- Para criar uma rede faça: `docker network crate <nome>`
- Esta rede será do tipo **bridge**

# Removendo Redes
- Para remover uma network fazemos: docker network rm <nome>``
- Para remover redes não utilizadas faça: `docker network prune`

# Instalação do Postman
- Vamos criar uma **API** para testar a conexão entre containers
- Para isso vamos utilizar o **Postman**

# Conexão Externa
- Os containers podem se conectar livremente ao mundo exterior
- Podemos acessar uma API de código aberto
- Veja isso na pasta: `networks_conexao_externa`
- Talvez você pode tomar erro de retry no download de pacotes ao rodar o build então faça: `docker build -t <imagem> . --network=host`

# Conexão com Host
- Podemos também conectar um container com o host do Docker
- **Host** é a maquina que está executando o Docker
- Como *ip* de host utilizamos: **host.docker.internal**

# Conexão entre Containers
- Podemos estabelecer uma conexão entre containers
- Duas imagens distintas rodando em containers separados que precisam se conectar para inserir uum dado no banco.
- Agora nosso container de flask vai inserir dados em um MySQL que roda pelo Docker também
- É preciso de uma rede **bridge**, para fazer essa conexão
- O comando para criar a network é: `docker network create <nome_da_sua_rede>`
- Para conectar os containers em rede faça: 
```
docker run -d -p 3306:3306 --name <nome_do_container> --rm --network <nome_da_sua_rede> -e MYSQL_ALLOW_EMPTY_PASSWORD=True <sua_image>
```
- O -e significa uma variavel de ambiente

# Conectando um container a uma rede
- Para isso utilizamos o comando: `docker network connect <rede> <container>`
- Após isso o container estara dentro da rede

# Desconectando um container
- Basta utilizarmos o comando: `docker network disconnect <rede> <container>`

# Inspecionando Redes
- Usamos o comando: `docker network inspect <nome>`
- Vamos receber informações como: data de criação, driver, nome e muito mais

#
