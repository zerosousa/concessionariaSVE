/**
* CABEÇALHO PADRÃO BRMODELO 
* Geração de Modelo físico
* Sql ANSI 2003 - brModelo.
*/


-- create database projetosbd; -- descomente para criar o banco de dados
-- create schema concessionaria; -- descomente para criar o schema
-- CREATE TYPE transacao AS ENUM ('V', 'C'); -- descomente para criar o datatype transacao, restrição que faz com que a tabela de transação só armazene compras e vendas

-- drop schema concessionaria cascade -- descomente para excluir o schema e reiniciar os testes.

-- -------------------[ CRIAÇÃO DAS TABELAS ]---------------------------

CREATE TABLE concessionaria.MARCA (
id_marca serial PRIMARY KEY,
de_marca varchar
);

CREATE TABLE concessionaria.LOCAL (
id_local serial PRIMARY KEY,
de_local varchar
);

CREATE TABLE concessionaria.BAIRRO (
id_bairro serial PRIMARY KEY,
nm_bairro varchar,
id_cidade bigint
);

CREATE TABLE concessionaria.FUNCIONARIO (
id_funcionario serial PRIMARY KEY,
nm_funcionario varchar
);

CREATE TABLE concessionaria.UF (
cd_uf varchar PRIMARY KEY,
nm_uf varchar
);

CREATE TABLE concessionaria.MOTO (
cd_chassi varchar PRIMARY KEY,
placa varchar,
cor varchar,
ano_fabricacao varchar,
id_local bigint,
id_modelo bigint
);

CREATE TABLE concessionaria.CLIENTE (
cd_cpfCliente char(11) PRIMARY KEY,
nm_cliente varchar,
nu_telefone varchar,
id_endereco bigint
);

CREATE TABLE concessionaria.TRANSACAO (
id_notaFiscal varchar PRIMARY KEY,
dt_data varchar,
tp_transacao transacao,
id_funcionario bigint,
cd_chassi varchar,
cd_cpfCliente char(11)
);

CREATE TABLE concessionaria.ENDERECO (
id_endereco serial PRIMARY KEY,
nu_numero varchar,
cd_cep varchar,
de_complemento varchar,
id_logradouro bigint
);

CREATE TABLE concessionaria.LOGRADOURO (
id_logradouro serial PRIMARY KEY,
nm_logradouro varchar,
id_bairro bigint
);

CREATE TABLE concessionaria.CIDADE (
id_cidade serial PRIMARY KEY,
nm_cidade varchar,
cd_uf varchar
);

CREATE TABLE concessionaria.MODELO (
id_modelo serial PRIMARY KEY,
de_modelo varchar,
id_marca bigint,
nu_ano bigint,
nu_cilindradas bigint
);

CREATE TABLE concessionaria.ServicoPorOrdem (
id_servico bigint,
nu_ordem bigint,
id_funcionario varchar,
id_produto bigint,
nu_quantidade bigint,
PRIMARY KEY(id_servico,nu_ordem)
);

CREATE TABLE concessionaria.ORDEMSERVICO (
nu_ordem serial PRIMARY KEY,
cd_cpfCliente char(11),
dt_ordem varchar,
cd_chassi varchar,
id_funcionario bigint
);

CREATE TABLE concessionaria.PRODUTO (
id_produto serial PRIMARY KEY,
de_produto varchar
);

CREATE TABLE concessionaria.SERVICO (
id_servico serial PRIMARY KEY,
de_servico varchar,
nu_valor bigint
);
-- --[ fim ]--------------------------------------------------------------

-- -------------------[ INSERÇÕES BASE ]---------------------------

-- MARCA
INSERT INTO concessionaria.marca (de_marca) VALUES('HONDA');
INSERT INTO concessionaria.marca (de_marca) VALUES('YAMAHA');

-- MODELO
INSERT INTO concessionaria.modelo (de_modelo, id_marca, nu_ano, nu_cilindradas) VALUES('CG TITAN', 1, 2016, 150);
INSERT INTO concessionaria.modelo (de_modelo, id_marca, nu_ano, nu_cilindradas) VALUES('FAZER', 1, 2016, 250);

-- uf
INSERT INTO concessionaria.uf (cd_uf,nm_uf) VALUES ('SC','SANTA CATARINA');	
INSERT INTO concessionaria.uf (cd_uf,nm_uf) VALUES ('PR','PARANA');

-- cidade
INSERT INTO concessionaria.cidade (nm_cidade,cd_uf) VALUES ('FLORIANOPOLIS','SC');
INSERT INTO concessionaria.cidade (nm_cidade,cd_uf) VALUES ('CURITIBA','PR');

-- bairro
INSERT INTO concessionaria.bairro (nm_bairro,id_cidade) VALUES ('CENTRO',1);
INSERT INTO concessionaria.bairro (nm_bairro,id_cidade) VALUES ('CENTRO',2);

-- logradouro
INSERT INTO concessionaria.logradouro (nm_logradouro,id_bairro) VALUES ('RUA DOS LIMOEIROS',2);
INSERT INTO concessionaria.logradouro (nm_logradouro,id_bairro) VALUES ('RUA DAS LARANJEIRAS',1);

-- endereco
INSERT INTO concessionaria.endereco (nu_numero,cd_cep,de_complemento,id_logradouro) VALUES ('15','82200530','AP 201',2);
INSERT INTO concessionaria.endereco (nu_numero,cd_cep,de_complemento,id_logradouro) VALUES ('10','88060000','CASA',1);

-- cliente
INSERT INTO concessionaria.cliente (cd_cpfcliente,nm_cliente,nu_telefone,id_endereco) VALUES ('98765432109','JOAO DE SOUSA','47 912348888',2);
INSERT INTO concessionaria.cliente (cd_cpfcliente,nm_cliente,nu_telefone,id_endereco) VALUES ('12345678910','JOSE DA SILVA','48 988881234',1);

-- local
INSERT INTO concessionaria."local" (de_local) VALUES ('DEPOSITO');
INSERT INTO concessionaria."local" (de_local) VALUES ('OFICINA');

-- moto
INSERT INTO concessionaria.moto (cd_chassi,cor,ano_fabricacao,id_local,id_modelo) VALUES ('M003','PRETA','2016',2,2);
INSERT INTO concessionaria.moto (cd_chassi,placa,cor,ano_fabricacao,id_local,id_modelo) VALUES ('M002','CAB4321','PRETA','2015',1,2);
INSERT INTO concessionaria.moto (cd_chassi,cor,ano_fabricacao,id_local,id_modelo) VALUES ('M004','VERMELHA','2016',2,2);
INSERT INTO concessionaria.moto (cd_chassi,placa,cor,ano_fabricacao,id_local,id_modelo) VALUES ('M001','ABC1234','VERMELHO','2016',1,1);

-- funcionario
INSERT INTO concessionaria.funcionario (nm_funcionario) VALUES ('ZECA BORRACHEIRO');
INSERT INTO concessionaria.funcionario (nm_funcionario) VALUES ('JUCA MECANICO');
INSERT INTO concessionaria.funcionario (nm_funcionario) VALUES ('VILSON VENDEDOR');

-- ordem de servico
INSERT INTO concessionaria.ordemservico (cd_cpfcliente,dt_ordem,cd_chassi,id_funcionario) VALUES ('98765432109','30/11/2016','M002',1);
INSERT INTO concessionaria.ordemservico (cd_cpfcliente,dt_ordem,cd_chassi,id_funcionario) VALUES ('12345678910','01/12/2016','M001',1);

-- servico
INSERT INTO concessionaria.servico (de_servico,nu_valor) VALUES ('MAO DE OBRA',100);
INSERT INTO concessionaria.servico (de_servico,nu_valor) VALUES ('TROCA DE OLEO',50);

-- produto
INSERT INTO concessionaria.produto (de_produto) VALUES ('REVISAO');
INSERT INTO concessionaria.produto (de_produto) VALUES ('OLEO ');

-- servicoporordem
INSERT INTO concessionaria.servicoporordem (id_servico,nu_ordem,id_funcionario,id_produto,nu_quantidade) VALUES (2,2,'2',1,1);
INSERT INTO concessionaria.servicoporordem (id_servico,nu_ordem,id_funcionario,id_produto,nu_quantidade) VALUES (1,1,'2',2,1);

-- transacao
INSERT INTO concessionaria.transacao (id_notafiscal,dt_data,tp_transacao,id_funcionario,cd_chassi,cd_cpfcliente) VALUES ('V001','01/12/2016','V',3,'M003','98765432109');
-- --[ fim ]--------------------------------------------------------------

-- -------------------[ CRIAÇÃO DAS RESTRIÇÕES ]---------------------------


ALTER TABLE concessionaria.BAIRRO ADD constraint fk_bairro_cidade FOREIGN KEY (id_cidade) REFERENCES concessionaria.CIDADE (id_cidade) on delete restrict on update cascade;
ALTER TABLE concessionaria.MOTO ADD constraint fk_moto_modelo FOREIGN KEY (id_modelo) REFERENCES concessionaria.MODELO (id_modelo) on delete restrict on update cascade;
ALTER TABLE concessionaria.CLIENTE ADD constraint fk_cliente_endereco foreign key (id_endereco) REFERENCES concessionaria.ENDERECO (id_endereco) on delete restrict on update cascade;
ALTER TABLE concessionaria.ENDERECO ADD constraint fk_endereco_logradouro  foreign key (id_logradouro) REFERENCES concessionaria.LOGRADOURO (id_logradouro) on delete restrict on update cascade;
ALTER TABLE concessionaria.ServicoPorOrdem ADD constraint fk_servicoPorOrdem_servico foreign KEY (id_servico) REFERENCES concessionaria.SERVICO (id_servico) on delete restrict on update cascade;
ALTER TABLE concessionaria.ServicoPorOrdem ADD constraint fk_servicoPorOrdem_ordem  foreign key (nu_ordem) REFERENCES concessionaria.ORDEMSERVICO (nu_ordem) on delete restrict on update cascade;
ALTER TABLE concessionaria.MOTO ADD constraint fk_moto_local FOREIGN KEY (id_local) REFERENCES concessionaria.LOCAL (id_local) on delete restrict on update cascade;
ALTER TABLE concessionaria.ORDEMSERVICO ADD constraint fk_ordemservico_cliente FOREIGN KEY (cd_cpfCliente) REFERENCES concessionaria.CLIENTE (cd_cpfCliente) on delete restrict on update cascade;
ALTER TABLE concessionaria.ORDEMSERVICO ADD constraint fk_ordemservico_moto FOREIGN KEY (cd_chassi) REFERENCES concessionaria.MOTO (cd_chassi) on delete restrict on update cascade;
ALTER TABLE concessionaria.ORDEMSERVICO ADD constraint fk_ordemservico_funcionario FOREIGN key (id_funcionario) REFERENCES concessionaria.FUNCIONARIO (id_funcionario) on delete restrict on update cascade;
ALTER TABLE concessionaria.MODELO ADD constraint fk_modelo_marca FOREIGN KEY (id_marca) REFERENCES concessionaria.MARCA (id_marca) on delete restrict on update cascade;
ALTER TABLE concessionaria.CIDADE ADD constraint fk_cidade_uf FOREIGN KEY (cd_uf) REFERENCES concessionaria.UF (cd_uf) on delete restrict on update cascade;
ALTER TABLE concessionaria.LOGRADOURO ADD constraint fk_logradouro_bairro FOREIGN KEY (id_bairro) REFERENCES concessionaria.BAIRRO (id_bairro) on delete restrict on update cascade;
ALTER TABLE concessionaria.TRANSACAO ADD constraint fk_transacao_funcionario FOREIGN KEY (id_funcionario) REFERENCES concessionaria.FUNCIONARIO (id_funcionario) on delete restrict on update cascade;
ALTER TABLE concessionaria.TRANSACAO ADD constraint fk_transacao_moto FOREIGN KEY (cd_chassi) REFERENCES concessionaria.MOTO (cd_chassi) on delete restrict on update cascade;
ALTER TABLE concessionaria.TRANSACAO ADD constraint fk_transacao_cliente FOREIGN KEY (cd_cpfCliente) REFERENCES concessionaria.CLIENTE (cd_cpfCliente) on delete restrict on update cascade;

-- restringir exclusao de produto e de serviço
-- --[ fim ]--------------------------------------------------------------

-- -------------------[ CRIAÇÃO DAS PROCEDURES ]---------------------------

-- procedure para ajuste de preco
create or replace function concessionaria.fn_atualiza_preco(vl_ajuste int) returns void as $$
	begin
		update concessionaria.servico set nu_valor = (nu_valor) + (nu_valor*vl_ajuste/100);
		raise notice 'Valores ajustados em % por cento.', vl_ajuste;
	end;
$$ language plpgsql;

-- procedure para a trigger
create or replace function concessionaria.fn_cadastra_bairro() returns trigger as $$
	begin
		insert into concessionaria.bairro values (nextval('concessionaria.bairro_id_bairro_seq'::regclass), 'CENTRO', new.id_cidade);
		raise notice 'Cadastrado bairro CENTRO para a cidade %.', new.id_cidade;

		return null;

	end; 
$$ language plpgsql;

-- teste do ajuste de preco
select fn_atualiza_preco(10); -- aumenta em 10 por cento
-- --[ fim ]--------------------------------------------------------------


-- -------------------[ CRIAÇÃO DA TRIGGER ]---------------------------

-- trigger para cadastro automatico de bairro a partir da cidade
create trigger tr_cadastra_bairro after insert on concessionaria.cidade
for each row execute procedure fn_cadastra_bairro();

-- teste da trigger de cadastro de bairro
insert into concessionaria.cidade ( nm_cidade, cd_uf ) values ('NOVA CIDADE', 'SC');
-- --[ fim ]--------------------------------------------------------------

-- -------------------[ CRIAÇÃO DAS VIEWS ]---------------------------

-- vw_nf_detalhada
create view concessionaria.vw_nf_detalhada as 
select mo.cd_chassi, mo.placa, os.nu_ordem, sum(se.nu_valor)
from concessionaria.MOTO mo
join concessionaria.ORDEMSERVICO os on (mo.cd_chassi = os.cd_chassi) 
join concessionaria.ServicoPorOrdem so on (os.nu_ordem = so.nu_ordem)
join concessionaria.servico se on (so.id_servico = se.id_servico)
group by 1, 2, 3;

-- vw_moto_detalhada
create view concessionaria.vw_moto_detalhada as 
select mo.cd_chassi, ma.de_marca, ml.de_modelo, mo.cor, mo.ano_fabricacao, ml.nu_cilindradas, mo.placa, lo.de_local
from concessionaria.moto mo
join concessionaria.modelo ml on (mo.id_modelo = ml.id_modelo)
join concessionaria.marca ma on (ml.id_marca = ma.id_marca)
join concessionaria.local lo on (mo.id_local = lo.id_local);

-- vw_cliente_detalhado
create view concessionaria.vw_cliente_detalhado as 
select cl.cd_cpfCliente, cl.nm_cliente, cl.nu_telefone, lg.nm_logradouro, en.nu_numero, ba.nm_bairro, en.cd_cep, ci.nm_cidade, uf.nm_uf, mo.cd_chassi, ma.de_marca, ml.de_modelo, mo.cor, mo.ano_fabricacao, ml.nu_cilindradas, mo.placa, lo.de_local
from concessionaria.CLIENTE cl
left join concessionaria.ENDERECO en on (cl.id_endereco = en.id_endereco)
left join concessionaria.LOGRADOURO lg on (en.id_logradouro = lg.id_logradouro)
left join concessionaria.BAIRRO ba on (lg.id_bairro = ba.id_bairro)
left join concessionaria.CIDADE ci on (ba.id_cidade = ci.id_cidade)
left join concessionaria.UF uf on (ci.cd_uf = uf.cd_uf)
left join concessionaria.ORDEMSERVICO os on (cl.cd_cpfCliente = os.cd_cpfCliente)
left join concessionaria.MOTO mo on (os.cd_chassi = mo.cd_chassi)
left join concessionaria.MODELO ml on (mo.id_modelo = ml.id_modelo)
left join concessionaria.MARCA ma on (ml.id_marca = ma.id_marca)
left join concessionaria.local lo on (mo.id_local = lo.id_local);
-- --[ fim ]--------------------------------------------------------------


