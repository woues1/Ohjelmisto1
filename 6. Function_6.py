
import math
def pizza_neliömetri_hinta(halkaisija, hinta):
    neliömetri_hinta = hinta/(math.pi * halkaisija)
    return neliömetri_hinta

def main():
    pizza1 = pizza_neliömetri_hinta(float(input("anna pizza halkaisija: ")),
                                    float(input("anna pizzan hinta: ")))
    pizza2 = pizza_neliömetri_hinta(float(input("anna pizza halkaisija: ")),
                                    float(input("anna pizzan hinta: ")))
    if pizza1 < pizza2:
        print("pizza1 yksikköhinta on halvempi kuin pizza2")
    else:
        print("pizza2 yksikköhinta on halvempi kuin pizza1")

if __name__ == "__main__":
    main()