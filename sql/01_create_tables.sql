CREATE TABLE accident (
    state_number                INT             NOT NULL,
    consecutive_number          INT             NOT NULL,
    year_of_crash               INT,
    month_of_crash              INT,
    day_of_week                 INT,
    hour_of_crash               INT,
    land_use_name               VARCHAR(100),
    manner_of_collision_name    VARCHAR(200),
    light_condition_name        VARCHAR(200),
    atmospheric_conditions_name VARCHAR(200),
    number_of_fatalities        INT,
    number_of_drunk_drivers     INT,
    PRIMARY KEY (state_number, consecutive_number)
);

CREATE TABLE vehicle (
    state_number                INT             NOT NULL,
    consecutive_number          INT             NOT NULL,
    vehicle_number              INT             NOT NULL,
    vehicle_make_name           VARCHAR(500),
    body_type_name              VARCHAR(200),
    travel_speed                INT,
    rollover                    VARCHAR(100),
    driver_drinking             VARCHAR(100),
    speeding_related            VARCHAR(100),
    fatalities_in_vehicle       INT,
    roadway_surface_condition_name VARCHAR(200),
    crash_type_name             VARCHAR(200),
    related_factors_driver_level_1 INT,
    PRIMARY KEY (state_number, consecutive_number, vehicle_number)
);

CREATE TABLE person (
    state_number                INT             NOT NULL,
    consecutive_number          INT             NOT NULL,
    vehicle_number              INT,
    person_number               INT             NOT NULL,
    person_type_name            VARCHAR(200),
    age                         INT,
    sex                         VARCHAR(50),
    restraint_system_helmet_use_name VARCHAR(200),
    injury_severity_name        VARCHAR(200),
    seating_position_name       VARCHAR(200),
    air_bag_deployed_name       VARCHAR(200),
    ejection_name               VARCHAR(200),
    police_reported_alcohol_involvement VARCHAR(200),
    PRIMARY KEY (state_number, consecutive_number, vehicle_number, person_number)
);

CREATE TABLE factor (
    state_number                INT             NOT NULL,
    consecutive_number          INT             NOT NULL,
    vehicle_number              INT             NOT NULL,
    contributing_circumstances_motor_vehicle      INT,
    contributing_circumstances_motor_vehicle_name VARCHAR(500)
);