#validate_functions.py

import csv

#takes in a csv file to process
#function that checks if Vict Sex is all M or F
#returns true if its all M or F, false if not
def validate_vict_sex(file_path):
  with open(file_path, mode='r') as csvfile:
      #read the csv file
      crime_csv_reader = csv.DictReader(csvfile)

      #bool to store whether column is clean or not
      all_valid = True

      #csv seems to read everything as strings, so even if you enter a number it will be read as a string
      for row in crime_csv_reader:
        #if the Vict Sex is not M or F, then there are invalid values
        #if the Vict Sex is null it will still be marked as invalid
        if row['Vict Sex'] not in ("M", "F"):
          all_valid = False

      return all_valid

#takes in a csv file to process
def validate_vict_age(file_path):
  with open(file_path, mode='r') as csvfile:
      #read the csv file
      crime_csv_reader = csv.DictReader(csvfile)

      #bool to store whether column is clean or not
      all_valid = True

      for row in crime_csv_reader:
        #if the value in the row is a valid digit
        if row['Vict Age'].isdigit():
          vict_age = int(row['Vict Age'])
          #if the vict_age is not within 1 to 100 inclusive, then its not valid
          if ((vict_age < 1) | (vict_age > 100)):
            all_valid = False
        else:
          #if the Vict Age is not a number then its not valid
          all_valid = False

      return all_valid
