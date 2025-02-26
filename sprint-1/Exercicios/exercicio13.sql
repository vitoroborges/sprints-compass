select tbv.cdpro, tbv.nmcanalvendas, tbv.nmpro, sum(tbv.qtd ) as quantidade_vendas 
from tbvendas tbv
where (tbv.nmcanalvendas = 'Ecommerce' or tbv.nmcanalvendas = 'Matriz')
and tbv.status = 'Concluído'
group by tbv.cdpro, tbv.nmcanalvendas
order by quantidade_vendas asc
limit 10;