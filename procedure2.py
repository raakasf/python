import oracledb

connection = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/FREE",
)

cursor = connection.cursor()

# Prepare output variables
out_username = cursor.var(str)
out_department = cursor.var(str)
out_age = cursor.var(int)
out_status = cursor.var(int)

cursor.callproc("get_user_info", [1, out_username, out_department, out_age, out_status])

if out_status.getvalue() == 0:
    print(
        f"User Info:\nName: {out_username.getvalue()}, Department: {out_department.getvalue()}, Age: {out_age.getvalue()}"
    )
else:
    print("User not found.")

cursor.close()
connection.close()
