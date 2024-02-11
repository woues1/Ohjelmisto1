from SQL_YHTEYS import sql_search


def hae_lentokentta(ICAO):

    sql = f"select name, municipality from airport where ident = '{ICAO}'"
    result = sql_search(sql)

    return result


def main():
    icao = input("anna lentokentän icao koodi ")
    tulos = hae_lentokentta(icao)

    for i in tulos:
        print(f"Lentokentän nimi: {i[0]}\nLetonkentän kunta: {i[1]}")


if __name__ == "__main__":
    main()