-- Criando a view fatos locação
create view vw_fato_locacao as
select distinct l.idLocacao as idFatoLocacao, cl.idCliente, c.idCarro, v.idVendedor, 
cast(strftime('%s', l.dataLocacao) - strftime('%s', l.dataEntrega) as integer) / 86400 as tempo, l.qtdDiaria, l.vlrDiaria, (l.qtdDiaria * l.vlrDiaria) as vlrTotal 
from Locacao l
join Clientes cl on cl.idCliente = l.idCliente
join Carro c on c.idCarro = l.idCarro
join Vendedor v on v.idVendedor = l.idVendedor;

-- Criando a view dimensão cliente
create view vw_dim_cliente as 
select distinct c.idCLiente, c.nomeCliente as 'Nome Cliente', c.cidadeCliente as Cidade, c.estadoCliente as Estado, c.paisCliente as Pais
from Clientes c;

-- Criando a view dimensão carro
create view vw_dim_carro as
select distinct c.idCarro, c.marcaCarro as Marca, c.modeloCarro as Modelo, c.chassiCarro as Chassi, 
c.anoCarro as Ano, c.kmCarro as Km, co.tipoCombustivel as Combustivel
from Carro c
join Combustivel co on co.idCombustivel = c.idCombustivel;

-- Criando a view dimensão vendedor
create view vw_dim_vendedor as
select distinct v.idVendedor, v.nomeVendedor as 'Nome Vendedor', v.sexoVendedor as Sexo, v.estadoVendedor as Estado
from Vendedor v;

-- Criando a view dimensão tempo
create view vw_dim_tempo as
select distinct l.dataLocacao as idTempo, strftime('%Y', l.dataLocacao) as Ano, strftime('%m', l.dataLocacao) as Mes, 
strftime('%d', l.dataLocacao) as Dia, strftime('%W', l.dataLocacao) as Semana
from Locacao l;