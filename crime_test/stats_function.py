#stats_function.py

import csv

#takes in a csv file to process
#function to calculate mean 'Vict Age'
def calculate_mean_vict_age(file_path):
  mean = 0;

  #open crime csv file
  with open(file_path, mode='r') as csvfile:
    crime_csv_reader = csv.DictReader(csvfile)

    total_sum = 0;
    count = 0;

    #loop through each row in the csv
    for row in crime_csv_reader:
      #if the age is a digit, then add it to the total sum
      #otherwise, dont include it in the calculation (skip)
      try:
        total_sum += int(row['Vict Age'])
        count += 1
      except:
        print(f"Vict Age entry '{row['Vict Age']}' was not an int")

    #get mean
    mean = total_sum / count

    #return mean
    return mean


#takes in a csv file to process
#function to calculate median 'Vict Age'
def calculate_median_vict_age(file_path):
  median = 0;
  with open(file_path, mode='r') as csvfile:
    crime_csv_reader = csv.DictReader(csvfile)

    count = 0;
    vict_age_vals = []
    middle_index = 0
    for row in crime_csv_reader:
      #if the age is a digit, then add it to the total sum
      #otherwise, dont include it in the calculation (skip)
      try:
        vict_age_vals.append(int(row['Vict Age']))
        count += 1
      except:
        print(f"Vict Age entry '{row['Vict Age']}' was not an int")

    #get median
    #sort the values
    vict_age_vals.sort()
    #if the count is even, take the average of the two middle numbers
    if (count % 2 == 0):
      middle_index = count / 2
      middle_index_plus_one = middle_index + 1
      val_at_mid = vict_age_vals[int(middle_index)]
      val_at_mid_plus_one = vict_age_vals[int(middle_index_plus_one)]
      median = (val_at_mid + val_at_mid_plus_one) / 2

    else:
      #if the count if odd, take the value in the middle index
      #since its divide by 2, the decimal will always be .5
      #so round() will always round up, which gives the proper midle index if your count starts at 1
      middle_index = round((count/2))
      #need to subtract middle index by 1 since list indexing starts at 0 instead of 1
      median = vict_age_vals[int(middle_index-1)]

    return median
