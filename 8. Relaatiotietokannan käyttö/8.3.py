from SQL_YHTEYS import sql_search
from geopy import distance


def etaisyys(icao1, icao2):
    lentokentta1 = sql_search(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}'")
    lentokentta2 = sql_search(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}'")

    print(lentokentta1)
    print(lentokentta2)
    laskettu_etaisyys = distance.distance(lentokentta1, lentokentta2).km
    return laskettu_etaisyys


def main():
    icao1 = input("Anna ensimmäinen icao koodi: ")
    icao2 = input("Anna toinen icao koodi: ")
    tulos = etaisyys(icao1, icao2)
    print(f"{tulos:.0f}")

if __name__ == "__main__":
    main()
