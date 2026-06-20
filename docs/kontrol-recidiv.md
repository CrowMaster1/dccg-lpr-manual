---
title: Kontrol & Recidiv
nav_order: 12
layout: default
---

# Kontrol & Recidiv

Kodning for recidiv følger LPR3 standard praksis, det er et krav fra DCCG-databasen at oplysning om lokalt recidiv angives - se opsummering info boks af sektion 6 & 10 i LPR-inberetningsvejledningen.

For at etablerer bedre datakvalitet på oplysninger om recidiv påføres patienter i kontrol aktiv kodning. Ligeledes registreres såfremt patient ikke vil eller skal kontrolleres efter klinisk skøn.

Disse oplysninger kan påføres kontrolundersøgelses proceduren.

## Kontrolundersøgelse -- Patient følger ikke kontrolprogram

Optræder denne kode efter initiale procedure eller efterfølgende i sygdomsforløb vil patienten ikke længere indgå i kontrolalgoritmen. Hvis patienten afslutter sit helbredsforløb for cancerdiagnosen, tolkes dette implicit, som at der ikke planlægges yderligere kontrol.

## Kontrolundersøgelse -- uden recidiv

Et kontrolbesøg uden recidiv tilføjes koden:

+------------------------------------------------------------------------------------+
|   -------------------------------------------------------------------------------- |
|   Uden recidiv   ZDW52A    Tillægskode til procedurekode for kontrolundersøgelse   |
|   -------------- --------- ------------------------------------------------------- |
|                                                                                    |
|   -------------------------------------------------------------------------------- |
+------------------------------------------------------------------------------------+

Anvendes også hvis der ikke konstateres genvækst efter kurativ stråleterapi for rektumcancer (se nedenfor), og tidligst efter 4 måneder (incidensperioden Cancerregisteret).

## Recidivsituationer

Recidivkodning følger standard LPR-kodning ift. indrapportering og kodning (indberetning til cancerregisteret). DCCG kræver at der også indrapporteres lokal-recidiv status.

### Kontrolundersøgelse -- Lokal recidiv 

+---------------------------------------------------------------------------+
|   ----------------------------------------------------------------------- |
|   Med lokalrecidiv      ZDW51G       Tillægskode til diagnosekode         |
|   --------------------- ------------ ------------------------------------ |
|                                                                           |
|   ----------------------------------------------------------------------- |
+---------------------------------------------------------------------------+

### 

### Kontrolundersøgelse -- Fjernrecidiv -- ingen lokal recidiv

Metastaselokalisationer kodes iht. LPR vejledning. Kodes der ikke for lokalrecidiv tolkes dette som ikke værende tilstede.

### Kontrolundersøgelse -- Fjernrecidiv & Lokal recidiv

+---------------------------------------------------------------------------+
|   ----------------------------------------------------------------------- |
|   Med lokalrecidiv      ZDW51G        Tillægskode til diagnosekode        |
|   --------------------- ------------- ----------------------------------- |
|                                                                           |
|   ----------------------------------------------------------------------- |
+---------------------------------------------------------------------------+

Metastaselokalisationer kodes iht. LPR vejledning

### Fjernrecidiv kodning (LPR-vejledning)

Ved systemisk recidiv kodes med recidivlokalisation fra organet som A-diagnose og med primær kolorektalcancer som bi-diagnose.

Dato for denne kode er dato for recidiv.

+------------------------------------------------------------------------------+
|   -------------------------------------------------------------------------- |
|    Hyppige lokalisationer   Diagnosekode               Kommentar             |
|   ------------------------ --------------- --------------------------------- |
|            Lever               DC78.7           Fjernmetastase i lever       |
|                                                                              |
|            Lunge               DC78.0           Fjernmetastase i lunge       |
|                                                                              |
|          Peritoneum            DC78.6D          Carcinose i peritoneum       |
|                                                                              |
|        Retroperitonum          DC78.6C      Metastase i retroperitoneal rum  |
|                                                                              |
|            Knogle              DC79.5B          Fjernmetastase i knogle      |
|                                                                              |
|        Metastase UNS           DC79.8                                        |
|   -------------------------------------------------------------------------- |
+------------------------------------------------------------------------------+

### Manglende kodning af recidiv status

Der foretages aktiv kodning (kodning af recidiv ej fundet) for at etablere recidiv data. Aktiv kodning i denne henseende er at der påsættes kode for "uden recidiv" og dette ikke er implicit ved manglende kodning.