# estudos-python

*Este e um texto em italico*
_Este também e um texto em italico_
Este **texto esta em negrito** e esse __também__
##Utilizando os titulos e aprendizagem em **MARKDOWN**
## Para imagem utilizamos a descrição abaixo
![Link an image.](/Animais-_4_.gif)
Linkd para um site
[Link to Microsoft Learn](/learn)
## Listas
1. First
2. Second
3. Third
## Listas não numeradas; Aqui está o markdown de uma lista não ordenada. Fazendo listas
Você pode definir listas ordenadas ou não ordenadas. Você também pode definir itens aninhados por meio de recuos.

As listas ordenadas começam com números.
As listas não ordenadas podem usar asteriscos ou traços (-).
- First
  - Nested
- Second
- Third
## Criando tabelas; Você pode construir tabelas usando uma combinação de barras verticais (|) para quebras de coluna e traços (-) para designar a linha anterior como um cabeçalho.
First|Second
-|-
1|2
3|4

## Texto de referência
Você pode criar blockquotes usando o caractere maior que (>).
> This is quoted text.

## Preenchendo lacunas com HTML embutido
Se você se deparar com um cenário de HTML que não tem suporte em Markdown, basta usar o HTML embutido.
Here is a<br />line break

## Trabalhando com código
O Markdown fornece um comportamento padrão para trabalhar com blocos de código embutidos delimitados pelo caractere de crase (`). Ao decorar o texto com esse caractere, ele é renderizado como código.
This is `code`.

Se tiver um segmento de código que abrange várias linhas, você poderá usar três crases (```) antes e depois para criar um bloco de código isolado.

```
var first = 1;
var second = 2;
var sum = first + second;
```

## O GFM estende esse suporte com realce de sintaxe para linguagens populares. Basta especificar a linguagem como parte da primeira sequência de crases.

```javascript
var first = 1;
var second = 2;
var sum = first + second;
```

## Vinculação cruzada de problemas e solicitações de pull
O GFM dá suporte a uma variedade de formatos de código curto para facilitar a vinculação a problemas e solicitações de pull. A maneira mais fácil de fazer isso é usar o formato #ID, como #3602. O GitHub ajustará automaticamente os links mais longos para esse formato se você colá-los. Você também poderá seguir convenções adicionais, por exemplo, se estiver trabalhando com outras ferramentas ou se quiser especificar outros projetos/branches.

## Vinculação de confirmações específicas
Você pode fazer a vinculação a uma confirmação colando a respectiva ID ou simplesmente usando o respectivo SHA (Secure Hash Algorithm).

SHA	8304e9c271a5e5ab4fda797304cd7bcca7158c87

## Mencionando usuários e equipes
Digitar um símbolo de @, seguido por um nome de usuário do GitHub, enviará uma notificação para essa pessoa sobre o comentário. Isso é chamado de uma "@menção", porque você está mencionando o indivíduo. Você também pode usar @mention com equipes dentro de uma organização.
@githubteacher

## Acompanhar listas de tarefas
Você pode criar listas de tarefas dentro de problemas ou solicitações de pull usando a sintaxe ilustrada abaixo. Isso pode ser útil para acompanhar o progresso quando usado no corpo de um problema ou solicitação de pull.

- [x] First task
- [x] Second task
- [ ] Third task