from SQL_YHTEYS import sql_search
from geopy import distance


def etaisyys(icao1, icao2):
    lentokentat = sql_search(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}' OR ident = '{icao2}'")
    laskettu_etaisyys = distance.distance(*lentokentat).km
    return laskettu_etaisyys


def main():
    icao1 = input("Anna ensimmäinen icao koodi: ")
    icao2 = input("Anna toinen icao koodi: ")
    tulos = etaisyys(icao1, icao2)
    print(f"{tulos:.0f}")

if __name__ == "__main__":
    main()
