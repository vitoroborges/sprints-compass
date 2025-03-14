select tbv.cdven
from tbvendas tbv
where tbv.deletado = '1'
order by tbv.cdven asc;