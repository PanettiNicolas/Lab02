import csv
from enum import nonmember


def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        biblioteca = {}

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                titolo = row[0]
                autore = row[1]
                anno = int(row[2])
                pagine = int(row[3])
                sezione = row[4]

                biblioteca[titolo] = { "Autore" : autore, "Anno" : anno, "Pagine" : pagine, "Sezione" : sezione}

        return biblioteca

    except FileNotFoundError:
        print("File non trovato")
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    if titolo in biblioteca:
        return None

    libro = { "Autore" : autore, "Anno" : anno, "Pagine" : pagine, "Sezione" : sezione}
    biblioteca[titolo] = libro

    with open(file_path, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([titolo, autore, anno, pagine, sezione])

    return libro



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    return biblioteca.get(titolo)


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""

    sezione = str(sezione)

    titoli = []
    for titolo, info in biblioteca.items():
        if info["Sezione"] == sezione:
            titoli.append(titolo)

    if not titoli:
        return None

    titoli_ordinati = sorted(titoli)

    return titoli_ordinati


def main():
    biblioteca = {}
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print("La sezione inserita non e' presente all'interno della biblioteca.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

