--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.1
-- Dumped by pg_dump version 9.4.1
-- Started on 2015-05-14 10:12:06 CEST

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
-- TOC entry 172 (class 1259 OID 16615)
-- Name: dane_firmy_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE dane_firmy_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dane_firmy_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 16617)
-- Name: dane_firmy; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE dane_firmy (
    id integer DEFAULT nextval('dane_firmy_seq'::regclass) NOT NULL,
    nazwa text,
    adres text
);


ALTER TABLE dane_firmy OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 16624)
-- Name: maszyny_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE maszyny_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE maszyny_seq OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 16626)
-- Name: maszyny; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE maszyny (
    id integer DEFAULT nextval('maszyny_seq'::regclass) NOT NULL,
    opis text
);


ALTER TABLE maszyny OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 16633)
-- Name: maszyny_operacje_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE maszyny_operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE maszyny_operacje_seq OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 16635)
-- Name: maszyny_operacje; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE maszyny_operacje (
    id integer DEFAULT nextval('maszyny_operacje_seq'::regclass) NOT NULL,
    id_operacje integer,
    id_maszyna integer,
    koszt integer
);


ALTER TABLE maszyny_operacje OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 16639)
-- Name: operacje_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE operacje_seq OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 16641)
-- Name: operacje; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE operacje (
    id integer DEFAULT nextval('operacje_seq'::regclass) NOT NULL,
    id_zadania integer
);


ALTER TABLE operacje OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 16645)
-- Name: permutacja_operacje_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE permutacja_operacje_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE permutacja_operacje_seq OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 16647)
-- Name: permutacja_operacje; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE permutacja_operacje (
    id integer DEFAULT nextval('permutacja_operacje_seq'::regclass) NOT NULL,
    id_operacja integer,
    kolejnosc integer
);


ALTER TABLE permutacja_operacje OWNER TO postgres;

--
-- TOC entry 2070 (class 0 OID 0)
-- Dependencies: 181
-- Name: COLUMN permutacja_operacje.id_operacja; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN permutacja_operacje.id_operacja IS '
';


--
-- TOC entry 182 (class 1259 OID 16651)
-- Name: zadania_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE zadania_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE zadania_seq OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 16653)
-- Name: zadania; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE zadania (
    id integer DEFAULT nextval('zadania_seq'::regclass) NOT NULL,
    data_przyjecia date,
    id_firmy integer NOT NULL,
    data_obliczenia date
);


ALTER TABLE zadania OWNER TO postgres;

--
-- TOC entry 2051 (class 0 OID 16617)
-- Dependencies: 173
-- Data for Name: dane_firmy; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY dane_firmy (id, nazwa, adres) FROM stdin;
25	Monsters Inc.	USA
26	Monsters Inc.	USA
28	Monsters Inc.	USA
29	Monsters Inc.	USA
30	Monsters Inc.	USA
31	Monsters Inc.	USA
32	Monsters Inc.	USA
33	Monsters Inc.	USA
34	Monsters Inc.	USA
35	Monsters Inc.	USA
36	Monsters Inc.	USA
37	Monsters Inc.	USA
38	Monsters Inc.	USA
39	Monsters Inc.	USA
\.


--
-- TOC entry 2071 (class 0 OID 0)
-- Dependencies: 172
-- Name: dane_firmy_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('dane_firmy_seq', 39, true);


--
-- TOC entry 2053 (class 0 OID 16626)
-- Dependencies: 175
-- Data for Name: maszyny; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY maszyny (id, opis) FROM stdin;
19	Nowa maszyna
20	Nowa maszyna
22	Nowa maszyna
23	Nowa maszyna
24	Nowa maszyna
25	Nowa maszyna
26	Nowa maszyna
27	Nowa maszyna
28	Nowa maszyna
29	Nowa maszyna
30	Nowa maszyna
31	Nowa maszyna
32	Nowa maszyna
33	Nowa maszyna
\.


--
-- TOC entry 2055 (class 0 OID 16635)
-- Dependencies: 177
-- Data for Name: maszyny_operacje; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY maszyny_operacje (id, id_operacje, id_maszyna, koszt) FROM stdin;
11	15	19	3
12	16	20	3
13	17	22	3
14	18	23	3
15	19	24	3
16	20	25	3
17	21	26	3
18	22	27	3
19	23	28	3
20	24	29	3
21	25	30	3
22	26	31	3
23	27	32	5
24	28	33	5
\.


--
-- TOC entry 2072 (class 0 OID 0)
-- Dependencies: 176
-- Name: maszyny_operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('maszyny_operacje_seq', 24, true);


--
-- TOC entry 2073 (class 0 OID 0)
-- Dependencies: 174
-- Name: maszyny_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('maszyny_seq', 33, true);


--
-- TOC entry 2057 (class 0 OID 16641)
-- Dependencies: 179
-- Data for Name: operacje; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY operacje (id, id_zadania) FROM stdin;
15	25
16	26
17	28
18	29
19	30
20	31
21	32
22	33
23	34
24	35
25	36
26	37
27	38
28	39
\.


--
-- TOC entry 2074 (class 0 OID 0)
-- Dependencies: 178
-- Name: operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('operacje_seq', 28, true);


--
-- TOC entry 2059 (class 0 OID 16647)
-- Dependencies: 181
-- Data for Name: permutacja_operacje; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY permutacja_operacje (id, id_operacja, kolejnosc) FROM stdin;
7	15	1
8	16	1
9	17	1
10	18	1
11	19	1
12	20	1
13	21	1
14	22	1
15	23	1
16	24	1
17	25	1
18	26	1
19	27	1
20	28	1
\.


--
-- TOC entry 2075 (class 0 OID 0)
-- Dependencies: 180
-- Name: permutacja_operacje_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('permutacja_operacje_seq', 20, true);


--
-- TOC entry 2061 (class 0 OID 16653)
-- Dependencies: 183
-- Data for Name: zadania; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY zadania (id, data_przyjecia, id_firmy, data_obliczenia) FROM stdin;
25	2015-05-11	25	2015-05-11
26	2015-05-11	26	2015-05-11
28	2015-05-13	28	2015-05-13
29	2015-05-13	29	2015-05-13
30	2015-05-14	30	2015-05-14
31	2015-05-14	31	2015-05-14
32	2015-05-14	32	2015-05-14
33	2015-05-14	33	2015-05-14
34	2015-05-14	34	2015-05-14
35	2015-05-14	35	2015-05-14
36	2015-05-14	36	2015-05-14
37	2015-05-14	37	2015-05-14
38	2015-05-14	38	2015-05-14
39	2015-05-14	39	2015-05-14
\.


--
-- TOC entry 2076 (class 0 OID 0)
-- Dependencies: 182
-- Name: zadania_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('zadania_seq', 39, true);


--
-- TOC entry 1925 (class 2606 OID 16658)
-- Name: PK_Maszyny_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY maszyny
    ADD CONSTRAINT "PK_Maszyny_id" PRIMARY KEY (id);


--
-- TOC entry 1931 (class 2606 OID 16660)
-- Name: PK_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "PK_id" PRIMARY KEY (id);


--
-- TOC entry 1927 (class 2606 OID 16662)
-- Name: PK_maszyny_zadania; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "PK_maszyny_zadania" PRIMARY KEY (id);


--
-- TOC entry 1933 (class 2606 OID 16664)
-- Name: PK_permutacja_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "PK_permutacja_id" PRIMARY KEY (id);


--
-- TOC entry 1929 (class 2606 OID 16666)
-- Name: UNIQUE_maszyny_zadania_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "UNIQUE_maszyny_zadania_id" UNIQUE (id);


--
-- TOC entry 1923 (class 2606 OID 16668)
-- Name: klucz_glowny; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY dane_firmy
    ADD CONSTRAINT klucz_glowny PRIMARY KEY (id);


--
-- TOC entry 1935 (class 2606 OID 16670)
-- Name: pk_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY zadania
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- TOC entry 1938 (class 2606 OID 16671)
-- Name: FK_id_proces; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY operacje
    ADD CONSTRAINT "FK_id_proces" FOREIGN KEY (id_zadania) REFERENCES zadania(id);


--
-- TOC entry 1936 (class 2606 OID 16676)
-- Name: FK_maszyny_zadania_zadania; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zadania_zadania" FOREIGN KEY (id_operacje) REFERENCES operacje(id);


--
-- TOC entry 1937 (class 2606 OID 16681)
-- Name: FK_maszyny_zdania_maszyny; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY maszyny_operacje
    ADD CONSTRAINT "FK_maszyny_zdania_maszyny" FOREIGN KEY (id_maszyna) REFERENCES maszyny(id);


--
-- TOC entry 1939 (class 2606 OID 16686)
-- Name: FK_permutacje_operacje_operacja; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY permutacja_operacje
    ADD CONSTRAINT "FK_permutacje_operacje_operacja" FOREIGN KEY (id_operacja) REFERENCES operacje(id);


--
-- TOC entry 1940 (class 2606 OID 16691)
-- Name: fk_firma; Type: FK CONSTRAINT; Schema: public; Owner: postgres
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


-- Completed on 2015-05-14 10:12:06 CEST

--
-- PostgreSQL database dump complete
--

