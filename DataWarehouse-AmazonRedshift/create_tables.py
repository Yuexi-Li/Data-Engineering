import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    To drop tables if exists in DB. 
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    To create staging  and analytics tables 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Connect to AWS Redshift, create sparkifydb DB. 
    Including drop any existing tables, create new tables. Close DB connection.
    """ 
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()