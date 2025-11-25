# Pilot_ZiRa-Slave
Pilot-ZiRa 2. System
-------------------------------------------------------------------------------
--- Hardware:
-------------------------------------------------------------------------------
------ LED-Belegung:
J401 -> Pin 2	->  26 -> Nutzwärme Austritt
J402 -> Pin 3   ->  54 -> Nutzwärem Eintritt
J403 -> Pin 4   ->  48 -> Kondensator
J404 -> Pin 5   ->  42 -> Abwärme Austritt
J405 -> Pin 6   ->  48 -> Drossel           -> Richtung anpassen
J406 -> Pin 7   ->  64 -> Verdampfer
J407 -> Pin 8   ->  52 -> Abwärme Eintritt  -> Richtung anpassen
J408 -> Pin 9	-> 109 -> Kompressor 1 und Kompressor 2
------------------------------------------------------------------------------
------ XIO-Belegung:
XIO -> 0	-> Pin(10) -> Input -> Status Bit 0
XIO -> 1    -> Pin(11) -> Input -> Status Bit 1
XIO -> 2    -> Pin(12) -> Input -> Status Bit 2
XIO -> 3    -> Pin(13) -> Input -> Status Bit 3
-------------------------------------------------------------------------------
------ Status:
0 -> Keine Anzeige
1 -> Animation  -> Grün
2 -> Animation  -> Rot
-------------------------------------------------------------------------------
LED-Zuordnung Master
01 -> 161 -> Gitter-Rahmen Horizontal 2 x parallel
02 ->  84 -> Gitter-Rahmen Vertikal   6 x parallel
03 ->  32 -> CO2-Anzeige
04 ->  28 -> Energie Windrad    -> Richtung drehen
05 ->  30 -> Energie Kohle      -> Richtung drehen

LED-Zuordnung Slave
Grün
01 ->  26 -> Nutzwärme Austritt
02 ->  54 -> Nutzwärem Eintritt
03 ->  48 -> Kondensator
04 ->  42 -> Abwärme Austritt
05 ->  48 -> Drossel           -> Richtung anpassen
06 ->  64 -> Verdampfer
07 ->  52 -> Abwärme Eintritt  -> Richtung anpassen
08 -> 109 -> Kompressor 1 und Kompressor 2
08 -> 41 - 56  -> Kompressor 1 
08 -> 91 - 106 -> Kompressor 2

Rot
02 ->  26 -> Dampf
03 ->  48 -> Auspuff
#------------------------------------------------------------------------------