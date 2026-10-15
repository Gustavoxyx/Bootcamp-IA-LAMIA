Comandos do curso:

Eu rodei tudo no Git Bash, dentro da pasta `curso-git-lamia`.

Configuração inicial:

git config --global user.name "Gustavo Nunes"
git config --global user.email "gustavonunesdasilva813@gmail.com"
git config --global --list        # vejo se gravou certo
Esses dados vão junto em todo commit que eu faço.

Criando o repositório:

git init
Isso cria uma pasta escondida `.git` dentro do projeto. Daqui pra frente, o Git começa a olhar tudo que acontece nessa pasta.
Ciclo de vida dos arquivos
echo "# Curso de Git e GitHub - LAMIA" > Readme.md

git status                       ## o arquivo aparece em vermelho, como untracked
git add Readme.md                 ##jogo ele pro stage(onde eu preparo o que vai entrar no próximo commit.) 
git status                       ## agora aparece em verde, prontinho pro commit
