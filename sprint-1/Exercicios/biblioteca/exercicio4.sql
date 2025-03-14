select a.nome, a.codautor, a.nascimento, count(l.titulo ) as quantidade 
from autor a
left join livro l on l.autor = a.codautor
group by a.codautor 
order by a.nome asc;
