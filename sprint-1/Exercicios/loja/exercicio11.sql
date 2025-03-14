select tbv.cdcli, tbv.nmcli, sum(tbv.vrunt * tbv.qtd) as gasto 
from tbvendas tbv
where tbv.status = 'Concluído'
group by tbv.cdcli
order by gasto desc
limit 1;
