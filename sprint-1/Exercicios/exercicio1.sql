select * from livro l
where l.publicacao > date('2014-12-31')
order by l.cod ASC;
