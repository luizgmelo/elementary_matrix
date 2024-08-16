## Row Reduced Echelon Form (WARN: Portuguese Brazil)

Forma da Matriz escada reduzida por linha.

**O que é o projeto?**
Um programa que transforma uma matriz para forma reduzida por linha feito em python.

**Como usar o projeto no seu computador?**

Em um terminal com o Git instalado faça:

```git clone https://github.com/luizgmelo/elementary_matrix.git```

Para rodar o projeto utilize o comando:

```python main.py```

Exemplo de uso:

![Screenshot from 2024-08-16 10-42-02](https://github.com/user-attachments/assets/42afd47b-98fa-4b9d-89c3-49d53ce00c9e)


**Requisitos para bom entendimento do código/projeto**

- Conhecimento de Python
- Saber transformar a matriz para forma escada reduzida por linha no papel.

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
5. Zerar os elementos da coluna do pivô que estão abaixo dele.
6. Zerar os elementos da coluna dos pivô que estão acima dele.
