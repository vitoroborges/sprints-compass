select v.cdvdd, v.nmvdd
from tbvendedor v
join tbvendas tv on tv.cdvdd = v.cdvdd 
where tv.status = 'Concluído'
group by v.nmvdd 
order by count(tv.cdvdd) desc
limit 1;
