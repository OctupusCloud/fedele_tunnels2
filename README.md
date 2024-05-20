# Fedele Tunnels Plugin
Este plugin es un fork de https://github.com/robertlynch3/netbox-tunnels2

## Creación del Fork
Para futuras actualizaciones del Plugin, si se desea realizar un nuevo fork, se debe realizar el siguiente procedimiento:

1. Hacer el Fork
2. Añadir remoto: 
  
  ```
  git remote add upstream [GitHub repo original]
  ```

3. Obtener tags: 
  ```
  git fetch upstream --tags
  ```

4. Ir a rama main:
  ```
  git checkout main
  ```

5. Reiniciar rama main con el tag a utilizar:

  ```
  git reset --hard tags/nombre-del-tag  
  ```

6. Pushear cambios:
  ```
  git push --force origin main
  ```

## Instalación

1. Cambiar netbox_tunnels2 por fedele_tunnels2 en ```__init__.py``` y en ```setup.py```

2. Cambiar nombre de carpeta de proyecto a ```fedele_tunnels2```

3. Cambiar nombre de carpeta ```/fedele_tunnels2/templates/netbox_tunnels2``` a ```/fedele_tunnels2/templates/fedele_tunnels2```

4. Con ```Ctrl + Shift + H``` reemplazar ```netbox_tunnels2``` por ```fedele_tunnels2``` en TODOS lados

5. Con ```Ctrl + Shift + H``` reemplazar ```netbox-tunnels2``` por ```fedele-tunnels2``` en TODOS lados

6. Activar entorno virtual: 
```
source /opt/o4n/O4N_FEDELE_SOURCE/venv/bin/activate
```

7. Instalar Extensión: 
  ```
  python setup.py develop
  ```

8. En ```configuration.py``` de Fedele agregar:
  ```
  PLUGINS = ["fedele_tunnels2"]
  ```

9. Eliminar todas las migraciones de la carpeta ```migrations```

10. Detectar migraciones:
  ```
  python manage.py makemigrations
  ```

11. Ejecutar migraciones:
  ```
  python manage.py migrate
  ```
