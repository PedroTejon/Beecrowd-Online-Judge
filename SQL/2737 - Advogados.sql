select name, customers_number from lawyers where customers_number = (select max(customers_number) from lawyers) 
union all
select name, customers_number from lawyers where customers_number = (select min(customers_number) from lawyers)
union all
select 'Average' as name, floor(avg(customers_number)) from lawyers;