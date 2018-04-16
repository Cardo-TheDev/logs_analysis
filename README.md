# Logs Analysis

## About

This is a project, part of Udacit's IPND program, Back-End specialization, Intro to Relational Database.
This program serves as an **internal reporting tool**, that interacts with a large database, with over a million rows, using complex queries to draw business conclusions.

Building an informative summary from logs is a real task that comes up very often in software engineering.

### What is needed:
- The VirtualBox VM environment
- The Vagrant configuration program
- [News Data File](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Python 2 or 3

### Geting Started

This program runs on a Linux virtual machine (VM), with PostgreSQL database installed on it.

Starting up the machine `vagrant up`, and log in `vagrant ssh`. Navigate to project vagrant folder directory. To access databse, run `psql -d news -f newsdata.sql`. To run python file, `python logs_analysis.py`

The desired output will then be displayed.
### Custom Views Created:

```
create view requests as select left(cast (time as text), 10) as date, status from log group by time, status;

create view errors as select date, count(status) as error_count from requests where status = '404 NOT FOUND' group by date;

create view one_percent_requests as select date, count (status)/100 as one_percent from requests group by date;

create view request_count as select date, count(status) as total_request from requests group by date;

```

