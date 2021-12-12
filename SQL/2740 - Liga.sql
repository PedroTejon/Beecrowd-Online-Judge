select 'Podium: ' || team from league where position in (1, 2, 3)
union all
select 'Demoted: ' || team from league where position in (14, 15);