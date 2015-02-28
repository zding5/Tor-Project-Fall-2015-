USE Tor;

DROP TABLE IF EXISTS tortest3;
CREATE TABLE tortest3
(
  ServerID        	varchar(255) NOT NULL, 				# The ID for the authority server
  Server_Name     	varchar(255) NOT NULL,              # The Name for the authority server
  Time            	varchar(255) NOT NULL,              # The time when test was done??
  RelayID         	varchar(255) NOT NULL,              # The ID for the relay tested
  Relay_Name	  	varchar(255) NOT NULL,				# The Name for the relay tested
  Advertised_BW	  	int NOT NULL,						# The Bandwidth advertised by the relay
  Measured_BW  	  	int NOT NULL,



  PRIMARY KEY     (Time, Server_Name, RelayID)
);