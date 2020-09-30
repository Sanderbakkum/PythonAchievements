

print("Je wordt wakker Sta je op of blijf je liggen.")
print("")
keus1 = input()
if ( keus1=="Sta op" ) :
	print("Oke je gaat uit bed want ga je eten. Brood/Musli")
	print("")
else:
	print("Je komt te laat op school!")
	print("")

keus2 = input()
if ( keus2=="Brood" ) :
	print("Je eet je broodje wat ga je nu doen.")
	print("Hoe ga je naar school? Fiets/Lopend")
	print("")
elif ( keus2=="Musli") :
	print("je eet je Müsli wat ga je nu doen.")
	print("Hoe ga je naar school? Fiets/Lopend")
	print("")

keus3 = input()
if ( keus3=="Fiets" ) : 
	print("Je pakt je fiets en gaat naar school")
	print("Het is warm tijdens het fietsen doe je je jas Aan of Uit?")
	print("")
elif ( keus3=="Lopend" ) :
	print("Je doet je schoenen aan en loopt naar school.")
	print("Het is warm terwijl je aan het lopen ben doe je je jas Aan of Uit?")
	print("")

keus4 = input()
if ( keus4=="Aan" ) :
	print("Je hebt het warm en begint een beetje te zweten")
	print("Je komt aan op school ga je je best doen? Ja/Nee")
	print("")
elif ( keus4=="Uit" ) :
	print("Je doet je jas uit")
	print("Je komt aan op school ga je vandaag je best doen? Ja/Nee")
	print("")

keus5 = input()
if ( keus5=="Ja" ) :
	print("Je let nu goed op in de les")
elif (keus5=="Nee" ) : 
	print("Je doet nu niet goed mee in de les")