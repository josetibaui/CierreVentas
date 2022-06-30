use plmerp_jti;

start transaction;
/*
INSERT INTO ig_locales
SELECT * FROM plm_rev.ig_local
ORDER BY codLocal;
*/

INSERT INTO loc_egresos VALUES
  (0, 'Compras Insumos', '', 1 )
, (0, 'Pago Días Libres', '', 1 )
, (0, 'Pago Eventuales', '', 1 )
, (0, 'Pago Sueldos', '', 1 )
, (0, 'Transporte', '', 1 )
, (0, 'Consumos Empleados', '', 1 )
, (0, 'Mantenimientos', '', 1 )
, (0, 'Otros Gastos', '', 1 );

INSERT INTO loc_formaPagos VALUES
  (0, 'Datafast','', 1)
, (0, 'Medianet','', 1)
, (0, 'Uber','', 1)
, (0, 'PedidosYa','', 1)
, (0, 'Rappic','', 1)
, (0, 'Cheques','', 1)
, (0, 'Transferencias','', 1)
, (0, 'Retenciones','', 1)
, (0, 'Efectivo','', 1);

INSERT INTO loc_pagosPersonal VALUES 
  (0, 'Anticipos', 'A', '', 1)
, (0, 'Préstamos', 'P', '', 1);

INSERT INTO loc_cortesias VALUES
  (0, '', '', 1);

ROLLBACK;