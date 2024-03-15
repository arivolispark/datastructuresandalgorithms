-- Database: leetcode
-- Schema: leetcode_question_bank

	
DROP TABLE "leetcode"."leetcode_question_bank"."World";

CREATE TABLE "leetcode"."leetcode_question_bank"."World" (
	name VARCHAR(80) NOT NULL,
	continent VARCHAR(40),
	area INTEGER,
	population INTEGER,
	gdp BIGINT,
	PRIMARY KEY (name)	
);

INSERT INTO "leetcode"."leetcode_question_bank"."World" (name, continent, area, population, gdp) VALUES ('Afghanistan', 'Asia', 652230, 25500100, 20343000000);
INSERT INTO "leetcode"."leetcode_question_bank"."World" (name, continent, area, population, gdp) VALUES ('Albania', 'Europe', 28748, 2831741, 12960000000);
INSERT INTO "leetcode"."leetcode_question_bank"."World" (name, continent, area, population, gdp) VALUES ('Algeria', 'Africa', 2381741, 37100000, 188681000000);
INSERT INTO "leetcode"."leetcode_question_bank"."World" (name, continent, area, population, gdp) VALUES ('Andorra', 'Europe', 468, 78115, 3712000000);
INSERT INTO "leetcode"."leetcode_question_bank"."World" (name, continent, area, population, gdp) VALUES ('Angola', 'Africa', 1246700, 20609294, 100990000000);

SELECT * FROM "leetcode"."leetcode_question_bank"."World";


--- Problem solution
SELECT 
name, population, area
FROM 
"leetcode"."leetcode_question_bank"."World"
WHERE
area >= 3000000
OR
population >= 25000000
;
