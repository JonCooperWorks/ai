import subprocess

def run():
  subprocess.call(['python', 'app.py'])
  run()

run()
