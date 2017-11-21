# awssql

![Alt text](https://media.giphy.com/media/k4ZItrTKDPnSU/giphy.gif "Optional Title")

This particular repo uses an AWS EC2 instance to stream Twitter data from the Twitter API to an AWS RDS postgres database.

Acknowledgements
========

This was based heavily on work from the following sources:

- [tweetsql](https://github.com/karlward/tweetsql) 

- [Python Central sqlalchemy tutorial](http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/)

Overview
========

Steps:

1. Set up AWS services
2. Initialize database on AWS RDS
3. Stream Twitter data using a Python script and the [Twitter](https://pypi.python.org/pypi/twitter) library
4. Begin to analyze data in a Jupyter Notebook file.


Walk through
========

1. *AWS setup*

Navigate to AWS. Log in and create an EC2 instance and an RDS instance. There's lots of info online about setting up an EC2 instance, so you should be good there. Things to note:

- You can save your .pem file in this directory and it will be gitignored. 

In terms of RDS, this was newer to me. [This walkthrough](https://aws.amazon.com/getting-started/tutorials/create-connect-postgresql-db/) is helpful in demonstrating how to set up a postgres database on Amazon's machines. Things to note:

- In this repository, we'll set the username, databasename, and password to 'tweetsql'. You can obviously use whatever you like.
- Set your database link. In your secrets.py file, add a variable `link` set to the string given as your RDS endpoint. It should be something like: '<NAME>...<REGION>.rds.amazonaws.com/<NAME>'
- Crucially, you need to give your AWS EC2 instance write access to your database. To do this, find your EC2 IPv4 Public IP. It should be something like 123.45.67.89. Copy this. In your RDS, there should be an information 'i' after the endpoint link. Click here to edit secutiry details. Change the inbound. Add a new rule which allows a PostgreSQL connection on port 5432 with IP address found at your EC2. So if you EC2 public IP was 123.45.67.89, add IP 123.45.67.89/32. 

With this all set up, do the usual sets to get your EC2 instance connected. 

From the command line, you'll need to do the following:

1.1. Install git in your EC2 machine. Run these commands:

    ec2user$ sudo yum install git

1.2. Git clone this repo!

	ec2user$ git clone https://github.com/wnowak10/awssql.git

1.3. Install pip.

	ec2user$ curl -O https://bootstrap.pypa.io/get-pip.py
	ec2user$ sudo python get-pip.py

1.4. Install dependencies

	ec2user$ sudo pip install -r requirements.txt


2. *Initialize DB*

Using the Python Central notebook's basic walkthough, I wrote `initialize.py` to create a database and a table to store our data. This needs to be run before we can start streaming data. Run:

	ec2user$ python initialize.py

3. *Collect data*

Now for the fun. `collect.py` imports Twitter credentials stored in secrets.py (which must be created and placed in this directory). To get these, go [here](https://apps.twitter.com/). 

Then, we use Twitter python library to search current Twitter stream for the phrases mentioned. Feel free to replace whatever search term (or terms in a python list) you like. This is set in the 'TRACK' variable. 

Run:

	ec2user$ python collect.py

4. *Analyze Tweets!*

So I just dumped the entire Tweet JSON object into one row in a database. I'm better at using python, pandas, and the like, so I figured I'd keep everything and then parse what I needed in Python after the fact. From your home machine (not on AWS EC2 machine), launch a jupyter notebook.

	user $ jupyter notebook

From here, you should be able to follow along with steps written to access data that, assuming everything worked properly, streamed into your AWS RDS postgreSQL database! Hoorah.
