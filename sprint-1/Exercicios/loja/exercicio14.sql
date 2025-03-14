select tbv.estado, round(avg(tbv.qtd * tbv.vrunt), 2) as gastomedio
from tbvendas tbv
where tbv.status = 'Concluído'
group by tbv.estado
order by gastomedio desc;