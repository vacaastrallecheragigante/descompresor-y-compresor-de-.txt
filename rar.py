
import heapq
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox
import json  # Para manejar los códigos de Huffman

# Clase para el nodo del árbol de Huffman
class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Función para construir el árbol de Huffman
def construir_arbol_huffman(frecuencia):
    heap = [Nodo(caracter, freq) for caracter, freq in frecuencia.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        fusionado = Nodo(None, izquierda.frecuencia + derecha.frecuencia)
        fusionado.izquierda = izquierda
        fusionado.derecha = derecha
        heapq.heappush(heap, fusionado)

    return heap[0]

# Función para crear los códigos de Huffman
def crear_codigos(nodo, codigo_actual, codigos):
    if nodo is None:
        return

    if nodo.caracter is not None:
        codigos[nodo.caracter] = codigo_actual
        return

    crear_codigos(nodo.izquierda, codigo_actual + "0", codigos)
    crear_codigos(nodo.derecha, codigo_actual + "1", codigos)

# Función principal para comprimir el texto usando Huffman
def comprimir_huffman(texto):
    frecuencia = defaultdict(int)
    for caracter in texto:
        frecuencia[caracter] += 1

    arbol_huffman = construir_arbol_huffman(frecuencia)
    codigos = {}
    crear_codigos(arbol_huffman, "", codigos)

    texto_comprimido = ''.join([codigos[caracter] for caracter in texto])
    return codigos, texto_comprimido

# Función para descomprimir el texto usando Huffman
def descomprimir_huffman(texto_comprimido, codigos):
    codigos_invertidos = {v: k for k, v in codigos.items()}
    codigo_actual = ""
    texto_descomprimido = ""

    for bit in texto_comprimido:
        codigo_actual += bit
        if codigo_actual in codigos_invertidos:
            texto_descomprimido += codigos_invertidos[codigo_actual]
            codigo_actual = ""

    return texto_descomprimido

# Función para convertir una cadena de bits en bytes
def bits_a_bytes(bits):
    arreglo_bytes = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        arreglo_bytes.append(int(byte, 2))  # Convierte cada bloque de 8 bits en un byte
    return bytes(arreglo_bytes)

# Función para leer un archivo binario y convertirlo a bits
def bytes_a_bits(datos_bytes):
    bits = ''.join(f"{byte:08b}" for byte in datos_bytes)  # Convierte cada byte a 8 bits
    return bits

# Función para cargar el archivo
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            return ruta_archivo, contenido
        except UnicodeDecodeError:
            messagebox.showerror("Error", "No se pudo leer el archivo. Prueba con un archivo codificado en UTF-8.")
            return None, None
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")
        return None, None

# Función para guardar el archivo de texto
def guardar_archivo(contenido, nombre_archivo):
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")], initialfile=nombre_archivo)
    if ruta_archivo:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Éxito", "Archivo guardado correctamente")

# Función para guardar un archivo binario
def guardar_archivo_binario(contenido, nombre_archivo):
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivos binarios", "*.bin")], initialfile=nombre_archivo)
    if ruta_archivo:
        with open(ruta_archivo, "wb") as archivo_binario:
            archivo_binario.write(contenido)
        messagebox.showinfo("Éxito", "Archivo binario guardado correctamente")

# Función para comprimir archivo e incluir el diccionario en el archivo binario
def comprimir_archivo():
    ruta_archivo, contenido = abrir_archivo()
    if contenido:
        codigos, texto_comprimido = comprimir_huffman(contenido)
        bits_comprimidos = bits_a_bytes(texto_comprimido)

        # Convertir el diccionario de Huffman a JSON
        codigos_json = json.dumps(codigos)

        # Agregar una secuencia especial de separación entre el diccionario y los bits comprimidos
        separador = "___"
        datos_binarios = codigos_json.encode('utf-8') + separador.encode('utf-8') + bits_comprimidos

        # Guardar todo en un archivo binario
        ruta_archivo_comprimido = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Archivos binarios", "*.bin")], initialfile="comprimido")
        if ruta_archivo_comprimido:
            with open(ruta_archivo_comprimido, "wb") as archivo_binario:
                archivo_binario.write(datos_binarios)

        messagebox.showinfo("Éxito", "Archivo comprimido correctamente")

# Función para descomprimir archivo con diccionario incluido
def descomprimir_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo comprimido", filetypes=[("Archivos binarios", "*.bin")])
    if ruta_archivo:
        try:
            with open(ruta_archivo, "rb") as archivo_binario:
                datos_binarios = archivo_binario.read()

            # Buscar el separador que indica el final del diccionario
            separador = "___".encode('utf-8')
            indice_separador = datos_binarios.find(separador)

            if indice_separador == -1:
                messagebox.showerror("Error", "No se encontró el separador de diccionario en el archivo.")
                return

            # Extraer el diccionario de Huffman (en JSON) y los bits comprimidos
            codigos_json = datos_binarios[:indice_separador].decode('utf-8')
            bits_comprimidos = datos_binarios[indice_separador + len(separador):]

            # Convertir el diccionario desde JSON
            codigos = json.loads(codigos_json)

            # Convertir los bytes comprimidos a la secuencia de bits
            texto_comprimido = bytes_a_bits(bits_comprimidos)

            # Descomprimir el texto
            texto_descomprimido = descomprimir_huffman(texto_comprimido, codigos)
            guardar_archivo(texto_descomprimido, "descomprimido.txt")
            messagebox.showinfo("Éxito", "Archivo descomprimido correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al descomprimir el archivo: {str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compresor y Descompresor de Huffman")
ventana.geometry("400x200")

# Etiquetas y botones
etiqueta = tk.Label(ventana, text="Seleccione una opción:")
etiqueta.pack(pady=10)

boton_comprimir = tk.Button(ventana, text="Comprimir Archivo", command=comprimir_archivo)
boton_comprimir.pack(pady=5)

boton_descomprimir = tk.Button(ventana, text="Descomprimir Archivo", command=descomprimir_archivo)
boton_descomprimir.pack(pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop()
