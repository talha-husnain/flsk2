from sqlalchemy import create_engine, text
import os
con_string = os.environ['PASS_1']

engine = create_engine(con_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))
  columns = result.keys()
  result_dic = [dict(zip(columns, row)) for row in result]
  print(result_dic)
