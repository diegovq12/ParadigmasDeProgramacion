# Reporte git y Github
## Reporte creado por Diego Demian Quiros Vicencio para la materia Paradigmas de la programacion

Github es una plataforma de desarrollo colaborativo basado en Git. Git es un sistema de control de versiones que permite a los desarrolladores gestionar y realizar un seguimiento de cambios en el codigo fuente durante el desarrollo de software.

### Crear cuenta en GitHub

1. Accede a Github en github.com
2. Haz clic en "Sign up".
3. Crea tu cuenta ingresando los datos requeridos(nombre de usuario, correo electronico y contraseña).
4. Verifica tu correo electronico mediante el enlace que te enviara github.
5. Personaliza tu perfil añadiendo una descripcion y foto de perfil.

### Crear repositorio en GitHub

1. **Crear un repositorio nuevo**:
   - Haz clic en el símbolo `+` en la esquina superior derecha de cualquier página de GitHub.
   - Selecciona "New repository" (Nuevo repositorio) del menú desplegable.
2. **Nombre y descripción**:
   - Ingresa un nombre para tu repositorio. Por ejemplo, "mi-proyecto".
   - Opcionalmente, añade una descripción corta del proyecto.
3. **Visibilidad**:
   - Elige si quieres que el repositorio sea público o privado.
   - Los repositorios públicos son visibles para todos. Los privados solo pueden ser vistos y colaborados por ti y los colaboradores que invites.
4. **Opciones adicionales**:
   - Puedes añadir un archivo README, que es una buena práctica para describir tu proyecto.
   - Puedes añadir un archivo de gitignore (ignorar archivos específicos, como los generados automáticamente) y una licencia de código abierto.
5. **Crear el repositorio**:
   - Haz clic en "Create repository" (Crear repositorio).


## Comandos basicos en git
### Iniciar sesion en git
```bash
git config --global user.name "Nombre de usuario"

git congig --global user.email "correo@correo.com"
```
### Clonar repositorio
```bash
git clone <url_repositorio>
```
### Agregar archivo
```bash
git add nombre_del_archivo
```

### Confirmar cambios
```bash
git commit -m "Descripcion del cambio"
```
### Subir cambios al repositorio
```bash
git git push origin <nombre_de_la_rama>
```

### Actualizar repositorio local
```bash
git pull origin <nombre_de_la_rama>
```

## Comandos utiles en terminal git

### Crear directorio
```bash
mkdir <nombre_del_directorio>
```

### Crear archivo
```bash
touch <nombre_del_archivo>
```
### Crear directorio
```bash
mkdir <nombre_del_directorio>
```

### Cambiar directorio
```bash
cd <nombre_del_directorio>
```

### Regresar un directorio arriba
```bash
cd ..
```
### Mostrar directorio actual
```bash
pwd
```

### Listar archivos en el directorio actual
```bash
ls
```

### Eliminar un archivo
```bash
rm <nombre_del_archivo>
```

### Eliminar un directorio y su contenido
```bash
rm -r <nombre_del_directorio>
```

### Copiar un archivo
```bash
cp <archivo_origen> <archivo_destino>
```

### Mover o renombrar un archivo o directorio
```bash
mv <archivo_origen> <archivo_destino>
```

## Conclusión

Dominar el uso de Git y GitHub, junto con comandos esenciales de la terminal, es fundamental para cualquier desarrollador de software. Git proporciona un control de versiones robusto y flexible, permitiendo a los desarrolladores rastrear y gestionar cambios en el código de manera eficiente. GitHub, como plataforma de colaboración basada en Git, facilita el trabajo en equipo y el manejo de proyectos abiertos o privados.

Los comandos de Git permiten configurar el entorno de trabajo, inicializar y clonar repositorios, gestionar archivos y ramas, y sincronizar cambios con repositorios remotos. Por otro lado, los comandos generales de terminal ayudan en la navegación del sistema de archivos, gestión de directorios y archivos, y obtención de información del sistema, lo cual es crucial para la administración efectiva del entorno de desarrollo.

Con una buena comprensión y práctica de estos comandos, los desarrolladores pueden mejorar su flujo de trabajo, colaborar más efectivamente y mantener un control preciso sobre el desarrollo de sus proyectos. Este conocimiento no solo incrementa la productividad individual, sino que también contribuye significativamente al éxito de los proyectos de equipo y la calidad del software producido.
