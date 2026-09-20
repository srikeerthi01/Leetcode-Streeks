# Write your MySQL query statement below
select c.name as Customers from Customers c where (select count(*) from Orders o where o.customerID = c.id)= 0;