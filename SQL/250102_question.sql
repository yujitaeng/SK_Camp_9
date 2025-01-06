use employeedb;

# Q1 - 연습
-- SELECT emp_name, sal_level, salary, emp_no, email, phone, hire_date
-- FROM employee
-- ORDER BY salary DESC;

# Q1 쌤 풀이
SELECT e.emp_name, e.sal_level, e.salary, e.emp_no, e.email, e.phone, e.hire_date, j.job_name
FROM employee e
JOIN job j on job_code = j.job_code -- USING (job_code) 로 쓸 수도 있음
WHERE e.ent_yn <> 'Y'
AND j.job_name = '대리'
ORDER BY e.salary DESC;

# Q2 쌤풀이
SELECT d.dept_title AS 부서명, count(*) AS 인원, sum(e.salary) AS 급여합계, avg(e.salary) AS 급여평균
  FROM employee e
  JOIN department d ON e.dept_code = d.dept_id
 WHERE e.ent_yn <> 'Y'
GROUP BY d.dept_title
WITH ROLLUP;

# Q3단계 쌤풀이
SELECT e.emp_name, e.emp_no, e.phone, d.dept_title, j.job_name
FROM employee e
LEFT JOIN department d on e.dept_code = d.dept_id
JOIN job j USING (job_code)
ORDER BY e.hire_date;

# Q4 1단계 쌤풀이
SELECT count(*)
FROM employee
WHERE manager_id IS NOT NULL;

# Q4 2단계 쌤풀이
SELECT count(*)
FROM employee e1
JOIN employee e2 on e1.manager_id = e2.emp_id;

# Q4 3단계 쌤풀이
SELECT e1.emp_name, e2.emp_name
FROM employee e1 # 직원 정보
LEFT JOIN employee e2 on e1.manager_id = e2.emp_id; # 관리자 정보

# Q4 4단계 쌤풀이
SELECT e1.emp_name, e2.emp_name, d1.dept_title, d2.dept_title
FROM employee e1 
JOIN employee e2 on e1.manager_id = e2.emp_id
JOIN department d1 on e1.dept_code = d1.dept_id
JOIN department d2 on e2.dept_code = d2.dept_id;
