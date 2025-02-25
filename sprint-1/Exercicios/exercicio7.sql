select a.nome 
from autor a 
left join livro l on l.autor = a.codautor
where l.autor is null
order by a.nome asc;
