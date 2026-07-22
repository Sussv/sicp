.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name,b.size FROM dogs AS a,sizes AS b WHERE b.min<a.height AND a.height<=b.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child AS name FROM parents AS p, dogs AS d WHERE p.parent = d.name ORDER BY d.height DESC;


CREATE TABLE siblings AS
  SELECT a.child as a1,b.child as a2,c.size as a3 FROM parents AS a,parents AS b,size_of_dogs AS c,size_of_dogs AS d 
  WHERE a.parent=b.parent AND a.child<b.child AND a.child=c.name AND b.child=d.name AND c.size=d.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || a1 || " plus " || a2 || " have the same size: " || a3 FROM siblings;


-- The almighty midterm score of the SICP'25 students
CREATE TABLE midterm_almighty AS
  SELECT MAX(p1_wwpd)+MAX(p2_env)+MAX(p3_lists)+MAX(p4_functions)+MAX(p5_abstraction)+MAX(p6_tests)+MAX(p7_generators)+MAX(p8_bonus) FROM midterm;


CREATE TABLE scores AS
  SELECT 10*FLOOR(total/10) AS score FROM midterm;


-- The total score distribution of SICP'25 midterm exam
CREATE TABLE midterm_distribution AS
  SELECT score,COUNT(*) FROM scores GROUP BY score;
