:- use_module(library(readutil)).
:- use_module(library(lists)).

% Cargar la base de conocimiento existente.
:- ensure_loaded('Area de conocimiento automOviles.pl').

% Inicio del chatbot.
iniciar :-
    nl,
    writeln('=================================='),
    writeln(' CHATBOT DE AUTOMOVILES - PROLOG'),
    writeln('=================================='),
    writeln('Escribe un numero para consultar.'),
    menu.

% Menu principal.

% Menu principal.
menu :-
    nl,
    writeln('========== MENU DE CONSULTAS =========='),
    writeln('1. El sedan es un tipo de automovil?'),
    writeln('2. Cuantas puertas tiene un sedan?'),
    writeln('3. Cuantos asientos tiene un SUV?'),
    writeln('4. Que automoviles tienen espacio de carga alto?'),
    writeln('5. Cual es el uso principal de una pickup?'),
    writeln('6. Que automoviles son aptos para familia?'),
    writeln('7. Que automoviles tienen consumo alto?'),
    writeln('8. Que automoviles tienen comodidad de conduccion alta?'),
    writeln('9. Que automoviles son familiares segun las reglas?'),
    writeln('10. Que automoviles son aptos para carga?'),
    writeln('11. Que automoviles son aptos para off-road?'),
    writeln('12. Que automoviles son urbanos?'),
    writeln('13. Que automoviles son grandes?'),
    writeln('14. Que automoviles tienen bajo consumo?'),
    writeln('15. Que automoviles son comodos para familia?'),
    writeln('16. Que automoviles son aptos para trabajo?'),
    writeln('17. Que automoviles tienen buena capacidad de pasajeros?'),
    writeln('18. Que automoviles son urbanos y de bajo consumo?'),
    writeln('19. El deportivo es apto para familia?'),
    writeln('20. Que automoviles tienen comodidad interior alta?'),
    writeln('21. Que automoviles son espaciosos?'),
    writeln('22. Que automoviles poseen interior comodo?'),
    writeln('23. Que automoviles son ecologicos?'),
    writeln('24. Que automoviles son de trabajo pesado?'),
    writeln('25. Que automoviles familiares sirven para aventuras?'),
    writeln('0. Salir'),
    write('Selecciona una opcion: '),
    read_line_to_string(user_input, Opcion),
    responder(Opcion).


% Consultas a la base de conocimiento.

responder("1") :-
    ( tipo_automovil(sedan) ->
        writeln('Si, el sedan es un tipo de automovil.')
    ;
        writeln('No, el sedan no figura como tipo de automovil.')
    ),
    menu.

responder("2") :-
    cantidad_puertas(sedan, X),
    format('El sedan tiene ~w puertas.~n', [X]),
    menu.

responder("3") :-
    cantidad_asientos(suv, X),
    format('El SUV tiene ~w asientos.~n', [X]),
    menu.

responder("4") :-
    findall(X, espacio_carga(X, alto), Lista),
    mostrar_resultados('Automoviles con espacio de carga alto', Lista),
    menu.

responder("5") :-
    uso_principal(pickup, X),
    format('El uso principal de una pickup es: ~w.~n', [X]),
    menu.

responder("6") :-
    findall(X, apto_familia(X, si), Lista),
    mostrar_resultados('Automoviles aptos para familia', Lista),
    menu.

responder("7") :-
    findall(X, consumo_combustible(X, alto), Lista),
    mostrar_resultados('Automoviles con consumo alto', Lista),
    menu.

responder("8") :-
    findall(X, comodidad_conduccion(X, alta), Lista),
    mostrar_resultados('Automoviles con comodidad de conduccion alta', Lista),
    menu.

responder("9") :-
    findall(X, automovil_familiar(X), Lista),
    mostrar_resultados('Automoviles familiares', Lista),
    menu.

responder("10") :-
    findall(X, apto_para_carga(X), Lista),
    mostrar_resultados('Automoviles aptos para carga', Lista),
    menu.

responder("11") :-
    findall(X, apto_offroad(X), Lista),
    mostrar_resultados('Automoviles aptos para off-road', Lista),
    menu.

responder("12") :-
    findall(X, vehiculo_urbano(X), Lista),
    mostrar_resultados('Automoviles urbanos', Lista),
    menu.

responder("13") :-
    findall(X, vehiculo_grande(X), Lista),
    mostrar_resultados('Automoviles grandes', Lista),
    menu.

responder("14") :-
    findall(X, vehiculo_bajo_consumo(X), Lista),
    mostrar_resultados('Automoviles de bajo consumo', Lista),
    menu.

responder("15") :-
    findall(X, comodo_para_familia(X), Lista),
    mostrar_resultados('Automoviles comodos para familia', Lista),
    menu.

responder("16") :-
    findall(X, apto_para_trabajo(X), Lista),
    mostrar_resultados('Automoviles aptos para trabajo', Lista),
    menu.

responder("17") :-
    findall(X, buena_capacidad_pasajeros(X), Lista),
    mostrar_resultados('Automoviles con buena capacidad de pasajeros', Lista),
    menu.

responder("18") :-
    findall(X, urbano_bajo_consumo(X), Lista),
    mostrar_resultados('Automoviles urbanos y de bajo consumo', Lista),
    menu.

responder("19") :-
    ( apto_familia(deportivo, si) ->
        writeln('Si, el deportivo es apto para familia.')
    ;
        writeln('No, el deportivo no es apto para familia.')
    ),
    menu.

responder("20") :-
    findall(X, comodidad_interior(X, alta), Lista),
    mostrar_resultados('Automoviles con comodidad interior alta', Lista),
    menu.

responder("21") :-
    findall(X, vehiculo_espacioso(X), Lista),
    mostrar_resultados('Automoviles espaciosos', Lista),
    menu.

responder("22") :-
    findall(X, interior_comodo(X), Lista),
    mostrar_resultados('Automoviles con interior comodo', Lista),
    menu.

responder("23") :-
    findall(X, vehiculo_ecologico(X), Lista),
    mostrar_resultados('Automoviles ecologicos', Lista),
    menu.

responder("24") :-
    findall(X, vehiculo_trabajo_pesado(X), Lista),
    mostrar_resultados('Automoviles de trabajo pesado', Lista),
    menu.

responder("25") :-
    findall(X, vehiculo_familiar_aventura(X), Lista),
    mostrar_resultados('Automoviles familiares para aventuras', Lista),
    menu.

responder("0") :-
    writeln('Gracias por utilizar el chatbot.').

responder(end_of_file) :-
    writeln('Chatbot finalizado.').

responder(_) :-
    writeln('Opcion no reconocida. Intenta nuevamente.'),
    menu.


% Mostrar respuestas obtenidas de Prolog.
mostrar_resultados(Titulo, Lista) :-
    nl,
    ( Lista = [] ->
        writeln('No se encontraron resultados.')
    ;
        sort(Lista, SinDuplicados),
        atomic_list_concat(SinDuplicados, ', ', Texto),
        format('~w: ~w.~n', [Titulo, Texto])
    ).
