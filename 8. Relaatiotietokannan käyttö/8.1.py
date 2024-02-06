from SQL_YHTEYS import sql_yhteys

yhteys = sql_yhteys()
def hae_lentokentta(ICAO):
    cursor = yhteys.cursor()
    sql = f"select name, municipality from airport where ident = '{ICAO}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    yhteys.close()
    return result

icao = input("anna lentokentän icao koodi ")
tulos = hae_lentokentta(icao)
for i in tulos:
    print(f"Lentokentän nimi: {i[0]}\nLetonkentän kunta: {i[1]}")