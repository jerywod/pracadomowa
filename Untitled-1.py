# 1. Utwórz pustą listę o nazwie "numbers".
numbers = []

# 2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
for i in range(5):
    number = float(input("Podaj liczbę: "))
    numbers.append(number)

# 3. Oblicz sumę liczb znajdujących się w liście "numbers".
suma = sum(numbers)
print(f"Suma liczb: {suma}")

# 4. Znajdź największą liczbę w liście "numbers".
max_number = max(numbers)
print(f"Największa liczba: {max_number}")

# 5. Znajdź najmniejszą liczbę w liście "numbers".
min_number = min(numbers)
print(f"Najmniejsza liczba: {min_number}")

# 6. Znajdź średnią arytmetyczną liczb w liście "numbers".
srednia = suma / len(numbers)
print(f"Średnia arytmetyczna: {srednia}")

# 7. Znajdź ilość liczb parzystych w liście "numbers".
liczby_parzyste = [x for x in numbers if x % 2 == 0]
ilosc_parzystych = len(liczby_parzyste)
print(f"Ilość liczb parzystych: {ilosc_parzystych}")

# 8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
duplicates = [x for x in numbers if numbers.count(x) > 1]
print(f"Powtarzające się elementy: {duplicates}")

# 9. Usuń wszystkie powtarzające się elementy z listy "numbers".
numbers = list(set(numbers))

# 10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
squares = [x**2 for x in numbers]

print(f"Kwadraty liczb: {squares}")