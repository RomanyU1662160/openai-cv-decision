import sqlite3


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def setup_database():
    database = "pdf_summarizer.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        skills text,
                                        experiences text,
                                        summary text,
                                        reasoning text
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()


def insert_user(name, email, skills, experiences, summary, reasoning):
    database = "pdf_summarizer.db"
    conn = create_connection(database)
    sql = """ INSERT INTO users(name,email,skills,experiences,summary,reasoning)
              VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, (name, email, skills, experiences, summary, reasoning))
    conn.commit()
    return cur.lastrowid