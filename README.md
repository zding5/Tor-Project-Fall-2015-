# Tor-Project-Fall-2015-
The Project of Analyzing Tor Relays with False Claiming Bandwidth

## Purpose
  * This repository is for research purpose on the topic of The Onion Router (Tor).
The focus is to determine the potentially malicious relays that false claim their bandwidth. The process includes collecting bandwidth data from reliable source, storing and organizing data with MySQL databases, plotting critical information (gnuplot) and analyzing.

## Research Workflow
  * See the poster.jpg for the project

## Procesure

###-Download Tor relay data files for certain months (usually use the newest, we used 2014-10) from:
  * https://collector.torproject.org/archive/relay-descriptors/votes/


###-Read all data files:
  
  * Extract the downloaded tar.xz file
  
  * The data will be organized by month and contained in folders labeled with month (../01,../02...), with a parent folder. 

  * Set up a MySQL server, create a database called 'Tor', then use source Tor.sql to create tables in 'Tor'

  * Run 'massive_reader.py' with parameters: your data parent path, database ip, database user, database password and database name.

  * Now all the data should be well organized in database.


###-Dump data to local

  * The database was set up for your future organizing or operation on the data. We still want the rest of the analysis to go on at local for speed.

  * Run 'database_dumper.py' with parameters: database ip, database user, database password, database table containing data.

  * You will get all data dumped into a .csv file


###-Analyze Data

  * Run 'data_selector_local(new)'

  * You will get multiple .csv files containing data for the top 25 most deviated bandwidth relays


###-Plotting

  * Run 'plotter.py' at your parent folder of all the generated .csv files folders
  
  * You will get the deviation bandwidth for each relay given by 4 testing servers in one chart for each relay.





