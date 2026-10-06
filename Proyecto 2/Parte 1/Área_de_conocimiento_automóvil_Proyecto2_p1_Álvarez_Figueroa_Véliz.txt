% __________________________________________
% BASE DE CONOCIMIENTO
% Dominio: Automóviles y mecánica básica
% Cristóbal Álvarez, Ignacio Figueroa, 
% Fracisca Véliz
% __________________________________________

% Permite que las definiciones de hecho/2 
% aparezcan separadas en distintas partes del archivo.
% Prolog lanza un aviso de muchas definiciones del 
% mismo predicado, pero van con distinto tipo de hechos.

:- discontiguous cantidad_puertas/2.
:- discontiguous cantidad_asientos/2.
:- discontiguous tamano/2.
:- discontiguous espacio_carga/2.
:- discontiguous altura_suelo/2.
:- discontiguous consumo_combustible/2.
:- discontiguous comodidad_conduccion/2.
:- discontiguous comodidad_interior/2.
:- discontiguous uso_principal/2.
:- discontiguous apto_familia/2.
:- discontiguous uso_fuera_carretera/2.
:- discontiguous tipo_motor/2.


% __________________________________________
% HECHOS DEFINIDOS
% __________________________________________



% __________________________________________
% TIPOS DE AUTOMOVIL
% __________________________________________

tipo_automovil(sedan).
tipo_automovil(suv).
tipo_automovil(pickup).
tipo_automovil(deportivo).
tipo_automovil(hatchback).

% __________________________________________
% SEDAN
% __________________________________________

cantidad_puertas(sedan, 4).
cantidad_asientos(sedan, 5).
tamano(sedan, mediano).
espacio_carga(sedan, medio).
altura_suelo(sedan, baja).
consumo_combustible(sedan, moderado).
comodidad_conduccion(sedan, alta).
comodidad_interior(sedan, alta).
uso_principal(sedan, urbano).
apto_familia(sedan, si).
uso_fuera_carretera(sedan, no).
tipo_motor(sedan, gasolina).

% __________________________________________
% SUV
% __________________________________________

cantidad_puertas(suv, 5).
cantidad_asientos(suv, 5).
tamano(suv, grande).
espacio_carga(suv, alto).
altura_suelo(suv, alta).
consumo_combustible(suv, alto).
comodidad_conduccion(suv, alta).
comodidad_interior(suv, media).
uso_principal(suv, familiar).
apto_familia(suv, si).
uso_fuera_carretera(suv, si).
tipo_motor(suv, diesel).

% __________________________________________
% PICKUP
% __________________________________________

cantidad_puertas(pickup, 4).
cantidad_asientos(pickup, 5).
tamano(pickup, grande).
espacio_carga(pickup, alto).
altura_suelo(pickup, alta).
consumo_combustible(pickup, alto).
comodidad_conduccion(pickup, media).
comodidad_interior(pickup, baja).
uso_principal(pickup, trabajo).
apto_familia(pickup, si).
uso_fuera_carretera(pickup, si).
tipo_motor(pickup, diesel).

% __________________________________________
% DEPORTIVO
% __________________________________________

cantidad_puertas(deportivo, 2).
cantidad_asientos(deportivo, 2).
tamano(deportivo, mediano).
espacio_carga(deportivo, bajo).
altura_suelo(deportivo, bajo).
consumo_combustible(deportivo, alto).
comodidad_conduccion(deportivo, alta).
comodidad_interior(deportivo, media).
uso_principal(deportivo, urbano).
apto_familia(deportivo, no).
uso_fuera_carretera(deportivo, no).
tipo_motor(deportivo, gasolina).

% __________________________________________
% HATCHBACK
% __________________________________________

cantidad_puertas(hatchback, 4).
cantidad_asientos(hatchback, 5).
tamano(hatchback, mediano).
espacio_carga(hatchback, bajo).
altura_suelo(hatchback, media).
consumo_combustible(hatchback, bajo).
comodidad_conduccion(hatchback, alta).
comodidad_interior(hatchback, alta).
uso_principal(hatchback, urbano).
apto_familia(hatchback, si).
uso_fuera_carretera(hatchback, no).
tipo_motor(hatchback, electrico).



% __________________________________________
% REGLAS DEFINIDAS
% __________________________________________



% __________________________________________
% REGLAS DE INFERENCIA CON LÓGICA DE
% PRIMER ORDEN (L.P.O)
% __________________________________________


% Regla 1: Automóvil familiar
% Si X es un tipo de automóvil, tiene al menos 5 asientos
% y es apto para familia, entonces X es un automóvil familiar.

% TipoAutomovil(x) ∧ CantidadAsientos(x,a) ∧ a >= 5 ∧
% AptoFamilia(x,si) -> AutomovilFamiliar(x)

automovil_familiar(X) :-
    tipo_automovil(X),
    cantidad_asientos(X, A),
    A >= 5,
    apto_familia(X, si).

% __________________________________________

% Regla 2: Automóvil apto para carga
% Si X es un tipo de automóvil y posee espacio de carga alto,
% entonces X es apto para transportar carga.

% TipoAutomovil(x) ∧ EspacioCarga(x,alto)
% -> AptoParaCarga(x)

apto_para_carga(X) :-
    tipo_automovil(X),
    espacio_carga(X, alto).

% __________________________________________

% Regla 3: Automóvil apto para uso off-road
% Si X es un tipo de automóvil, posee una altura de suelo alta
% y permite uso fuera de carretera, entonces X es apto para off-road.

% TipoAutomovil(x) ∧ AlturaSuelo(x,alta) ∧
% UsoFueraCarretera(x,si) -> AptoOffRoad(x)

apto_offroad(X) :-
    tipo_automovil(X),
    altura_suelo(X, alta),
    uso_fuera_carretera(X, si).

% __________________________________________

% Regla 4: Vehículo urbano
% Si X es un tipo de automóvil y su uso principal es urbano,
% entonces X se considera un vehículo urbano.

% TipoAutomovil(x) ∧ UsoPrincipal(x,urbano)
% -> VehiculoUrbano(x)

vehiculo_urbano(X) :-
    tipo_automovil(X),
    uso_principal(X, urbano).

% __________________________________________

% Regla 5: Vehículo grande
% Si X es un tipo de automóvil y su tamaño es grande,
% entonces X se considera un vehículo grande.

% TipoAutomovil(x) ∧ Tamano(x,grande)
% -> VehiculoGrande(x)

vehiculo_grande(X) :-
    tipo_automovil(X),
    tamano(X, grande).

% __________________________________________

% Regla 6: Vehículo de bajo consumo
% Si X es un tipo de automóvil y su consumo de combustible
% es bajo, entonces X se considera un vehículo de bajo consumo.

% TipoAutomovil(x) ∧ ConsumoCombustible(x,bajo)
% -> VehiculoBajoConsumo(x)

vehiculo_bajo_consumo(X) :-
    tipo_automovil(X),
    consumo_combustible(X, bajo).

% __________________________________________

% Regla 7: Automóvil cómodo para la familia
% Si X es un automóvil familiar y posee comodidad de conducción
% alta, entonces X es cómodo para una familia.

% AutomovilFamiliar(x) ∧ ComodidadConduccion(x,alta)
% -> ComodoParaFamilia(x)

comodo_para_familia(X) :-
    automovil_familiar(X),
    comodidad_conduccion(X, alta).

% __________________________________________

% Regla 8: Automóvil apto para trabajo
% Si X es un tipo de automóvil, su uso principal es trabajo
% y posee espacio de carga alto, entonces X es apto para trabajo.

% TipoAutomovil(x) ∧ UsoPrincipal(x,trabajo) ∧
% EspacioCarga(x,alto) -> AptoParaTrabajo(x)

apto_para_trabajo(X) :-
    tipo_automovil(X),
    uso_principal(X, trabajo),
    espacio_carga(X, alto).

% __________________________________________

% Regla 9: Buena capacidad de pasajeros
% Si X es un tipo de automóvil y tiene al menos 5 asientos,
% entonces X posee buena capacidad de pasajeros.

% TipoAutomovil(x) ∧ CantidadAsientos(x,a) ∧ a >= 5
% -> BuenaCapacidadPasajeros(x)

buena_capacidad_pasajeros(X) :-
    tipo_automovil(X),
    cantidad_asientos(X, A),
    A >= 5.

% __________________________________________

% Regla 10: Vehículo urbano de bajo consumo
% Si X es un tipo de automóvil, su uso principal es urbano
% y su consumo de combustible es bajo, entonces X combina
% uso urbano y bajo consumo.

% TipoAutomovil(x) ∧ UsoPrincipal(x,urbano) ∧
% ConsumoCombustible(x,bajo) -> UrbanoBajoConsumo(x)

urbano_bajo_consumo(X) :-
    tipo_automovil(X),
    uso_principal(X, urbano),
    consumo_combustible(X, bajo).

% __________________________________________

% Regla 11: Vehículo espacioso para pasajeros
% Si X es un tipo de automóvil, tiene 4 o más puertas
% y tiene 5 o más asientos, entonces X se considera
% un vehículo espacioso para pasajeros.

% TipoAutomovil(x) ∧ CantidadPuertas(x,p) ∧ p>=4 ∧
% CantidadAsientos(x,a) ∧ a>=5 -> VehiculoEspacioso(x)

vehiculo_espacioso(X) :-
    tipo_automovil(X),
    cantidad_puertas(X, P),
    P >= 4,
    cantidad_asientos(X, A),
    A >= 5.

% __________________________________________

% Regla 12: Vehículo con interior cómodo
% Si X es un tipo de automóvil y su comodidad interior
% es alta, entonces X se considera un vehículo con
% interior cómodo.

% TipoAutomovil(x) ∧ ComodidadInterior(x,alta)
% -> InteriorComodo(x)

interior_comodo(X) :-
    tipo_automovil(X),
    comodidad_interior(X, alta).
% __________________________________________

% Regla 13: Vehículo ecológico
% Si un automóvil utiliza motor eléctrico,
% entonces se considera ecológico.

% TipoAutomovil(x) ∧ TipoMotor(x,electrico)
% -> VehiculoEcologico(x)

vehiculo_ecologico(X) :-
    tipo_automovil(X),
    tipo_motor(X, electrico).
% __________________________________________

% Regla 14: Vehículo de trabajo pesado
% Si un automóvil utiliza motor diesel
% y posee espacio de carga alto,
% entonces es apto para trabajo pesado.

% TipoMotor(x,diesel) ∧ EspacioCarga(x,alto)
% ∧ UsoPrincipal(x,trabajo)
% -> VehiculoTrabajoPesado(x)

vehiculo_trabajo_pesado(X) :-
    tipo_motor(X, diesel),
    espacio_carga(X, alto),
    uso_principal(X, trabajo).
% __________________________________________

% Regla 15: Vehículo familiar para aventuras
% Si un automóvil es familiar y además
% es apto para uso off-road, entonces
% se considera adecuado para viajes y aventuras.

% AutomovilFamiliar(x) ∧ AptoOffRoad(x)
% -> VehiculoFamiliarAventura(x)

vehiculo_familiar_aventura(X) :-
    automovil_familiar(X),
    apto_offroad(X).

% __________________________________________
% PREGUNTAS DE PRUEBA
% __________________________________________

% 1. ¿El sedán es un tipo de automóvil?
% ?- tipo_automovil(sedan).

% 2. ¿Cuántas puertas tiene un sedán?
% ?- cantidad_puertas(sedan, X).

% 3. ¿Cuántos asientos tiene un suv?
% ?- cantidad_asientos(suv, X).

% 4. ¿Qué tipos de automóvil tienen espacio de carga alto?
% ?- espacio_carga(X, alto).

% 5. ¿Cuál es el uso principal de una pickup?
% ?- uso_principal(pickup, X).

% 6. ¿Qué automóviles son aptos para familia?
% ?- apto_familia(X, si).

% 7. ¿Qué automóviles tienen consumo de combustible alto?
% ?- consumo_combustible(X, alto).

% 8. ¿Qué automóviles tienen comodidad de conducción alta?
% ?- comodidad_conduccion(X, alta).

% 9. ¿Qué automóviles pueden considerarse familiares según las reglas?
% ?- automovil_familiar(X).

% 10. ¿Qué automóviles son aptos para transportar carga?
% ?- apto_para_carga(X).

% 11. ¿Qué automóviles son aptos para uso off-road según las reglas?
% ?- apto_offroad(X).

% 12. ¿Qué automóviles son considerados urbanos?
% ?- vehiculo_urbano(X).

% 13. ¿Qué automóviles son considerados grandes?
% ?- vehiculo_grande(X).

% 14. ¿Qué automóviles tienen bajo consumo de combustible?
% ?- vehiculo_bajo_consumo(X).

% 15. ¿Qué automóviles son cómodos para una familia?
% ?- comodo_para_familia(X).

% 16. ¿Qué automóviles son apropiados para trabajo?
% ?- apto_para_trabajo(X).

% 17. ¿Qué automóviles tienen buena capacidad de pasajeros?
% ?- buena_capacidad_pasajeros(X).

% 18. ¿Qué automóviles combinan uso urbano y bajo consumo?
% ?- urbano_bajo_consumo(X).

% 19. ¿El deportivo es apto para una familia?
% ?- apto_familia(deportivo, si).

% 20. ¿Qué tipo de automóvil tiene comodidad interior alta?
% ?- comodidad_interior(X, alta).

% 21. ¿Qué automóviles son espaciosos para pasajeros?
% ?- vehiculo_espacioso(X).

% 22. ¿Qué automóviles poseen un interior cómodo?
% ?- interior_comodo(X).

% 23. ¿Qué automóviles son ecológicos?
% ?- vehiculo_ecologico(X).

% 24. ¿Qué automóviles son de trabajo pesado?
% ?- vehiculo_trabajo_pesado(X).

% 25. ¿Qué automóviles familiares sirven para aventuras?
% ?- vehiculo_familiar_aventura(X).

%____________________________________________________
% Descripción de la Base de Conocimiento

% La presente base de conocimiento corresponde al dominio de automóviles y mecánica básica, y tiene como objetivo representar información sobre distintos tipos de automóviles para ser utilizada posteriormente por un chatbot desarrollado mediante Lógica de Primer Orden y Prolog.
% Se definieron cinco tipos de automóvil: sedán, SUV, pickup, deportivo y hatchback. Para cada uno se incorporaron hechos relacionados con características como cantidad de puertas y asientos, tamaño, espacio de carga, altura al suelo, consumo de combustible, comodidad, uso principal y aptitud para uso familiar o fuera de carretera.
% La información se representa mediante predicados de Prolog, donde cada hecho describe una característica determinada. Además, se incorporan reglas de inferencia que relacionan estos hechos para obtener nuevo conocimiento, como determinar si un automóvil es familiar, apto para carga, uso fuera de carretera, trabajo o si presenta bajo consumo.
% De esta manera, la base permite realizar tanto consultas directas sobre los hechos almacenados como consultas que requieren inferencia mediante reglas, sirviendo como base para el posterior desarrollo del chatbot.
% También se incorporó el atributo tipo_motor para representar aspectos básicos de mecánica automotriz.Esto permite generar nuevas inferencias, como la identificación de vehículos ecológicos, vehículos aptos para trabajo pesado y vehículos familiares adecuados para actividades fuera de carretera.