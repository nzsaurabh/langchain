import os

def run_myscript():
  my_secret = os.environ['TEST_SECRET']
  print(my_secret)

