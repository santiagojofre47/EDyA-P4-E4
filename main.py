from claseArbolHuffman import ArbolHuffman

if __name__ == '__main__':
    objAlgoritmo = ArbolHuffman()
    print('Arbol de huffman generado...')
    objAlgoritmo.preOrder(objAlgoritmo.getRaiz())