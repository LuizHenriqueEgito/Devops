# 📂 Git Toolkit
```bash
# iniciando um novo projeto
>> git init  # na pasta do projeto
>> git add <nome-do-arquivo>  # adiciona o arquivo
>> git commit -m "first commit"  # commit
>> git remote add origin <link-do-github>
>> git push
```
## Comandos
### Clássicos
`git status`: Verifica as mudanças feitas.
`git add .` / `git add <nome-do-arquivo>`: Colocam as mudanças na *staging area (área de preparação)*, esses arquivos estão preparados para a próxima etapa.
    - `git add .`: Adiciona todas as mudanças na pasta atual;
    - `git add nome_do_arquivo.txt`: Adiciona apenas este arquivo.
`git commit -m "Seu comentário"`: Cria um *snapshot (fotográfia)* do projeto no histórico, salva o que está no *staging (feito no add)* com uma mensagem descritiva.
`git push`:
`git pull`:
`git clone`:
`git rm`:
`git mv`:
`git log`:
`git reset`:
### Branches
`git branch`:


---
## Dúvidas
#### Como desfazer um git add?
``` bash
git reset arquivo.txt
# Ou todos os arquivos que estão no add
git reset
# Ou ainda maneiras mais novas
git restore --staged arquivo.txt  # volta apenas esse arquivo
git restore --staged .  # Volta todo mundo
```
#### Como desfazer um git commit?
```bash
# Desfaz o commit mas mantem as mudanças no código:
git reset --soft HEAD~1  # remove o commit mas mantém o add
git reset --mixed HEAD~1  # remove o commit e o add mas mantém o código
git reset --hard HEAD~1  # desfaz tudo, commit, add e mudanças no código
git revert <hash_do_commit>  # novo commit que desfaz o anterior sem apagar o histórico
```
#### Qual a diferença entre `merge` e `rebase`?
`merge`: Junta os históricos (mantém a linha do tempo original)
`rebase`: Replica os commits em outra base (deixa o histórico linear)
#### Como resolver conflitos de merge?
Editando os arquivos marcados com `<<<<<<<` e depois fazendo `git add` e `git commit`
#### Como voltar em uma versão especifica do meu código?
```bash
git log --oneline  # Vê os hashs para conseguir saber em qual voltar
git log  # Vê os commits bem detalhados

git revert --no-commit <hash-do-commit-que-deseja-voltar> ..HEAD
git commit -m "Reverte alteração para o estado xpto"
git push origin main
```
#### Como sempre evitar conflitos?
```bash
git pull
```