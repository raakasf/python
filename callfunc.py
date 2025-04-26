import oracledb


class Generate:
    def __init__(self):
        self.db = oracledb.connect(
            user="your_username", password="your_password", dsn="your_dsn"
        )

    def get_employee_salary(self, employee_id):
        # Use the instance's database connection
        cursor = self.db
        try:
            # Call the stored function using the connection object
            salary = cursor.callfunc(
                "get_salary", int, keyword_parameters={employee_id}
            )
            return salary
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            cursor.close()
