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
menu :-
    nl,
    writeln('1. Que automoviles son familiares?'),
    writeln('2. Que automoviles son aptos para carga?'),
    writeln('3. Que automoviles son ecologicos?'),
    writeln('0. Salir'),
    write('Selecciona una opcion: '),
    read_line_to_string(user_input, Opcion),
    responder(Opcion).

% Consultas a la base de conocimiento.
responder("1") :-
    findall(X, automovil_familiar(X), Lista),
    mostrar_resultados('Automoviles familiares', Lista),
    menu.

responder("2") :-
    findall(X, apto_para_carga(X), Lista),
    mostrar_resultados('Automoviles aptos para carga', Lista),
    menu.

responder("3") :-
    findall(X, vehiculo_ecologico(X), Lista),
    mostrar_resultados('Automoviles ecologicos', Lista),
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
