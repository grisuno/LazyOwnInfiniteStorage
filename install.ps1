# Verificar si Python está instalado
if (-not (Get-Command python3 -ErrorAction SilentlyContinue)) {
    Write-Host "Python3 no está instalado. Por favor, instálalo e intenta de nuevo."
    exit 1
}

# Verificar si pip está instalado
if (-not (Get-Command pip3 -ErrorAction SilentlyContinue)) {
    Write-Host "pip3 no está instalado. Por favor, instálalo e intenta de nuevo."
    exit 1
}

# Crear un entorno virtual
Write-Host "Creando un entorno virtual de Python..."
python3 -m venv env

# Activar el entorno virtual
Write-Host "Activando el entorno virtual..."
& .\env\Scripts\Activate.ps1

# Instalar las dependencias de Python en el entorno virtual
Write-Host "Instalando dependencias de Python..."
pip install -r requirements.txt

# Verificar si FFmpeg está instalado
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Host "FFmpeg no está instalado. Instalándolo..."
    # Descargar FFmpeg para Windows
    $ffmpegZip = "ffmpeg-release-essentials.zip"
    Invoke-WebRequest -Uri https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -OutFile $ffmpegZip
    # Extraer FFmpeg
    Expand-Archive -Path $ffmpegZip -DestinationPath .\ffmpeg -Force
    # Mover FFmpeg a una ubicación permanente
    Move-Item -Path .\ffmpeg\ffmpeg-* -Destination .\ffmpeg\ffmpeg -Force
    # Añadir FFmpeg al PATH
    $env:Path += ";$(Resolve-Path .\ffmpeg\ffmpeg\bin)"
    [System.Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User)
    Write-Host "FFmpeg ha sido instalado y añadido al PATH."
}

Write-Host "Instalación completada. Todo está listo."
Write-Host "Para activar el entorno virtual, ejecuta '.\env\Scripts\Activate.ps1'"
