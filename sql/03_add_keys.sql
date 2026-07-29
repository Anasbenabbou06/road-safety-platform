ALTER TABLE accident ADD COLUMN accident_key VARCHAR(50);
UPDATE accident SET accident_key = state_number || '-' || consecutive_number;

ALTER TABLE vehicle ADD COLUMN accident_key VARCHAR(50);
UPDATE vehicle SET accident_key = state_number || '-' || consecutive_number;

ALTER TABLE vehicle ADD COLUMN vehicle_key VARCHAR(50);
UPDATE vehicle SET vehicle_key = state_number || '-' || consecutive_number || '-' || vehicle_number;

ALTER TABLE person ADD COLUMN accident_key VARCHAR(50);
UPDATE person SET accident_key = state_number || '-' || consecutive_number;

ALTER TABLE person ADD COLUMN vehicle_key VARCHAR(50);
UPDATE person SET vehicle_key = state_number || '-' || consecutive_number || '-' || vehicle_number;

ALTER TABLE factor ADD COLUMN accident_key VARCHAR(50);
UPDATE factor SET accident_key = state_number || '-' || consecutive_number;

ALTER TABLE factor ADD COLUMN vehicle_key VARCHAR(50);
UPDATE factor SET vehicle_key = state_number || '-' || consecutive_number || '-' || vehicle_number;

SELECT 'accident' AS tbl, COUNT(DISTINCT accident_key) AS keys FROM accident
UNION ALL
SELECT 'vehicle', COUNT(DISTINCT accident_key) FROM vehicle
UNION ALL
SELECT 'person', COUNT(DISTINCT accident_key) FROM person
UNION ALL
SELECT 'factor', COUNT(DISTINCT accident_key) FROM factor;