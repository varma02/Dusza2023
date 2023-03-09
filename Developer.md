# Asztalfoglalás (fejlesztői dokumentáció)

## Hello, world!
Szeretnénk segíteni azoknak a fejlesztőknek, akik szerkesztenék vagy javítanák a kódot, vagy éppen együttműködnének velünk az alkalmazásunk fejlesztésében.

Külön célunk volt az, hogy a kódunk átlátható, és fejlesztőbarát legyen. Tehát célunk volt a clean coding elv teljesítése, ennek érdekében több dolgot végeztünk a kód írása közben:
- Több helyre kommenteket tettünk, mindezt angolul, ugyanis a szakmában hatékonyabb ha angolul írjuk körbe a kódot. Számunkra is, és akár az együttműködőknek is egyszerűbb lehet.
- Figyeltünk a változók neveire, ezzel próbáltuk minél egyértelműnek tartani a kódot
- Modulárissá tettük a kódot, hogy ne minden egy fájlba kerüljön, és a kód könnyen bővíthető legyen. Persze külön választott ablakot(modult, menüpontot) is meg lehet nyitni, ami elősegíti a fejlesztők munkájának hatékonyságát.
- Egyértelmű fájlneveket adtunk meg továbbá, hogy mindenki megtalálja amit keres. Ezt szintén angolul tettük.

## A `db.py fájl`

Ez a fájl felel azért, hogy az adatbázisba rendelést írjunk, vagy éppen abból rendelést olvassunk ki.

A fájl láthatunk 2 struktúrát annak érdekében (class Record, class Table), hogy látni lehessen milyen adatokat ad vissza az adatbázis-kezelő.  
Persze vannak kivételek, amikor nem feltétlen ilyen struktúrákat adunk vissza.

## A `del_records.py fájl`

Ez a fájl felel a rendelések lemondásáért, annak megjelenéséért, és annak funkcionalitásáért is. A `db.py` fájl eljárásait (function-jeit) alkalmazza az **adatbázis adatainak manipulálásához**.

## A `list_records.py fájl`

Ez a fájl felel a rendelések listázásáért, annak megjelenéséért, és annak funkcionalitásáért (pl. szűrés) is. A `db.py` fájl eljárásait (function-jeit) alkalmazza az **adatok lekéréséhez**.

## A `main.py fájl`
Ez az alkalmazásunk kezdete. Ezt fogja elsőnek meglátni a felhasználó, itt van felépítve a **menü kialakítása**, és itt gyűlik össze az alkalmazás **összes modulja, ablaka**.

## A `new_record.py fájl`
Itt lehet az asztal foglalását lebonyolítani. Itt építettük fel az **ablak felületét és elrendezését**, a **hibakezelést**, és a **bekérő mezők funkcionalitását**. A `db.py` fájl eljárásait alkalmazza az **adatbázis manipulálásához**.

## A `stats.py fájl`
Ez a közel legbonyolultabb fájl, ide épül fel a statisztikák ablak **felülete és bemeneti mezői**, az ehhez tartozó **hibakezelés** (helytelen időpontok), a **szűrési metódusok**, és a **statisztikát alakító metódusok**. A `db.py` fájl eljárásait alkalmazza az adatbázis adatainak beolvasására.

## A `table_map.py fájl`
Ez a fájl felel az asztaltérkép funkcióért, itt építettük fel az **ablak struktúráját és elrendezését**, és az **adatok összesítéséért felelő metódusokat**. A `db.py` fájl eljárásait alkalmazza az adatbázis adatainak beolvasására. 