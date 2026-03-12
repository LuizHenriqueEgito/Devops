# O que é Docker Compose
- O Docker Compose é uma ferramenta para rodar multipĺos containers
- Teremos apenas um arquivo de configuração, que orquestrara totalmente esta situação
- É uma forma simples de rodar múltiplos builds e runs com um comando
- Em projetos maiores é essencial o uso do Compose

# Instalando o Compose no Linux
- Siga as instruções de: https://docs.docker.com/compose/install/

# Criando nosso  arquivo de Compose
- Crie um arquivo chamado: `docker-compose.yaml`
- Este arquivo vai **coordenar os containers e imagens**
- Ele possui algumas chaves muito utilizadas:  
    - *version*: versão do Compose
    - *services*: Containers/serviços que vão rodar nessa aplicação
    - *volumes*: Possivel adição de volumes

# Rodando o Compose em backgroud
- Para rodar um arquivo Compose use: `docker compose up`
- Para rodar em backgroud use a flag `-d` como seria com um container

# Parando o Compose
- Para para um docker compose em backgroud use: `docker compose down`


# Variaveis de ambiente no Compose
- Para isso vamos definir um arquivo chamado *env_file*
- As variaveis podem ser chamadas pela sintaxe: **${VARIAVEL}**
- Está tecnica é util quanmdo o dado a ser inserido é sensivel/não pode ser compartilhado, como uma senha por exemplo

# Redes no Compose
- O Compose cria uma rede basica **Bridge** entre os containers da aplicação
- Poreḿ podemos isolar as redes com a chave **networks**
- Assim podemos conectar apenas os containers que optarmos
- Também é possivel definirmos drivers diferentes também


# Criando o Compose do nosso projeto
- Como fazer a transferencia do docker file para o compose:
```
docker build -t nome_da_sua_img_1 .
docker build -t nome_da_sua_img_2 .

docker-compose up
```
``` YAML
version: '3.3'

services:
  db: # Container de MySQL
    image: nome_da_sua_img_1
    volumes: 
      - db_data:/var/lib/mysql
    restart: always
    env_files:
      - ./db.env
    networks:
      - backend
  
  wordpress:
    depends_on:
      - db
    image: nome_da_sua_img_2
    ports:
      -"8000:80"
    restart: always
    environment:
      - WORDPRESS_DB_HOST: db:3306
      - WORDPRESS_DB_USER: luiz
      - WORDPRESS_DB_PASSWORD: secret
      - WORDPRESS_DB_NAME: wordpress
    networks:
      - backend
volumes:
  db_data: {}
networks:
  backend: 
    driver: bridge
```

# Build de imagens no Compose
- Podemos gerar o build durante o Compose também
- Isso vai eliminar o processo de gerar o build da imagem a cada atualização
``` YAML
version: '3.3'

services:
  db: # Container de MySQL
    build: ./caminho para o seu dockerfile  # você tira a image e coloca o build
    volumes: 
      - db_data:/var/lib/mysql
    restart: always
    env_files:
      - ./db.env
    networks:
      - backend
  
  wordpress:
    depends_on:
      - db
    build: ./caminho para o seu dockerfile  # você tira a image e coloca o build
    ports:
      -"8000:80"
    restart: always
    environment:
      - WORDPRESS_DB_HOST: db:3306
      - WORDPRESS_DB_USER: luiz
      - WORDPRESS_DB_PASSWORD: secret
      - WORDPRESS_DB_NAME: wordpress
    networks:
      - backend
volumes:
  db_data: {}
networks:
  backend: 
    driver: bridge
```

# Volume bind mount no Compose
- O volume de bind Mount garante atualização em tempo real do arquivos do container
``` YAML
version: '3.3'

services:
  db: # Container de MySQL
    build: ./caminho para o seu dockerfile  # você tira a image e coloca o build
    volumes: 
      - db_data:/var/lib/mysql
    restart: always
    env_files:
      - ./db.env
    networks:
      - backend
  
  wordpress:
    depends_on:
      - db
    build: ./caminho para o seu dockerfile  # você tira a image e coloca o build
    ports:
      -"8000:80"
    restart: always
    environment:
      - WORDPRESS_DB_HOST: db:3306
      - WORDPRESS_DB_USER: luiz
      - WORDPRESS_DB_PASSWORD: secret
      - WORDPRESS_DB_NAME: wordpress
    volumes:
      - "m:\\seu-diretorio\\fica\\aqui:/app"
    networks:
      - backend

networks:
  backend: 
    driver: bridge
```

# Verificando serviços do Compose
- Para verificar o compose faça: `docker-compose ps`
