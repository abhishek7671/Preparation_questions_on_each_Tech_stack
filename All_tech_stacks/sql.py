# 1. Second Highest Salary
# SQL Query to find the second highest salary from the Employee table



# select max(salary) as SecondHighestSalary
# from Employee 
# where salary < (select max(salary) from Employee);


# ------------------------------------------------------------------------------------------------------


# 2. Department-wise average salary
# SQL Query to find the average salary for each department from the Employee table

# note: having - filters aggregated groups based on a condition


# select department_id, avg(salary) as average_salary
# from Employee
# group by department_id
# having count(*) > 5;


# -----------------------------------------------------------------------------------------


# 3. Employees with above-average salaries
# SQL Query to find employees with salaries above the average salary
    

# select name, salary
# from Employee
# where salary > (select avg(salary) from Employee);



# --------------------------------------------------------------------------------------------------------------


# 4. Count of Employees in Each Department
# SQL Query to find the count of employees in each department from the Employee table


# select department_id, count(*) as employee_count
# from Employee
# group by department_id;


# --------------------------------------------------------------------------------------------------


# 5. customers with >3 orders in last 30 days
# SQL Query to find customers who have placed more than 3 orders in the last 30 days



# select customer_id, count(*) as order_count
# from Orders
# where order_date >= CURRENT_DATE - INTERVAL '30 days'
# group by customer_id
# having count(*) > 3;


# --------------------------------------------------------------------------------------------------------------


# 6. Find duplicates on multiple fields


# select first_name, last_name, count(*) as duplicate_count
# from Employee
# group by first_name, last_name
# having count(*) > 1;


# --------------------------------------------------------------------------------------------------------------


# 7. Transpose rows into columns using case


# select user_id,
#        max(case when action = 'jan' then 1 else 0 end) as jan,
#        max(case when action = 'feb' then 1 else 0 end) as feb
# from user_spend
# group by user_id;   



# --------------------------------------------------------------------------------------------------------------


# 8. Inner Join vs Exists

# note: Inner Join returns rows that have matching values in both tables.
# note: Exists checks for the existence of rows in a subquery and returns true or false.



# select name 
# from customers c
# where exists (select 1 from orders o where o.customer_id = c.id);



# ---------------------------------------------------------------------


# 9. Products never sold


# select p.id, p.name
# from products p
# left join orders o on p.id = o.product_id
# where o.product_id is null;



# ------------------------------------------------------------------------------------------------------------


# 10. Find the highest salary in each department



# select department_id, name, salary
# from Employee e1
# where salary = (select max(salary) from Employee e2 where e1.department_id = e2.department_id);



# ------------------------------------------------------------------------------------------------------------------------------


# 11. Products with below average sales


# select product_id, SUM(quantity) as total_quantity
# from order_items
# group by product_id
# having SUM(quantity) < (select AVG(total_quantity) from (select SUM(quantity) as total_quantity from order_items group by product_id) as avg_table);



# -------------------------------------------------------------------------------------------------------------------------------------------------


# 12. Customers with no orders in the last year


# select c.id, c.name
# from customers c
# left join orders o on c.id = o.customer_id and o.order_date >= CURRENT_DATE - INTERVAL '1 year'
# where o.id is null;



# -----------------------------------------------------------------------------------------------------------------------------------------------------


# 13. Employees hired in the last 6 months with salary > 50000


# select name, salary, hire_date
# from Employee
# where hire_date >= CURRENT_DATE - INTERVAL '6 months' and salary > 50000;



# ---------------------------------------------------------------------------------------------------------------------------------------


# 14. Departments with average salary > 60000


# select department_id, avg(salary) as average_salary
# from Employee
# group by department_id
# having avg(salary) > 60000;


# ------------------------------------------------------------------------------------------------------------


# 15. Customers with more than 5 orders


# select customer_id, count(*) as order_count
# from Orders
# group by customer_id
# having count(*) > 5;


# ----------------------------------------------------------------------------------------------------------


# 16. Employees with the top 3 salaries


# select name, salary
# from (
#     select name, salary,
#            DENSE_RANK() OVER (ORDER BY salary DESC) as salary_rank
#     from Employee
# ) ranked_salaries
# where salary_rank <= 3;

# ---------------------------------------------------------------------------------------------------------------------


# 17. Highest order value per customer

# select customer_id, MAX(total_amount) as highest_order_value
# from Orders
# group by customer_id;


# SELECT *
# FROM Orders
# WHERE total_amount = (SELECT MAX(total_amount) FROM Orders);


# -------------------------------------------------------------------------------------------------------------------


# 18. Compare today vs yesterday active users


# with daily_active_users as (
#     select activity_date, count(distinct user_id) as active_user_count
#     from UserActivity
#     where activity_date in (CURRENT_DATE, CURRENT_DATE - INTERVAL '1 day')
#     group by activity_date
# )
# select 
#     today.active_user_count as today_active_users,
#     yesterday.active_user_count as yesterday_active_users
# from daily_active_users today
# join daily_active_users yesterday on today.activity_date = CURRENT_DATE and yesterday.activity_date = CURRENT_DATE - INTERVAL '1 day';


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

19. 