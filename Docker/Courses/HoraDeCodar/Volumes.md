# O que são Volumes
- Forma de salvar dados fora do Container
- Forma prática de `persistir` dados em aplicações e não depdender de containers para isso
- Isso porque todo dado criado por um container é salvo nele, quando o container é removido perdemos os dados
- Por isso precisamos dos **volumes** para gerenciar os dados e também conseguir fazer backups de forma mais simples

# Tipos de Volumes
- **Anônimos (anonymous)**: Criados pela `flag -v` porém com um nome aleatório
- **Nomeados (named)**: São volumes com nomes
- **Bind Mounts**: Uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informanmos um diretório para este fim

# O problema da persistência
- Se criarmos um container com alguma imagem, todos os arquivos que geramos dentro deles serão do container
- Quando o container for removido, perderemos estes arquivos
- Por isso precisamos de **volumes**
- Exemplo prático:
``` 
FROM php:8-apache

WORKDIR /var/www/html

COPY . .

EXPOSE 80

RUN chown -R www-data:www-data /var/www
```
``` shell
docker build -t phpmessagens
docker run -d -p 80:80 --name phpmessages_container phpmessages
```
- Nota: Se você der um stop e depois um start seus arquivos continuaram a existir, no entanto se você remover o container e depois criar de novo ai sim as informações serão perdidas e é isso que os **volumes** resolver

# Craindo Volumes Anônimos
- Criamos um volume anônimo da seguinte maneira:
```
docker run -v /data
```
- Onde *data* será o diretório que contém o volume anônimo
- Com o comando `docker volume ls`, podemos ver todos os volumes do nosso ambiente


# Criando Volumes Nomeados
- Criamos um volume nomeado desta maneira:
```
docker run -v nome_do_volume:/data
```
- Todos os atributos dos volumes anônimos funcionam aqui
- Para rodar um container com um volume atrelado faça:
```
docker run <container> -v meu_volume:/minha_pasta
```
# Criando Volumes Bind Mounts
- Salva dados na maquina Host
- Não criamos um volume mas apontamos um diretório
- O comando é: `docker run -v /dir/data_host:/data_do_container`
- Dessa maneira o diretório /dir/data no nosso computador, será o volume deste container

# Atualização do projeto com bind mount
- Bind mount não serve apenas para *volumes*
- Pode também ser usado para **atualizar em tempo real o projeto** sem ter que fazer novamente o build
```
docker run <container> -v diretorio_do_build:/data_container
```

# Criando volumes manualmente
- Use o comando: `docker volume create <nome>`
- Desta maneira temos um named volume podemos atrelar a algum container na sua execução:
``` 
ocker run <container> -v volume_criado_manualmente:/data_container
```

# Listando Volumes
- Use: `docker volume ls`
- Temos acesso aos volumes anonimos e nomeados

# Inspecionando Volumes
- Use: `docker volume inspect nome`
- Desta fomra temos acesso ao local em que o volume guarda dados, nome, escopo e muito mais
- O docker salva os dados dos volumes em algum diretŕoio do nosso computador, desta forma podemos saber qual é.

# Removendo Volumes
- Use: `docker volume rm <nome>`
- Os dados serão 100% removidos
- Para remover volumes em massa faça: `docker volume prune`
- Isso remove todos os containers que não estão sendo utilizados


# Volume Somente Leitura
- Podemos criar um volume que tem apenas permissão ed leitura
- Use: `docker run -v volume:/data:ro`
- `:ro` de read only
