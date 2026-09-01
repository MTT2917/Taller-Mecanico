# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

### 31 de Agosto de 2026
- **Creación de Subclases con Herencia:**
  - **`Auto` (`auto.py`):** Subclase que hereda de `Vehiculo`. Incluye constructor propio invocando `super().__init__()` y el atributo privado `__capacidad_maletero` (litros).
  - **`Camion` (`camion.py`):** Subclase que hereda de `Vehiculo`. Incluye constructor propio invocando `super().__init__()` y el atributo privado `__capacidad_carga` (kilos).
  - **`Moto` (`moto.py`):** Subclase que hereda de `Vehiculo`.
- **Actualización de `main.py`:** Incorporación de las importaciones de `Auto`, `Moto` y `Camion`.
- **Configuración de Proyecto:** Creación de `.gitignore` para excluir archivos de caché `__pycache__/` y `.pyc`.
- **Gestión de Versiones:** Creación y publicación de la rama de trabajo `feature/desarrollo`.
