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
    rol NUMBER,
);

CREATE TABLE VEHICULO(
    placa varchar(7), /* Primary Key*/
    modelo varchar (20),
    marca varchar (10),
    color varchar (10)
)

CREATE TABLE REGISTRO_VISITA(
    fecha_ingreso DATE,
    placa varchar(7), /* foreing key */
    cedula_visita varchar(12),
    motivo varchar(500)
)

CREATE TABLE BLACK_LIST(

)

CREATE TABLE ALERTS(

)
