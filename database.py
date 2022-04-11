import psycopg2 as pg
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pg.connect(
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PW"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            database=os.environ.get("DB_NAME"),
        )
        self.curr = self.conn.cursor()

    def get_query(self, query_name):
        query = open(f"./SQL/{query_name}", "r")
        return query.read()

    def execute_query(self, query=None, query_name=None, filters=None):
        if query_name:
            query = self.get_query(query_name)

        if filters:
            query += f"\n {filters}"

        if query:
            self.curr.execute(query)
            records = self.curr.fetchall()
            return records

        return None


if __name__ == "__main__":
    ## example usage
    db = Database()
    records = db.execute_query(query="sample_query.sql", filters="WHERE 1=1")
