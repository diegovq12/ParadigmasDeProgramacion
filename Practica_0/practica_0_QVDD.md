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
