use FileIdentification;
create table Information(
	extension    varchar(100) NOT NULL,
	description  mediumtext,
	type 	     varchar(200) DEFAULT NULL,
	applications mediumtext,
	Primary Key(extension));