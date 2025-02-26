select tbvd.nmvdd as vendedor, round(sum(tbv.qtd * tbv.vrunt), 2) as valor_total_vendas, 
round(sum(tbv.qtd * tbv.vrunt)* tbvd.perccomissao /100, 2) as comissao  
from tbvendas tbv
join tbvendedor tbvd on tbvd.cdvdd = tbv.cdvdd
where tbv.status = 'Concluído'
group by tbvd.nmvdd 
order by comissao desc;