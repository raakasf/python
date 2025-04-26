import unittest
import oracledb
from unittest.mock import patch, MagicMock
from callfunc import Generate


class TestGetEmployeeSalary(unittest.TestCase):

    @patch("oracledb.connect")
    def test_get_employee_salary(self, mock_connect):
        # Arrange
        employee_id = 123
        expected_salary = 50000

        # Mock the connection and its callfunc method
        mock_connection = MagicMock()
        mock_connection.callfunc.return_value = expected_salary
        mock_connect.return_value = mock_connection

        # Act
        generator = Generate()
        actual_salary = generator.get_employee_salary(employee_id)

        # Assert
        mock_connection.callfunc.assert_called_once_with(
            "get_salary", int, keyword_parameters={employee_id}
        )
        self.assertEqual(actual_salary, expected_salary)


if __name__ == "__main__":
    unittest.main()
