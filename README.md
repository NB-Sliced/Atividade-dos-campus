Este projeto implementa um sistema em Python para gerenciar os campos da UFC e seus cursos. O programa permite cadastrar campos, procurar um campus, adicionar cursos, remover cursos e consultar todos os campos cadastrados. O código foi organizado utilizando módulos e um pacote principal.


Arquivos:

main.py
Arquivo responsável por executar o sistema e apresentar o menu principal. Ele realiza as chamadas para as funções que estão dentro do pacote UUFC.

Pasta UFC
Contém um arquivo init.py que define a pasta como um pacote Python. Dentro dela também estão os módulos lista_de_campos.py e cursos.py.

lista_de_campos
Armazena e gerencia a lista de campos . Possui funções para cadastrar campos, procurar campos, consultar todos os campos e chamar as operações relacionadas aos cursos.

cursos.py
Contém funções para adicionar cursos, remover cursos e listar os cursos de cada campus.
