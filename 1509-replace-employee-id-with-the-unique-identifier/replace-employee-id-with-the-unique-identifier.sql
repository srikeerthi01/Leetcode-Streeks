# Write your MySQL query statement below
select u.unique_id,e.name from
Employees e  left join EmployeeUNI u on
e.id = u.id;
#we used left join becoz we need all names to be displayed
