-- Database: leetcode

-- DROP DATABASE IF EXISTS leetcode;

/*
CREATE DATABASE leetcode
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
--- Leetcode problem
--- 511. Game Play Analysis I
---

CREATE TABLE "leetcode"."leetcode_question_bank"."511_Activity" (
	player_id INTEGER,
	device_id INTEGER,
	event_date DATE,
	games_played INTEGER,
	PRIMARY KEY (player_id, event_date)
)

INSERT INTO "leetcode"."leetcode_question_bank"."511_Activity" VALUES(1, 2, '2016-03-01', 5);
INSERT INTO "leetcode"."leetcode_question_bank"."511_Activity" VALUES(1, 2, '2016-05-02', 6);
INSERT INTO "leetcode"."leetcode_question_bank"."511_Activity" VALUES(2, 3, '2017-06-25', 1);
INSERT INTO "leetcode"."leetcode_question_bank"."511_Activity" VALUES(3, 1, '2016-03-02', 0);
INSERT INTO "leetcode"."leetcode_question_bank"."511_Activity" VALUES(3, 4, '2018-07-03', 5);


SELECT 
* 
FROM 
"leetcode"."leetcode_question_bank"."511_Activity"
;

*/


SELECT 
player_id,
MIN(event_date) AS first_login
FROM 
"leetcode"."leetcode_question_bank"."511_Activity"
GROUP BY
player_id
ORDER BY
player_id
;
