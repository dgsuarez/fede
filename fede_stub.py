import os
import stat

def create_stub_dir():
  if not os.path.exists(stub_dir_path()):
    os.makedirs(stub_dir_path())

def stub_dir_path():
  return ".fede/stubs"

def stub_path(stub_name):
  return stub_dir_path() + "/" + stub_name

def stub_content(args):
  command = "fede exec " + " ".join(args)
  return """
  #! /bin/sh

  %s "$@"

  """ % (command,)

def create_stub(stub_name, args):
  create_stub_dir()
  with open(stub_path(stub_name), 'w') as f:
    f.write(stub_content(args))
  st = os.stat(stub_path(stub_name))
  os.chmod(stub_path(stub_name), st.st_mode | stat.S_IEXEC)

def fede_stub(args):
  create_stub(args[0], args[1:])
