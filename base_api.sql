PGDMP                         z            pythonprojet    11.14    11.14     	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16393    pythonprojet    DATABASE     ?   CREATE DATABASE pythonprojet WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United Kingdom.1252' LC_CTYPE = 'English_United Kingdom.1252';
    DROP DATABASE pythonprojet;
             postgres    false            ?            1259    16396 	   categorie    TABLE     q   CREATE TABLE public.categorie (
    id integer NOT NULL,
    libelle_categorie character varying(50) NOT NULL
);
    DROP TABLE public.categorie;
       public         postgres    false            ?            1259    16394    categorie_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.categorie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.categorie_id_seq;
       public       postgres    false    197                       0    0    categorie_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.categorie_id_seq OWNED BY public.categorie.id;
            public       postgres    false    196            ?            1259    16404    livres    TABLE     *  CREATE TABLE public.livres (
    id integer NOT NULL,
    isbn character varying(50) NOT NULL,
    titre character varying(255) NOT NULL,
    date_publication date NOT NULL,
    auteur character varying(50) NOT NULL,
    editeur character varying(50) NOT NULL,
    categorie_id integer NOT NULL
);
    DROP TABLE public.livres;
       public         postgres    false            ?            1259    16402    livres_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.livres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.livres_id_seq;
       public       postgres    false    199                       0    0    livres_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.livres_id_seq OWNED BY public.livres.id;
            public       postgres    false    198            ?
           2604    16399    categorie id    DEFAULT     l   ALTER TABLE ONLY public.categorie ALTER COLUMN id SET DEFAULT nextval('public.categorie_id_seq'::regclass);
 ;   ALTER TABLE public.categorie ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    197    196    197            ?
           2604    16407 	   livres id    DEFAULT     f   ALTER TABLE ONLY public.livres ALTER COLUMN id SET DEFAULT nextval('public.livres_id_seq'::regclass);
 8   ALTER TABLE public.livres ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    198    199    199                      0    16396 	   categorie 
   TABLE DATA               :   COPY public.categorie (id, libelle_categorie) FROM stdin;
    public       postgres    false    197   ?                 0    16404    livres 
   TABLE DATA               b   COPY public.livres (id, isbn, titre, date_publication, auteur, editeur, categorie_id) FROM stdin;
    public       postgres    false    199   ?                  0    0    categorie_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.categorie_id_seq', 6, true);
            public       postgres    false    196                       0    0    livres_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.livres_id_seq', 6, true);
            public       postgres    false    198            ?
           2606    16401    categorie categorie_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.categorie
    ADD CONSTRAINT categorie_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.categorie DROP CONSTRAINT categorie_pkey;
       public         postgres    false    197            ?
           2606    16409    livres livres_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_pkey;
       public         postgres    false    199            ?
           2606    16410    livres livres_categorie_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.livres
    ADD CONSTRAINT livres_categorie_id_fkey FOREIGN KEY (categorie_id) REFERENCES public.categorie(id);
 I   ALTER TABLE ONLY public.livres DROP CONSTRAINT livres_categorie_id_fkey;
       public       postgres    false    199    2694    197               f   x?%?;
?0 ?99EO ?????EW?A?Ec?sx1+????^??ی*|*a?e???H??:,?W??L?x???#????oilO?䞘R?A/?%C?B?#F         ?   x?UϱN?0?????9i?HۡK+6??s-???j;??鹘B?b??????||iu?"?&?ʘ?0??(??P?	?!?KU?iw?h??%MIGo;9?x????????Z?ȑ??idKq???i??o>??????(a??M=????^ػ??H???[???\d?iƑ)H???}?x_?.J?Й???<?Ш??,?????^??o3?swӪ???Ob%     