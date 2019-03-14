#!/usr/bin/env python3
import psycopg2


query_1 = (
    "SELECT title, COUNT(path) AS views FROM articles,"
    "log WHERE articles.slug = SUBSTRING(path, 10) GROUP BY path,"
    "title ORDER BY views DESC LIMIT 3")
query_2 = (
    "SELECT name, COUNT(SUBSTRING(path, 10)) AS views FROM authors, articles,"
    "log "
    "WHERE authors.id = articles.author AND "
    "articles.slug = SUBSTRING(path, 10)"
    "GROUP BY name ORDER BY views DESC;")
query_3 = (
    "SELECT request_count.date, "
    "ROUND(((error_count)/total_request::numeric)*100, 2) FROM "
    "request_count, one_percent_requests, errors "
    "WHERE request_count.date = one_percent_requests.date AND "
    "one_percent_requests.date = errors.date "
    "AND error_count > one_percent GROUP BY request_count.date, error_count,"
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


def get_most_popular_article_authors():
    # Extracts most popular author according to views of their article
    c, db = connect()
    c = db.cursor()
    c.execute(query_2)
    log = c.fetchall()
    db.close()
    print("The most popular authors according to viewership are:")
    print_views_result(log)


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
          " request led to errors are:")
    for data in log:
        print("%s - %s %% errors" % (data[0], data[1]))


if __name__ == '__main__':
    get_top_three_articles = get_top_three_articles()
    get_most_popular_article_authors = get_most_popular_article_authors()
    get_error_greater_than_one_percent_of_request = \
        get_error_greater_than_one_percent_of_request()
