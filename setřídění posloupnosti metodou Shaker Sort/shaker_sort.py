#funkce načítající textový soubor s reálnými čísly, specifikovaný v argumentu 'file', vracející seznam těchto reálných čísel
def load_numbers(file):
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
    return list_to_be_sorted

#funkce do které jako první argument patří seznam reálných čísel, které jsou setříděny v pořadí specifikovaném ve druhém argumentu, pro vzestupné setřídění method = 'asc' a pro sestupné setřídění method = 'desc'
def shaker_sort(list_to_be_sorted, method):
    for i in range(len(list_to_be_sorted)-1, 0, -1):
        finished = True
        
        if method == "asc":
            for j in range(i):
                if list_to_be_sorted[j] > list_to_be_sorted[j+1]:
                    list_to_be_sorted[j], list_to_be_sorted[j+1] = list_to_be_sorted[j+1], list_to_be_sorted[j]
                    finished = False

            for k in range(i, 0, -1):
                if list_to_be_sorted[k] < list_to_be_sorted[k-1]:
                        list_to_be_sorted[k], list_to_be_sorted[k-1] = list_to_be_sorted[k-1], list_to_be_sorted[k]
                        finished = False
        
        elif method == "desc":
            for j in range(i):
                if list_to_be_sorted[j] < list_to_be_sorted[j+1]:
                    list_to_be_sorted[j], list_to_be_sorted[j+1] = list_to_be_sorted[j+1], list_to_be_sorted[j]
                    finished = False 

            for k in range(i, 0, -1):
                if list_to_be_sorted[k] > list_to_be_sorted[k-1]:
                    list_to_be_sorted[k], list_to_be_sorted[k-1] = list_to_be_sorted[k-1], list_to_be_sorted[k]
                    finished = False
        
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
sorted_list = shaker_sort(numbers, "asc")

#uložení seřazené posloupnosti do textového souboru
save_sort(sorted_list, file)
