-- https://www.youtube.com/playlist?list=PLxHEfsUVhEwMqw-nDG2zd3mpXpvY1v9xX

-- Link for interview questions 


-- Get total of top 2 students from subjects 

select s_name, sum(score) as top_2_scores from (
        select * , 
            row_number() over(partition by s_name order by score desc) RN 
        from students
        ) x
    where x.RN < 3
    group by s_name


-- get the maximum employee id, but ignore the duplicate ID

select max(emp_id) from employee 
    where emp_id not in (
                        select distinct(emp_id) from employee 
                        group by emp_id
                        having count(*) > 1
                        )


--Alternate solution
WITH DUPLICATE_ID AS (
SELECT EMP_ID FROM
    (
    select * , 
    ROW_NUMBER() OVER(partition BY EMP_ID ORDER BY EMP_ID) RN
    FROM employee) x 
    WHERE X.RN > 1)

SELECT MAX(EMP_ID) FROM EMPLOYEE WHERE EMP_ID NOT IN (SELECT EMP_ID FROM DUPLICATE_ID)

--- get the emp with minimum salary , employees are spread across 2 table, 1 emp may have 2 different salay so consider minimum salary emp

with union_table as (
    select * from table_A
    union ALl
    select * from table B
    )
select id, name, min(slary) from union_table
group by id, name



-- get the differance between previous month sale and current month 

    with new_sale as (
        select * , lag(sales) over(partition by month_name order by month_num) previous_month_sale
        from sales_data
    )
select month_name, (sales -  previous_month_sale) as sale_differance from new_sale




-- delete duplicate records
delete from cars where modelId not in (
    select min(model_id) from cars group by model_name, brand
)

-- delete duplicate records Using Row Number
delete from cars 
    where model_id in (
                select models_id from
                            (
                            select *, 
                            row_number()  over(partiotion by model_name, brand order by model_id ) RN 
                            from cars 
                            ) X
                        where x.rn > 1
                        )

