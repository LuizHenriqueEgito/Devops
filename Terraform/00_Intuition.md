# Terraforms
O `Terraforms` é uma ferramenta de **Infraestrutura** como código **(IaC)** (semelhante ao `CloudFormation`). Você cria servidores, bancos de dados, redes utilizando código ao invés de cliques. Ele serve para *automatizar* criações de infraestrutura, versionar etc.

# Como utilizar
Para utilizar o `Terraforms` precisamos conhecer alguns conceitos básicos:
- **Provides**: Quem você está usando, AWS, Azure, GCP, etc;
- **Resource**: O que você está criando, um servidor, banco de dados, etc;
- **Variables**: Parametriza sua criação, você pode aumentar a maquina, memoria etc tudo por meio de variaveis;
- **Output**: Retorno do que foi criado, as vezes você precisa ter um componente criado para fazer ou vincular a outro.

# Linguagem
Ele é uma linguagem de configuração desenvolvida pela `HashiCorp`, e utiliza a própia `HashiCorp Configuration Language (HCL)` que é uma linguagem declarativa *(linguagens declarativas = você diz o que quer fazer e não como vai fazer)*.

Ela possui controles de fluxo limitados como `for` e `if`.

# Funcionamento
1. Escreva os arquivos `.tf` com a configuração que desejar;
2. O terraform vai analisar o código no `plan`, comparar o estuda atual e as modificações e mostrar um plano de execução: o que será criado, alterado ou destruído.
3. Aplica `apply` o plano da etapa anterior.
