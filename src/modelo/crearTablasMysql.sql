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


REATE TABLE IF NOT EXISTS loc_formasPagos(
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

CREATE TABLE IF NOT EXISTS loc_gastosGenerales (
  idGastoGeneral INTEGER  PRIMARY KEY,
  gastoGeneral TEXT NOT NULL,
  cuentaContabilidad TEXT,
  estado TEXT NOT NULL
);
CREATE UNIQUE INDEX locGastosGenerales_UK ON loc_gastosGenerales (gastoGeneral);

CREATE TABLE IF NOT EXISTS loc_gastos_no_locales (
  idGastoNoLocal INTEGER PRIMARY KEY,
  idGastoGeneral INTEGER NOT NULL,
  idLocal INTEGER NOT NULL,
  estado INTEGER NOT NULL,
  FOREIGN KEY (idGastoGeneral) REFERENCES loc_gastosGenerales (idGastoGeneral) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (idLocal) REFERENCES ig_locales (idLocal) ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX loc_gastoNoLocales_UK ON loc_gasto_no_locales(idLocal,idGastoNoLocal);

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


CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_ins AFTER INSERT ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        new.idPor,
        datetime('now'),
        NULL,
        new.idCierreVentas || '|' ||
            new.idLocal || '|' ||
            new.fecha || '|' ||
            new.data || '|' ||
            new.idPor
    )
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_upd AFTER UPDATE ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        new.idPor,
        datetime('now'),
        old.idCierreVentas || '|' ||
            old.idLocal || '|' ||
            old.fecha || '|' ||
            old.data || '|' ||
            old.idPor,
        new.idCierreVentas || '|' ||
            new.idLocal || '|' ||
            new.fecha || '|' ||
            new.data || '|' ||
            new.idPor
    )
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_del AFTER DELETE ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        old.idPor,
        datetime('now'),
        old.idCierreVentas || '|' ||
            old.idLocal || '|' ||
            old.fecha || '|' ||
            old.data || '|' ||
            old.idPor,
        NULL
    )
  END;
  

Las siguientes tablas son las que se usan en la base de datos  central

CREATE TABLE IF NOT EXISTS loc_cierreVentas (
  idCierreVentas INTEGER PRIMARY KEY,
  idLocal INTEGER NOT NULL,
  fecha TEXT NOT NULL,
  ventaTotal NUMERIC NOT NULL,
  anulaciones NUMERIC NOT NULL,
  devoluciones NUMERIC NOT NULL,
  diferencia NUMERIC NOT NULL,
  idPor INTEGER NOT NULL,
  FOREIGN KEY (idLocal) REFERENCES ig_locales (idLocal) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX locCierreVentas_locFecha_UK ON loc_cierreVentas (idLocal,fecha);

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_ins AFTER INSERT ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        new.idPor,
        datetime('now'),
        NULL,
        new.idCierreVentas || '|' ||
            new.idLocal || '|' ||
            new.fecha || '|' ||
            new.ventaTotal || '|' ||
            new.anulaciones || '|' ||
            new.devoluciones || '|' ||
            new.diferencia || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_upd AFTER UPDATE ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        new.idPor,
        datetime('now'),
        old.idCierreVentas || '|' ||
            old.idLocal || '|' ||
            old.fecha || '|' ||
            old.ventaTotal || '|' ||
            old.anulaciones || '|' ||
            old.devoluciones || '|' ||
            old.diferencia || '|' ||
            old.idPor,
        new.idCierreVentas || '|' ||
            new.idLocal || '|' ||
            new.fecha || '|' ||
            new.ventaTotal || '|' ||
            new.anulaciones || '|' ||
            new.devoluciones || '|' ||
            new.diferencia || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_del AFTER DELETE ON loc_cierreVentas
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas',
        old.idPor,
        datetime('now'),
        old.idCierreVentas || '|' ||
            old.idLocal || '|' ||
            old.fecha || '|' ||
            old.ventaTotal || '|' ||
            old.anulaciones || '|' ||
            old.devoluciones || '|' ||
            old.diferencia || '|' ||
            old.idPor,
        NULL
    );
  END;
  

CREATE TABLE loc_cierreVentas_formaPagos (
  idcvfp INTEGER  PRIMARY KEY,
  idCierreVentas INTEGER NOT NULL,
  idFormaPago INTEGER NOT NULL,
  valor NUMERIC NOT NULL,
  descripcion TEXT,
  idPor INTEGER NOT NULL,
  FOREIGN KEY (idFormaPago) REFERENCES loc_formaPagos (idFormaPagos) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (idCierreVentas) REFERENCES loc_cierreVentas (idCierreVentas) ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_formaPagos_ins AFTER INSERT ON loc_cierreVentas_formaPagos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_formaPagos',
        new.idPor,
        datetime('now'),
        NULL,
        new.idcvfp || '|' ||
            new.idCierreVentas || '|' ||
            new.idFormaPago || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_formaPagos_upd AFTER UPDATE ON loc_cierreVentas_formaPagos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_formaPagos',
        new.idPor,
        datetime('now'),
        old.idcvfp || '|' ||
            old.idCierreVentas || '|' ||
            old.idFormaPago || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        new.idcvfp || '|' ||
            new.idCierreVentas || '|' ||
            new.idFormaPago || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_formaPagos_del AFTER DELETE ON loc_cierreVentas_formaPagos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_formaPagos',
        old.idPor,
        datetime('now'),
        old.idcvfp || '|' ||
            old.idCierreVentas || '|' ||
            old.idFormaPago || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        NULL
    );
  END;


CREATE TABLE loc_cierreVentas_egresos (
  idcve INTEGER  PRIMARY KEY,
  idCierreVentas INTEGER NOT NULL,
  idlocEgreso INTEGER NOT NULL,
  valor NUMERIC NOT NULL,
  descripcion TEXT,
  idPor INTEGER NOT NULL,
  FOREIGN KEY (idCierreVentas) REFERENCES loc_cierreVentas (idCierreVentas) ON UPDATE CASCADE,
  FOREIGN KEY (idlocEgreso) REFERENCES loc_egresos (idLocEgreso) ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_egresos_ins AFTER INSERT ON loc_cierreVentas_egresos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_egresos',
        new.idPor,
        datetime('now'),
        NULL,
        new.idcve || '|' ||
            new.idCierreVentas || '|' ||
            new.idlocEgreso || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_egresos_upd AFTER UPDATE ON loc_cierreVentas_egresos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_egresos',
        new.idPor,
        datetime('now'),
        old.idcve || '|' ||
            old.idCierreVentas || '|' ||
            old.idlocEgreso || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        new.idcve || '|' ||
            new.idCierreVentas || '|' ||
            new.idlocEgreso || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_egresos_del AFTER DELETE ON loc_cierreVentas_egresos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_egresos',
        old.idPor,
        datetime('now'),
        old.idcve || '|' ||
            old.idCierreVentas || '|' ||
            old.idlocEgreso || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        NULL
    );
  END;

CREATE TABLE loc_cierreVentas_pagosPersonal (
  idCVPP INTEGER PRIMARY KEY,
  idCierreVentas INTEGER NOT NULL,
  idPagosPersonal INTEGER NOT NULL,
  idPersona INTEGER NOT NULL,
  valor NUMERIC NOT NULL,
  descripcion TEXT,
  idPor INTEGER  NOT NULL,
  FOREIGN KEY (idCierreVentas) REFERENCES loc_cierreVentas (idCierreVentas) ON UPDATE CASCADE,
  FOREIGN KEY (idPagosPersonal) REFERENCES loc_pagosPersonal (idPagosPersonal) ON UPDATE CASCADE,
  FOREIGN KEY (idPersona) REFERENCES ig_personas (idPersona) ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);
CREATE UNIQUE INDEX loc_cvpp_idCierrePagoPersona_UK ON loc_cierreVentas_pagosPersonal (idCierreVentas,idPagosPersonal,idPersona);

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_pagosPersonal_ins AFTER INSERT ON loc_cierreVentas_pagosPersonal
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_pagosPersonal',
        new.idPor,
        datetime('now'),
        NULL,
        new.idCVPP || '|' ||
            new.idCierreVentas || '|' ||
            new.idPagosPersonal || '|' ||
            new.idPersona || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

  CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_pagosPersonal_upd AFTER UPDATE ON loc_cierreVentas_pagosPersonal
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_pagosPersonal',
        new.idPor,
        datetime('now'),
        old.idCVPP || '|' ||
            old.idCierreVentas || '|' ||
            old.idPagosPersonal || '|' ||
            old.idPersona || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        new.idCVPP || '|' ||
            new.idCierreVentas || '|' ||
            new.idPagosPersonal || '|' ||
            new.idPersona || '|' ||
            new.valor || '|' ||
            new.descripcion || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_pagosPersonal_del AFTER DELETE ON loc_cierreVentas_pagosPersonal
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_pagosPersonal',
        old.idPor,
        datetime('now'),
        old.idCVPP || '|' ||
            old.idCierreVentas || '|' ||
            old.idPagosPersonal || '|' ||
            old.idPersona || '|' ||
            old.valor || '|' ||
            old.descripcion || '|' ||
            old.idPor,
        NULL
    );
  END;

CREATE TABLE loc_cierreVentas_depositos (
  idCierreVentasDepositos INTEGER PRIMARY KEY,
  idCierreVentas INTEGER NOT NULL,
  idBanco INTEGER NOT NULL,
  valor NUMERIC NOT NULL,
  observaciones TEXT,
  idPor INTEGER  NOT NULL,
  FOREIGN KEY (idBanco) REFERENCES ba_bancos (idBanco) ON UPDATE CASCADE,
  FOREIGN KEY (idCierreVentas) REFERENCES loc_cierreVentas (idCierreVentas) ON UPDATE CASCADE,
  FOREIGN KEY (idPor) REFERENCES ig_personas (idPersona) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_depositos_ins AFTER INSERT ON loc_cierreVentas_depositos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_depositos',
        new.idPor,
        datetime('now'),
        NULL,
        new.idCierreVentasDepositos || '|' ||
            new.idCierreVentas || '|' ||
            new.idBanco || '|' ||
            new.valor || '|' ||
            new.observaciones || '|' ||
            new.idPor
    );
  END;

  CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_depositos_upd AFTER UPDATE ON loc_cierreVentas_depositos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_depositos',
        new.idPor,
        datetime('now'),
        old.idCierreVentasDepositos || '|' ||
            old.idCierreVentas || '|' ||
            old.idBanco || '|' ||
            old.valor || '|' ||
            old.observaciones || '|' ||
            old.idPor,
        new.idCierreVentasDepositos || '|' ||
            new.idCierreVentas || '|' ||
            new.idBanco || '|' ||
            new.valor || '|' ||
            new.observaciones || '|' ||
            new.idPor
    );
  END;

CREATE TRIGGER IF NOT EXISTS loc_cierreVentas_depositos_del AFTER DELETE ON loc_cierreVentas_depositos
  BEGIN
    INSERT INTO ig_log VALUES(
        0, 
        'loc_cierreVentas_depositos',
        old.idPor,
        datetime('now'),
        old.idCierreVentasDepositos || '|' ||
            old.idCierreVentas || '|' ||
            old.idBanco || '|' ||
            old.valor || '|' ||
            old.observaciones || '|' ||
            old.idPor,
        NULL
    );
  END; */