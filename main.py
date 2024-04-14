print("""Dzien dobry! Jak się masz?""")
odpowiedz=input()
print("Cieszę się, że możemy razem popracować! A Ty?")
reakcja=input()
print("""Pomogę Ci przygotować kartkę urodzionową z życzeniami dla kogoś bliskiego!
Możemy zaczynać?""")
odpowiedz2=input()
print("""Zatem Pierwsze pytanie: 
Jak ma na imię solenizant?""")
name=input()
print("Drugie pytanie. Jaki jest rok urodzenia solenizanta?")
rok_urodzenia=input()
print(f"Zgodnie z powyższymi informacjami, imię solenianta to {name} a rok urodzenia to {rok_urodzenia}.")
print(f"Teraz napisz proszę życzenia urodzinowe, jakie chcesz przekazać solenizantowi o imieniu {name}!")
zyczenia=input()
print("Super! I ostatnie pytanie. Jak masz na imię? Podpiszemy nim kartkę, aby solenizant znał nadawcę!")
name2=input()
print("Dziękuję! Mam już wszystkie dane. Chcesz zobaczyć efekt?")
odpowiedz3=input()
wiek=2024-int(rok_urodzenia)
print(f"""Oto on:

{name}! Wszystkiego najlepszego z okazji {wiek} urodzin! 

{name2} ma dla Ciebie wiadomość:

{zyczenia}

Szczęśliwego dnia urodzin!""")

