BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, email TEXT, phone TEXT, website TEXT, regdate TEXT);
INSERT INTO "users" VALUES(1,'Ryu','tester@gmail.com','010-xxxx-xxxx','tester.com','2020-10-24 22:10:19');
INSERT INTO "users" VALUES(2,'Park','park@gmail.com','010-yyyy-yyyy','park.com','2020-10-24 22:10:19');
INSERT INTO "users" VALUES(3,'Lee','lee@gmail.com','010-zzzz-zzzz','lee.com','2020-10-24 22:10:19');
INSERT INTO "users" VALUES(4,'Cho','cho@gmail.com','010-0000-0000','cho.com','2020-10-24 22:10:19');
INSERT INTO "users" VALUES(5,'Yoo','yoo@gmail.com','010-0101-0101','yoo.com','2020-10-24 22:10:19');
COMMIT;
