# O que é YAML
- É uma linguagem usada para arquivos de configuração
- É facil para humanos lerem
- A extensão de seus arquivos são *.yml* ou *.yaml*
- Os arquivos .yaml possuem **chaves** e **valores**

# Espaçamento e indentação
- A indentação deve conter um ou mais espaços, não devemos utilizar tab
- O espaço é obrigatório após a declaração da chave

# comentarios
- Os comentarios são feitos usando #
- Como qualquer linguagem o que está no comentario não será levado em conta

# Numerics
- **Inteiros** = 12
- **Floats** = 15.8

# Strings
- Podemos escrever textos de duas maneiras no yaml:  
    - *Sem aspas*: este é um texto valido
    - *Com aspas*: "este também é"

# Valores Nulos
- Podemos definir um dado como nulo de duas formas:  
    - *~* ou *null*
- Os dois vão resultar em None, após a interpretação

# Booleanos
- Podemos inserir booleanos em YAML da seguinte forma:  
    - *True* e *On* = verdadeiro
    - *False* e *Off* = falso

# Listas
- Os arrays, tipos ded ados para listas, possuem duas sintaxes:  
    - primeira: [1, 2, 3, 4, 5]
    - segunda: Items:  (mais usada)
                - 1  
                - 2  
                - 3  
                - 4  
                - 5  

# Dicionarios
- Os dicionarios, tipo de dados para objetos ou listas com chaves e valores, podem ser escritos assim:  
     - obj: {a: 1, b: 2, c: 3}
     - obj:  (indentado)
            a: 1  
            b: 2  
            c: 3  

