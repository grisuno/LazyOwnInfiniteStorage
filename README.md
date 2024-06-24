```sh
 ▄█          ▄████████  ▄███████▄  ▄██   ▄    ▄██████▄   ▄█     █▄  ███▄▄▄▄             
███         ███    ███ ██▀     ▄██ ███   ██▄ ███    ███ ███     ███ ███▀▀▀██▄           
███         ███    ███       ▄███▀ ███▄▄▄███ ███    ███ ███     ███ ███   ███           
███         ███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███ ███    ███ ███     ███ ███   ███           
███       ▀███████████   ▄███▀   ▀ ▄██   ███ ███    ███ ███     ███ ███   ███           
███         ███    ███ ▄███▀       ███   ███ ███    ███ ███     ███ ███   ███           
███▌    ▄   ███    ███ ███▄     ▄█ ███   ███ ███    ███ ███ ▄█▄ ███ ███   ███           
█████▄▄██   ███    █▀   ▀████████▀  ▀█████▀   ▀██████▀   ▀███▀███▀   ▀█   █▀            
▀                                                                                       
 ▄█  ███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄    ▄█      ███        ▄████████                
███  ███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄ ███  ▀█████████▄   ███    ███                
███▌ ███   ███   ███    █▀  ███▌ ███   ███ ███▌    ▀███▀▀██   ███    █▀                 
███▌ ███   ███  ▄███▄▄▄     ███▌ ███   ███ ███▌     ███   ▀  ▄███▄▄▄                    
███▌ ███   ███ ▀▀███▀▀▀     ███▌ ███   ███ ███▌     ███     ▀▀███▀▀▀                    
███  ███   ███   ███        ███  ███   ███ ███      ███       ███    █▄                 
███  ███   ███   ███        ███  ███   ███ ███      ███       ███    ███                
█▀    ▀█   █▀    ███        █▀    ▀█   █▀  █▀      ▄████▀     ██████████                
                                                                                        
   ▄████████     ███      ▄██████▄     ▄████████    ▄████████    ▄██████▄     ▄████████ 
  ███    ███ ▀█████████▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀     ▀███▀▀██ ███    ███   ███    ███   ███    ███   ███    █▀    ███    █▀  
  ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀   ███    ███  ▄███         ▄███▄▄▄     
▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███ ████▄  ▀▀███▀▀▀     
         ███     ███     ███    ███ ▀███████████   ███    ███   ███    ███   ███    █▄  
   ▄█    ███     ███     ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
 ▄████████▀     ▄████▀    ▀██████▀    ███    ███   ███    █▀    ████████▀    ██████████ 
                                      ███    ███                                        
```

# LazyOwnInfiniteStorage

![License](https://img.shields.io/github/license/grisuno/LazyOwn?style=flat-square)



LazyOwnInfiniteStorage es una herramienta para codificar y decodificar archivos en videos. Este proyecto permite almacenar datos en videos mediante la creación de frames que representan bits de datos, lo que facilita la recuperación de la información original incluso después de que el video haya sido modificado (por ejemplo, cambiando su resolución).

quedando un video como esto:

![image](https://github.com/grisuno/LazyOwnInfiniteStorage/assets/1097185/39044629-7e0c-4806-806a-9bbc5a847d88)


## Características

- Codificación de archivos en videos utilizando bloques de píxeles.
- Decodificación de archivos a partir de videos, incluso si se ha cambiado la resolución del video.
- Uso de nombres de archivos para almacenar información sobre la resolución original.

## Requisitos

- Python 3.6+
- OpenCV
- FFmpeg

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/grisuno/LazyOwnInfiniteStorage.git
    cd LazyOwnInfiniteStorage
    ```

2. Instala las dependencias:

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

## Uso

### Codificación

Para codificar un archivo en un video:

```sh
python lazyown_infinitestorage.py --mode encode --input archivo.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4
```

### Decodificación
Para decodificar un archivo a partir de un video:

```sh
python lazyown_infinitestorage.py --mode decode --input video_640x480.mp4 --output recoveredfile.zip --block_size 4
```

# Using the GUI

![image](https://github.com/grisuno/LazyOwnInfiniteStorage/assets/1097185/2e9085ce-0a4f-42b9-bc08-d13e44deb777)


## Mode Selection:

```sh
python gui
```

### Selección de Modo:

Elige entre los modos Codificar y Decodificar usando el menú desplegable.
Modo Codificar:

Seleccionar Archivo ZIP: Haz clic en Buscar para elegir el archivo ZIP que deseas codificar.
Nombre del Video: Ingresa el nombre deseado para el archivo de video de salida.
Tamaño del Marco: Ajusta el ancho y alto de los marcos (en píxeles).
Tamaño del Bloque: Define el tamaño de los bloques utilizados para la codificación (en píxeles).
Frames por Segundo: Especifica la velocidad de cuadros para el video de salida.
Haz clic en Iniciar para comenzar el proceso de codificación.
Modo Decodificar:

- Seleccionar Archivo de Video: Haz clic en Buscar para elegir el archivo de video que deseas decodificar.
- Nombre del Archivo ZIP Recuperado: Ingresa el nombre para el archivo ZIP recuperado.
- Tamaño del Bloque: Define el tamaño de los bloques utilizados para la decodificación (debe coincidir con el tamaño de bloque utilizado durante la codificación).
- Haz clic en Iniciar para comenzar el proceso de decodificación.


#### Mensajes:

Al finalizar o en caso de error, aparecerá una ventana de mensaje indicando el estado del proceso.

# Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o un pull request.

# Agradecimientos
Este proyecto está inspirado en el trabajo de DvorakDwarf en Infinite-Storage-Glitch. Agradezco cualquier crítica del código para poder mejorar.

Haz lo que quieras con el código, pero se agradecería el crédito. Si tienes algún problema con LazyOwnInfiniteStorage, por favor contáctame en Discord.

## Creado por grisuno
