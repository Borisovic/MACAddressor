from sys import platform
import os
from getmac import get_mac_address
from random import randrange
import re
import subprocess
import string

class MACAddressor:
  def __init__(self):
    self.__old_mac_address = self.__get_mac_address()
    self.__os = self.__get_os()
    
    # Clear console
    if self.__os == "windows":
      os.system("cls")
    else:
      os.system("clear")
      
    print("Current MAC address: {}".format(self.__old_mac_address))
  
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
    self.__prompt()
    
  def __prompt(self):
    print("Please choose an option: \n1. Assign a random MAC address \n2. Enter my own MAC address")
    option = input()
    
    if option == "1":
      # Assign a random mac address  
      self.__assign_random_mac_address()
    elif option == "2":
      # Let user enter a mac address
      self.__prompt_for_new_address()
    else:
      print("Please select 1 or 2\n=============================")
      
      self.run()
    
  def __assign_random_mac_address(self):
    new_mac_address = self.__generate_random_mac_address()
    
    print("New MAC address: {}".format(new_mac_address))
  
  def __generate_random_mac_address(self):
    old_split_mac_address = self.__old_mac_address.split(":")
    current_oui = old_split_mac_address[0] + old_split_mac_address[1] + old_split_mac_address[2]
    new_mac_address = ':'.join(re.findall("..", current_oui + hex(randrange(0, 16**6))[2:].zfill(6)))
    return new_mac_address
  
  def __prompt_for_new_address(self):
    pass
  
  def __verify_mac_address(self, new_mac_address):
    pass