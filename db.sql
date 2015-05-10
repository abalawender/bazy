--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dane_firmy; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE dane_firmy (
    id integer NOT NULL,
    nazwa text,
    adres text
);


--
-- Name: maszyny; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE maszyny (
    id integer NOT NULL,
    opis text
);


--
-- Name: maszyny_operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE maszyny_operacje (
    id integer NOT NULL,
    id_operacje integer,
    id_maszyna integer
);


--
-- Name: operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE operacje (
    id integer NOT NULL,
    koszt integer,
    id_zadania integer
);


--
-- Name: permutacja_operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE permutacja_operacje (
    id integer NOT NULL,
    id_operacja integer,
    kolejnosc integer
);


--
-- Name: COLUMN permutacja_operacje.id_operacja; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN permutacja_operacje.id_operacja IS '
';


--
-- Name: zadania; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE zadania (
    id integer NOT NULL,
    data_przyjecia date,
    id_firmy integer NOT NULL,
    data_obliczenia date
);


--
-- Name: PK_Maszyny_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny
    ADD CONSTRAINT "PK_Maszyny_id" PRIMARY KEY (id);


--
-- Name: PK_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "PK_id" PRIMARY KEY (id);


--
-- Name: PK_maszyny_zadania; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "PK_maszyny_zadania" PRIMARY KEY (id);


--
-- Name: PK_permutacja_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "PK_permutacja_id" PRIMARY KEY (id);


--
-- Name: UNIQUE_maszyny_zadania_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "UNIQUE_maszyny_zadania_id" UNIQUE (id);


--
-- Name: klucz_glowny; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY dane_firmy
    ADD CONSTRAINT klucz_glowny PRIMARY KEY (id);


--
-- Name: pk_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY zadania
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- Name: FK_id_proces; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "FK_id_proces" FOREIGN KEY (id_zadania) REFERENCES zadania(id);


--
-- Name: FK_maszyny_zadania_zadania; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zadania_zadania" FOREIGN KEY (id_operacje) REFERENCES operacje(id);


--
-- Name: FK_maszyny_zdania_maszyny; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zdania_maszyny" FOREIGN KEY (id_maszyna) REFERENCES maszyny(id);


--
-- Name: FK_permutacje_operacje_operacja; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "FK_permutacje_operacje_operacja" FOREIGN KEY (id_operacja) REFERENCES operacje(id);


--
-- Name: fk_firma; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY zadania
    ADD CONSTRAINT fk_firma FOREIGN KEY (id_firmy) REFERENCES dane_firmy(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

