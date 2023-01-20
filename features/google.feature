# language: pt

Funcionalidade: realizar pesquisa no Google

    '''
    Eu como usuário desejo acessar a página do google e realizar uma pesuisa.
    '''

    Contexto: acessar página de teste
        Dado que acesso a página do Google

    Cenário: acessar página do Google e realizar pesquisa
        Dado que preencho o campo de pesquisa com Python
        Quando clico no botão de pesquisar
        Então devo visualizar os resultados
