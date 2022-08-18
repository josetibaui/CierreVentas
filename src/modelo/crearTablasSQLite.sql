CREATE TABLE IF NOT EXISTS ig_personas (
  idPersona INTEGER PRIMARY KEY,
  nombres TEXT NOT NULL,
  apellidos TEXT NOT NULL,
  tipoIdentificacion TEXT NOT NULL,
  identificacion TEXT NOT NULL,
  codigoNomina TEXT,
  email TEXT,
  login TEXT,
  password TEXT,
  estado INTEGER
);
CREATE UNIQUE INDEX ig_persona_nombreApellidos_UK ON ig_personas(nombres,apellidos);
CREATE UNIQUE INDEX ig_persona_identificacion_UK ON ig_personas(tipoIdentificacion,identificacion);

INSERT INTO ig_personas (
    nombres,
    apellidos,
    tipoIdentificacion,
    identificacion,
    codigoNomina,
    email,
    login,
    password,
    estado
)
VALUES (
    'LAS PALMERAS',
    'GROUPALMERAS S.A.',
    'R',
    '1792014336001',
    '',
    '',
    '',
    '',
    0
);


CREATE TABLE ig_locales (
  idLocal INTEGER PRIMARY KEY,
  codLocal INTEGER NOT NULL,
  local TEXT NOT NULL,
  alias TEXT,
  tipo TEXT NOT NULL,
  ciudad TEXT NOT NULL,
  direccion TEXT NOT NULL,
  referencia TEXT,
  codigoArea TEXT,
  telefono TEXT NOT NULL,
  codigoPostal TEXT,
  estado INTEGER  NOT NULL
);
CREATE UNIQUE INDEX ig_locales_codLocal_UK on ig_locales(codLocal);
CREATE UNIQUE INDEX ig_localesLocal_UK on ig_locales(local);


CREATE TABLE IF NOT EXISTS ig_personas_locales(
    idPersonaLocal INTEGER  PRIMARY KEY,
    idPersona INTEGER NOT NULL,
    idLocal INTEGER NOT NULL,
    estado INTEGER NOT NULL,
    FOREIGN KEY (idPersona) REFERENCES ig_personas (idPersona) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY(idLocal) REFERENCES ig_locales (idLocal) ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE UNIQUE INDEX pe_personaLocal_UK ON ig_personas_locales(idpersona, idLocal);

CREATE TABLE IF NOT EXISTS ig_perfiles(
    idPerfil INTEGER PRIMARY KEY,
    perfil TEXT NOT NULL,
    estado INTEGER NOT NULL
);
CREATE UNIQUE INDEX ig_perfiles_UK ON ig_perfiles(perfil);


CREATE TABLE IF NOT EXISTS ig_perfiles_personas_locales(
  idPerfilPersonaLocal INTEGER PRIMARY KEY,
  idPerfil INTEGER NOT NULL,
  idPersona INTEGER NOT NULL,
  idLocal INTEGER NOT NULL,
  estado INTEGER NOT NULL,
  FOREIGN KEY (idperfil) REFERENCES ig_perfil (idPerfil) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (idPersona) REFERENCES ig_personas (idPersona) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY(idLocal) REFERENCES ig_locales (idLocal) ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE UNIQUE INDEX ig_personasLocalPerfiles_UK ON ig_perfiles_personas_locales(idPerfil, idPersona, idLocal);

CREATE TABLE IF NOT EXISTS ig_log (
  idLog INTEGER  PRIMARY KEY,
  tabla TEXT NOT NULL,
  idPersona INTEGER NOT NULL,
  fechaHora TEXT NOT NULL,
  preCondicion TEXT,
  postCondicion TEXT,
  FOREIGN KEY (idPersona) REFERENCES ig_personas (idPersona) ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE INDEX igLog_persona_FK_idx ON ig_log(idPersona);
CREATE INDEX igLog_tablafechaHora_IDX ON ig_log(tabla,fechaHora);
CREATE INDEX igLog_tablaPersonaFecha_IDX ON ig_log(tabla,idPersona,fechaHora);


CREATE TABLE IF NOT EXISTS loc_egresos (
  idEgreso INTEGER  PRIMARY KEY,
  egreso TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado TEXT NOT NULL
);
CREATE UNIQUE INDEX locEgresos_UK ON loc_egresos (egreso);


CREATE TABLE IF NOT EXISTS loc_egresos_no_locales (
  idEgresoNoLocal INTEGER PRIMARY KEY,
  idEgreso INTEGER NOT NULL,
  idLocal INTEGER NOT NULL,
  estado INTEGER NOT NULL,
  FOREIGN KEY (idEgreso) REFERENCES loc_egresos (idLocEgreso) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (idLocal) REFERENCES ig_locales (idLocal) ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX loc_egresoNoLocal_UK ON loc_egresos_no_locales(idLocal,idEgreso);


CREATE TABLE IF NOT EXISTS loc_formasPagos(
  idFormaPago INTEGER  PRIMARY KEY,
  formaPago TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado TEXT NOT NULL
);
CREATE UNIQUE INDEX locFormaPagos_UK ON loc_formasPagos (formaPago);


CREATE TABLE IF NOT EXISTS loc_cortesias(
  idCortesia INTEGER  PRIMARY KEY,
  cortesia TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado TEXT NOT NULL
);
CREATE UNIQUE INDEX locCortesias_UK ON loc_cortesias(cortesia);

CREATE TABLE IF NOT EXISTS loc_pagosPersonal (
  idPagoPersonal INTEGER PRIMARY KEY,
  tipoPago TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado TEXT NOT NULL
);
CREATE UNIQUE INDEX locPagosPersonal_UK ON loc_pagosPersonal (tipoPago);


CREATE TABLE IF NOT EXISTS ba_bancos (
  idBanco INTEGER PRIMARY KEY,
  banco TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado INTEGER NOT NULL
);
CREATE UNIQUE INDEX banBanco_UK ON ba_bancos (banco);

CREATE TABLE IF NOT EXISTS loc_cierreVentas (
  idCierreVentas INTEGER PRIMARY KEY,
  idLocal INTEGER NOT NULL,
  fecha TEXT NOT NULL,
  data text NOT NULL,
  idPor INTEGER NOT NULL,
  FOREIGN KEY (idLocal) REFERENCES ig_locales (idLocal) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX locCierreVentas_locFecha_UK ON loc_cierreVentas (idLocal,fecha);
