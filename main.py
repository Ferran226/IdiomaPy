import tkinter as tk
from tkinter import ttk
from langdetect import detect
from langdetect import DetectorFactory

# Configurar DetectorFactory para obtener resultados en nombres completos de idiomas
DetectorFactory.seed = 0

# Diccionario que mapea códigos de idioma a nombres completos de idiomas
nombres_idiomas = {
    'af': 'Afrikáans',
    'sq': 'Albanés',
    'am': 'Amárico',
    'ar': 'Árabe',
    'hy': 'Armenio',
    'az': 'Azerí',
    'eu': 'Euskera',
    'bn': 'Bengalí',
    'bs': 'Bosnio',
    'bg': 'Búlgaro',
    'ca': 'Catalán',
    'hr': 'Croata',
    'cs': 'Checo',
    'da': 'Danés',
    'nl': 'Holandés',
    'en': 'Inglés',
    'et': 'Estonio',
    'fi': 'Finlandés',
    'fr': 'Francés',
    'gl': 'Gallego',
    'de': 'Alemán',
    'el': 'Griego',
    'he': 'Hebreo',
    'hi': 'Hindi',
    'hu': 'Húngaro',
    'is': 'Islandés',
    'id': 'Indonesio',
    'ga': 'Irlandés',
    'it': 'Italiano',
    'ja': 'Japonés',
    'ko': 'Coreano',
    'lv': 'Letón',
    'lt': 'Lituano',
    'mk': 'Macedonio',
    'ms': 'Malayo',
    'mt': 'Maltés',
    'no': 'Noruego',
    'fa': 'Persa',
    'pl': 'Polaco',
    'pt': 'Portugués',
    'ro': 'Rumano',
    'ru': 'Ruso',
    'sr': 'Serbio',
    'sk': 'Eslovaco',
    'sl': 'Esloveno',
    'es': 'Español',
    'sw': 'Suajili',
    'sv': 'Sueco',
    'tl': 'Tagalo',
    'th': 'Tailandés',
    'tr': 'Turco',
    'uk': 'Ucraniano',
    'ur': 'Urdu',
    'vi': 'Vietnamita',
    'cy': 'Galés',
    'xh': 'Xhosa',
    'yi': 'Yidis',
    'zu': 'Zulú',
    # Puedes agregar más idiomas según sea necesario
}


def detectar_idioma():
    texto = entrada_texto.get()
    try:
        idioma_codigo = detect(texto)
        if idioma_codigo in nombres_idiomas:
            idioma_nombre = nombres_idiomas[idioma_codigo]
            resultado.set(f"El idioma es {idioma_nombre}")
        else:
            resultado.set("Idioma no reconocido")
    except Exception as e:
        # Capturar errores generales y mostrar un mensaje de error
        resultado.set("Error al detectar el idioma: " + str(e))

def limpiar():
    entrada_texto.delete(0, tk.END)
    resultado.set("")

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Detector de Idioma")
ventana.geometry("550x250")

# Crear un marco para organizar los elementos
marco = ttk.Frame(ventana)
marco.pack(padx=20, pady=20, fill="both", expand=True)

# Etiqueta de instrucción
instruccion = ttk.Label(marco, text="Ingrese un texto:")
instruccion.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada de texto
entrada_texto = ttk.Entry(marco, width=40)
entrada_texto.grid(row=0, column=1, padx=10, pady=10)

# Botón para detectar idioma
boton_detectar = ttk.Button(marco, text="Detectar Idioma", command=detectar_idioma)
boton_detectar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para limpiar
boton_limpiar = ttk.Button(marco, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()
etiqueta_resultado = ttk.Label(marco, textvariable=resultado)
etiqueta_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()



