select format('%s.%s.%s-%s', 
substring(cpf from 1 for 3),
substring(cpf from 4 for 3),
substring(cpf from 7 for 3),
substring(cpf from 10 for 2)
) as CPF from natural_person;