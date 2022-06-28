select_movies_query = "SELECT title, release_year FROM movies LIMIT 5"
with connection.cursor() as cursor:
     cursor.execute(select_movies_query)
     for row in cursor.fetchall():
        print(row)

('Forrest Gump', 1994)
('3 Idiots', 2009)
('Eternal Sunshine of the Spotless Mind', 2004)
('Good Will Hunting', 1997)
('Skyfall', 2012)

# >>> cursor.execute("SELECT * FROM employees ORDER BY emp_no")
# >>> head_rows = cursor.fetchmany(size=2)
# >>> remaining_rows = cursor.fetchall()

# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

SELECT t1.name, t2.salary FROM employee AS t1, info AS t2
  WHERE t1.name = t2.name;

SELECT t1.name, t2.salary FROM employee t1, info t2
  WHERE t1.name = t2.name;