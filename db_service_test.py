from unittest.mock import MagicMock
import db_service


def test_fetch_user_age():
    fake_cursor = MagicMock()
    fake_cursor.fetchone.return_value = (30,)

    fake_connection = MagicMock()
    fake_connection.cursor.return_value = fake_cursor

    service = db_service.DatabaseService(fake_connection)

    age = service.fetch_user_age(user_id=123)

    assert age == 30
    fake_cursor.execute.assert_called_once_with(
        "SELECT age FROM users WHERE user_id = :id", {"id": 123}
    )
    fake_connection.cursor.assert_called_once()
