DROP TABLE user_accounts

CREATE TABLE user_accounts (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY, -- Auto-generated unique ID for each user
    username VARCHAR2(50) NOT NULL,
    password_hash RAW(64) NOT NULL, -- Assuming a 64-character hashed password
    lat DECIMAL(9,6), -- Assuming 6 decimal places for latitude
    lng DECIMAL(9,6),  -- Assuming 6 decimal places for longitude
    CONSTRAINT pk_user_id PRIMARY KEY (user_id),
    CONSTRAINT uc_username UNIQUE (username)
);
 --Test Inputs Will remove later
INSERT INTO user_accounts (username, password_hash)
VALUES ('john_doe', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

INSERT INTO user_accounts (username, password_hash)
VALUES ('jane_smith', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4');

INSERT INTO user_accounts (username, password_hash)
VALUES ('alice_jones', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764');

SELECT * FROM user_accounts