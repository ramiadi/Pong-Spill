# Pong-Spill
 Pong Spill
 
 Jeg importerer pygame, tastatur og random
 
 #Vindu
 Vi laget et vindu med bredde og lengde
 
 #Klasse Spiller
      Konstruktør:
      x, y, farge, bredde, høyde, xfart, yfart, key_up og key_down
      
      Metoder:
      tegn metoden lager en rektangel som skal være i vinduet, ha et farge, den skal ha x posisjon, y posisjon, bredde og høyde
      
      flytt(taster):
      #if testen skal flytte spilleren (høyde)
      if taster[key_up] og y er større enn 2: # Legger til en verdi for å hindre i å gå øvre kant av vinduet
         y posisjonen minsker med 1 når man trykker og holder key_up verdien
      ellers taster[key_down] og y + høyde er mindre enn Vindu sitt høyde - 2 #legger til en verdi for å hindre spilleren i å gå under nedre kant av vinduet
         y posisjonen økes med 1 når man trykker og holder key_down verdien
     
#Klasse Ball
      Konstruktør: 
      farge og radius
      
      Derretter under konstruktøren lager jeg flere verdier
      x posisjonen er halvparten av Vinduets bredde
      y posisjonen er halvparten av Vinduets høyde
      xfart er enten -0,5 eller 0.5
      yfart en samme som xfart
      score1 er på verdien null
      score2 er på verdien null
      score_font er en standard font fra Sysfont med en størrelse på 100 piksler. Første argumentet None lager et standard font fra systemet
      
      Metoder:
      tegn_sirkel metoden lager en sirkel som skal være i vinduet, ha et farge, den skal ha en x posisjon og y posisjon, og ha en radius  
     
      #hver gang flytt metoden kalles, vil ballens posisjon på skjermen oppdateres ved hjelp av if-tester
          #Denne if- testen holder ballen innenfor skjermens høyde
          hvis y posisjonen - radius er mindre eller ælik 0 eller y posisjonen + radius er større eller ælik Vinduets høyde skal y-farten være lik - yfart.      
       
      #Denne if testen sjekker om ballen har gått utenfor venstre side av skjermen, slik at ballen starter å gå mot høyre spiller og oppdaterer poeng til spiller 2  
      hvis x posisjonen - radius er mindre eller ælik 0: #denne if testen sjekker om ballen har gått utenfor venstre side av skjermen, slik at ballen starter å gå mot høyre spiller       og oppdaterer poeng til spiller 2  
          øk score2 med 1
          sett ballens posisjon til midten av skjermen
          sett ballens x-fart til 0.5
          sett ballens y-fart til en tilfeldig verdi mellom -1 og 1

     #Sjekker om ballen har gåttt utenfor høyre side av skjermen, slik at ballen starter å gå mot venstre spiller og oppdaterer poeng til spiller1
      hvis x + radius er større eller ælik Vinduets bredde:
          øk score1 med 1
          sett ballens posisjon til midten av skjermen
          sett ballens xfart til -0.5
          sett ballens yfart til en tilfeldig verdi mellom -1 og 1
      #




     
