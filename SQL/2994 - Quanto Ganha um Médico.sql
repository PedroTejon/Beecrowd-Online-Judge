select doctors.name, round(sum(((hours * 150) + (hours * 150) * (bonus / 100))), 1) as salary 
from (attendances inner join doctors on attendances.id_doctor = doctors.id)inner join work_shifts on attendances.id_work_shift = work_shifts.id 
group by (doctors.name) order by (salary) desc;