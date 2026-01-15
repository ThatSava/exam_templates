# Skripta za inicijalizaciju repozitoriijuma,

from examGenerator import *
import os 
import shutil

def main(rok, godina, datum, k = False, i = False, opcije = True):
    #Proveri da li je dobar mesec i godina
    if rok not in validMonths or not validYear(godina):
        raise ValueError("Pogresan format roka ili godine!")

    #Proveri tip obaveze
    if not bool(k)^bool(i):
            raise ValueError("Tip mora biti postavljen ili kao kolokvijum ili kao ispit")
    
    exam_name = f"si1oe_{rok}-{godina}"

    try:
        shutil.copytree('template', exam_name)
        print('Uspesno kreiran direktorijum za obavezu')
        
        with open(os.path.join(exam_name, "generics.tex"), 'w', encoding='utf-8') as generics:
            #Definisi boolean-e
            generics.write(r"\newboolean{opcijeZaPolaganje}" + "\n")
            generics.write(r"\newboolean{ispit}" + "\n" )

            generics.write(r"\newcommand{\datumIspita}{" + datum + " г}" + "\n")
            
            # U ispitnim rokovima posle februara, ne treba nuditi opcije za polaganje ispita
            # odnosno, polaže se samo integralni ispit. 
            if validMonths.index('FEB') < validMonths.index(rok):
                generics.write(r"\setboolean{opcijeZaPolaganje}{false}" + "\n")
            else:
                generics.write(r"\setboolean{opcijeZaPolaganje}{true}" + "\n")

            if i:
                generics.write(r"\setboolean{ispit}{true}" + "\n")
                generics.write(r"\newcommand{\naslovFormulara}{ИСПИТ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n") 
                generics.write(r"\newcommand{\tablicaPDF}{si1oe_tablica_ispit.pdf}" + "\n") 
            else:
                generics.write(r"\setboolean{ispit}{false}" + "\n")
                generics.write(r"\newcommand{\tablicaPDF}{si1oe_tablica_kolokvijum.pdf}" + "\n") 
                if k == "1":
                    generics.write(r"\newcommand{\naslovFormulara}{ПРВИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
                elif k == "2":
                    generics.write(r"\newcommand{\naslovFormulara}{ДРУГИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
                elif k == "3":
                    generics.write(r"\newcommand{\naslovFormulara}{ТРЕЋИ КОЛОКВИЈУМ ИЗ ОСНОВА ЕЛЕКТРОНИКЕ}" + "\n")    
            print('Uspesno je napravljena datoteka sa konstantama')
    except Exception as e:
         print(f"Doslo je do greske: {e}")

if __name__ == '__main__':
    args = p.parse_args()
    main(**vars(args))

    
