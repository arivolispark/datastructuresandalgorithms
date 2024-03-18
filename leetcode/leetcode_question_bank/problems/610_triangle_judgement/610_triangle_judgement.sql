--- Leetcode problem:
--- 610. Triangle Judgement
--- https://leetcode.com/problems/triangle-judgement/
---

/*
CREATE TABLE "leetcode"."leetcode_question_bank"."Triangle" (
	x INTEGER,
	y INTEGER,
	z INTEGER,
	PRIMARY KEY (x, y, z)
)
;


INSERT INTO "leetcode"."leetcode_question_bank"."Triangle"(x, y, z) VALUES (13, 15, 30);
INSERT INTO "leetcode"."leetcode_question_bank"."Triangle"(x, y, z) VALUES (10, 20, 15);

SELECT
*
FROM
"leetcode"."leetcode_question_bank"."Triangle"
;

*/

SELECT x, y, z,
CASE
    WHEN x+y>z AND x+z>y AND y+z>x THEN 'Yes'
	ELSE 'No'
END AS triangle
FROM 
Triangle
;
