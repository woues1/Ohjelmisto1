from SQL_YHTEYS import sql_search


def lentokennta(maakoodi):
    result = sql_search(f"SELECT type, COUNT(*) AS airport_count FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type")
    return result


def main():
    maakoodi = input("anna maan tunnus")
    tulos = lentokennta(maakoodi)
    for i in tulos:
        print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    main()
