from subprocess import Popen, PIPE

def get_all_files():
  grep_process = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE)
  file_list = Popen(["awk","-F","/",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

def add_file(filename,content):
  add_process = Popen(["sudo","adduser","--password",password,filename], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if username in get_all_files() else False

def remove_file(filename):
  vip = ["operativos","jenkins","postgres","root"]
  if filename in vip:
    return True
  else:
    remove_process = Popen(["sudo","userdel","-r",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if filename in get_all_files() else True
