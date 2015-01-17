import sys
import os
import re
from distutils import spawn

def docker_path():
  return spawn.find_executable("docker")

def docker_ps():
  cmd = docker_path() + " ps"
  return os.popen(cmd).read().split("\n")[1:]

def detect_container(name):
  container_names = [l.split()[-1] for l in docker_ps() if len(l) > 0]
  matching_containers = [container for container in container_names if re.search(name, container)]
  container_count = len(matching_containers)
  if container_count == 0:
    sys.stderr.write("No container matching " + name + "\n")
    sys.exit(1)
  elif container_count > 1:
    sys.stderr.write(str(container_count) + " matching containers found, running on " + matching_containers[0] + "\n")
  return matching_containers[0]

def docker_execv_params(container_name, docker_opts, exec_params):
  params = ["docker", "exec", docker_opts, container_name] + exec_params
  return [x for x in params if x]

def fede_exec(args):
  if args[0].startswith("-"):
    container_idx = 1
    docker_opts = args[0]
  else:
    container_idx = 0
    docker_opts = None
  params_start = container_idx + 1
  container = detect_container(args[container_idx])
  params = docker_execv_params(container, docker_opts, args[params_start:])
  os.execv(docker_path(), params)

