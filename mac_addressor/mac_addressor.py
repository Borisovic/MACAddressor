from sys import platform
import os
from getmac import get_mac_address

class MACAddressor:
  def __init__(self):
    self.__old_mac_address = self.__get_mac_address()
    self.__os = self.__get_os()
  
  # Helper methods (maybe transfer to helper class later on if it gets too big?)
  @staticmethod
  def __get_os():
    if platform == "linux" or platform == "linux2":
      return "linux"
    elif platform == "darwin":
      return "mac"
    elif platform == "win32":
      return "windows"
  
  @staticmethod
  def __get_mac_address():
    return get_mac_address()
  
  def run(self):
    # Clear console
    if self.__os == "windows":
      os.system("cls")
    else:
      os.system("clear")
      
    self.__prompt()
    
  def __prompt(self):
    print("Please choose an option: \n1. Assign a random MAC address \n2. Enter my own MAC address")
    option = input()
    if option == 1:
      print("Option 1")
    elif option == 2:
      print("Option 2")
    else:
      print("Please select 1 or 2")
      
      self.run()
    pass
    # Prompt user if to assign random mac address or let them enter their own
    
  def __assign_random_mac_address(self):
    new_mac_address = self.__generate_random_mac_address()
  
  def __generate_random_mac_address(self):
    pass
  
  def __prompt_for_new_address(self):
    pass
  
  def __verify_mac_address(self, new_mac_address):
    pass