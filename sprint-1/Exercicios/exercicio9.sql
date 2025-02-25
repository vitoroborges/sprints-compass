select tbp.cdpro, tbv.nmpro
from tbestoqueproduto tbp
join tbvendas tbv on tbp.cdpro = tbv.cdpro
where tbv.status = 'Concluído'
and (tbv.dtven between '2014-02-03' and '2018-02-02')
group by tbp.cdpro
order by count(tbp.cdpro) desc
limit 1;
