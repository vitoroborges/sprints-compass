select a.nome 
from autor a 
join livro l on l.autor = a.codautor
join editora e on e.codeditora = l.editora
join endereco en on en.codendereco = e.endereco
where not en.estado = "RIO GRANDE DO SUL" and not en.estado = "PARANÁ"
group by a.nome
order by a.nome asc;
