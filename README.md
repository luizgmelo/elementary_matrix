## Matrix Operations (WARN: Portuguese Brazil)

**O que é o projeto?**

Um programa que deve simular uma matriz.

**Caracteristicas**
O programa tem que ser feito para manipular matrizes.

Ele precisa trocar uma linha por outra da matriz. (Permutar Duas Linhas) <br>
Ele precisa multiplicar uma linha por um determinado número não nulo. (Multiplicar Linha) <br>
Ele precisa multiplicar uma linha por um determinado número com o movimento fazendo uma soma. (Multiplicar com movimento) <br>

**Algoritmo**
1. Encontre a primeira coluna não nula (da esquerda para a direita). Esta coluna é chamada de coluna pivô.
2. Na coluna pivô identifique o primeiro elemento (de cima para baixo) não nulo. Este elemento é chamado de elemento pivô.
3. Se o elemento pivô não pertence à primeira linha então permute a linha que contenha o pivô pela primeira linha.
4. Multiplique a primeira linha pelo inverso do pivô, para obter na primeira linha da coluna do pivô o elemento 1.
5. Zerar os elementos da coluna do pivô.
6. Seja B a submatriz de A obtida retirando-se a primeira linha de A. Repita os passos 1 a 5 para a matriz B.

