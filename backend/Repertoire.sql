--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

-- Started on 2025-01-08 14:38:15 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16439)
-- Name: duo; Type: TABLE; Schema: public; Owner: adam
--

CREATE TABLE public.duo (
    id integer NOT NULL,
    artist character varying(50),
    title character varying(50) NOT NULL,
    artist_alternative character varying(50)[],
    title_alternative character varying(50)[],
    known_from character varying(50),
    tags text[],
    sara character varying(20),
    dominika character varying(20),
    ania character varying(20)
);


ALTER TABLE public.duo OWNER TO adam;

--
-- TOC entry 219 (class 1259 OID 16438)
-- Name: duo_id_seq; Type: SEQUENCE; Schema: public; Owner: adam
--

CREATE SEQUENCE public.duo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.duo_id_seq OWNER TO adam;

--
-- TOC entry 3615 (class 0 OID 0)
-- Dependencies: 219
-- Name: duo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adam
--

ALTER SEQUENCE public.duo_id_seq OWNED BY public.duo.id;


--
-- TOC entry 218 (class 1259 OID 16393)
-- Name: solo; Type: TABLE; Schema: public; Owner: adam
--

CREATE TABLE public.solo (
    id integer NOT NULL,
    artist character varying(50),
    youtube_link character varying(100),
    musicsheet_link character varying(100),
    capo integer,
    tags text[],
    title character varying(50),
    known_from character varying(50),
    title_alternative text[],
    artist_alternative text[]
);


ALTER TABLE public.solo OWNER TO adam;

--
-- TOC entry 217 (class 1259 OID 16392)
-- Name: solo_id_seq; Type: SEQUENCE; Schema: public; Owner: adam
--

CREATE SEQUENCE public.solo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.solo_id_seq OWNER TO adam;

--
-- TOC entry 3616 (class 0 OID 0)
-- Dependencies: 217
-- Name: solo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adam
--

ALTER SEQUENCE public.solo_id_seq OWNED BY public.solo.id;


--
-- TOC entry 3456 (class 2604 OID 16442)
-- Name: duo id; Type: DEFAULT; Schema: public; Owner: adam
--

ALTER TABLE ONLY public.duo ALTER COLUMN id SET DEFAULT nextval('public.duo_id_seq'::regclass);


--
-- TOC entry 3455 (class 2604 OID 16396)
-- Name: solo id; Type: DEFAULT; Schema: public; Owner: adam
--

ALTER TABLE ONLY public.solo ALTER COLUMN id SET DEFAULT nextval('public.solo_id_seq'::regclass);


--
-- TOC entry 3609 (class 0 OID 16439)
-- Dependencies: 220
-- Data for Name: duo; Type: TABLE DATA; Schema: public; Owner: adam
--

COPY public.duo (id, artist, title, artist_alternative, title_alternative, known_from, tags, sara, dominika, ania) FROM stdin;
10	Amy Winehouse	You Know I'm No Good	\N	{"You Know That I'm No Good"}	\N	{pop,R&B}	d	\N	\N
13	Jorja Smith	On My Mind	\N	\N	\N	{pop,R&B}	gis (-2)	\N	\N
20	Joy Crookes	Two Nights	\N	\N	\N	{pop,R&B}	h (-1)	\N	\N
12	Gnarls Barkley	Crazy	\N	\N	\N	{pop,R&B}	c	\N	c
57	Sting	Englishman in New York	\N	\N	\N	{jazz,R&B}	e	\N	\N
4	Ray Charles	Hit the Road Jack	\N	\N	\N	{jazz,R&B}	a (+1)	\N	a (+1)
3	Amy Winehouse	Valerie	\N	\N	\N	{pop,R&B}	Es	Es	Es
59	Edmund Fetting	Nim wstanie dzień	{"Krzysztof Komeda",Komeda}	\N	Prawo i pięść	{"Prawo i pięść",ballad,Polish,film}	a (+2)	\N	\N
9	Gone Gone Beyond	Coast	\N	\N	\N	{rock}	g	\N	\N
17	Duffy	Mercy	\N	\N	\N	{R&B}	\N	g	\N
63	Bill Medley & Jennifer Warnes	(I've Had) The Time of My Life	{"Bill Medley","Jennifer Warnes"}	{"The Time of My Life","Time of My Life"}	Dirty Dancing	{"Dirty Dancing",pop,disco,musical,film}	\N	E	\N
77	Katarzyna Bończyk	O mnie się nie martw	\N	\N	\N	{R&B,Polish}	\N	C (-2)	\N
72	Shania Twain	Man! I Feel Like a Woman	\N	\N	\N	{rock}	\N	A (-1)	\N
60	\N	Colors of the Wind	{"Edyta Górniak","Vanessa Williams","Judy Kuhn"}	{"Kolorowy wiatr"}	Pocahontas	{Pocahontas,Disney,film}	\N	C (-1)	\N
71	Bajm	Do lata	\N	\N	\N	{pop,Polish}	\N	C (-4)	C (-4)
58	Roberta Flack	Killing Me Softly	{Fugees,"Frank Sinatra"}	{"Killing Me Softly With His Song"}	\N	{jazz,ballad}	e (-1)	\N	e (-1)
2	Kings of Leon	Use Somebody	\N	\N	\N	{rock,pop}	a	\N	\N
7	Anthony Hamilton & Elanya Boynton	Freedom	{"Anthony Hamilton","Elanua Boynton"}	\N	Django Unchained	{film,"Django Unchained"}	h	\N	\N
76	Hanka Ordonówna	Na pierwszy znak	\N	\N	\N	{jazz,Polish}	\N	B (-4)	\N
8	Kovacs	Tutti Frutti Tequila	\N	\N	\N	{dance}	es	\N	\N
67	Meghan Trainor	All About That Bass	\N	{"All About The Bass"}	\N	{pop,R&B,dance}	\N	A	\N
56	Anna Jurksztowicz	Na dobre i na złe	{"Krzesimir Dębski"}	\N	\N	{TV,Polish}	\N	\N	a
75	Michael Bublé	Sway	\N	\N	\N	{jazz,dance}	\N	a (+2)	\N
14	Tones and I	Dance Monkey	\N	\N	\N	{pop,dance}	fis	\N	\N
51	Alicia Keys	If I Ain't Got You	\N	\N	\N	{pop}	G	\N	\N
15	Billie Eillish	Bad Guy	\N	\N	\N	{pop,dance}	g	\N	\N
6	Britney Spears	Toxic	{"Melanie Martinez"}	\N	\N	{pop,R&B}	cis (+1)	D	\N
11	Kings of Leon	Sex on Fire	\N	\N	\N	{rock,pop}	E	E	E
68	Shocking Blue	Venus	\N	\N	\N	{rock,pop}	\N	e	\N
66	Gloria Gaynor	I Will Survive	\N	\N	\N	{pop,dance,soul}	\N	a	a
70	The Pointer Sisters	I'm So Excited	\N	\N	\N	{pop,dance}	\N	g	e (-3)
69	ABBA	Waterloo	\N	\N	\N	{pop}	\N	D	\N
1	Bajm	Co mi Panie dasz	\N	\N	\N	{rock,pop,Polish,ballad}	c (-4)	c (-4)	c (-4)
5	Chris Isaak	Wicked Game	\N	\N	\N	{pop,ballad}	h	\N	\N
55	Leonard Cohen	Hallelujah	\N	\N	\N	{ballad,Shrek,ballad}	\N	G (-4)	G (-4)
62	Bobby McFerrin	Don't Worry, Be Happy	\N	\N	\N	{pop}	\N	\N	D (+3)
45	Ella Fitzgerald	Cry Me a River	\N	\N	\N	{jazz}	g (-1)	\N	g (-1)
78	Frank Sinatra	Fly Me to the Moon	\N	\N	\N	{jazz}	\N	a	a
38	Krzysztof Zalewski & Maria Dębska	Nie będzie romansu	{"Krzysztof Zalewski","Maria Dębska"}	\N	Bo we mnie jest seks	{film,Polish,"Bo we mnie jest seks"}	c	\N	\N
21	Amy Winehouse	Back to Black	\N	\N	\N	{R&B,ballad}	d	\N	\N
25	Amy Winehouse	Will You Still Love Me Tomorrow	{"The Shirelles","Leslie Grace"}	\N	\N	{soul,ballad}	C	\N	\N
19	Tina Turner	Simply The Best	\N	\N	\N	{R&B,pop}	E (-1)	E (-1)	E (-1)
37	Cher	Believe	{"John Adams"}	\N	\N	{pop,soul,ballad}	E (-2)	\N	Fis
18	Amy Winehouse	Love Is a Losing Game	\N	\N	\N	{jazz,soul}	C	\N	\N
28	Imany	You Will Never Know	\N	\N	\N	{pop,R&B}	g	\N	\N
30	Lenny Kravitz	I Belong to You	\N	\N	\N	{pop,R&B}	c	\N	\N
34	Billie Eillish	Bossa Nova	\N	\N	\N	{pop,R&B}	g	\N	\N
36	Harry Styles	Watermelon Sugar	\N	\N	\N	{pop,R&B}	d	\N	\N
39	Miley Cyrus	Flowers	\N	\N	\N	{pop,R&B}	a	a	a
16	Brodka	Granda	{"Monika Brodka"}	{"Nie polubię Cię"}	\N	{rock,R&B,Polish}	e	e	e
24	sanah	Proszę pana	\N	\N	\N	{pop,Polish}	a (-2)	\N	\N
23	Beth Hart	Bang Bang Boom Boom	\N	\N	\N	{folk}	a	\N	\N
40	The Weeknd	Blinding Lights	\N	\N	\N	{pop,R&B,dance}	e (-1)	\N	\N
54	Krzysztof Krawczyk & Edyta Bartosiewicz	Trudno tak	{"Edyta Bartosiewicz","Krzysztof Krawczyk"}	\N	\N	{pop,Polish,R&B}	\N	e	\N
42	Lionel Ritchie	All Night Long	\N	\N	\N	{pop,R&B,dance}	G (-1)	\N	\N
73	Margaret	Wasted	\N	\N	\N	{pop,dance}	\N	e	\N
74	Moloko	Sing It Back	\N	\N	\N	{pop,dance}	\N	es	\N
61	Madonna	La Isla Bonita	{"Krzysztof Antkowiak"}	\N	\N	{meme,Spanish,pop,dance}	h (-2)	\N	\N
35	Lady Gaga	Bad Romance	\N	\N	\N	{pop,dance}	a	\N	\N
52	The Mamas & The Papas	Dream a Little Dream of You	\N	\N	\N	{jazz,R&B,pop}	\N	C (-1)	\N
53	ABBA	Lay All Your Love On Me	\N	\N	\N	{disco,musical,dance,pop}	\N	\N	h (-2)
64	ABBA	Mamma Mia	\N	\N	\N	{disco,musical,pop}	\N	D	D
22	Jessie J	Prize Tag	\N	\N	\N	{pop}	F	\N	\N
27	Imany	Don't Be So Shy	\N	\N	\N	{pop}	a	\N	\N
29	Destiny's Child	Survivor	\N	\N	\N	{pop}	a (+1)	\N	\N
32	Lykke Li	I Follow Rivers	\N	\N	\N	{pop}	F	\N	\N
26	Rufus & Chaka Khan	Ain't Nobody	{Rufus,"Chaka Khan","Felix Jaehn","Jasmine Thompson","Felix Jaehn & Jasmine Thompson"}	{"Ain't Nobody (Loves Me Better)"}	\N	{pop}	d (-1)	\N	d (-1)
95	Bing Crosby	It's Beginning to Look a Lot Like Christmas	{"Michael Bublé"}	\N	\N	{jazz,Christmas}	E (+1)	\N	\N
96	Wham!	Last Christmas	{"George Michael"}	\N	\N	{Christmas,pop}	D	\N	\N
97	Frank Sinatra	Santa Claus Is Coming to Town	{"Mariah Carey"}	\N	\N	{Christmas,pop}	G (-3)	\N	\N
98	Brenda Lee	Rockin' Around Christmas Tree	\N	\N	\N	{Christmas,R&B}	G (-1)	\N	\N
100	Sia	Snowman	\N	\N	\N	{pop,Christmas}	Des	\N	\N
99	Johnny Marks	Rudolph the Red-Nosed Reindeer	{"Zbigniew Wodecki","Gene Autry"}	{"Rudolf Czerwononosy"}	\N	{jazz,Christmas}	G (-1)	\N	\N
102	Laufey	From the Start	\N	\N	\N	{jazz,pop}	\N	es	\N
101	James Brown	I Got You (I Feel Good)	\N	{"I Got You","I Feel Good"}	\N	{soul,funk}	\N	D	\N
49	Laufey	Street by Street	\N	\N	\N	{jazz}	C	\N	\N
41	Kayah	Testosteron	\N	\N	\N	{pop,R&B}	d	d	d
31	LP	Lost on You	\N	\N	\N	{pop,R&B}	\N	\N	\N
46	Renata Przemyk	Jakby nie miało być	\N	\N	\N	{Polish}	h	\N	\N
47	Dawid Podsiadło	Nie kłami	\N	\N	\N	{pop,Polish}	e (-2)	\N	\N
48	Brodka	Miałeś być	{"Monika Brodka"}	\N	\N	{pop,Polish}	C	\N	\N
43	Whitney Houston	I Wanna Dance With Somebody	\N	\N	\N	{pop,R&B,dance}	E (-2)	E (-2)	E (-2)
50	Gone Gone Beyond	Another Earth	\N	\N	\N	{ballad}	a	\N	\N
33	George Michael	Careless Whisper	\N	\N	\N	{pop,R&B,ballad}	\N	\N	\N
44	Ania Karwan	Kiedy mrugam	{"Ania Karwan & Leszek Możdzer","Leszek Możdżer"}	\N	\N	{pop,Polish,ballad}	g	g	\N
65	4 Non Blondes	What's Up	\N	{Heeyyeeeyyaa}	\N	{rock,rock,pop}	\N	G (-2)	\N
79	Eugeniusz Bodo	Sex appeal	\N	\N	\N	{R&B,Polish}	\N	a (-5)	\N
80	\N	Wilcza zamieć	{"Anna Terpiłowska",sanah}	{"Pieśń Priscilli","Priscilla's Song"}	The Witcher 3	{"video game",Polish,ballad,wiedźmin,witcher}	\N	d	\N
81	Amy Winehouse	Rehab	\N	\N	\N	{R&B,pop}	\N	C	\N
82	Lady Pank	Mniej niż zero	\N	\N	\N	{Polish,rock,ballad}	\N	\N	e
83	Mr. Zoob	Kawałek podgłogi	\N	{"Mój jest ten kawałek podłogi"}	\N	{Polish,rock,pop,dance}	\N	\N	c
84	George Gershwin	Summertime	\N	\N	\N	{jazz}	d (+3)	\N	d (+3)
85	Ben E. King	Stand By Me	\N	\N	\N	{R&B}	\N	\N	A
86	Manaam	Krakowski spleen	\N	\N	\N	{Polish,rock,ballad}	h (-1)	\N	d (+2)
87	Teddy Swims	Lose Control	\N	\N	\N	{pop,R&B}	fis	\N	\N
91	Irving Berlin	White Christmas	{"Michael Bublé","Bing Crosby"}	\N	\N	{jazz,Christmas}	A	\N	\N
92	José  Feliciano	Feliz Navidad	{"Michael Bublé"}	\N	\N	{pop,rock,Christmas}	D	\N	\N
93	Eartha Kitt	Santa Baby	{Laufey}	\N	\N	{jazz,Christmas}	Des	\N	\N
88	Billie Eillish	L'Amour de Ma Vie	\N	\N	\N	{pop,R&B}	fis	\N	\N
89	Kalina Jędrusik	S.O.S.	{"Jerzy Wasowski & Jeremi Przybora","Jerzy Wasowski","Jeremi Przybora","Kabaret Starszych Panów"}	\N	\N	{Polish,jazz,ballad}	c	\N	\N
90	Frank Sinatra	Let It Snow	\N	\N	\N	{Christmas,jazz}	D	\N	\N
94	Frank Sinatra	Have Yourself a Merry Little Christmas	{"Michael Bublé","Judy Garland"}	\N	\N	{Christmas,jazz,ballad}	E (-4)	\N	\N
\.


--
-- TOC entry 3607 (class 0 OID 16393)
-- Dependencies: 218
-- Data for Name: solo; Type: TABLE DATA; Schema: public; Owner: adam
--

COPY public.solo (id, artist, youtube_link, musicsheet_link, capo, tags, title, known_from, title_alternative, artist_alternative) FROM stdin;
109	Vitas	https://youtu.be/_pgxzH0LprQ	\N	1	{meme,disco}	7th Element	\N	\N	\N
24	Jeanette	\N	\N	0	{pop,Spanish}	Porque te vas	\N	\N	\N
105	The Turtles	\N	\N	0	{rock}	So Happy Together	\N	\N	\N
33	Kai Rosenkranz	https://youtu.be/UceYjZdXE50	\N	4	{Gothic,"video game",instrumental}	Love Scene	Gothic	\N	\N
117	Queen	\N	\N	0	{rock}	Bohemian Rhapsody	\N	\N	\N
108	The Moody Blues	https://youtu.be/h--rMkVidn0	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270458	0	{rock}	Nights in White Satin	\N	\N	\N
40	Paul Anthony Romero	https://youtu.be/jyknsmfFxZQ	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270477	1	{"Heroes of Might and Magic 3","video game",instrumental}	Stronghold Theme	Heroes of Might and Magic 3	\N	\N
19	Celine Dion	\N	\N	2	{Titanic,film,ballad}	My Heart Will Go On	Titanic	\N	\N
123	Simon & Garfunkel	\N	\N	0	{rock}	The Sound of Silence	\N	\N	{"Paul Simon","Art Garfunkel"}
27	Ennio Morricone	https://youtu.be/NozcpiX9SYY	https://www.musicnotes.com/l/KNVKQ	0	{film,instrumental}	The Good, the Bad, and the Ugly	\N	{"Good Bad and Ugly"}	\N
146	The Mamas & The Papas	https://youtu.be/lKMQvZmWKDM	https://www.musicnotes.com/l/7BVKP	1	{jazz,pop}	Dream a Little Dream of You	\N	\N	\N
94	Edmund Fetting	https://youtu.be/vNL8f2D7yMo	https://www.musicnotes.com/l/3VxhW	0	{Polish,TV}	Deszcze niespokojne	\N	\N	{"Adam Walaciński"}
39	Paul Anthony Romero	https://youtu.be/trUvh5TXuJM	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270476	3	{"Heroes of Might and Magic 3","video game",instrumental}	Rampart Theme	Heroes of Might and Magic 3	\N	\N
72	Przemysław Gintrowski	\N	\N	0	{Polish,ballad}	Powrót	\N	\N	{"Jacek Kaczmarski","Kaczmarski, Gintrowski, Łapiński"}
83	KULT	\N	\N	0	{rock,Polish}	Nie dorosłem do swych lat	\N	\N	{Kazik,"Kazik Staszewski"}
76	Marek Grechuta	\N	\N	0	{Polish,ballad}	Dni, których nie znamy	\N	{"Dni, których jeszcze nie znamy"}	{"Jan Kanty Pawluśkiewicz"}
34	Kai Rosenkranz	https://youtu.be/xtXtTkKHoNA	\N	3	{Gothic,"video game",instrumental}	Gothic Piano	Gothic	\N	\N
74	Mieczysław Fogg	https://youtu.be/m72uwDJF5I0	\N	3	{"old song",Polish,ballad}	Ta ostatnia niedziela	\N	\N	\N
20	Jason Wade	\N	\N	4	{Shrek,film,pop,ballad}	You Belong to Me	Shrek	\N	\N
98	Krzesimir Dębski	https://youtu.be/iL_7Dt4jT0k	https://youtu.be/iL_7Dt4jT0k	5	{TV,Polish,instrumental}	Złotopolscy	\N	\N	\N
82	Krzysztof Krawczyk	\N	\N	2	{pop,Polish,ballad}	Bo jesteś ty	\N	\N	\N
111	ABBA	\N	\N	4	{pop,disco,musical}	Lay All Your Love On Me	\N	\N	\N
14	Krzesimir Dębski	\N	\N	0	{"Ogniem i mieczem",film,Polish,instrumental}	Pieśń Jana	Ogniem i mieczem	\N	\N
25	\N	\N	\N	0	{"Song of the Sea",film,folk}	Song of the Sea	Song of the Sea	\N	\N
99	Jerzy Matuszkiewicz	\N	\N	1	{TV,Polish,instrumental}	Janosik	\N	\N	\N
52	\N	\N	\N	0	{folk,Polish}	My Cyganie	\N	\N	{"Krzysztof Krawczyk"}
81	Czesław Niemen	\N	\N	0	{rock,Polish}	Sen o Warszawie	\N	\N	\N
89	Skaldowie	\N	\N	0	{TV,Polish}	Wszystko mi mówi, że mnie ktoś pokochał	\N	\N	\N
101	Big Cyc	https://youtu.be/yk40MNcyNXg	https://www.musicnotes.com/l/BxSNb	4	{TV,meme,Polish}	Świat według Kiepskich	\N	\N	\N
79	Krystyna Prońko	\N	\N	0	{rock,pop,Polish}	Jesteś lekiem na całe zło	\N	\N	\N
12	Hans Zimmer	https://www.youtube.com/shorts/C17YFECbRTw	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270460	0	{"The Pirates of the Carribean",film,Disney}	The Black Pearl	The Pirates of the Carribean	\N	\N
114	Toto	\N	\N	0	{rock,meme}	Africa	\N	\N	\N
15	Waldemar Kazanecki	https://youtu.be/GUBU5QzfUCw	\N	0	{"Noce i dnie",film,Polish,instrumental}	Walc Barbary	Noce i dnie	\N	\N
73	Krzysztof Krawczyk	https://youtu.be/Gk0okfosGTk	\N	3	{pop,Polish}	Chciałem być	\N	\N	\N
106	Leonard Cohen	\N	\N	0	{ballad,Shrek}	Hallelujah	\N	\N	\N
8	\N	https://youtu.be/sv2jHO5d48k	https://www.musicnotes.com/l/V9Vhp	1	{Frozen,film,Disney}	Let It Go	Frozen	{"Mam tę moc"}	\N
86	Krzysztof Krawczyk & Edyta Bartosiewicz	\N	\N	0	{pop,Polish,R&B}	Trudno tak	\N	\N	{"Krzysztof Krawczyk","Edyta Bartosiewicz"}
9	\N	https://youtu.be/taofqsdmV4k	https://www.musicnotes.com/l/dRGNJ	3	{Frozen,film,Disney}	Do You Want to Build a Snowman?	Frozen	{"Ulepimy dziś bałwana"}	\N
148	\N	https://youtu.be/9Ve8wu3K9gU	https://www.musicnotes.com/l/5R7KW	3	{film,musical,Disney,pop}	Breaking Free	High School Musical	\N	{"Jamie Houston","Zac Efron","Vanessa Hudgens","Zac Efron & Vanessa Hudgens"}
149	Deep Purple	https://www.youtube.com/shorts/4eTyorDOx30	\N	0	{rock,meme}	Smoke on the Water	\N	\N	\N
150	Johnny Marks	https://youtu.be/ZwMzDAKeecw	https://www.musicnotes.com/l/hGcKQ	0	{Christmas,jazz}	Rudolph the Red-Nosed Reindeer	\N	{"Rudolf Czerwononosy"}	\N
151	Brathanki	https://youtu.be/oIluZ2Vswm0	\N	\N	{meme,Polish,folk,rock}	Czerwone korale	\N	{"Sprężone korale","Sprenrzone korale"}	{WIXAPOL}
75	Krzysztof Antkowiak	\N	\N	0	{pop,meme,Polish}	Zakazany owoc	\N	\N	\N
118	Garou	\N	\N	2	{pop,French}	Gitan	\N	\N	\N
113	a-ha	\N	\N	0	{pop,disco}	Take On Me	\N	\N	\N
45	Danny McCarthy	https://youtu.be/-tge6UrZRDI	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270465	0	{"League of Legends","video game",instrumental,meme}	Silver Scrapes	League of Legends	\N	\N
96	Anna Jurksztowicz	\N	\N	0	{TV,Polish}	Na dobre i na złe	\N	\N	{"Krzesimir Dębski"}
133	Sting	\N	\N	0	{jazz,R&B}	Englishman in New York	\N	\N	\N
5	Hans Zimmer	https://youtu.be/yW_qibWbuA4	\N	0	{"The Lion King",film,Disney,musical,instrumental}	This Land	The Lion King	\N	\N
91	Igo, Mrozu & Vito Bambino	https://youtu.be/gprWhIp9Nc4	https://www.musicnotes.com/l/kVgNZ	0	{pop,Polish}	Supermoce	\N	\N	{Igo,Mrozu,"Vito Bambino","Męskie Granie Orkiestra","Męskie Granie"}
26	Dana Glover	\N	\N	0	{Shrek,rock,film,pop,ballad}	It Is You (I Have Loved)	Shrek	{"It Is You"}	\N
127	Elvis Presley	\N	\N	0	{pop,ballad}	Can't Help Falling in Love	\N	\N	\N
85	Ryszard Rynkowski	\N	\N	0	{pop,Polish,ballad}	Za młodzi, za starzy	\N	{"Za młodzi na sen","Za młodzi"}	\N
93	Edyta Górniak	https://youtu.be/Xn8SGAm542A	https://www.musicnotes.com/l/t3gKb	0	{pop,Polish,ballad}	To nie ja	\N	{"To nie ja byłam Ewą"}	\N
119	Bonnie Tyler	\N	\N	0	{pop,disco,Shrek}	Holding Out for a Hero	\N	{"I Need a Hero"}	\N
77	Budka Suflera	https://youtu.be/5EeSDh34M6Y	\N	0	{rock,meme,Polish,ballad}	Jolka, Jolka pamiętasz	\N	{Jolka,"Jolka, Jolka"}	{"Felicjan Andrzejczak"}
115	ABBA	https://youtu.be/ZfqBXueQrFg	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270456	0	{pop,disco,musical}	Dancing Queen	\N	\N	\N
144	Robert Miles	https://youtube.com/shorts/lij_Nit-6Hg	https://www.musicnotes.com/l/GdzK8	0	{pop,instrumental}	Children	\N	\N	\N
130	The Animals	\N	\N	0	{rock,ballad}	The House of the Rising Sun	\N	\N	\N
120	Roberta Flack	https://youtu.be/Y5nF33Jd5GU	https://www.musicnotes.com/l/CLzKF	1	{jazz,ballad}	Killing Me Softly	\N	{"Killing Me Softly With His Song"}	{Fugees,"Frank Sinatra"}
116	Katie Melua	\N	\N	0	{pop,ballad}	Spider's Web	\N	\N	\N
137	Coolio feat. L.V.	https://youtube.com/shorts/_UXWe-Yc50w	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270464	1	{meme,hip-hop,R&B}	Gangsta's Paradise	\N	\N	{"Stevie Wonder",Coolio,L.V.}
84	Kayah & Bregovic	\N	\N	0	{pop,Polish,ballad}	To nie jest ptak	\N	\N	{Kayah,Bregovic,"Goran Bregovic"}
35	Paul Anthony Romero	https://youtu.be/KsgsbY_AW_g	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270471	0	{"Heroes of Might and Magic 3","video game",instrumental}	Castle Theme	Heroes of Might and Magic 3	\N	\N
37	Paul Anthony Romero	https://youtu.be/eAPKDe-bvhI	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270473	0	{"Heroes of Might and Magic 3","video game",instrumental}	Dungeon Theme	Heroes of Might and Magic 3	\N	\N
10	\N	\N	\N	4	{"Vaiana (Moana)",film,Disney}	How Far I'll Go	Vaiana (Moana)	{"Pół kroku stąd"}	\N
132	Grover Washington Jr feat. Bill Withers	\N	\N	0	{jazz,R&B}	Just the Two of Us	\N	{"Two of Us"}	{"Grover Washington Jr","Bill Withers"}
38	Paul Anthony Romero	https://youtu.be/EmP4Pqi6xhU	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270474	0	{"Heroes of Might and Magic 3","video game",instrumental}	Fortress Theme	Heroes of Might and Magic 3	\N	\N
32	John Williams	https://youtube.com/shorts/9Op-y_CACYA	\N	0	{"Harry Potter",film,instrumental}	Hedwig's Theme	Harry Potter	{"Harry Potter"}	\N
55	\N	\N	\N	0	{folk}	Katyusha	\N	{Katiusza}	\N
138	Queen	https://youtu.be/b-IARRRCu4w	https://www.musicnotes.com/l/MkDhq	0	{rock}	The Show Must Go On	\N	{"Show Must Go On"}	\N
57	\N	\N	\N	0	{folk}	Shanty Medley	\N	{Shanty}	\N
1	\N	\N	\N	0	{TV,pop}	The Gummi Bears	\N	{"Gummi Bears",Gumisie}	{"Joseph Williams","Andrzej Zaucha"}
7	\N	\N	\N	0	{Mulan,film,Disney}	I'll Make a Man Out of You	Mulan	{"Zrobię z was mężczyzn"}	{"Matthew Wilder"}
6	\N	https://youtu.be/o2nWYwlduxY	https://www.musicnotes.com/l/vMKKP	2	{Mulan,film,Disney}	Reflection	Mulan	{Lustro}	{"Edyta Górniak","Christina Aguilera","Matthew Wilder"}
70	Andrew Lloyd Webber	https://youtu.be/BluunXnCAEQ	https://www.musicnotes.com/l/BfDN4	0	{"The Phantom of the Opera"}	The Phantom of the Opera	The Phantom of the Opera	\N	\N
58	\N	https://youtu.be/9bsD_0jU4gM	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270468	0	{Metro,musical,Polish,Christmas}	Uciekali	Metro	\N	\N
22	Yann Tiersen	https://youtu.be/N2GzBKH9XZ8	https://www.musicnotes.com/l/glxhw	0	{Amélie,film,French,instrumental}	Comptine d'un autre été: L'après-midi	Amélie	{"Comptine d'un autre été"}	\N
142	ABBA	https://youtu.be/GK_JztRZGO8	https://www.musicnotes.com/l/HMKKb	0	{pop,disco,musical}	Money, Money, Money	\N	\N	\N
23	Yann Tiersen	\N	\N	5	{Amélie,film,French,instrumental}	La Valse d'Amelie	Amélie	{"Amelia's Waltz","Valse d'Amelie"}	\N
68	\N	\N	\N	0	{Metro,musical,Polish,ballad}	Szyba	Metro	\N	{"Edyta Górniak","Katarzyna Groniec"}
18	\N	\N	\N	3	{"Love Story",film,ballad}	Love Story	Love Story	{"Where do I begin"}	\N
92	Artur Rojek	\N	\N	0	{pop,Polish,rock}	Do końca	\N	\N	\N
103	Frank & Nancy Sinatra	https://youtu.be/WjinqGIRHN8	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270459	2	{jazz}	Somethin' Stupid	\N	\N	{"Frank Sinatra","Nancy Sinatra","Robbie Williams","Nicole Kidman"}
28	Nino Rota	\N	\N	0	{"The Godfather",film,ballad,instrumental}	Speak Softly, Love	The Godfather	{"The Godfather Theme"}	\N
63	\N	https://youtu.be/oA2Gsugre-Y	https://www.musicnotes.com/marketplace/sheetmusic/MK0051226	0	{"Notre-Dame de Paris",French,musical}	Belle	Notre-Dame de Paris	\N	{Garou,"Riccardo Cocciante"}
64	\N	https://youtu.be/yxwSXgrGoo4	\N	0	{"Notre-Dame de Paris",French,musical}	Le Temps des Cathédrales	Notre-Dame de Paris	\N	{"Riccardo Cocciante"}
131	Whitney Houston	\N	\N	0	{pop,disco}	I Wanna Dance With Somebody	\N	\N	\N
41	Paul Anthony Romero	https://youtu.be/Jy_EohMNrG8	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270472	3	{"Heroes of Might and Magic 3","video game",instrumental}	Conflux Theme	Heroes of Might and Magic 3	\N	\N
61	\N	https://youtu.be/uhsAC8PaX38	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270454	0	{"La La Land",film,musical}	Audition	La La Land	\N	{"Justin Hurwitz","Emma Stone"}
42	Paul Anthony Romero	https://youtu.be/nwZqqvcvntw	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270475	5	{"Heroes of Might and Magic 3","video game",instrumental}	Inferno Theme	Heroes of Might and Magic 3	\N	\N
43	Paul Anthony Romero	https://youtu.be/9XWxXDdKozk	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270463	1	{"Heroes of Might and Magic 3","video game",instrumental}	Necropolis Theme	Heroes of Might and Magic 3	\N	\N
67	\N	\N	\N	0	{Metro,musical,Polish}	Bluzwis	Metro	\N	\N
13	Edyta Górniak & Mietek Szcześniak	https://youtu.be/WS1m1s13aJQ	\N	2	{"Ogniem i mieczem",film,Polish,ballad}	Dumka na dwa serca	Ogniem i mieczem	\N	{"Edyta Górniak","Mietek Szcześniak","Krzesimir Dębski"}
66	\N	https://youtu.be/AZ23dPU9bV8	\N	0	{Grease,film,musical}	Summer Nights	Grease	\N	{"John Travolta","Olivia Newton-John","John Travolta & Olivia Newton-John"}
54	\N	\N	\N	0	{folk,Polish}	Hej sokoły	\N	\N	\N
16	Edmund Fetting	https://youtu.be/-0eLovGdfrI	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270462	0	{"Prawo i pięść",film,Polish,ballad}	Nim wstanie dzień	Prawo i pięść	\N	{"Krzysztof Komeda",Komeda}
47	Imagine Dragons	https://youtu.be/WxcNdTHD7N4	https://www.musicnotes.com/l/R62Kp	0	{"League of Legends",rock,"video game"}	Warriors	League of Legends	\N	\N
95	Ryszard Rynkowski	\N	\N	0	{Klan,TV,Polish}	Życie jest nowelą	Klan	{Klan,"Jak pory roku Vivaldiego"}	{"Krzesimir Dębski"}
140	Miley Cyrus	https://youtu.be/zfCNXILaXx8	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0271044	0	{pop}	Flowers	\N	\N	\N
53	\N	\N	\N	0	{folk}	Greensleeves	\N	\N	\N
11	\N	\N	\N	1	{Pocahontas,film,Disney}	Colors of the Wind	Pocahontas	{"Kolorowy wiatr"}	{"Edyta Górniak","Vanessa Williams","Judy Kuhn"}
3	\N	https://youtu.be/uHTOVe7aAAE	https://www.musicnotes.com/l/TBGhX	0	{"The Lion King",film,Disney,musical}	Circle of Life	The Lion King	{"Krąg życia"}	{"Elton John","Carmen Twillie","Lebo M.","Beata Bednarz"}
147	\N	https://youtu.be/iG7vj-FwI1w	\N	7	{TV,Polish,instrumental}	Jeden z dziesięciu	\N	{"1 z 10"}	\N
88	Budka Suflera	\N	\N	0	{Polish}	Takie tango	\N	{"Bo do tanga"}	\N
121	Madonna	\N	\N	4	{meme,Spanish}	La Isla Bonita	\N	\N	{"Krzysztof Antkowiak"}
97	Tadeusz Woźnik	https://youtu.be/A5bwIotVARA	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270467	2	{Plebania,TV,meme,Polish,ballad}	Pośrodku świata	Plebania	{Plebania}	\N
124	Nancy Sinatra & Lee Hazlewood	\N	\N	0	{rock,pop,ballad}	Summer Wine	\N	\N	{"Nancy Sinatra","Lee Hazlewood","Lana Del Rey"}
145	Coldplay	https://youtube.com/shorts/tr9L_V1739k	\N	1	{rock,pop}	Fix You	\N	\N	\N
134	The Beatles	https://youtu.be/VA3w0SA6uv0	https://www.musicnotes.com/l/H9Vhq	0	{rock,pop,ballad}	Yesterday	\N	\N	{"Paul McCartney"}
78	Kwiat Jabłoni	https://youtu.be/20I0F24H31E	\N	5	{pop,Polish}	Dziś późno pójdę spać	\N	\N	\N
2	\N	\N	\N	2	{TV}	The Moomins	\N	{Moomins,Muminki}	\N
21	John Williams	https://youtu.be/fw9EIMp4s-0	\N	0	{"Star Wars",film,instrumental}	Leia's Theme	Star Wars	\N	\N
29	Nino Rota	https://youtu.be/LDAYr51MmbM	https://www.musicnotes.com/l/j9Vhw	0	{"The Godfather",film,instrumental}	The Godfather Waltz	The Godfather	\N	\N
135	The Beatles	\N	\N	0	{rock,pop}	Eleanor Rigby	\N	\N	{"Paul McCartney",Lennon/McCartney}
30	Vangelis	\N	\N	4	{"Chariots of Fire",film,instrumental}	Chariots of Fire	Chariots of Fire	\N	\N
110	Bobby McFerrin	\N	\N	0	{pop}	Don't Worry, Be Happy	\N	\N	\N
87	Krzysztof Krawczyk	https://youtu.be/VYJLRKATNic	https://www.musicnotes.com/l/MHlhp	0	{pop,Polish}	Mój przyjacielu	\N	\N	\N
71	Frederic Chopin	\N	\N	0	{Polish,instrumental,classic}	Nocturne op. 9 no. 2	\N	{"Nocturne in E flat major"}	\N
100	Wojciech Gąssowski	\N	\N	5	{TV,Polish}	M jak miłość	\N	\N	{"Mietek Jurecki"}
125	\N	https://youtube.com/shorts/BT8hfbsyiX8	\N	0	{jazz,film,"old song",Christmas}	White Christmas	\N	\N	{"Irving Berlin"}
56	\N	https://youtu.be/dB9D5C-ILpk	\N	0	{meme,"old song"}	USSR Anthem	\N	{"Russia's Anthem"}	\N
126	Baccara	https://youtu.be/SQCuRoITUt0	https://www.musicnotes.com/l/jlkKn	2	{pop,disco}	Yes Sir, I Can Boogie	\N	\N	\N
31	Bill Medley & Jennifer Warnes	\N	\N	0	{"Dirty Dancing",film,pop,disco,musical}	(I've Had) The Time of My Life	Dirty Dancing	{"The Time of My Life","Time of My Life"}	{"Bill Medley","Jennifer Warnes"}
4	Elton John	\N	\N	2	{"The Lion King",film,Disney,musical}	Can You Feel the Love Tonight	The Lion King	{"Miłość rośnie wokół nas"}	\N
80	Andrzej Piaseczny	https://youtu.be/vlaEF9xk-JY	\N	0	{Złotopolscy,TV,pop,Polish}	Pogodniej (złoty środek)	Złotopolscy	{Pogodniej,"Złoty środek","Złotopolscy piosenka"}	\N
129	ABBA	https://youtu.be/BJVndj7sSw0	https://www.musicnotes.com/l/HC9Nb	0	{pop,disco,musical}	Knowing Me, Knowing You	\N	\N	\N
17	\N	https://youtu.be/-r3y11MSALU	\N	1	{"Akademia Pana Kleksa",film,Polish}	Witajce w naszej bajce	Akademia Pana Kleksa	\N	\N
36	Paul Anthony Romero	https://youtu.be/f30zWeExFnk	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270470	0	{"Heroes of Might and Magic 3","video game",instrumental}	Main Menu Theme	Heroes of Might and Magic 3	\N	\N
107	ABBA	https://youtu.be/vsPv7lDJdLU	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270457	0	{pop,disco,musical}	Mamma Mia	\N	\N	\N
102	The Rembrandts	https://youtu.be/5GV6gcASy_M	https://www.musicnotes.com/l/RhHNS	0	{Friends,rock,TV,pop}	I'll Be There For You	Friends	\N	\N
69	\N	https://youtu.be/DE9Pgcm5k8s	https://www.musicnotes.com/l/N6HKb	0	{"Fiddler on the Roof",musical,ballad}	Sunrise, Sunset	Fiddler on the Roof	\N	{"Jerry Bock"}
143	Coldplay	https://youtu.be/-i5AcP-Yi04	https://www.musicnotes.com/l/vldKP	0	{rock,pop}	A Sky Full of Stars	\N	\N	\N
48	\N	\N	\N	0	{folk,Polish}	Hej Mazury	\N	\N	\N
44	Paul Anthony Romero	https://youtu.be/qGd9hydCpZI	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270478	0	{"Heroes of Might and Magic 3","video game",instrumental}	Tower Theme	Heroes of Might and Magic 3	\N	\N
49	\N	\N	\N	0	{folk,Polish}	Hej bystra woda	\N	\N	\N
50	\N	\N	\N	0	{folk,Polish}	Czerwone jabłuszko	\N	\N	\N
51	\N	\N	\N	0	{folk,Polish}	Prząśniczka	\N	\N	\N
90	sanah & Dawid Podsiadło	https://youtu.be/GI7l7l2gE1I	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270466	0	{rock,pop,folk,Polish}	ostatnia nadzieja	\N	\N	{sanah,"Dawid Podsiadło",Podsiadło}
46	\N	\N	\N	0	{"League of Legends","video game",instrumental}	Leage of Legends World Championship Theme	League of Legends	\N	\N
122	Frank Sinatra	\N	\N	0	{jazz,Christmas}	Let It Snow	\N	\N	{"Dean Martin"}
139	Irma Thomas	https://youtu.be/xst0emn60uA	\N	0	{R&B}	Anyone Who Knows What Love Is (Will Understand)	\N	{"Anyone Who Knows What Love Is"}	\N
141	4 Non Blondes	https://youtu.be/UHTWy-KN77U	https://www.musicnotes.com/l/cNMKw	0	{rock,pop}	What's Up	\N	{Heeyyeeeyyaa}	\N
136	Aqua	https://youtu.be/jp6JPvznFF4	https://www.musicnotes.com/l/V2Thp	0	{pop,meme,disco}	Barbie Girl	\N	\N	\N
112	Rick Astley	https://youtu.be/CMAadbjirkY	\N	1	{pop,meme,disco}	Never Gonna Give You Up	\N	{Rickroll}	\N
60	\N	https://youtu.be/DSLTvUqde9Y	https://www.musicnotes.com/sheetmusic/mtd.asp?ppn=MN0270455	0	{"La La Land",jazz,film,musical}	City of Stars	La La Land	\N	{"Justin Hurwitz","Emma Stone","Ryan Gosling","Ryan Gosling & Emma Stone"}
59	\N	\N	\N	3	{"La La Land",jazz,film,musical}	Another Day of Sun	La La Land	\N	\N
62	Justin Hurwitz	https://youtu.be/oSJLV8jkMwU	https://www.musicnotes.com/l/C35NS	2	{"La La Land",jazz,film,musical}	Mia & Sebastian's Theme	La La Land	\N	\N
65	\N	\N	\N	0	{"The Wizard of Oz",jazz,film,musical}	Somewhere Over the Rainbow	The Wizard of Oz	\N	\N
128	ABBA	https://youtu.be/BN5fiTn0M4I	https://www.musicnotes.com/l/xKMN8	0	{meme,disco,musical}	Gimme! Gimme! Gimme! (A Man After Midnight)	\N	{Gimme,"Gimme! Gimme!","Gimme! Gimme! Gimme!"}	\N
104	Smash Mouth	\N	\N	0	{Shrek,film,pop,meme}	All Star	Shrek	{"Somebody Once Told Me"}	\N
\.


--
-- TOC entry 3617 (class 0 OID 0)
-- Dependencies: 219
-- Name: duo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adam
--

SELECT pg_catalog.setval('public.duo_id_seq', 90, true);


--
-- TOC entry 3618 (class 0 OID 0)
-- Dependencies: 217
-- Name: solo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adam
--

SELECT pg_catalog.setval('public.solo_id_seq', 150, true);


--
-- TOC entry 3460 (class 2606 OID 16446)
-- Name: duo duo_pkey; Type: CONSTRAINT; Schema: public; Owner: adam
--

ALTER TABLE ONLY public.duo
    ADD CONSTRAINT duo_pkey PRIMARY KEY (id);


--
-- TOC entry 3458 (class 2606 OID 16400)
-- Name: solo solo_pkey; Type: CONSTRAINT; Schema: public; Owner: adam
--

ALTER TABLE ONLY public.solo
    ADD CONSTRAINT solo_pkey PRIMARY KEY (id);


-- Completed on 2025-01-08 14:38:15 CET

--
-- PostgreSQL database dump complete
--

