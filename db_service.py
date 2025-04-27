import oracledb


class DatabaseService:
    def __init__(self, connection):
        self.connection = connection

    def fetch_user_age(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT age FROM users WHERE user_id = :id", {"id": user_id})
        row = cursor.fetchone()
        print(f"Fetched row: {row}")
        if row:
            return row[0]
        return None


if __name__ == "__main__":
    connection = oracledb.connect(
        user="system",
        password="oracle",
        dsn="localhost:1521/FREE",
    )
    service = DatabaseService(connection)
    age = service.fetch_user_age(user_id=1)
    print(f"User age: {age}")
    connection.close()
