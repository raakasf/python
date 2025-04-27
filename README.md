# How to setup and run
docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PASSWORD=oracle gvenzl/oracle-xe

sqlplus system/oracle@localhost:1521/FREE

CREATE TABLE users (
    user_id NUMBER PRIMARY KEY,
    username VARCHAR2(50),
    age NUMBER
);

INSERT INTO users (user_id, username, age) VALUES (1, 'Alice', 25);
INSERT INTO users (user_id, username, age) VALUES (2, 'Bob', 28);
INSERT INTO users (user_id, username, age) VALUES (3, 'Charlie', 32);

COMMIT;

SELECT * FROM users;

python my_db_service.py
