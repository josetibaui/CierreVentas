use palmeras;

drop table if exists loc_cierreVentasD;
create table if not exists loc_cierreVentasD (
codLocal smallint
,fecha DATE
,ventaTotal DECIMAL(14,4) DEFAULT 0
,datafast DECIMAL(14,4) DEFAULT 0
,medianet DECIMAL(14,4) DEFAULT 0
,uber DECIMAL(14,4) DEFAULT 0
,pedidosYa DECIMAL(14,4) DEFAULT 0
,rappic DECIMAL(14,4) DEFAULT 0
,cheques DECIMAL(14,4) DEFAULT 0
,transferencias DECIMAL(14,4) DEFAULT 0
,retenciones DECIMAL(14,4) DEFAULT 0
,efectivo DECIMAL(14,4) DEFAULT 0
,compras DECIMAL(14,4) DEFAULT 0
,pagoDiasLibres DECIMAL(14,4) DEFAULT 0
,eventuales DECIMAL(14,4) DEFAULT 0
,sueldos DECIMAL(14,4) DEFAULT 0
,anticipos DECIMAL(14,4) DEFAULT 0
,prestamos DECIMAL(14,4) DEFAULT 0
,transporte DECIMAL(14,4) DEFAULT 0
,cEmpleados DECIMAL(14,4) DEFAULT 0
,mantenimientos DECIMAL(14,4) DEFAULT 0
,otrosGastos DECIMAL(14,4) DEFAULT 0
,totalGastos DECIMAL(14,4) DEFAULT 0
,deposito1 DECIMAL(14,4) DEFAULT 0
,deposito2 DECIMAL(14,4) DEFAULT 0
,diferenciaDepositos DECIMAL(14,4) DEFAULT 0
,cortEmpleados DECIMAL(14,4) DEFAULT 0
,cortGerencia DECIMAL(14,4) DEFAULT 0
,cortCumpleaneros DECIMAL(14,4) DEFAULT 0
,cortPromociones DECIMAL(14,4) DEFAULT 0
,cortTotal DECIMAL(14,4) DEFAULT 0
,por CHAR(3)
);
load data local infile
'/home/users/jtibau/Desarrollo/Palmeras/CierreVentas/CierreVentas_M6J.csv'
into table loc_cierreVentasD
fields terminated by ','
ignore 16 lines
(
 codLocal
, @fecha
, @ventaTotal
, @datafast
, @medianet
, @uber
, @pedidosYa
, @rappic
, @cheques
, @transferencias
, @retenciones
, @efectivo
, @compras
, @pagoDiasLibres
, @eventuales
, @sueldos
, @anticipos
, @prestamos
, @transporte
, @cEmpleados
, @mantenimientos
, @otrosGastos
, @totalGastos
, @deposito1
, @deposito2
, @diferenciaDepositos
, @cortEmpleados
, @cortGerencia
, @cortCumpleaneros
, @cortPromociones
, @cortTotal
, por
)
set 
  fecha = STR_TO_DATE(@fecha, '%d-%m-%y')
, ventaTotal = IF(@ventaTotal = '', 0, @ventaTotal)
, datafast = IF(@datafast = '', 0, @datafast)
, medianet = IF(@medianet = '', 0, @medianet)
, uber = IF(@uber = '' ,0 ,uber)
, pedidosYa = IF(@pedidosYa = '', 0, @pedidosYa)
, rappic = IF(@rappic = '', 0, @rappic)
, cheques = IF(@cheques = '', 0, @cheques)
, transferencias = IF(@transferencias = '', 0, @transferencias)
, retenciones = IF(@retenciones = '', 0, @retenciones)
, efectivo = IF(@efectivo = '', 0, @efectivo)
, compras = IF(@compras = '', 0, @compras)
, pagoDiasLibres = IF(@pagoDiasLibres = '', 0, @pagoDiasLibres)
, eventuales = IF(@eventuales = '', 0, @eventuales)
, sueldos = IF(@sueldos = '', 0, @sueldos)
, anticipos = IF(@anticipos = '', 0, @anticipos)
, prestamos = IF(@prestamos = '', 0, @prestamos)
, transporte = IF(@transporte = '', 0, @transporte)
, cEmpleados = IF(@cEmpleados = '', 0, @cEmpleados)
, mantenimientos = IF(@mantenimientos = '', 0, @mantenimientos)
, otrosGastos = IF(@otrosGastos = '', 0, @otrosGastos)
, totalGastos = IF(@totalGastos = '', 0, @totalGastos)
, deposito1 = IF(@deposito1 = '', 0, @deposito1)
, deposito2 = IF(@deposito2 = '', 0, @deposito2)
, diferenciaDepositos = IF(@diferenciaDepositos = '', 0, @diferenciaDepositos)
, cortEmpleados = IF(@cortEmpleados = '', 0, @cortEmpleados)
, cortGerencia = IF(@cortGerencia = '', 0, @cortGerencia)
, cortCumpleaneros = IF(@cortCumpleaneros = '', 0, @cortCumpleaneros)
, cortPromociones = IF(@cortPromociones = '', 0, @cortPromociones)
, cortTotal = IF(@cortTotal = '', 0, @cortTotal)
;

select codLocal, fecha, count(*) from loc_cierreVentasD
group by 1,2 having count(*) > 1;
SELECT * FROM loc_cierreVentasD where fecha < '2022-01-01';

CREATE OR REPLACE
SQL SECURITY INVOKER
VIEW loc_cierreVentas_vw AS
SELECT `loc_cierreVentasD`.`codLocal` AS 'Local',
    `loc_cierreVentasD`.`fecha` AS 'Fecha',
    `loc_cierreVentasD`.`ventaTotal` AS 'Venta Total',
    `loc_cierreVentasD`.`datafast` AS 'Datafast',
    `loc_cierreVentasD`.`medianet` AS 'Medianet',
    `loc_cierreVentasD`.`uber` AS 'Uber',
    `loc_cierreVentasD`.`pedidosYa` AS 'Pedidos Ya',
    `loc_cierreVentasD`.`rappic` AS 'Rappi',
    `loc_cierreVentasD`.`cheques` AS 'Cheques',
    `loc_cierreVentasD`.`transferencias` AS 'Transferencias',
    `loc_cierreVentasD`.`retenciones` AS 'Retenciones',
    `loc_cierreVentasD`.`efectivo` AS 'Efectivo',
    `loc_cierreVentasD`.`compras` AS 'Compras Insumos',
    `loc_cierreVentasD`.`transporte` AS 'Transporte',
    `loc_cierreVentasD`.`mantenimientos` AS 'Mantenimientos',
    `loc_cierreVentasD`.`cEmpleados` AS 'Consumo Empleados',
    `loc_cierreVentasD`.`sueldos` AS 'Sueldos',
    `loc_cierreVentasD`.`pagoDiasLibres` AS 'Pago Días Libres',
    `loc_cierreVentasD`.`eventuales` AS 'Eventuales',
    `loc_cierreVentasD`.`anticipos` AS 'Anticipos',
    `loc_cierreVentasD`.`prestamos` AS 'Préstamos',
    `loc_cierreVentasD`.`otrosGastos` AS 'Otros Gastos',
    `loc_cierreVentasD`.`totalGastos` AS 'Total Gastos',
    `loc_cierreVentasD`.`deposito1` AS 'Depósito 1',
    `loc_cierreVentasD`.`deposito2` AS 'Depósito 2',
    `loc_cierreVentasD`.`diferenciaDepositos` AS 'Diferencia en Depósitos',
    `loc_cierreVentasD`.`cortEmpleados` AS 'Cortesías Empleados',
    `loc_cierreVentasD`.`cortGerencia` AS 'Cortesías Gerencia',
    `loc_cierreVentasD`.`cortCumpleaneros` AS 'Cortesías Cumpleañeros',
    `loc_cierreVentasD`.`cortPromociones` AS 'Cortesías Promociones',
    `loc_cierreVentasD`.`cortTotal` AS 'Total Cortesías',
    `loc_cierreVentasD`.`por` AS 'Digitado'
FROM `palmeras`.`loc_cierreVentasD`
ORDER BY 
 `loc_cierreVentasD`.`fecha`
,`loc_cierreVentasD`.`codLocal`;

update loc_cierreVentasD set fecha = '2022-02-03' where fecha = '2002-02-03' and por = 'ECT';
