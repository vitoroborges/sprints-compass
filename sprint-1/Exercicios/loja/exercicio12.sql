select tbd.cddep, tbd.nmdep, tbd.dtnasc, sum(tbv.qtd * tbv.vrunt) as valor_total_vendas 
from tbvendas tbv
join tbdependente tbd on tbd.cdvdd = tbv.cdvdd
where tbv.status = 'Concluído'
group by tbd.cddep
having valor_total_vendas > 0
order by valor_total_vendas asc
limit 1; 
