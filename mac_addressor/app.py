from ast import Num
from sys import platform

class MACAddressor:
  def __init__(self):
    self.os = self.get_os()
  
  # Helper methods (maybe transfer to helper class later on if it gets too big?)
  @staticmethod
  def get_os():
    if platform == "linux" or platform == "linux2":
      return "linux"
    elif platform == "darwin":
      return "mac"
    elif platform == "win32":
      return "windows"
    