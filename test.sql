--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.1
-- Dumped by pg_dump version 9.4.1
-- Started on 2015-05-10 15:29:07 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 184 (class 3079 OID 11860)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2069 (class 0 OID 0)
-- Dependencies: 184
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- TOC entry 178 (class 1259 OID 16596)
-- Name: dane_firmy_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE dane_firmy_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dane_firmy_seq;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 172 (class 1259 OID 16533)
-- Name: dane_firmy; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE dane_firmy (
    id integer DEFAULT nextval('dane_firmy_seq'::regclass) NOT NULL,
    nazwa text,
    adres text
);


ALTER TABLE dane_firmy OWNER TO -;

--
-- TOC entry 179 (class 1259 OID 16598)
-- Name: maszyny_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE maszyny_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE maszyny_seq OWNER TO -;

--
-- TOC entry 173 (class 1259 OID 16539)
-- Name: maszyny; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE maszyny (
    id integer DEFAULT nextval('maszyny_seq'::regclass) NOT NULL,
    opis text
);


ALTER TABLE maszyny OWNER TO -;

--
-- TOC entry 180 (class 1259 OID 16600)
-- Name: maszyny_operacje_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE maszyny_operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE maszyny_operacje_seq OWNER TO -;

--
-- TOC entry 174 (class 1259 OID 16545)
-- Name: maszyny_operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE maszyny_operacje (
    id integer DEFAULT nextval('maszyny_operacje_seq'::regclass) NOT NULL,
    id_operacje integer,
    id_maszyna integer
);


ALTER TABLE maszyny_operacje OWNER TO -;

--
-- TOC entry 181 (class 1259 OID 16602)
-- Name: operacje_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE operacje_seq OWNER TO -;

--
-- TOC entry 175 (class 1259 OID 16548)
-- Name: operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE operacje (
    id integer DEFAULT nextval('operacje_seq'::regclass) NOT NULL,
    koszt integer,
    id_zadania integer
);


ALTER TABLE operacje OWNER TO -;

--
-- TOC entry 182 (class 1259 OID 16604)
-- Name: permutacja_operacje_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE permutacja_operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE permutacja_operacje_seq OWNER TO -;

--
-- TOC entry 176 (class 1259 OID 16551)
-- Name: permutacja_operacje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE permutacja_operacje (
    id integer DEFAULT nextval('permutacja_operacje_seq'::regclass) NOT NULL,
    id_operacja integer,
    kolejnosc integer
);


ALTER TABLE permutacja_operacje OWNER TO -;

--
-- TOC entry 2070 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN permutacja_operacje.id_operacja; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN permutacja_operacje.id_operacja IS '
';


--
-- TOC entry 183 (class 1259 OID 16606)
-- Name: zadania_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE zadania_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE zadania_seq OWNER TO -;

--
-- TOC entry 177 (class 1259 OID 16554)
-- Name: zadania; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE zadania (
    id integer DEFAULT nextval('zadania_seq'::regclass) NOT NULL,
    data_przyjecia date,
    id_firmy integer NOT NULL,
    data_obliczenia date
);


ALTER TABLE zadania OWNER TO -;

--
-- TOC entry 2050 (class 0 OID 16533)
-- Dependencies: 172
-- Data for Name: dane_firmy; Type: TABLE DATA; Schema: public; Owner: -
--

COPY dane_firmy (id, nazwa, adres) FROM stdin;
\.


--
-- TOC entry 2071 (class 0 OID 0)
-- Dependencies: 178
-- Name: dane_firmy_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('dane_firmy_seq', 1, false);


--
-- TOC entry 2051 (class 0 OID 16539)
-- Dependencies: 173
-- Data for Name: maszyny; Type: TABLE DATA; Schema: public; Owner: -
--

COPY maszyny (id, opis) FROM stdin;
\.


--
-- TOC entry 2052 (class 0 OID 16545)
-- Dependencies: 174
-- Data for Name: maszyny_operacje; Type: TABLE DATA; Schema: public; Owner: -
--

COPY maszyny_operacje (id, id_operacje, id_maszyna) FROM stdin;
\.


--
-- TOC entry 2072 (class 0 OID 0)
-- Dependencies: 180
-- Name: maszyny_operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('maszyny_operacje_seq', 1, false);


--
-- TOC entry 2073 (class 0 OID 0)
-- Dependencies: 179
-- Name: maszyny_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('maszyny_seq', 1, false);


--
-- TOC entry 2053 (class 0 OID 16548)
-- Dependencies: 175
-- Data for Name: operacje; Type: TABLE DATA; Schema: public; Owner: -
--

COPY operacje (id, koszt, id_zadania) FROM stdin;
\.


--
-- TOC entry 2074 (class 0 OID 0)
-- Dependencies: 181
-- Name: operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('operacje_seq', 1, false);


--
-- TOC entry 2054 (class 0 OID 16551)
-- Dependencies: 176
-- Data for Name: permutacja_operacje; Type: TABLE DATA; Schema: public; Owner: -
--

COPY permutacja_operacje (id, id_operacja, kolejnosc) FROM stdin;
\.


--
-- TOC entry 2075 (class 0 OID 0)
-- Dependencies: 182
-- Name: permutacja_operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('permutacja_operacje_seq', 1, false);


--
-- TOC entry 2055 (class 0 OID 16554)
-- Dependencies: 177
-- Data for Name: zadania; Type: TABLE DATA; Schema: public; Owner: -
--

COPY zadania (id, data_przyjecia, id_firmy, data_obliczenia) FROM stdin;
\.


--
-- TOC entry 2076 (class 0 OID 0)
-- Dependencies: 183
-- Name: zadania_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('zadania_seq', 1, false);


--
-- TOC entry 1925 (class 2606 OID 16558)
-- Name: PK_Maszyny_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny
    ADD CONSTRAINT "PK_Maszyny_id" PRIMARY KEY (id);


--
-- TOC entry 1931 (class 2606 OID 16560)
-- Name: PK_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "PK_id" PRIMARY KEY (id);


--
-- TOC entry 1927 (class 2606 OID 16562)
-- Name: PK_maszyny_zadania; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "PK_maszyny_zadania" PRIMARY KEY (id);


--
-- TOC entry 1933 (class 2606 OID 16564)
-- Name: PK_permutacja_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "PK_permutacja_id" PRIMARY KEY (id);


--
-- TOC entry 1929 (class 2606 OID 16566)
-- Name: UNIQUE_maszyny_zadania_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "UNIQUE_maszyny_zadania_id" UNIQUE (id);


--
-- TOC entry 1923 (class 2606 OID 16568)
-- Name: klucz_glowny; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY dane_firmy
    ADD CONSTRAINT klucz_glowny PRIMARY KEY (id);


--
-- TOC entry 1935 (class 2606 OID 16570)
-- Name: pk_id; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY zadania
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- TOC entry 1938 (class 2606 OID 16571)
-- Name: FK_id_proces; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "FK_id_proces" FOREIGN KEY (id_zadania) REFERENCES zadania(id);


--
-- TOC entry 1936 (class 2606 OID 16576)
-- Name: FK_maszyny_zadania_zadania; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zadania_zadania" FOREIGN KEY (id_operacje) REFERENCES operacje(id);


--
-- TOC entry 1937 (class 2606 OID 16581)
-- Name: FK_maszyny_zdania_maszyny; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zdania_maszyny" FOREIGN KEY (id_maszyna) REFERENCES maszyny(id);


--
-- TOC entry 1939 (class 2606 OID 16586)
-- Name: FK_permutacje_operacje_operacja; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "FK_permutacje_operacje_operacja" FOREIGN KEY (id_operacja) REFERENCES operacje(id);


--
-- TOC entry 1940 (class 2606 OID 16591)
-- Name: fk_firma; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY zadania
    ADD CONSTRAINT fk_firma FOREIGN KEY (id_firmy) REFERENCES dane_firmy(id);


--
-- TOC entry 2068 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2015-05-10 15:29:07 CEST

--
-- PostgreSQL database dump complete
--

