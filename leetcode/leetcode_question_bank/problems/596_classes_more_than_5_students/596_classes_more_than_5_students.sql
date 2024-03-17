/*
-- Database: leetcode

-- DROP DATABASE IF EXISTS leetcode;

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
	
	
--- Leetcode problem:
--- 596. Classes More Than 5 Students
--- https://leetcode.com/problems/classes-more-than-5-students/description/
---

CREATE TABLE "leetcode"."leetcode_question_bank"."Courses" (
	student VARCHAR(80),
	class VARCHAR(80),
	PRIMARY KEY (student, class)
)
;


INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('A', 'Math');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('B', 'English');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('C', 'Math');

INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('D', 'Biology');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('E', 'Math');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('F', 'Computer');

INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('G', 'Math');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('H', 'Math');
INSERT INTO "leetcode"."leetcode_question_bank"."Courses"(student, class) VALUES ('I', 'Math');

SELECT
*
FROM
"leetcode"."leetcode_question_bank"."Courses"
;

*/


SELECT 
class
FROM
"leetcode"."leetcode_question_bank"."Courses"
GROUP BY 
class
HAVING count(class) >= 5
;



SELECT 
class
FROM
Courses
GROUP BY 
class
HAVING count(class) >= 5
;
