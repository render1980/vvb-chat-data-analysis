-- init schema VVB --
create schema vvb;
create table vvb.records ( id serial primary key, rectime timestamp DEFAULT current_timestamp, nick varchar(40) DEFAULT 'vvb bot', message text NULL);
grant all privileges on all tables in schema vvb to postgres;
grant all privileges on all sequences in schema vvb to postgres;
