-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
select score, name
	from second_table
	where name is not null
	order by score desc
