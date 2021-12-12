select products.name, categories.name from products inner join categories on products.id_categories = categories.id
where products.id_categories in (1,2,3,6,9) and products.amount > 100;