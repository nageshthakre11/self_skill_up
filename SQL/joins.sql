----------------------------------------- JOINS -------------------------------------------
```
inner join      --> joins only matching records
Left join       --> inner join + all remaining records from left Table
Right join      --> Inner join + all remaining records from Right Table 

Full Join       --> Inner Join + Left Join + Right Join
Cross Join      --> Cartesian  Join ( No need to give join condtion)
Natural Join    --> Join will be decided by SQL itself, based on same name of columns from both Tables
                    Mostly its Inner Join but if matching column is not present in btween both tables
                    then it will do cartesian Join 

self Join       --> table A joined with itself when data need to be compare is present in same table.
```
--SELF JOIN 
-- write a querry to fetch the child name and age along with their parent name and age

select child.name, child.age,
    parent.name, parent.age
from family as child
join family as parent 
    on child.parent_id = parent.member_id




	-- thierd highest salary 
select x.name, x.salary
from 
	(
	select *, 
		row_number() over(partition by dept order by salary desc) rn
		from employees 
		) x
	where x.rn  = 3
	
	
	-- duplicate students 
	select * from 
	(
	select *, 
		row_number() over(partition by ID order by id) rn
	from Students) x
	where x.rn > 1
	
	-- employees who earns more than manager
	
	select * from employees e1
	join employees e2
		on e1.manager_id = e2.employee_id
	where e1.salary > e2.salary 
	
	
	-- find department with highest avg salary 
	
	select dept, avg(salary) avg_salary 
		from employees
	group by dept 
	order by avg_salary desc


-- to get passanger names who can go by lift for the total weight of passenges should be less than permitted_wt
    	
	with lift_status as 
		(
		select *,
		sum(weight_kg) over(partition by lift_id order by id, weight_kg ) as cum_sum,
		case when permitted_wt >  sum(weight_kg) over(partition by lift_id order by id, weight_kg ) then 1 else 0 end as Flag
		from lift_pasanger P 
		inner join lifts L 
		on p.id = l.lift_id
		order by id, weight_kg 
		)
	
	select lift_id, string_agg(passanger_name,',') as passanger_names from  lift_status
	where flag = 1
	group by lift_id 
	order by lift_id desc
	
	
	