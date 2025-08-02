import oracledb

connection = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/FREE",
)

cursor = connection.cursor()

# Prepare output variable
out_age = cursor.var(int)

# Call the stored procedure
cursor.callproc("get_user_age", [1, out_age])

print(f"User age is: {out_age.getvalue()}")

cursor.close()
connection.close()
