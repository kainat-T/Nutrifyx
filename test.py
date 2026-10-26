import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\instantclient_21_19")

conn = oracledb.connect(
    user="KT",
    password="123456789",
    dsn="//localhost:1521/xe" 
)

print("Connected successfully!")

cur = conn.cursor()
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)

cur.close()
conn.close()
