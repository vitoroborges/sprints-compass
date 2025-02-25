select count(l.titulo) as quantidade, e.nome, en.estado, en.cidade  
from editora e
join livro l on l.editora = e.codeditora
join endereco en on e.endereco  = en.codendereco
group by e.nome
order by count(l.titulo) desc
limit 5;
