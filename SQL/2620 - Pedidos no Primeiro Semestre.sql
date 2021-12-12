select customers.name, orders.id
from customers inner join orders on customers.id = orders.id_customers
where extract(month from orders.orders_date) <= 6;