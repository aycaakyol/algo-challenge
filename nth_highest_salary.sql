-- Problem: https://leetcode.com/problems/nth-highest-salary/

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    
      select e.salary from employee e
      order by e.salary offset N-1 limit 1
  );
END;
$$ LANGUAGE plpgsql;