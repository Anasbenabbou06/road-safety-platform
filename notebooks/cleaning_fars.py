
from google.cloud import bigquery
import pandas as pd
import csv

client = bigquery.Client()

# Valeurs textuelles à remplacer par "Non documenté"
valeurs_manquantes = ['Unknown', 'Not Reported', 'None', 'Reported as Unknown']


# TABLE 1 : ACCIDENT

query_accident = """
    SELECT
        state_number, consecutive_number,
        year_of_crash, month_of_crash, day_of_week, hour_of_crash,
        land_use_name, manner_of_collision_name,
        light_condition_name, atmospheric_conditions_name,
        number_of_fatalities, number_of_drunk_drivers
    FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
"""
accident = client.query(query_accident).to_dataframe()
print("Accident shape :", accident.shape)

# Codes FARS → NULL
accident.loc[accident['hour_of_crash'] >= 99, 'hour_of_crash'] = None

# Encodage Unicode
cols_texte = accident.select_dtypes(include='object').columns
for col in cols_texte:
    accident[col] = accident[col].str.replace('\u2013', '-', regex=False)
    accident[col] = accident[col].str.replace('\u2014', '-', regex=False)
    accident[col] = accident[col].str.replace('\n', ' ', regex=False)

# Valeurs inconnues textuelles → "Non documenté"
for col in cols_texte:
    accident[col] = accident[col].replace(valeurs_manquantes, 'Non documenté')

# Doublons
accident = accident.drop_duplicates()
print("Accident après cleaning :", accident.shape)

# Export
accident.to_csv('accident_final.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
print("accident_final.csv exporté ✅")


# TABLE 2 : VEHICLE

query_vehicle = """
    SELECT
        state_number, consecutive_number, vehicle_number,
        vehicle_make_name, body_type_name,
        travel_speed, rollover, driver_drinking,
        speeding_related, fatalities_in_vehicle,
        roadway_surface_condition_name, crash_type_name,
        related_factors_driver_level_1
    FROM `bigquery-public-data.nhtsa_traffic_fatalities.vehicle_2015`
"""
vehicle = client.query(query_vehicle).to_dataframe()
print("\nVehicle shape :", vehicle.shape)

# Codes FARS → NULL
vehicle.loc[vehicle['travel_speed'] >= 97, 'travel_speed'] = None

# Encodage Unicode
cols_texte = vehicle.select_dtypes(include='object').columns
for col in cols_texte:
    vehicle[col] = vehicle[col].str.replace('\u2013', '-', regex=False)
    vehicle[col] = vehicle[col].str.replace('\u2014', '-', regex=False)
    vehicle[col] = vehicle[col].str.replace('\n', ' ', regex=False)

# Valeurs inconnues textuelles → "Non documenté"
for col in cols_texte:
    vehicle[col] = vehicle[col].replace(valeurs_manquantes, 'Non documenté')

# Doublons
vehicle = vehicle.drop_duplicates()
print("Vehicle après cleaning :", vehicle.shape)

# Export
vehicle.to_csv('vehicle_final.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
print("vehicle_final.csv exporté ✅")


# TABLE 3 : PERSON

query_person = """
    SELECT
        state_number, consecutive_number, vehicle_number, person_number,
        person_type_name, age, sex,
        restraint_system_helmet_use_name, injury_severity_name,
        seating_position_name, air_bag_deployed_name,
        ejection_name, police_reported_alcohol_involvement
    FROM `bigquery-public-data.nhtsa_traffic_fatalities.person_2015`
"""
person = client.query(query_person).to_dataframe()
print("\nPerson shape :", person.shape)

# Codes FARS → NULL
person.loc[person['age'] >= 120, 'age'] = None

# Encodage Unicode
cols_texte = person.select_dtypes(include='object').columns
for col in cols_texte:
    person[col] = person[col].str.replace('\u2013', '-', regex=False)
    person[col] = person[col].str.replace('\u2014', '-', regex=False)
    person[col] = person[col].str.replace('\n', ' ', regex=False)

# Valeurs inconnues textuelles → "Non documenté"
for col in cols_texte:
    person[col] = person[col].replace(valeurs_manquantes, 'Non documenté')

# Doublons
person = person.drop_duplicates()
print("Person après cleaning :", person.shape)

# Export
person.to_csv('person_final.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
print("person_final.csv exporté ✅")



# TABLE 4 : FACTOR

query_factor = """
    SELECT
        state_number, consecutive_number, vehicle_number,
        contributing_circumstances_motor_vehicle,
        contributing_circumstances_motor_vehicle_name
    FROM `bigquery-public-data.nhtsa_traffic_fatalities.factor_2015`
"""
factor = client.query(query_factor).to_dataframe()
print("\nFactor shape :", factor.shape)

# Encodage Unicode
cols_texte = factor.select_dtypes(include='object').columns
for col in cols_texte:
    factor[col] = factor[col].str.replace('\u2013', '-', regex=False)
    factor[col] = factor[col].str.replace('\u2014', '-', regex=False)
    factor[col] = factor[col].str.replace('\n', ' ', regex=False)

# Valeurs inconnues textuelles → "Non documenté"
for col in cols_texte:
    factor[col] = factor[col].replace(valeurs_manquantes, 'Non documenté')

# Doublons
factor = factor.drop_duplicates()
print("Factor après cleaning :", factor.shape)

# Export
factor.to_csv('factor_final.csv', index=False, encoding='utf-8', quoting=csv.QUOTE_ALL)
print("factor_final.csv exporté ✅")



# RÉSUMÉ FINAL

print("\n" + "=" * 50)
print("RÉSUMÉ DU NETTOYAGE")
print("=" * 50)
print(f"  accident : {accident.shape[0]:,} lignes × {accident.shape[1]} colonnes")
print(f"  vehicle  : {vehicle.shape[0]:,} lignes × {vehicle.shape[1]} colonnes")
print(f"  person   : {person.shape[0]:,} lignes × {person.shape[1]} colonnes")
print(f"  factor   : {factor.shape[0]:,} lignes × {factor.shape[1]} colonnes")
print(f"  TOTAL    : {accident.shape[0] + vehicle.shape[0] + person.shape[0] + factor.shape[0]:,} lignes")
print("\nRègles appliquées :")
print("  R1 : hour_of_crash >= 99 → NULL")
print("  R2 : travel_speed >= 97 → NULL")
print("  R3 : age >= 120 → NULL")
print("  R4 : Caractères Unicode (\\u2013, \\u2014) → tiret simple")
print("  R5 : Retours à la ligne internes → espace")
print("  R6 : Valeurs Unknown/Not Reported → Non documenté")
print("  R7 : Doublons supprimés")
print("  R8 : Export CSV avec quoting=QUOTE_ALL")