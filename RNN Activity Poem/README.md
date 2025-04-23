# Generador de Poemas con LSTM en Español

Este proyecto entrena una red neuronal recurrente (RNN) con arquitectura LSTM para generar poemas en español a partir de un corpus de Pablo Neruda. La red aprende la estructura y estilo del poeta, permitiendo generar nuevos versos a partir de una frase inicial.

##  Descripción del Proyecto

- **Tipo de red**: LSTM con dos capas y Dropout para evitar overfitting.
- **Corpus utilizado**: Conjunto de 363 poemas en español de Pablo Neruda.
- **Tokenización**: A nivel palabra.
- **Objetivo**: Dado un texto semilla, generar texto con coherencia poética en el estilo del corpus.
- **Control de creatividad**: Implementación de temperatura en la generación.

---

##  Requisitos y dependencias
Instala las siguientes bibliotecas antes de ejecutar el proyecto:

```bash
pip install numpy tensorflow
