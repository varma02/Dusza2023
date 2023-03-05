# Asztalfoglalás
Ez a 2023-as Dusza versenyre készített projekt egy olyan program, amely elősegíti egy étterem asztalfoglalási folyamatát. A program könnyen kezelhető, és lehetővé teszi a foglalások és lemondások egyszerű kezelését. Emellett a feljegyzett adatokból statisztikák is készíthetők.

## Felhasználói felület
A programot elindítva első látásra a menü fogad minket, ahol az alábbi lehetőségeket választhatjuk:
- Foglalás rögzítése
- Foglalás törlése
- Foglalások listája
- Asztaltérkép
- Statisztika
- Kilépés

Minden menüpont neve lényegre törő funkcionalitás terén, a foglalást végző munkatárs számára is könnyen érthető komolyabb informatikai ismeretek nélkül. A hatékonyság érdekében egérrel is kezelhető grafikus felületet hoztunk létre úgy, hogy minden könnyen elérhető és egyértelmű legyen.

****
### **Asztalfoglalás, foglalás rögzítése**
Az asztalfoglalást, vagyis foglalást rögzíteni a Menün belül a _"Foglalás rögzítése"_ gombbal lehet előhívni.

A menüpont megjelenését követően több bemeneti mező tárul elénk. A bemeneti mezők mellett ott vannak azok nevei is, így a foglalást lebonyolító munkatárs egyértelműen fel tudja dolgoztatni a kérést. Annak érdekében, hogy segíthessük a foglalás menetét és hatékonyságát több bemeneti mezőbe alapértelmezetten megjelennek azok az értékek, amik relevánsak lehetnek a foglaláskor. A kezdő-, záró időpont, és a mai dátum automatikusan megjelennek a bemeneti mezőkben, ahogyan a székek száma is.

A *"Mentés"* gombot megnyomva lefut a hibaellenőrzés, hogy az elgépelt adatok, vagy a problémás rendelést visszajelezze a program. Ha a rendelés teljesíthető a foglalás rögzítési ablaka hiba nélkül becsukódik, majd a Menü jelenik meg a helyére a hatékonyság érdekében.


****
### **Lemondott asztalfoglalás, foglalás törlése**
Abban az esetben, ha egy foglalást lemondtak vagy éppen valamilyen okból törölni kell a rendelést a Menün belül a _"Foglalás törlése"_ gombbal lehet előhívni.

A felületet felső sávában egy bemeneti mező, és egy év választó mező található.

A bemeneti mezőbe a lemondó rendelő neve kerülhet (opcionális), annak érdekében hogy a folyamat hatékonyabban végbemehessen. Az évválasztó mezőben az adott évre tudunk szűrni, ha erre szükség lenne. 

A program egy listát fog mutatni a keresési feltételeknek megfelelően, és egy nagy, piros *"Lemondás"* gombot fog mindegyik mellett megjeleníteni. A program ezen kívül a kezdeti dátumot és időpontot, ezen kívül a befejezési időt is megjeleníti a foglaló neve után.

****
### **Eddigi foglalások megtekintése, foglalások áttekintése**
Ahhoz, hogy az eddigi foglalásokat meg lehessen tekinteni, a felhasználónak a *"Foglalások listája"* gombot kell működtetnie.
Annak érdekében, hogy a foglalásokat ellenőrző munkatárs hatékonyan a kívánt információhoz juthasson szűrési lehetőségeket készítettünk. Lehetősége van az évet kiválasztania, ezen kívül az aktuális napi foglalásokat is megtekintheti.

A megjelenő táblázatban a következő oszlopok találhatóak: Név, Dátum (kezdő- hónap, nap, óra, perc; végző óra, perc), Székek száma, és a lefoglalt asztalok számai. A csúszkát használva lehet a többi, a képernyőről lelógó adatot megtekinteni. 

****
### **Asztalok foglaltságának megtekintése, asztaltérkép**
Az asztalok foglaltságának ellenőrzéséhez az *"Asztaltérkép"* gombot megnyomva lehet ahhoz a felülethet jutni, amely a kívánt információkat tartalmazza.  
Nagyobb látogatási hullámoknál előfordul, hogy az étterem zsúfoltabb vagy épp nincs szabad asztal kültéren vagy beltéren.
Ilyen esetekre jött létre ez a funkció is annak érdekében, hogy segíthessük a foglalás menetében azzal, hogy hol van szabad asztal.

****
### **Statisztikák**
A menüben lévő *"Statisztika"* gombot megnyomva, majd az ott lévő két bemeneti mezőbe betáplált (kezdő és végző) dátummal lehet kiolvasni azokat a statisztikákat, amelyek a megadott időben történt foglalásokra vonatkoznak. Többek közt láthatóak a várólistára került foglalások száma, a lemondott foglalások száma, stb..
Természetesen ezt is külön beltérre és kültérre bontva láthatja az olvasó annak érdekében, hogy ha pl. az étterem jövőbeli bővítést tervez, akkor tudja mely tere(ke)t kell bővítenie. Sok más célra is hasznos lehet ez a lehetőség.

