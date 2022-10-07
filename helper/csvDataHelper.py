import sys
from datetime import datetime
import pandas as pd
from django.conf import settings
from psycopg2 import extras
from psycopg2._psycopg import OperationalError
from sqlalchemy.dialects.postgresql import psycopg2
from psycopg2 import connect
import logging
from helper.Validator import ValidatUrl

#logger = logging.getLogger(__name__)
conn_params_dic = {
    "host": settings.DATABASES['default']['HOST'],
    "database": settings.DATABASES['default']['NAME'],
    "user": settings.DATABASES['default']['USER'],
    "password": settings.DATABASES['default']['PASSWORD']
}
dbConnection = None

# Define a function that handles and parses psycopg2 exceptions
def show_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()
    # get the line number when exception occured
    line_n = traceback.tb_lineno
    # print the connect() error
    print("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)
    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)
    # print the pgcode and pgerror exceptions
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")

# Define a connect function for PostgreSQL database server
def connect_to_postgres(conn_params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL...........')
        conn = connect(**conn_params_dic)
        print("Connection successful..................")
        #logger.debug('Connection successful..................')
    except Exception as err:
        print("Oops! An exception has occured:", err)
        print("Exception TYPE:", type(err))
        #logger.debug("Oops! An exception has occured:", err)
    except OperationalError as err:
        # passing exception to function
        show_psycopg2_exception(err)
        # set the connection to 'None' in case of error
        conn = None
    return conn

# Define function using psycopg2.extras.execute_batch() to insert the dataframe
def execute_batch(conn, datafrm, table, page_size=150):
    print("in execute_batch...")
    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]

    # dataframe columns with Comma-separated
    cols = ','.join(list(datafrm.columns))

    # SQL query to execute
    sql = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, sql, tpls, page_size)
        conn.commit()
        print("Data inserted using execute_batch() successfully...")
        #logger.debug("Data inserted using execute_batch() successfully...")
    except Exception as err:
        print("Oops! An exception has occured:", err)
        #logger.debug("Oops! An exception has occured:", err)
        print("Exception TYPE:", type(err))
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)
        cursor.close()

# Define function for delete all record before insert
def empty_table(table):
    print("in empty_table...")
    # Connect to the database
    dbConnection = connect_to_postgres(conn_params_dic)

    # prepaired SQL query to execute
    sql = "DELETE FROM %s(%s) " % (table)
    cursor = dbConnection.cursor()

    try:
        cursor.execute(cursor, sql)

        # Closing the cursor & connection
        cursor.close()
        dbConnection.close()
        print("All record deleted successfully...")
        #logger.debug("All record deleted successfully...")
    except Exception as err:
        print("Oops! An exception has occured:", err)
        #logger.debug("Oops! An exception has occured:", err)
        print("Exception TYPE:", type(err))
    except (Exception, psycopg2.DatabaseError) as err:
        # pass exception to function
        show_psycopg2_exception(err)

#import function for import csv data to postgres
def do_import(csvData, pageSize):
    # Connect to the database
    dbConnection = connect_to_postgres(conn_params_dic)
    dbConnection.autocommit = True
    # Run the execute_batch method
    execute_batch(dbConnection, csvData, 'assignment_information', pageSize)

#create chunck for import
def chunck_creator(filename, header=False, chunk_size = 15):
   for chunk in pd.read_csv(filename, delimiter=',', iterator=True, chunksize=chunk_size, parse_dates=[1]):
        yield (chunk)

#get creator for chunck generator
def _creator(filename, header=False, chunk_size = 15):
    chunk = chunck_creator(filename, header=False, chunk_size=chunk_size)
    for row in chunk:
        yield row

# Define function for read csv data from file and use in scheduler
def read_csv_data():
    #logger.debug("read_csv_data fired... at", str(datetime.now()))
    #check is file url is valid and file exist in url then start
    if settings.CSVURL and ValidatUrl(settings.CSVURL):
        empty_table('assignment_information')
        generator = _creator(filename=settings.CSVURL, chunk_size=15)
        while True:
            date = next(generator)
            do_import(date, 15)
            #next(generator)
        # Close the connection
        dbConnection.close()

#test job
def testJob():
    print('job run at=', str(datetime.now()))



