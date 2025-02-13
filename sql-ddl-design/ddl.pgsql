-- medical_center_seed.sql
-- Drop and recreate the database to ensure a clean slate
DROP DATABASE IF EXISTS medical_center;
CREATE DATABASE medical_center;
\c medical_center

-- Create the tables
CREATE TABLE Doctors (
    doctor_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    contact_info TEXT
);

CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    date_of_birth DATE,
    contact_info TEXT
);

CREATE TABLE Diseases (
    disease_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE Visits (
    visit_id SERIAL PRIMARY KEY,
    doctor_id INT REFERENCES Doctors(doctor_id),
    patient_id INT REFERENCES Patients(patient_id),
    visit_date DATE,
    notes TEXT
);

CREATE TABLE Diagnoses (
    diagnosis_id SERIAL PRIMARY KEY,
    visit_id INT REFERENCES Visits(visit_id),
    disease_id INT REFERENCES Diseases(disease_id)
);



INSERT INTO Doctors (name, specialization, contact_info) 
VALUES ('Dr. Smith', 'Cardiology', '123-456-7890');

INSERT INTO Patients (name, date_of_birth, contact_info) 
VALUES ('John Doe', '1990-01-01', 'john.doe@example.com');

INSERT INTO Diseases (name, description) 
VALUES ('Hypertension', 'High blood pressure');

INSERT INTO Visits (doctor_id, patient_id, visit_date, notes) 
VALUES (1, 1, '2024-12-01', 'Routine check-up');

INSERT INTO Diagnoses (visit_id, disease_id) 
VALUES (1, 1);
