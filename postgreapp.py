import psycopg2 as psg

connect_str = "dbname = 'trump_tweets' user='postgres' host='127.0.0.1' " + \
              "password = 'Karolina69!'"

conn = psg.connect(connect_str)

cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE test (
# name char(40));
# """)

# from sqlalchemy import create_engine
# import pandas as pd
# df = pd.DataFrame({'name': ['User1', 'User2', 'User3']})
# engine = create_engine('postgresql://postgres:Karolina69!@localhost:5432/trump_tweets')
# df.to_sql('pandas_example', engine)

conn.commit()
conn.close()