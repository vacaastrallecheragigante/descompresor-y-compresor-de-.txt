# Compresor y Descompresor de Archivos con Algoritmo de Huffman

Este proyecto implementa una aplicación para la compresión y descompresión de archivos de texto utilizando el algoritmo de Huffman, uno de los métodos más eficientes para reducir el tamaño de los datos sin pérdida de información. El programa incluye una interfaz gráfica (GUI) simple y fácil de usar, creada con Tkinter, para que cualquier usuario pueda comprimir o descomprimir archivos rápidamente.

## Características principales:

- **Compresión de archivos**: Toma un archivo de texto y lo convierte en un archivo comprimido binario.
- **Descompresión de archivos**: Convierte el archivo comprimido de vuelta a su estado original en texto.
- **Diccionario embebido**: El archivo binario comprimido contiene el diccionario de Huffman necesario para la descompresión.
- **Interfaz gráfica**: Los usuarios pueden seleccionar archivos fácilmente a través de una GUI amigable.

## ¿Cómo funciona?

### Algoritmo de Huffman:

1. Se analiza la frecuencia de los caracteres del archivo de texto.
2. Se genera un árbol binario donde los caracteres más frecuentes tienen códigos de menor longitud.
3. Cada carácter del archivo se reemplaza por su secuencia de bits única, reduciendo el tamaño total.

### Proceso de compresión:

1. El archivo de texto se convierte en una secuencia de bits comprimida.
2. Se guarda junto con el diccionario que mapea los caracteres a sus códigos binarios.

### Proceso de descompresión:

1. La secuencia de bits comprimida se interpreta usando el diccionario de Huffman.
2. El archivo original se restaura completamente a su formato de texto sin pérdida de datos.

## Uso:

- **Compresión**: Elige un archivo `.txt` para comprimir, y guarda el archivo comprimido en formato `.bin`.
- **Descompresión**: Selecciona un archivo `.bin` generado por el programa, y descomprime el contenido en un archivo de texto.

## Beneficios:

- **Reducción del tamaño de archivos**: Útil para almacenar y transferir archivos de texto más pequeños.
- **Fácil de usar**: No es necesario tener conocimientos de programación para usar la interfaz gráfica.




# Transformación a Bits y Almacenamiento en Archivos Binarios

El proceso de compresión mediante el algoritmo de Huffman convierte el texto en una secuencia de unos (1) y ceros (0), lo que refleja la representación binaria de los caracteres. Esta transformación es clave para maximizar la eficiencia de la compresión.

## Motivos Técnicos de la Transformación a Bits

### Eficiencia de Almacenamiento
Los datos en la memoria del computador se representan en formato binario, es decir, en una secuencia de bits (0s y 1s). El algoritmo de Huffman genera códigos binarios (de longitud variable) para cada carácter en función de su frecuencia, donde los caracteres más frecuentes tienen representaciones más cortas (menos bits) y los menos frecuentes, más largas.  
Al transformar el texto a secuencias de bits, reducimos el tamaño total de la representación del archivo.

### Compresión Basada en Frecuencia
Cada carácter se asigna a una secuencia única de bits que varía en longitud, lo que permite que los caracteres más comunes tengan una representación más compacta, y los menos comunes utilicen más bits. Esta conversión a bits permite realizar la codificación óptima de los datos antes de almacenarlos.

## ¿Por Qué se Pasa a un Archivo Binario?
Una vez que el texto original ha sido transformado en su representación binaria comprimida (como una secuencia de bits), esta información debe ser guardada de manera eficiente para su almacenamiento o transmisión. Aquí es donde entra en juego el archivo binario.

### Eficiencia de Almacenamiento
Un archivo binario es la representación más eficiente para almacenar datos en disco, ya que en este formato los datos se guardan directamente en su forma de bits. Si se intentara almacenar una secuencia de bits como texto, se incrementaría el tamaño del archivo debido a las limitaciones del formato textual, como los delimitadores o caracteres adicionales.  
Al escribir directamente en un archivo binario, cada conjunto de 8 bits (un byte) se almacena en su formato nativo, lo que minimiza el tamaño del archivo final.

### Compatibilidad y Recuperación de Datos
Los archivos binarios permiten una recuperación precisa de los datos comprimidos sin necesidad de codificaciones adicionales. Esto es crucial para el algoritmo de Huffman, ya que para descomprimir el archivo, se necesita recuperar exactamente la secuencia de bits original para poder reconstruir el texto.  
Además, el formato binario facilita la manipulación de datos a nivel de byte, lo que es ideal para el manejo de secuencias de bits generadas por el algoritmo de compresión.

### Velocidad de Procesamiento
Al guardar los datos comprimidos en formato binario, se mejora la velocidad de escritura y lectura del archivo, ya que se evitan las conversiones innecesarias entre formatos de texto y binario durante las operaciones de almacenamiento y recuperación.

### Como usar el compresor 
al descargar el compresor que es un archivo.py puede crear un acceso directo en el escritorio, ahi puede abrir con doble click se le presentara una interefaz grafica simple y facil de manipular 
ahi se presentan dos opciones las cuales son comprimir y descompromir
##comprimir 
darle click al boton de comprirmir archivo ahi puedes decidir que archivo .txt deseas comprimir 
##descomprimir 
darle click al boton de descomprimir achivo elegir el .bin para comvertirlo en un archivo entendible que seria un .txt




