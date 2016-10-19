# PARCIAL 1

****
Estudiante | Código
--- | --- | ---
Dylan Torres | 12103021 
****
##PASOS PREVIOS PARA DESARROLLAR EL PARCIAL
SE SIGUEN LOS SIGUIENTES PASOS CON SUS COMANDOS

**1)En root modificamos la iptables:**
```
Vi etc/sysconfig/iptables
```
Luego agregamos los puertos que necesitemos
```
Services iptables restart
```

**2)Modificamos el visudo:**

Añadimos 
```
Filesystem_user ALL = (ALL) ALL
```
Posteriormente añadimos:
```
User_Alias RESTUSERS = filesystem_user
Cmnd_Alias MANAGEUSERS = /usr/sbin/adduser, /usr/sbin/userdel, /usr/bin/passwd
RESTUSERS    ALL=NOPASSWD: MANAGEUSERS
```


##SEGUIMOS CON LOS SIGUIENTES PASOS
**1)Creo un user**
```
Adduser filesystem_user
Passwd file
```
**2)Creo un directorio y el ambiente**
```
cd ~/
$ mkdir ambientes
$ cd ambientes
$ virtualenv miambiente1
```
Lo activo:
```
cd ~/ambientes
. miambiente1/bin/activate
```
Instalo El Flask en el ambiente
```
Pip install Flask
```
**3)Clono el repositorio que necesito**
En este repositorio añadiremos los archivos que se manejen
```
mkdir los_repositorios
cd los_repositorios
git clone https://github.com/dylan9538/parcialUno.git
cd parcialUno

git config remote.origin.url "https://token@github.com/dylan9538/parcialUno.git"
```
En el campo token añado el token generado en github

**4)Creo un directorio para el ejercicio dentro del repositorio clonado**
```
$ cd ~/
$ mkdir -p ejercicios/ejercicio1
$ cd ejercicios/ejercicio1
```
**5)Creo el archivo files_commands.py que contiene el siguiente codigo **

![alt text](https://github.com/dylan9538/BodegaeSemaforo/blob/master/DiagramClassSemaforo.PNG "Diagrama de clases")
 
**6)Creo el archivo files.py que maneje los procesos de files_commands.py y que contenga las URIS. El siguiente es el código:**
 

Luego ejecuto el comando:
```
Python files.py
```
##Pantallazos Solución

![alt text](https://github.com/dylan9538/BodegaeSemaforo/blob/master/Prueba1.PNG "Prueba GET de /files")

##CUANDO QUIERA SUBIR ARCHIVOS

1)Creo el archivo si no existe.

2)Sigo los siguientes comandos:
Estos comandos los ejecuto donde se encuentra ubicado el archivo a cargar.

```
git add nombreArchivo
git commit -m "upload README file"
git push origin master
```

