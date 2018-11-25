#!/usr/bin/env python3
import psycopg2


query_1 = (
    "select title, count(path) as views from articles,"
    "log where articles.slug = substring(path, 10) group by path,"
    "title order by views desc limit 3")
query_2 = (
    "select name, count (substring(path, 10)) as views from authors, articles,"
    "log "
    "where authors.id = articles.author and "
    "articles.slug = substring(path, 10)"
    "group by name order by views desc;")
query_3 = (
    "select request_count.date, "
    "round(((error_count*100)/total_request::numeric), 2) from "
    "request_count, one_percent_requests, errors "
    "where request_count.date = one_percent_requests.date and "
    "one_percent_requests.date = errors.date "
    "and error_count > one_percent group by request_count.date, error_count,"
    "total_request;")


def print_views_result(log):
    # Prints out query results
    for data in log:
        print("%s - %s views" % (data[0], data[1]))
    print()


def connect(dbname="news"):
    # Connects to databse, else, it throws an exception
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return c, db
    except psycopg2.DatabaseError as error:
        print("Did not connect to database!!!")
        print(error)


def get_top_three_articles():
    # Extracts the top three articles arcoding to viewership
    c, db = connect()
    c.execute(query_1)
    log = c.fetchall()
    db.close()
    print("The top three articles are:")
    print_views_result(log)


get_top_three_articles()


def get_most_popular_article_authors():
    # Extracts most popular author according to views of their article
    c, db = connect()
    c = db.cursor()
    c.execute(query_2)
    log = c.fetchall()
    db.close()
    print("The most popular authors according to viewership are:")
    print_views_result(log)


get_most_popular_article_authors()


def get_error_greater_than_one_percent_of_request():
    ''' Gets the date where more than one percent of request led to errors
    Note that this query has custom tables (views) used to extract the data.
    Check the README file for more info. '''
    c, db = connect()
    c = db.cursor()
    c.execute(query_3)
    log = c.fetchall()
    db.close()
    print("The day(s) where more than 1% percent of"
          "request led to errors are:")
    for data in log:
        print("%s - %s %% errors" % (data[0], data[1]))


get_error_greater_than_one_percent_of_request()
