#unitTest_math_functions.py

from math_functions import my_division, my_power

#testing edge cases for divide function
def division_edge_cases():
  #get results for various divide edge cases
  result_division_1 = my_division(10,4)
  result_division_2 = my_division(10,2)
  result_division_3 = my_division(10,0)
  result_division_4 = my_division(0,2)
  result_division_5 = my_division(-10,2)
  result_division_6 = my_division(10,-2)
  result_division_7 = my_division(-10,-2)

  #print results for various divide edge cases
  print("Dividing 10 by 4 gives:",result_division_1)
  print("Dividing 10 by 2 gives:",result_division_2)
  print("Dividing 10 by 0 gives:",result_division_3)
  print("Dividing 0 by 2 gives:",result_division_4)
  print("Dividing -10 by 2 gives:",result_division_5)
  print("Dividing 10 by -2 gives:",result_division_6)
  print("Dividing -10 by -2 gives:",result_division_7)
  print("")

#testing edge cases for power function
def power_edge_cases():
  #get results for various power edge cases
  result_power_1 = my_power(2,3)
  result_power_2 = my_power(5,0)
  result_power_3 = my_power(4,-3)
  result_power_4 = my_power(-4,3)
  result_power_5 = my_power(0,3)
  result_power_6 = my_power(2,1/2)
  result_power_7 = my_power(1/2,2)

  #print results for various power edge cases
  print("Raising 2 to the power of 3 gives:",result_power_1)
  print("Raising 5 to the power of 0 gives:",result_power_2)
  print("Raising 4 to the power of -3 gives:",result_power_3)
  print("Raising -4 to the power of 3 gives:",result_power_4)
  print("Raising 0 to the power of 3 gives:",result_power_5)
  print("Raising 2 to the power of 1/2 gives:",result_power_6)
  print("Raising 1/2 to the power of 2 gives:",result_power_7)
  print("")

division_edge_cases()
power_edge_cases()
