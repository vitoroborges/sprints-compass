-- Criando o banco de dados normalizado

create table Clientes (
	idCliente int primary key,
	nomeCliente varchar(100) not null,
	cidadeCliente varchar(40) not null,
	estadoCliente varchar(40) not null,
	paisCliente varchar(40) not null
);

create table Combustivel (
	idCombustivel int primary key,
	tipoCombustivel varchar(20) not null
);

create table Carro (
	idCarro int primary key,
	kmCarro int not null,
	chassiCarro varchar(50) not null,
	marcaCarro varchar(80) not null,
	modeloCarro varchar(80) not null,
	anoCarro int not null,
	idCombustivel int,
	foreign key (idCombustivel) references Combustivel(idCombustivel)
);

create table Vendedor (
	idVendedor int primary key,
	nomeVendedor varchar(15) not null,
	sexoVendedor smallint not null,
	estadoVendedor varchar(40) not null
);

create table Locacao (
	idLocacao int primary key,
	dataLocacao datetime not null,
	qtdDiaria int not null,
	vlrDiaria decimal(18, 2) not null,
	dataEntrega datetime not null,
	idCliente int not null,
	idVendedor int not null,
	idCarro int not null,
	foreign key (idCliente) references Clientes(idCliente),
	foreign key (idVendedor) references Vendedor(idVendedor),
	foreign key (idCarro) references Carro(idCarro)
);

