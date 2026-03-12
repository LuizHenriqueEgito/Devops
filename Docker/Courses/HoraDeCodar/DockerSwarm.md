# O que é orquestração de containers
- É o ato de gerenciar e escalar os containers da nossa aplicação
- Um serviço que rege sobre outros serviços, verificando a funcionalidade deles
- Alguns deles: Docker **Swarm**, **Kubernetes** e **Apache Mesos**

# O que é Docker Swarm
- Uma ferramenta do Docker para **orquestrar containers**
- Podem escolar *horizontalmente* nossos projetos de maneira simples
- Seus comandos são muito semelhantes aos do Docker
- Toda instalação do Docker já vem com o *Swarm* porém desabilitado

# Conceitos fundamentais
- **Nodes**: É uma instância (máquina) que participa do Swarm
- **Manager Node**: Node que gerencia os demais Nodes
- **Worker Node**: Nodes que trabalham em função do Manager
- **Service**: Um conjunto de Tasks que o Manager Node manda o Work Node executar
- **Task**: Comandos que são executados nos Nodes

# Instalando o Docker na AWS
- `sudo yum update -y`
- `sudo yum install Docker`
- `sudo service docker start`
- `sudo usermod -a -G docker <nome da maquina>`  # da o acesso
- `sudo docler swarm init`

# Iniciando o Swarm
- Para iniciar o Swarm usamos: `docker swarm init`
- As vezes precisamos declarar o IP do servidor com a flag: `docker swarm init --advertise-addr`
- Isso faz a instancia virar um Node
- Para listar os nodes ativos fazemos: `docker node ls`

# Adicionando máquinas ao Swarm
- Para adicionar um novo serviço fazemos: `docker swarm join --token <TOKEN><IP>:<PORTA>`
- A nova maquina entra na hierarquia como Worker

# Subindo serviços no Swarm
- Podemos iniciar um serviço com o comando: `docker service create --name <nome><imagem>`
- Assim teremos um container novo sendo adicionado ao nosso *Manager*
- Esse serviço estará sendo gerenciado pelo Swarm

# Listando serviços
- Use: `docker service ls`
- Só as máquinas Manager conseguem rodar esses comandos, maquinas Workers não

# Removendo serviços
- Podemos remover um serviço com: `docker service rm <nome>`
- Para checar usamos: `docker service ls`

# Replicando serviços
- Podemos criar um serviço com um número maior de réplicas: `docker service create --name <NOME> --replicas <NUMERO><IMAGEM>`


# Testando a orquestração do Swarm
- Se um container for removido o orquestrador coloca ele de pé novamente sozinho

# Recuperando o Token do Swarm
- Para pegar o token pelo terminal usamos: `docker swarm join-token manager`

# Checando o Swarm
- Fazendo: `docker info`
- Recebemos informações importantes como: ID do node, número de nodes, numero de managers, etc

# Deixando o Swarm em um Node
- Use: `docker swarm leav`
- Paramos de executar o Swarm em uma determinada instância

# Removendo um Node
- Para remover o Node do nosso ecossistema do Swarm fazemos: `docker node rm <ID>`
- A instância não será considerada mais um Node, saindo do Swarm
- Caso esteja sendo rodado será preciso utilizar a flag `-f`

# Inspecionando serviços
- Para inspecionar serviços fazemos: `docker service inspect <ID>`

# Verificando quais containers estão rodando
- Podemos verificar quais containers um serviço já rodou com: `docker service ps <ID>`
- Esse comando é semelhante ao `docker ps -a`

# Compose no Swarm
- Para rodar o Compose com Swarm utilizamos o comando: `docker stack deploy -c <ARQUIVO.YAML><NOME>`
- Para escalar, criar novas réplicas nos Worker Nodes fazemos: `docker service scale <NOME>=<Nº REPLICAS>`

# Parar de receber Tasks em um Node
- Podemos fazer com que um serviço não receba mais ordens do Manager
- Fazemos: `docker node update --availability drain <ID>`
- Drain: Não recebe mais task
- Active: Recebe tasks

# Atualizando uma imagem no Swarm
- Podemos atualizar as configurações dos nossos nodes com o comando: `docker service update --image <IMAGEM><SERVICO>`
```
docker service update --image nginx:lastest pdq
``````
- Dessa forma apenas os nodes que estão com o status _activce_ receberão atualizações.

# Criando redes para serviços do Swarm
- A conexão entre instâncias usa um driver diferente, o _overlay_
- Podemos criar a rede com `docker network create`
- E por fim criar um servico a flag `--network <REDE>` para inserir as instâncias na nossa nova rede.

# Conectando serviço a uma rede jé existente
- Podemos conectar serviços que já estão em execução a uma rede
- Vamos utilizar o comando de update: `docker service update --network-add <REDE><NOME>`
- Depois podemos ver o resultado com _inspect_