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
Luego agregamos los puertos que necesitemos.

Luego ejecutamos el siguiente comando:
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
En este repositorio añadiremos los archivos que se manejen.
```
mkdir los_repositorios
cd los_repositorios
git clone https://github.com/dylan9538/parcialUno.git
cd parcialUno

git config remote.origin.url "https://token@github.com/dylan9538/parcialUno.git"
```
En el campo token añado el token generado en github.

**4)Creo un directorio para el ejercicio dentro del repositorio clonado**
```
$ cd ~/
$ mkdir -p ejercicios/ejercicio1
$ cd ejercicios/ejercicio1
```
**5)Creo el archivo files_commands.py que contiene el siguiente código**
```
from subprocess import Popen, PIPE

def get_all_files():
  grep_process = Popen(["ls"], stdout=PIPE, stderr=PIPE)
  file_list = Popen(["awk","-F","/",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

def add_file(filename,content):
  add_process = Open(filename+'.txt','a')
  add_process.write(content+'/n')
  add_process.close()
  return "Se creo el archivo" , 201

def remove_file(filename):
  vip = ["ambientes","los_repositorios","files","files_commands"]
  if filename in vip:
    return True
  else:
    remove_process = Popen(["rm","-r",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if filename in get_all_files() else True
 ```
**6)Creo el archivo files.py que maneje los procesos de files_commands.py y que contenga las URIS. El siguiente es el código:**
```
from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file

app = Flask(__name__)

api_url = '/recently_created'

@app.route('/files',methods=['POST'])
def create_file():
  content = request.get_json(silent=True)
  filename = content['filename']
  content =  content['content']
  add_file(filename,content)  
  return "Se creo",201
  

@app.route('/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route('/files',methods=['PUT'])
def update_file():
  return "not found", 404

@app.route('/files',methods=['DELETE'])
def delete_file():
  error = False
  for username in get_all_files():
    if not remove_file(filename):
        error = True

  if error:
    return 'some files were not deleted', 400
  else:
    return 'all files  were deleted', 200  	 

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```

Luego ejecuto el comando:
```
Python files.py
```
##PANTALLAZOS SOLUCIÓN

**Prueba GET FILES**
![alt text](https://github.com/dylan9538/parcialUno/blob/master/GET%20FILES.PNG "Prueba GET de /files")

**Prueba CREATE FILES**
![alt text](https://github.com/dylan9538/parcialUno/blob/master/CREATE_FILE.PNG "Prueba GET de /files")

**Prueba DELETE FILES**
![alt text](https://github.com/dylan9538/parcialUno/blob/master/DELETE_FILE.png "Prueba GET de /files")

**Prueba UPDATE FILES**
![alt text](https://github.com/dylan9538/parcialUno/blob/master/UPDATE_FILE.PNG "Prueba GET de /files")

##CUANDO QUIERA SUBIR ARCHIVOS AL GITHUB REPOSITORIO

1)Creo el archivo si no existe.

2)Sigo los siguientes comandos:
Estos comandos los ejecuto donde se encuentra ubicado el archivo a cargar.

```
git add nombreArchivo
git commit -m "upload README file"
git push origin master
```


