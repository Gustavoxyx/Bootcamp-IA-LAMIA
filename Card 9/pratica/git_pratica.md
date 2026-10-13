Prática - clonando o repositório do curso
Aqui eu peguei o repositório que o professor usa nas aulas e trouxe ele pra minha conta. Rodei tudo no PowerShell.

Clonando
cd ~/Downloads
git clone https://github.com/willianjusten/github-course.git
cd github-course
git log --oneline # os 11 commits dele já estão no meu computador
git remote -v # o origin ainda aponta pro repositório do professor

Essa é a diferença entre o clone e o git init. O init começa um projeto vazio, e o clone já traz o histórico inteiro junto.

Trocando o destino
Antes disso eu criei um repositório vazio chamado github-course na minha conta.

git remote remove origin
git remote add origin https://github.com/Gustavoxyx/github-course.git
git remote -v # agora aponta pro meu
git push -u origin master

Os onze commits foram pro meu perfil, cada um ainda com o nome do autor original. O Git guarda essa informação junto com o commit e não troca por quem fez o envio.

Deixando a minha marca
Add-Content -Path Readme.md -Value "Repositorio clonado e usado por mim no card 9 do bootcamp do LAMIA."
git status # o Readme.md aparece como modified
git diff # a minha linha aparece em verde com um sinal de mais
git commit -am "adiciona uma linha minha no readme"
git push

Depois disso o repositório ficou com doze commits. Os onze primeiros são do professor e o último é meu.