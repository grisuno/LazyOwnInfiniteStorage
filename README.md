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
    pip install -r requirements.txt
    ```

## Uso

### Codificación

Para codificar un archivo en un video:

```sh
python script.py --mode encode --input archivo.zip --output video.mp4 --frame_size 640 480 --fps 30 --block_size 4
```

### Decodificación
Para decodificar un archivo a partir de un video:

```sh
python script.py --mode decode --input video_640x480.mp4 --output recoveredfile.zip --block_size 4
```

# Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o un pull request.

# Agradecimientos
Este proyecto está inspirado en el trabajo de DvorakDwarf en Infinite-Storage-Glitch. Agradezco cualquier crítica del código para poder mejorar.

Haz lo que quieras con el código, pero se agradecería el crédito. Si tienes algún problema con LazyOwnInfiniteStorage, por favor contáctame en Discord.

## Creado por grisuno
