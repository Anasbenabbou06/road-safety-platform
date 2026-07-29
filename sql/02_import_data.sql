\copy accident FROM 'C:\Users\HP\Downloads\Dataset1\accident_final.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', FORCE_NULL(hour_of_crash, number_of_drunk_drivers));

\copy vehicle FROM 'C:\Users\HP\Downloads\Dataset1\vehicle_final.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', FORCE_NULL(travel_speed, related_factors_driver_level_1, fatalities_in_vehicle));

\copy person FROM 'C:\Users\HP\Downloads\Dataset1\person_final.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', FORCE_NULL(age, vehicle_number));

\copy factor FROM 'C:\Users\HP\Downloads\Dataset1\factor_final.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', FORCE_NULL(contributing_circumstances_motor_vehicle));

SELECT 'accident' AS tbl, COUNT(*) AS lignes FROM accident
UNION ALL
SELECT 'vehicle', COUNT(*) FROM vehicle
UNION ALL
SELECT 'person', COUNT(*) FROM person
UNION ALL
SELECT 'factor', COUNT(*) FROM factor;