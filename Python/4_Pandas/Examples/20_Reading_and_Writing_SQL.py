import pandas as pd
from sqlalchemy import create_engine

mysql_cn= create_engine("mysql://anto:anto131284@hinton/my_database")
#mysql_cn= create_engine("{flavor}://{username}:{password}@{host}/{database}")

df_mysql = pd.read_sql('select * from colored_objects;', mysql_cn)  
  
print df_mysql

df_mysql.to_csv('colored_objects.csv', sep = '\t', index=None, header=None)

print  pd.read_sql('select color from colored_objects;', mysql_cn) 

print  pd.read_sql('select * from colored_objects where id =2;', mysql_cn) 

#create table colors in my_database
pd.read_sql('select color from colored_objects;', mysql_cn).to_sql('colors', mysql_cn)

print  pd.read_sql_query('select * from colors;', mysql_cn) 
print  pd.read_sql_query('show tables; drop table colors;', mysql_cn)
print  pd.read_sql_query('show tables;', mysql_cn) 
