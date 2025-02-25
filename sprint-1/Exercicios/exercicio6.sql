select a.codautor, a.nome, count(l.autor ) as quantidade_publicacoes
from autor a 
join livro l on l.autor = a.codautor
group by a.nome
order by count(l.autor) desc
limit 1;
