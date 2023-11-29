DROP TABLE user_accounts;
DROP SEQUENCE user_accounts_seq;

CREATE SEQUENCE user_accounts_seq --lack permissions on temple server to auto generate an incremented unique ID, these changes solve that
    START WITH 1
    INCREMENT BY 1
    NOCACHE;

CREATE TABLE user_accounts (
    user_id NUMBER,
    username VARCHAR2(50) NOT NULL,
    password_hash VARCHAR2(64) NOT NULL,
    CONSTRAINT pk_user_id PRIMARY KEY (user_id)
);

CREATE OR REPLACE TRIGGER user_accounts_trigger
BEFORE INSERT ON user_accounts
FOR EACH ROW
BEGIN
    SELECT user_accounts_seq.NEXTVAL
    INTO :new.user_id
    FROM dual;
END;


 --Test Inputs Will remove later
INSERT INTO user_accounts(username, password_hash)
VALUES ('john_doe', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

INSERT INTO user_accounts (username, password_hash)
VALUES ('jane_smith', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4');

INSERT INTO user_accounts (username, password_hash)
VALUES ('alice_jones', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764');

SELECT * FROM user_accounts;

