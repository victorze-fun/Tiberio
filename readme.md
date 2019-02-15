# Tiberio

## Requerimientos
- Python 3.5 o superior

## Instalación
```bash
git clone git@github.com:victorze-fun/Tiberio.git
cd Tiberio
virtualenv venv -p python (opcional)
pip install -r requirements.txt
python tiberio/main.py (previamente se debe activar el entorno virtual)
```

## Flujo de trabajo para crear formularios
* Abrir Qt Designer `venv\Lib\site-packages\PySide2\designer.exe`
* Crear un formulario con Qt Designer.
* Guardar el formulario Ej. myform.ui.
* Convertir el formulario en un archivo python: `pyside2-uic myform.ui > ui_myform.py`

