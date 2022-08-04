### Repositorio basic-blockchain

basic-blockchain es una actividad académica en la que se implementan  de manera poco realistas algunos aspectos fundamentales de la red Bitcoin como lo son: la costrucción del árbol de merkle para obtener el rootHash, la prueba de trabajo que para efectos académicos y bajo la ausencia de nodos mineros, se simula un minero elegido aleatoriamente de las wallets iniciales, y la construcción de los bloques.

basic-blockchain se construyó bajo las siguientes premisas:

- La red inicia con 50000000 unidades de la moneda para minar
- La recompensa por bloque minado es de 50 unidades
- Existen 5 wallets iniciales en 0
- Cada bloque almacena solo una transacción

Para la construcción de los bloques primero se realizan la cantidad de transacciones deseadas y luego se construyen los bloques.

El punto de ejecución es blockchain.py en donde se hace llamado a la función buildBlockchain con un parámetro  de dificltad establecido en 5.
Los módulos merkle.py y proof-of-work.py también pueden ser ejecutados individualmente para ser probados.