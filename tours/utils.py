# меняет окончание к слову тур (-а, -ов,)
def change_ending_word(count):
    if 10 <= count <= 20 or (count % 10 in [5, 6, 7, 8, 9, 0]):
        return 'туров'
    if count == 1 or count % 10 in [1]:
        return 'тур'
    if count % 10 in [2, 3, 4]:
        return 'тура'
