"""
DML - Manipulação de dados
"""

import sqlite3


con = sqlite3.connect('base.db')

cur = con.cursor()


sql = """
INSERT INTO users(name, phone, email)
    VALUES('Paulo', 93293923929, 'silva@gmail.com')
"""


def db_insert(name, phone, email):
  return f"""
  INSERT INTO users(name, phone, email)
    VALUES('{name}', {phone}, '{email}')
  """


def db_update(name, email):
  return f"""
  UPDATE users SET name = '{name}' WHERE email = '{email}'
  """

def db_delete(email):
  return f"""
  DELETE FROM users WHERE email = '{email}'
  """

def db_select(data,field):
  return f"""
  SELECT id, name, phone, email
  FROM users
  WHERE {field}={data}
  """

cur.execute(db_select('3', 'id'))

#con.commit()

data = cur.fetchone()

con.close()

print(data)