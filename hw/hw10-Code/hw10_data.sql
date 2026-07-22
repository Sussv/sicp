CREATE TABLE parents AS
  SELECT 'abraham' AS parent, 'barack' AS child UNION
  SELECT 'abraham'          , 'clinton'         UNION
  SELECT 'delano'           , 'herbert'         UNION
  SELECT 'fillmore'         , 'abraham'         UNION
  SELECT 'fillmore'         , 'delano'          UNION
  SELECT 'fillmore'         , 'grover'          UNION
  SELECT 'eisenhower'       , 'fillmore';

CREATE TABLE dogs AS
  SELECT 'abraham' AS name, 'long' AS fur, 26 AS height UNION
  SELECT 'barack'         , 'short'      , 52           UNION
  SELECT 'clinton'        , 'long'       , 47           UNION
  SELECT 'delano'         , 'long'       , 46           UNION
  SELECT 'eisenhower'     , 'short'      , 35           UNION
  SELECT 'fillmore'       , 'curly'      , 32           UNION
  SELECT 'grover'         , 'short'      , 28           UNION
  SELECT 'herbert'        , 'curly'      , 31;

CREATE TABLE sizes AS
  SELECT 'toy' AS size, 24 AS min, 28 AS max UNION
  SELECT 'mini'       , 28       , 35        UNION
  SELECT 'medium'     , 35       , 45        UNION
  SELECT 'standard'   , 45       , 60;

CREATE TABLE midterm AS
  SELECT 83 AS student_id, 6 AS p1_wwpd, 8 AS p2_env, 6 AS p3_lists, 3 AS p4_functions, 11 AS p5_abstraction, 5 AS p6_tests, 10.5 AS p7_generators, 1 AS p8_bonus, 50.5 AS total
  UNION
  SELECT 4, 13, 10, 8, 10, 16, 17, 17.0, 2, 93.0
  UNION
  SELECT 42, 11, 0, 6, 8, 14, 8, 12.5, 1, 60.5
  UNION
  SELECT 40, 8, 9, 6, 8, 11, 7, 10.5, 1, 60.5
  UNION
  SELECT 10, 11, 8, 9, 12, 18, 11, 16.0, 0, 85.0
  UNION
  SELECT 47, 6, 9, 5, 8, 8, 12, 9.5, 2, 59.5
  UNION
  SELECT 110, 4, 0, 5, 2, 8, 5, 12.0, 1, 37.0
  UNION
  SELECT 36, 8, 6, 5, 8, 13, 10, 11.0, 1, 62.0
  UNION
  SELECT 70, 10, 9, 4, 2, 9, 7, 12.0, 1, 54.0
  UNION
  SELECT 11, 13, 10, 9, 8, 17, 13, 13.0, 2, 85.0
  UNION
  SELECT 45, 9, 7, 7, 4, 11, 11, 10.0, 1, 60.0
  UNION
  SELECT 26, 9, 3, 5, 10, 14, 8, 14.0, 2, 65.0
  UNION
  SELECT 94, 6, 1, 5, 7, 11, 6, 11.0, 0, 47.0
  UNION
  SELECT 53, 9, 4, 3, 4, 15, 10, 12.5, 1, 58.5
  UNION
  SELECT 18, 10, 4, 8, 10, 16, 10, 15.0, 2, 75.0
  UNION
  SELECT 0, 15, 9, 9, 10, 19, 18, 16.0, 3, 99.0
  UNION
  SELECT 56, 10, 3, 7, 8, 10, 7, 12.0, 1, 58.0
  UNION
  SELECT 85, 8, 5, 7, 4, 11, 6, 7.0, 2, 50.0
  UNION
  SELECT 109, 6, 3, 4, 2, 8, 5, 8.0, 1, 37.0
  UNION
  SELECT 100, 7, 7, 2, 0, 10, 7, 8.0, 1, 42.0
  UNION
  SELECT 93, 6, 2, 6, 4, 12, 5, 10.0, 2, 47.0
  UNION
  SELECT 88, 8, 3, 8, 4, 9, 7, 9.0, 0, 48.0
  UNION
  SELECT 67, 5, 3, 5, 5, 6, 15, 14.0, 2, 55.0
  UNION
  SELECT 12, 10, 10, 7, 8, 14, 15, 16.0, 2, 82.0
  UNION
  SELECT 15, 11, 5, 7, 10, 19, 10, 15.5, 2, 79.5
  UNION
  SELECT 68, 7, 9, 8, 4, 16, 4, 3.0, 3, 54.0
  UNION
  SELECT 31, 7, 9, 6, 7, 13, 6, 15.0, 1, 64.0
  UNION
  SELECT 24, 12, 2, 5, 4, 17, 10, 15.0, 1, 66.0
  UNION
  SELECT 55, 9, 3, 6, 2, 14, 9, 13.0, 2, 58.0
  UNION
  SELECT 22, 10, 9, 7, 6, 9, 13, 13.0, 1, 68.0
  UNION
  SELECT 62, 10, 5, 8, 10, 7, 5, 9.0, 2, 56.0
  UNION
  SELECT 114, 7, 4, 2, 0, 6, 3, 10.0, 2, 34.0
  UNION
  SELECT 80, 9, 5, 7, 4, 10, 3, 13.5, 0, 51.5
  UNION
  SELECT 30, 5, 8, 7, 4, 8, 14, 16.5, 2, 64.5
  UNION
  SELECT 84, 11, 9, 3, 4, 8, 4, 10.5, 1, 50.5
  UNION
  SELECT 9, 9, 8, 8, 12, 18, 15, 16.0, 0, 86.0
  UNION
  SELECT 33, 11, 2, 1, 7, 16, 14, 12.0, 0, 63.0
  UNION
  SELECT 64, 9, 8, 3, 4, 15, 3, 13.0, 1, 56.0
  UNION
  SELECT 66, 6, 8, 6, 3, 11, 6, 13.0, 2, 55.0
  UNION
  SELECT 28, 10, 4, 7, 6, 14, 13, 11.0, 0, 65.0
  UNION
  SELECT 44, 10, 9, 6, 8, 10, 6, 10.0, 1, 60.0
  UNION
  SELECT 111, 8, 1, 6, 0, 7, 5, 6.0, 2, 35.0
  UNION
  SELECT 5, 11, 10, 9, 12, 18, 18, 13.0, 2, 93.0
  UNION
  SELECT 95, 9, 9, 4, 4, 2, 7, 10.0, 1, 46.0
  UNION
  SELECT 65, 8, 6, 5, 6, 10, 6, 13.0, 2, 56.0
  UNION
  SELECT 39, 13, 2, 3, 3, 17, 7, 14.0, 2, 61.0
  UNION
  SELECT 35, 13, 7, 6, 4, 13, 6, 13.5, 0, 62.5
  UNION
  SELECT 16, 9, 9, 9, 10, 15, 12, 13.0, 2, 79.0
  UNION
  SELECT 72, 10, 6, 8, 1, 12, 5, 12.0, 0, 54.0
  UNION
  SELECT 34, 11, 8, 5, 3, 12, 11, 12.0, 1, 63.0
  UNION
  SELECT 73, 10, 9, 7, 0, 10, 5, 12.0, 1, 54.0
  UNION
  SELECT 7, 12, 10, 9, 12, 12, 15, 16.0, 2, 88.0
  UNION
  SELECT 43, 10, 5, 5, 4, 15, 6, 13.0, 2, 60.0
  UNION
  SELECT 69, 6, 4, 8, 2, 13, 10, 10.0, 1, 54.0
  UNION
  SELECT 76, 7, 5, 6, 5, 14, 4, 11.5, 0, 52.5
  UNION
  SELECT 27, 8, 9, 9, 4, 13, 12, 9.0, 1, 65.0
  UNION
  SELECT 19, 11, 9, 7, 2, 16, 10, 15.5, 3, 73.5
  UNION
  SELECT 113, 9, 4, 1, 4, 8, 3, 4.0, 1, 34.0
  UNION
  SELECT 97, 7, 6, 4, 3, 13, 5, 6.0, 0, 44.0
  UNION
  SELECT 25, 7, 8, 8, 10, 12, 11, 8.0, 2, 66.0
  UNION
  SELECT 8, 12, 9, 7, 9, 16, 17, 15.5, 1, 86.5
  UNION
  SELECT 105, 4, 4, 5, 1, 10, 5, 10.0, 1, 40.0
  UNION
  SELECT 49, 9, 9, 4, 3, 17, 5, 12.0, 0, 59.0
  UNION
  SELECT 13, 13, 9, 9, 5, 15, 14, 14.0, 2, 81.0
  UNION
  SELECT 81, 7, 8, 3, 6, 8, 7, 12.0, 0, 51.0
  UNION
  SELECT 3, 14, 9, 7, 10, 19, 18, 17.0, 1, 95.0
  UNION
  SELECT 17, 12, 10, 9, 4, 17, 8, 15.5, 0, 75.5
  UNION
  SELECT 38, 8, 5, 8, 4, 13, 6, 16.0, 1, 61.0
  UNION
  SELECT 89, 4, 4, 1, 8, 6, 12, 10.0, 2, 47.0
  UNION
  SELECT 6, 12, 10, 9, 9, 19, 15, 16.0, 1, 91.0
  UNION
  SELECT 103, 5, 3, 6, 4, 10, 5, 6.0, 1, 40.0
  UNION
  SELECT 101, 7, 5, 5, 2, 10, 6, 7.0, 0, 42.0
  UNION
  SELECT 91, 9, 9, 5, 4, 5, 5, 10.0, 0, 47.0
  UNION
  SELECT 54, 8, 6, 6, 4, 10, 8, 15.0, 1, 58.0
  UNION
  SELECT 50, 10, 9, 7, 5, 10, 4, 13.0, 1, 59.0
  UNION
  SELECT 77, 8, 9, 4, 4, 8, 5, 14.5, 0, 52.5
  UNION
  SELECT 46, 12, 9, 7, 2, 14, 6, 9.0, 1, 60.0
  UNION
  SELECT 78, 11, 9, 3, 4, 10, 6, 9.0, 0, 52.0
  UNION
  SELECT 61, 9, 4, 6, 2, 13, 7, 15.0, 0, 56.0
  UNION
  SELECT 112, 4, 3, 1, 1, 8, 5, 12.0, 1, 35.0
  UNION
  SELECT 79, 7, 7, 4, 4, 10, 4, 14.0, 2, 52.0
  UNION
  SELECT 90, 9, 2, 1, 4, 11, 4, 14.0, 2, 47.0
  UNION
  SELECT 41, 12, 9, 6, 6, 11, 5, 10.5, 1, 60.5
  UNION
  SELECT 58, 10, 6, 3, 9, 12, 7, 9.0, 1, 57.0
  UNION
  SELECT 48, 6, 1, 8, 10, 12, 6, 15.0, 1, 59.0
  UNION
  SELECT 98, 6, 5, 3, 3, 11, 6, 9.0, 1, 44.0
  UNION
  SELECT 57, 10, 7, 3, 4, 11, 8, 14.0, 1, 58.0
  UNION
  SELECT 75, 4, 9, 5, 4, 11, 7, 11.0, 2, 53.0
  UNION
  SELECT 32, 10, 8, 5, 3, 9, 11, 16.0, 2, 64.0
  UNION
  SELECT 108, 7, 4, 2, 0, 8, 5, 12.0, 0, 38.0
  UNION
  SELECT 59, 9, 8, 5, 3, 10, 7, 15.0, 0, 57.0
  UNION
  SELECT 63, 7, 7, 4, 4, 12, 6, 14.0, 2, 56.0
  UNION
  SELECT 96, 11, 7, 1, 6, 6, 7, 8.0, 0, 46.0
  UNION
  SELECT 37, 11, 9, 5, 6, 11, 10, 9.0, 0, 61.0
  UNION
  SELECT 29, 8, 6, 6, 4, 15, 12, 14.0, 0, 65.0
  UNION
  SELECT 107, 8, 3, 5, 2, 11, 4, 5.0, 1, 39.0
  UNION
  SELECT 1, 15, 10, 9, 12, 19, 17, 17.0, 0, 99.0
  UNION
  SELECT 52, 9, 9, 7, 5, 2, 10, 15.5, 1, 58.5
  UNION
  SELECT 21, 12, 6, 5, 4, 16, 13, 13.0, 1, 70.0
  UNION
  SELECT 2, 15, 9, 9, 10, 19, 16, 17.0, 2, 97.0
  UNION
  SELECT 23, 6, 10, 7, 4, 13, 10, 16.0, 1, 67.0
  UNION
  SELECT 99, 8, 3, 4, 4, 10, 5, 9.0, 0, 43.0
  UNION
  SELECT 87, 9, 3, 3, 8, 10, 4, 11.0, 0, 48.0
  UNION
  SELECT 104, 5, 2, 3, 2, 12, 4, 10.0, 2, 40.0
  UNION
  SELECT 74, 7, 5, 6, 4, 12, 8, 11.0, 1, 54.0
  UNION
  SELECT 86, 9, 2, 2, 4, 16, 3, 11.0, 2, 49.0
  UNION
  SELECT 82, 7, 6, 6, 3, 13, 6, 9.0, 1, 51.0
  UNION
  SELECT 115, 5, 1, 3, 0, 5, 4, 9.0, 0, 27.0
  UNION
  SELECT 20, 7, 9, 8, 6, 14, 11, 16.0, 1, 72.0
  UNION
  SELECT 60, 8, 3, 7, 4, 14, 6, 14.0, 1, 57.0
  UNION
  SELECT 71, 9, 9, 7, 2, 8, 6, 12.0, 1, 54.0
  UNION
  SELECT 106, 7, 2, 4, 1, 11, 4, 9.5, 1, 39.5
  UNION
  SELECT 14, 14, 10, 9, 8, 17, 6, 15.0, 2, 81.0
  UNION
  SELECT 92, 11, 5, 3, 4, 10, 6, 8.0, 0, 47.0
  UNION
  SELECT 51, 8, 8, 7, 5, 12, 5, 12.0, 2, 59.0
  UNION
  SELECT 102, 6, 9, 7, 4, 8, 4, 0.0, 2, 40.0;
