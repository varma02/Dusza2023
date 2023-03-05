# Asztalfoglalás
Ez a 2023-as Dusza versenyre készített projekt egy olyan program, amely elősegíti egy étterem asztalfoglalási folyamatát. A program könnyen kezelhető, és lehetővé teszi a foglalások és lemondások egyszerű kezelését. Emellett a feljegyzett adatokból statisztikák is készíthetők.

## Letöltés / Első lépések
A program legfrissebb verziója letölthető [innen.](https://github.com/varma02/Dusza2023/releases/tag/latest)
Letöltés és egyszeri futtatás után a program létrehoz egy `data` mappát. Ebbe fogja tárolni a foglalások adatait. A `data` mappán belül létre kell hozni egy `asztalok.txt` nevű fájlt, melybe soronként egy-egy asztal adatait lehet megadni ebben a formátumban: `asztal_azonosító;székek_száma;hely(K=kültéri, B=beltéri)`

[A fejlesztői dokumentáció itt érhető el.](https://github.com/varma02/Dusza2023/blob/master/Developer.md)

## Felhasználói felület
A programot elindítva első látásra a menü fogad minket, ahol az alábbi lehetőségeket választhatjuk:
- Foglalás rögzítése
- Foglalás törlése
- Foglalások listája
- Asztaltérkép
- Statisztika
- Kilépés

Minden menüpont neve lényegre törő funkcionalitás terén, a foglalást végző munkatárs számára is könnyen érthető komolyabb informatikai ismeretek nélkül. A hatékonyság érdekében egérrel is kezelhető grafikus felületet hoztunk létre úgy, hogy minden könnyen elérhető és egyértelmű legyen.

![image](https://user-images.githubusercontent.com/57862878/222977816-2e58f54f-5c51-4523-b5b7-f6e867e827a1.png)


****
### **Asztalfoglalás, foglalás rögzítése**
Az asztalfoglalást, vagyis foglalást rögzíteni a Menün belül a _"Foglalás rögzítése"_ gombbal lehet előhívni.

A menüpont megjelenését követően több bemeneti mező tárul elénk. A bemeneti mezők mellett ott vannak azok nevei is, így a foglalást lebonyolító munkatárs egyértelműen fel tudja dolgoztatni a kérést. Annak érdekében, hogy segíthessük a foglalás menetét és hatékonyságát több bemeneti mezőbe alapértelmezetten megjelennek azok az értékek, amik relevánsak lehetnek a foglaláskor. A kezdő-, záró időpont, és a mai dátum automatikusan megjelennek a bemeneti mezőkben, ahogyan a székek száma is.

![image](https://user-images.githubusercontent.com/57862878/222977835-7256170a-40d5-4e03-8e7c-46aad7ea529a.png)


A *"Mentés"* gombot megnyomva lefut a hibaellenőrzés, hogy az elgépelt adatok, vagy a problémás rendelést visszajelezze a program. Ha a rendelés teljesíthető a foglalás rögzítési ablaka hiba nélkül becsukódik, majd a Menü jelenik meg a helyére a hatékonyság érdekében.

Példa:

![image](https://user-images.githubusercontent.com/57862878/222977858-36a1f420-719d-487e-bbd5-a80ffe74984b.png)


****
### **Lemondott asztalfoglalás, foglalás törlése**
Abban az esetben, ha egy foglalást lemondtak vagy éppen valamilyen okból törölni kell a rendelést a Menün belül a _"Foglalás törlése"_ gombbal lehet előhívni.

A felületet felső sávában egy bemeneti mező, és egy év választó mező található.

![image](https://user-images.githubusercontent.com/57862878/222977902-455312d9-1989-44cb-8f87-c204dbb9519a.png)

A bemeneti mezőbe a lemondó rendelő neve kerülhet (opcionális), annak érdekében hogy a folyamat hatékonyabban végbemehessen. Az évválasztó mezőben az adott évre tudunk szűrni, ha erre szükség lenne. 

A program egy listát fog mutatni a keresési feltételeknek megfelelően, és egy nagy, piros *"Lemondás"* gombot fog mindegyik mellett megjeleníteni. A program ezen kívül a kezdeti dátumot és időpontot, ezen kívül a befejezési időt is megjeleníti a foglaló neve után.

![image](https://user-images.githubusercontent.com/57862878/222977927-c6396bad-cab7-4172-a598-f6ff79e7b132.png)

****
### **Eddigi foglalások megtekintése, foglalások áttekintése**
Ahhoz, hogy az eddigi foglalásokat meg lehessen tekinteni, a felhasználónak a *"Foglalások listája"* gombot kell működtetnie.
![image](https://user-images.githubusercontent.com/57862878/222977996-4e6a7b81-0610-450f-8cab-d8840f5cacbb.png)
Annak érdekében, hogy a foglalásokat ellenőrző munkatárs hatékonyan a kívánt információhoz juthasson szűrési lehetőségeket készítettünk. Lehetősége van az évet kiválasztania, ezen kívül az aktuális napi foglalásokat is megtekintheti.
![image](https://user-images.githubusercontent.com/57862878/222978021-bc9c2ea5-cac3-4608-b9ef-100eac8e3b44.png)
![image](https://user-images.githubusercontent.com/57862878/222978034-36708ccd-85b8-438a-814f-c375989f4daf.png)

A megjelenő táblázatban a következő oszlopok találhatóak: Név, Dátum (kezdő- hónap, nap, óra, perc; végző óra, perc), Székek száma, és a lefoglalt asztalok számai. A csúszkát használva lehet a többi, a képernyőről lelógó adatot megtekinteni. Igény esetén oszloponként, értékek szerint is lehet rendezni úgy, hogy a táblázat címsorában a kívánt rendezési szempontra nyom.

****
### **Asztalok foglaltságának megtekintése, asztaltérkép**
Az asztalok foglaltságának ellenőrzéséhez az *"Asztaltérkép"* gombot megnyomva lehet ahhoz a felülethet jutni, amely a kívánt információkat tartalmazza.  
Nagyobb látogatási hullámoknál előfordul, hogy az étterem zsúfoltabb vagy épp nincs szabad asztal kültéren vagy beltéren.
Ilyen esetekre jött létre ez a funkció is annak érdekében, hogy segíthessük a foglalás menetében azzal, hogy hol van szabad asztal.
![image](https://user-images.githubusercontent.com/57862878/222978111-30da78af-c149-49ed-ad9b-1a7079550e8d.png)


****
### **Statisztikák**
A menüben lévő *"Statisztika"* gombot megnyomva, majd az ott lévő két bemeneti mezőbe betáplált (kezdő és végző) dátummal lehet kiolvasni azokat a statisztikákat, amelyek a megadott időben történt foglalásokra vonatkoznak. 
![image](https://user-images.githubusercontent.com/57862878/222978187-53786ae7-b576-432d-a24a-2a57ede92cf3.png)

Többek közt láthatóak a várólistára került foglalások száma, a lemondott foglalások száma, stb..
Természetesen ezt is külön beltérre és kültérre bontva láthatja az olvasó annak érdekében, hogy ha pl. az étterem jövőbeli bővítést tervez, akkor tudja mely tere(ke)t kell bővítenie. Sok más célra is hasznos lehet ez a lehetőség.

![image](https://user-images.githubusercontent.com/57862878/222978156-dfa83e8e-07b9-4681-b703-b687e409bc59.png)
