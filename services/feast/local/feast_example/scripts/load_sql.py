import psycopg2
import datetime

# Connect to the DB
conn = psycopg2.connect(user="postgres",
                        password="secretpassword",
                        host="127.0.0.1",
                        port="5432",
                        database="postgres",
                        )
conn.autocommit = True
cur = conn.cursor()

tables = [
    "CORESTICKM159SFRBATL",
    "GDP",
    "USACPICORMINMEI",
    "M1V",
    "WM1NS"
]

for table in tables:
    table = table.lower()
    try:
        cur.execute("""
            DROP TABLE IF EXISTS %s;
        """ % table) 
    except Exception as e: 
        print(e)

    try:
        cur.execute("""
            CREATE TABLE %s (
            date text,
            value float
        )
        """ % table) 
    except Exception as e: 
        print(e)

    # Load CSV into the DB
    with open('./data/%s.csv' % table, 'r') as f:
        next(f) 
        cur.copy_from(f, table, sep=',')

    # Create and set event_record_created with now (fixes the tz.info error)
    now = datetime.datetime.now(datetime.timezone.utc)
    try:
        cur.execute("""
            ALTER TABLE %s
            ADD COLUMN event_record_created TIMESTAMP;
        """ % table)
    except Exception as e: print(e)

    try:
        cur.execute("""
            UPDATE %s
            SET event_record_created = '%s'
        """ % (table,now))
    except Exception as e: print(e)

    # Create and set event_timestamp with now (fixes the tz.info error)
    col = "date"
    try:
        cur.execute("""
            ALTER TABLE %s
            ADD COLUMN event_timestamp TIMESTAMP;
        """ % table)
    except Exception as e: print(e)

    try:
        cur.execute("""
            UPDATE %s
            SET event_timestamp = %s::timestamp
        """ % (table,col))
    except Exception as e: print(e)

# We also need a table of dates to easily use for entity_df's. 
start_date = "1975-01-01"
end_date = "2025-01-01"
try:
    cur.execute("""       
        DROP TABLE IF EXISTS _dates; 
        CREATE TABLE _dates (
            event_timestamp timestamp
        );
        INSERT INTO _dates (event_timestamp)
        SELECT i::timestamp
        FROM generate_series('%s', '%s', '1 day'::interval) i
    """ % (start_date,end_date))
except Exception as e: print(e)



