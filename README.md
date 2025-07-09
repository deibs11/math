# Proyecto Matemáticas II

Este repositorio contiene un proyecto de análisis y visualización matemática utilizando Python. Incluye visualización gráfica, interfaces básicas y manejo de datos con bibliotecas populares.

---

## Requisitos

El proyecto requiere tener instalados los siguientes componentes:

- Python (versión 3.8 o superior)
- matplotlib
- tkinter
- pandas

---

##  Instalación

### Windows

1. **Instalar Python**  
   Descargar el instalador oficial de Python:  
   👉 https://www.python.org/downloads/windows/

   Durante la instalación:
   - Asegúrate de marcar la opción **"Add Python to PATH"**
   - Selecciona **Instalación personalizada**, y asegúrate de que `tkinter` esté habilitado (viene por defecto)

2. **Verificar instalación**
   ```powershell
   python --version
   pip --version

   
3. **Instalar dependencias**
 ```bash
   pip install matplotlib pandas
```
--- 


###  macOS

#### 1. Instalar Python

**Opción A – Usando Homebrew**

```bash
brew install python

```

**Opción B - Desde la web de Python**
 👉   https://www.python.org/downloads/mac-osx/


 #### Verificar instalacion
```
 python3 --version
 pip3 --version
```


**Instalar Tkinter si no estaba incluido:**
```bash
brew install tcl-tk
echo 'export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"' >> ~/.zshrc
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
source ~/.zshrc
```
## Abrir en VS Code  y ejecutar en el archivo `main.py` .

**NOTA: Para ver otra grafica, esta nueva no se abrirá hasta que la anterior grafica se cierre. Así mismo, al cambiar de método, ingresar datos nuevamente `NO USAR` los datos ingresados previamente.**
