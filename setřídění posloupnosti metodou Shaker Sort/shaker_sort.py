#funkce načítající textový soubor s reálnými čísly, specifikovaný v argumentu 'file', vracející seznam těchto reálných čísel
def load_numbers(file):
    try:
        with open(file) as f:
            a_string = ""
            for line in f:
                a_string += line
            if len(a_string) == 0:
                exit("Vstupní soubor je prázdný")
            a_list = a_string.split()
            list_to_be_sorted = []
            for a in a_list:
                try:
                    number = float(a)
                    list_to_be_sorted.append(number)
                except ValueError:
                    exit("Vstup obsahuje neplatnou hodnotu ležící mimo množinu reálných čísel: '{}'".format(a))
    except FileNotFoundError:
        exit('Zadaný soubor neexistuje')
    except UnicodeDecodeError:
        exit('Soubor nelze otevřít')

    return list_to_be_sorted

#funkce porovnávající argumenty 'a' a 'b' v pořadí závislém na argumentu 'is_descendant' jejímž třetím argumentem 'finished' je booleovská proměnná, funkce vrací proměnné 'a' a 'b' v určitém pořadí a booleovskou proměnnou
def compare(a, b, finished, is_descendant):
    if is_descendant:
        if a > b:
            return a, b, False
        else:
            return b, a, finished
    else:
        if a < b:
            return a, b, False
        else:
            return b, a, finished

#funkce do které jako první argument patří seznam reálných čísel, které jsou setříděny v pořadí specifikovaném ve druhém argumentu, pro vzestupné setřídění method = 'asc' a pro sestupné setřídění method = 'desc'
def shaker_sort(list_to_be_sorted, method):
    for i in range(len(list_to_be_sorted)-1, 0, -1):
        finished = True
        is_descendant = False
        
        if method == "desc":
            is_descendant = True
            
        for j in range(i):
            list_to_be_sorted[j], list_to_be_sorted[j+1], finished = compare(list_to_be_sorted[j+1], list_to_be_sorted[j], finished, is_descendant)
            
        for j in range(i, 0, -1):
            list_to_be_sorted[j-1], list_to_be_sorted[j], finished = compare(list_to_be_sorted[j], list_to_be_sorted[j-1], finished, is_descendant)
        
        if finished:
            return list_to_be_sorted

#funkce ukládající setříděnou posloupnost vloženou v prvním argumentu do textového souboru specifikovaného v argumentu druhém
def save_sort(sorted_list, file):
    num_string = ""
    for num in sorted_list:
        num = str(num) + " "
        num_string += num

    with open(file, mode = 'w') as f:
        f.write(num_string)

#proměnná file obsahuje místo uložení vstupního souboru s posloupností reálných čísel
file = 'numbers_sort.txt'

#do proměnné numbers se ukládá seznam reálných čísel
numbers = load_numbers(file)

#do proměnné sorted list se ukládá seřazený seznam reálných čísel
sorted_list = shaker_sort(numbers, "desc")

#uložení seřazené posloupnosti do textového souboru
save_sort(sorted_list, "numbers_sorted.txt")
