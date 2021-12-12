select products.name
from (products inner join providers on products.id_providers = providers.id)
where 10 <= products.amount and products.amount <= 20 and providers.name like 'P%';