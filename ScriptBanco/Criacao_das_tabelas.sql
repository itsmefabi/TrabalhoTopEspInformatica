CREATE TABLE tb_usuario (
    id_usuario          SERIAL,
    email               VARCHAR(50) UNIQUE NOT NULL,
    nome                VARCHAR(50) NOT NULL,
    senha               VARCHAR(50) NOT NULL,
    
    CONSTRAINT pk_tb_usuario_id_usuario
    PRIMARY KEY(id_usuario)
);

CREATE TABLE tb_produtor (
    id_produtor       SERIAL,
    nome                VARCHAR(150) UNIQUE NOT NULL,

    CONSTRAINT pk_tb_marca_id_produtor 
    PRIMARY KEY(id_produtor)
);

CREATE TABLE tb_filme (
    id_filme             SERIAL,
    id_produtor          INTEGER,
    titulo               VARCHAR(50) UNIQUE NOT NULL,
    diretor              VARCHAR(50) NOT NULL,
    ano_lancamento       VARCHAR(50) NOT NULL,

    CONSTRAINT pk_tb_filme_id_filme 
    PRIMARY KEY(id_filme),

    CONSTRAINT fk_tb_filme_id_produtor 
    FOREIGN KEY(id_produtor)
    REFERENCES tb_produtor(id_produtor)
);