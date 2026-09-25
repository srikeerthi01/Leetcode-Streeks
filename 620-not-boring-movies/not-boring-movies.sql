# Write your MySQL query statement below
select * from Cinema where description != 'boring' and id % 2 = 1 
order by rating desc;
#order by rating is used becoz we are supposed to write it in the desceending order