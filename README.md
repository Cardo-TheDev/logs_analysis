# Logs Analysis

## About

This is an internal reporting tool that will use information from the database
to discover what kind of articles the site's readers like. The tool interacts
with a large database, with over a million rows, using complex queries to draw
business conclusions. The database contains newspaper articles, as well as the
web server log for the site. The log has a database row for each time a reader
loaded a web page. Using that information, the code will answer questions about
the site's user activity. The program will run from the command line. It won't
take any input from the user. Instead, it will connect to that database, use SQL
queries to analyze the log data, and print out the answers to some questions.

This tool is based on a project form Udacit's Full Stack Nanodegree program,
Intro to Relational Database. Building an informative summary from logs is a
real task that comes up very often in software engineering.

### What is needed:
You'll run these program using a Unix-style terminal on your computer; the
point of it is to be able to offer the same software (Linux and PostgreSQL)
regardless of what kind of computer you're running on. If you are using a Mac
or Linux system, your regular terminal program will do just fine. On Windows,
we recommend using the Git Bash terminal that comes with the Git software.

### Geting Started
- Download and install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
Install the platform package for your operating system. You do not need the
extension pack or the SDK. You do not need to launch VirtualBox after
installing it; Vagrant will do that. **Ubuntu users:** If you are running
Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead.
Due to a reported bug, installing VirtualBox from the site may uninstall other
software you need.
- Download and Install [vagrant](https://www.vagrantup.com/downloads.html). You
can check if vagrant is installed by running `vagrant --version`
- Download the [VM configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip). Unzip the file. Using the terminal, navigate into the vagrant subdirectory.
- Clone the **_logs-analysis_** project and move it into the vagrant
subdirectory. This particular step can actually be done at any point in time,
but to avoid any confusion, do this.
- From your terminal, inside the vagrant subdirectory, run the command
`vagrant up`. This will cause Vagrant to download the Linux operating system
and install it. This may take quite a while (many minutes) depending on how
fast your Internet connection is. When vagrant up is finished running, you will
get your shell prompt back. At this point, you can run `vagrant ssh` to log in
to your newly installed Linux VM! Inside the VM, change directory to
**/vagrant** and look around with `ls`.

The files you see here are the same as the ones in the vagrant subdirectory on
your computer (where you started Vagrant from). Any file you create in one will
be automatically shared to the other. This means that you can edit code in your
favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your
computer. But other data inside the VM is not. For instance, the PostgreSQL
database itself lives only inside the VM.

- Next, Download the news data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
You will need to unzip this file after downloading it. The file inside is
called _newsdata.sql_. Put this file into the vagrant subdirectory, which is
shared with your virtual machine. To load the data, cd into the vagrant
directory and use the command `psql -d news -f newsdata.sql`. Running this
command will connect to your installed database server and execute the SQL
commands in the downloaded file, creating tables and populating them with data.

Getting an error? Such as\- 
```
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused

```
\- this means the database server is not running or is not set up correctly.
This can happen if you have an older version of the VM configuration from
before this project was added. To continue, download the virtual machine
configuration into a fresh new directory and start it from there.

- If all else goes well, explore the data by connecting to it using
`psql news` command.

- To get the results of the queries in python file, run the
**_logs_analysis.py_** file in your virtual enviroment with this
command: `python3 logs_analysis.py`.

The desired output will then be displayed on your terminal.

### Custom Views Created:

```
CREATE VIEW request_count AS SELECT LEFT(CAST (time AS text), 10) AS date, COUNT(status) AS total_request FROM log GROUP BY date;

CREATE VIEW errors AS SELECT LEFT(CAST (time AS text), 10) AS date, COUNT(status) AS error_count FROM log WHERE status = '404 NOT FOUND' GROUP BY date;

CREATE VIEW one_percent_requests AS SELECT LEFT(CAST (time AS text), 10) AS date, COUNT(status)/100 AS one_percent FROM log GROUP BY date;

```
