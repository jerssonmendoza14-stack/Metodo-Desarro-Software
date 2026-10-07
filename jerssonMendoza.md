## Comandos

### 1. Crear una rama local con su nombre
- 1. Ejecuto el comando 'git branch' para ver en que rama estoy parado actualmente.
- 2. Ejecuto el comando 'git branch jmendoza' para crear una nueva rama con mi nombre.
- 3. Vuelvo y ejecuto el comando 'git branch' para validar que estén las dos ramas creadas.
- 4. Ejecuto el comando 'git checkout jmendoza' para pasarme a la nueva rama que e creado.
- 5. Ejecuto el comando 'git branch' para validar que estoy en la rama jmendoza, ya con esto puedo realizar cualquier cambio y trabajar sobre la rama sin afectar el main principal.

### 2. Crear un nuevo commit en dicha rama local
- 1. Creo cualquier archivo o hago cualquier cambio, porque ya estoy tranquilo de que estoy trabajando sobre la rama jmendoza.
- 2. Ejecuto el comando 'git status' para que me muestre que cambios hay en el archivo o el repositorio desde que creé la nueva rama.
- 3. Ejecuto el comando 'git add .' para que me adjunte los cambios que se han realizado.
- 4. Luego ejecuto el comando 'git commit -m 'tercer commit'' para hacer el commit en la rama local.
- 5. Luego para validar los commits que he realizado, ejecuto el comando 'git log' esto me muestra los commits que e ejecutado.

### Subir su rama local al repositorio
- 1. Para subir la rama local al repositorio debo ejecutar el comando 'git push origin jmendoza'.
- 2. Ya con esto me voy al GitHub remoto, actualizo la página y ya podré ver las dos ramas creadas.

- Esta ultima la agrego desde mi rama jmendoza para diferenciarla de la rama main y que se vea la diferencia.