select products.name, providers.name from providers inner join products on
products.id_providers = providers.id where providers.name = 'Ajax SA';