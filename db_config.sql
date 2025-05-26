psql -U postgres
create database lampdb;
\connect lampdb

create table lampdb_users(
	id bigserial primary key,
	email varchar(255) unique not null,
	uname varchar(255) unique not null,
	passwd text,
	joined_at timestamp default current_timestamp
);
