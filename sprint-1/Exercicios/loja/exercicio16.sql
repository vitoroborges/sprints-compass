select tbv.estado, tbv.nmpro, round(avg(tbv.qtd), 4) as quantidade_media
from tbvendas tbv
where tbv.status = 'Concluído'
group by tbv.estado, tbv.nmpro
order by tbv.estado, tbv.nmpro;  