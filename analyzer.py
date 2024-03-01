parser_table = {
    "S": {"automata": ["A", "I", "B", "V"]},
    "A": {"automata": ["automata"]},
    "V": {"}": ["}"]},
    "B": {"alfabeto": ["AL", "F"]},
    "AL": {"alfabeto": ["G", ":", "SM", "RA", ";"]},
    "G": {"alfabeto": ["alfabeto"]},
    "SM": {
        "a": ["a"],
        "b": ["b"],
        "c": ["c"],
        "d": ["d"],
        "e": ["e"],
        "f": ["f"],
        "g": ["g"],
        "h": ["h"],
        "i": ["i"],
        "j": ["j"],
        "k": ["k"],
        "l": ["l"],
        "m": ["m"],
        "n": ["n"],
        "o": ["o"],
        "p": ["p"],
        "q": ["q"],
        "r": ["r"],
        "s": ["s"],
        "t": ["t"],
        "u": ["u"],
        "v": ["v"],
        "w": ["w"],
        "x": ["x"],
        "y": ["y"],
        "z": ["z"],
        "0": ["0"],
        "1": ["1"],
        "2": ["2"],
        "3": ["3"],
        "4": ["4"],
        "5": ["5"],
        "6": ["6"],
        "7": ["7"],
        "8": ["8"],
        "9": ["9"],
    },
    "RA": {",": [",", "SM", "RA"], ";": []},
    "F": {"aceptacion": ["C", ":", "N", "R", ";"]},
    "C": {"aceptacion": ["aceptacion"]},
    "N": {"q": ["Q", "D"]},
    "D": {
        "0": ["0"],
        "1": ["1"],
        "2": ["2"],
        "3": ["3"],
        "4": ["4"],
        "5": ["5"],
        "6": ["6"],
        "7": ["7"],
        "8": ["8"],
        "9": ["9"],
    },
    "R": {",": [",", "N", "R"], ";": []},
    "I": {"{": ["{"]},
    "Q": {"q": ["q"]},
}


terminal_tokens = {
    "automata",
    "alfabeto",
    "aceptacion",
    "{",
    "}",
    ",",
    ";",
    ":",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "$",
}


def isTerminal(token: str):
    return token in terminal_tokens


def analyzer(input_list: list):
    history = "" #registro de los pasos que realiza
    input_list.append("$") #se manda al final para indicar el final de la entrada
    stack = ["$", "S"] #se inicializa la pila con el simbolo inicial

    while len(stack) > 0: #si la pila tiene elementos se ejecuta
        a_str = input_list[0] #analiza el primer dato de la lista
        X_str = stack[-1] # toma el ultimo elemnto de la pila
        history += f"Pila: {stack} | Entrada: {a_str}\n"
        print(f"Pila: {stack} | Entrada: {a_str}")
        if isTerminal(X_str):
            if X_str == a_str:
                stack.pop()
                input_list.pop(0)
            else:
                return {
                    "success": False,
                    "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {X_str}",
                    "history": history,
                }
        else:
            try:
                if parser_table[X_str][a_str] or parser_table[X_str][a_str] == []:
                    stack.pop()
                    stack.extend(parser_table[X_str][a_str][::-1])
                else:
                    return {
                        "success": False,
                        "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {parser_table[X_str]}",
                        "history": history,
                    }
            except KeyError:
                return {
                    "success": False,
                    "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {parser_table[X_str]}",
                    "history": history,
                }

    return {"success": True, "message": "Gramatica correcta", "history": history}
