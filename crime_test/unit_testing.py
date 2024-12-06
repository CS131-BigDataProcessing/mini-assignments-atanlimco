#unit_testing.py

import validate_functions as vf
import stats_function as sf

#unit testing using the original Crime_Data_from_2020_to_Present.csv file
print("***Testing using the original Crime_Data_from_2020_to_Present.csv file:")
#run the validate)functions methods
is_sex_valid = vf.validate_vict_sex('./Crime_Data_from_2020_to_Present.csv')
print(f"Result of validate_vict_sex: {is_sex_valid}")

is_age_valid = vf.validate_vict_age('./Crime_Data_from_2020_to_Present.csv')
print(f"Result of validate_vict_age: {is_age_valid}")

#run the stats_function methods
#note that it doesn't remove the invalid values in the vict age column
#the values match the results from the pandas dataframe mean and median methods
mean_vict_age = sf.calculate_mean_vict_age('./Crime_Data_from_2020_to_Present.csv')
print(f"Result of calculate_mean_vict_age: {mean_vict_age}")

median_vict_age = sf.calculate_median_vict_age('./Crime_Data_from_2020_to_Present.csv')
print(f"Result of calculate_median_vict_age: {median_vict_age}")

#unit test stats_function module
#using the dirty_data csv file, calculate_mean_vict_age should return 7, calculate_median_vict_age should return 7
#the k in the Vict Age column should be ignored

print("***Testing using small dirty_data.csv file:")

unit_test_mean_age = sf.calculate_mean_vict_age('./dirty_data.csv')
print(f"Result of calculate_mean_vict_age using dirty_data (should be 7): {unit_test_mean_age}")

unit_test_median_age = sf.calculate_median_vict_age('./dirty_data.csv')
print(f"Result of calculate_median_vict_age using dirty_data (should be 7): {unit_test_median_age}")

#unit test validate_function module
#using the dirty_data csv file,
#validate_vict_sex should return False since there is a number in the Vict Sex column (wrong datatype)
#validate_vict_age should return False since there is a string character in the Vict Age column (wrong datatype)
unit_test_is_sex_valid = vf.validate_vict_sex('./dirty_data.csv')
print(f"Result of validate_vict_sex using dirty_data (should be False): {unit_test_is_sex_valid}")

unit_test_is_age_valid = vf.validate_vict_age('./dirty_data.csv')
print(f"Result of validate_vict_age using dirty_data (should be False): {unit_test_is_age_valid}")
