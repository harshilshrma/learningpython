
"""
Module 1 - PLATFORM

The Platform module is used to retrieve as much possible information about the platform on which the program is
being currently executed. Now by platform info, it means information about the device, it’s OS, node, OS version, Python version,
etc. This module plays a crucial role when you want to check whether your program is compatible with the python version installed
on a particular system or whether the hardware specifications meet the requirements of your program.
"""

import platform

print("\t\t\t\t\t\t***** CHECK YOUR PC! *****")
print("\t\t\t\t\t\t Welcome to this program!\nHere you can check your system's information right at the click of a button.")
print("\nHere are the following system configurations with their respective serial numbers:")
print("\t1. Platform Processor\n\t2. Platform Architecture\n\t3. Platform Information\n\t4. Network Name\n\t5. OS"
      "\n\t6. Machine Type\n\t7. Python Build Date and Number\n\t8. Python Version")

while True:
      user_input = int(input("\nEnter the configuration's serial number that you want to check: "))
      if user_input == 1:
            print("Your Platform Processor is:", platform.processor())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 2:
            print("Your Platform Architecture is:", platform.architecture())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 3:
            print("Your Platform Information is:", platform.platform())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 4:
            print("Your System's Network Name is:", platform.node())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 5:
            print("Your OS is:", platform.system())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 6:
            print("Your Machine Type is:", platform.machine())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 7:
            print("Your Python Build Date and Number is:", platform.python_build())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      if user_input == 8:
            print("Your Python Version is:", platform.python_version())
            again_input = int(input("\n\tEnter 1 to check more or 2 to end: "))
            if again_input == 1:
                  continue
            if again_input == 2:
                  print("\n\t\t\t\t\t  Thank you for using this program!\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break
            else:
                  print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
                  break

      else:
            print("INVALID ENTRY!\nABORTING SESSION...\n\t\t\t\t\t\t***** CHECK YOUR PC! *****")
            break