#!/bin/bash

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 no está instalado. Por favor, instálalo e intenta de nuevo."
    exit
fi

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "pip3 no está instalado. Por favor, instálalo e intenta de nuevo."
    exit
fi

# Crear un entorno virtual
echo "Creando un entorno virtual de Python..."
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate

# Instalar las dependencias de Python en el entorno virtual
echo "Instalando dependencias de Python..."
pip install -r requirements.txt

# Verificar si FFmpeg está instalado
if ! command -v ffmpeg &> /dev/null
then
    echo "FFmpeg no está instalado. Instalándolo..."
    sudo apt update
    sudo apt install ffmpeg -y
fi

echo "Instalación completada. Todo está listo."
echo "Para activar el entorno virtual, ejecuta 'source env/bin/activate'"
