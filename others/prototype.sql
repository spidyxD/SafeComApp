-- Table: public.persona

-- DROP TABLE public.persona;

CREATE TABLE public.persona
(
    cedula character varying(12) COLLATE pg_catalog."default" NOT NULL,
    nombre character varying(20) COLLATE pg_catalog."default",
    primer_apellido character varying(30) COLLATE pg_catalog."default",
    segundo_apellido character varying(30) COLLATE pg_catalog."default",
    rol character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT pkpersona PRIMARY KEY (cedula)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.persona
    OWNER to postgres;
	
	
-- Table: public.registro_visita

-- DROP TABLE public.registro_visita;

CREATE TABLE public.registro_visita
(
    fecha_ingreso date,
    fecha_salida date,
    placa character varying(7) COLLATE pg_catalog."default",
    cedula_visita character varying(12) COLLATE pg_catalog."default",
    motivo character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT registro_visita_cedula_visita_fkey FOREIGN KEY (cedula_visita)
        REFERENCES public.persona (cedula) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT registro_visita_placa_fkey FOREIGN KEY (placa)
        REFERENCES public.vehiculo (placa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.registro_visita
    OWNER to postgres;
	
-- Table: public.vehiculo

-- DROP TABLE public.vehiculo;

CREATE TABLE public.vehiculo
(
    placa character varying(7) COLLATE pg_catalog."default" NOT NULL,
    modelo character varying(20) COLLATE pg_catalog."default",
    marca character varying(10) COLLATE pg_catalog."default",
    color character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT pkvehiculo PRIMARY KEY (placa)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.vehiculo
    OWNER to postgres;
	
	
-- Table: public.black_list

-- DROP TABLE public.black_list;

CREATE TABLE public.black_list
(
    placa character varying(7) COLLATE pg_catalog."default",
    cedula character varying(12) COLLATE pg_catalog."default",
    CONSTRAINT black_list_cedula_fkey FOREIGN KEY (cedula)
        REFERENCES public.persona (cedula) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT black_list_placa_fkey FOREIGN KEY (placa)
        REFERENCES public.vehiculo (placa) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.black_list
    OWNER to postgres;