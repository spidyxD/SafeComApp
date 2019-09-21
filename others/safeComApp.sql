-- Database: safeComApp

-- DROP DATABASE "safeComApp";

/*
 9 AGOSTO 2019
 ANDRES GUTIERREZ ARCIA
 ROGER AMADOR VILLAGRA
 MARCO CALDERON ALPIZAR
*/

/*
    PSEUDO SQL CODE
*/

CREATE TABLE PERSONA(
    cedula varchar(12), /* Primary Key */
    nombre varchar(20),
    primer_apellido varchar(30),
    segundo_apellido varchar (30),
    rol varchar(30),
);
CONSTRAINT PKPersona PRIMARY KEY REFERENCES cedula FROM Persona;

CREATE TABLE VEHICULO(
    placa varchar(7), /* Primary Key*/
    modelo varchar (20),
    marca varchar (10),
    color varchar (10)
)
CONSTRAINT PKVehiculo PRIMARY KEY  REFERENCES placa FROM Vehiculo;

CREATE TABLE REGISTRO_VISITA(
    fecha_ingreso DATE,
	fecha_salida DATE,
    placa varchar(7), /* foreing key */
    cedula_visita varchar(12),
    motivo varchar(500)
)
CONSTRAINT FKVehiculo FOREIGN KEY REFERENCES placa FROM REGISTRO_VISITA;
CONSTRAINT FKPersona FOREIGN KEY REFERENCES cedula FROM REGISTRO_VISITA;

CREATE TABLE BLACK_LIST(
	placa varchar(7),
	cedula varchar(12)
)
CONSTRAINT FKVehiculo2 FOREIGN KEY REFERENCES placa FROM BLACK_LIST;
CONSTRAINT FKPersona2 FOREIGN KEY REFERENCES cedula FROM BLACK_LIST;