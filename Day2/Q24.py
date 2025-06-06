""" 24 : write a program to count number of times SQL is there in this paragraph (with any case : sql or SQL or Sql)

SQL is a powerful language used to manage and query relational databases. With SQL  you can 
easily retrieve specific data using SELECT statements, update records with UPDATE, or remove unwanted 
entries using DELETE. Learning sql is essential for data analysts, as most data stored in companies resides in SQL 
based systems. Advanced SQL techniques like window functions and common table expressions allow for more complex data manipulation. 
Whether you are
 building dashboards or running reports, SQL is the foundation of effective data analysis. """

string = """SQL is a powerful language used to manage and query relational databases. With SQL  you can easily retrieve specific data using SELECT statements, update records with UPDATE, or remove unwanted 
entries using DELETE. Learning sql is essential for data analysts, as most data stored in companies resides in SQL 
based systems. Advanced SQL techniques like window functions and common table expressions allow for more complex data manipulation. 
Whether you are building dashboards or running reports, SQL is the foundation of effective data analysis."""

print(string.upper().count('SQL'))
