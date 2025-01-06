use employeedb;

SELECT phone, hire_date, emp_no, emp_name, ent_yn
FROM employee
where ent_yn = 'N'
AND phone like '%2'
ORDER BY hire_date
LIMIT 3;
