---
title: Basisinformationer
nav_order: 3
layout: default
---

# Basisinformationer

Disse koder indsamles i forbindelse med initial diagnostik af en kolorektalcancerpatient. Følger normal resultatindberetning for cancer diagnoser (indberetning til cancerregisteret).

### Cancer Anmeldelse (TNM)

stadieindberetningen følger kravene til indberetning til cancerregisteret\*.

Databasen anvender både cTNM og pTNM. pTNM opsamles fra PATOBANK.

Vær opmærksom på at DCCG-databasen anvender subgrupper af cT stadiet mhp. at undgå dobbelt registrering (se afsnit for dette)

#### Lokalisationskode

Tumor lokalisation kodes efter bedste endoskopiske og/eller billeddiagnostiske skøn.

Uspecifik lokalisation (DC18.9) bør ikke anvendes, da databasen dermed mister muligheden for at skelne mellem flere synkrone eller metakrone cancere. Optræder denne i sammenhæng med mere specifik kodning, vil specifik kodning have højere prioritet.

Databasen vil som udgangspunkt anvende den DC kode der er anvendt til stadieinddeling.

DC18.9 må gerne anvendes i henvisninger etc, da databasen ikke indsamler dette. Denne nomenklatur er at foretrække end en "forkert" anatomisk kodning.

#### Synkrone tumorer

Ved synkrone tumorer kodes alle lokalisationer. Befinder der sig flere tumorer i samme segment, kodes disse som én lokalisation og data indhentes fra Patobank.

Ved evt. senere behandling/recidiv anvendes den lokalisation, der vurderes som udløsende for behandling.

+-----------------------------------------------------------------------------------------------+
|   ------------------------------------------------------------------------------------------- |
|   **Diagnose \[P\]**               **ICD-10 kode**               ** Kommentar**               |
|   ------------------------------- ----------------- ----------------------------------------- |
|   Kræft i caecum                        DC180                                                 |
|                                                                                               |
|   Kræft i blindtarmen                   DC181                                                 |
|                                                                                               |
|   Kræft i colon ascendens               DC182                                                 |
|                                                                                               |
|   Kræft i flexura coli dextra           DC183                                                 |
|                                                                                               |
|   Kræft i colon transversum             DC184                                                 |
|                                                                                               |
|   Kræft i flexura coli sinistra         DC185                                                 |
|                                                                                               |
|   Kræft i colon descendens              DC186                                                 |
|                                                                                               |
|   Kræft i colon sigmoideum              DC187                                                 |
|                                                                                               |
|   Kræft i tyktarmen UNS                 DC189        Bør ikke anvendes (til stadieinddeling)  |
|                                                                                               |
|   Kræft i endetarm                      DC209                                                 |
|   ------------------------------------------------------------------------------------------- |
+-----------------------------------------------------------------------------------------------+

\*(10.4.2.4.1 Krav til angivelse af TNM-stadie)

### 

### Klinisk T kategori 

T kategori tilføjes i forbindelse med diagnosen.

cTx klassifikation benyttes kun, når der ikke foreligger nogen undersøgelser på patienten. Er tumor ikke synlig på billeddannelse men ved skopi, anvendes mindste T kategori. Se gerne TNM vejledning på dccg.dk

Underklassifikation af T3 & T4 stadier **[bør]{.underline}** anvendes, da dette erstatter separat variable for nedvækstdybde.

Databasen anvender ikke neo-adjuverende T kategori (ycT)

Foreligger cTNM først efter en procedure, hvor der endnu ikke har været erkendt cancer f.eks. akut operation eller endoskopisk fjernelse af polyp. cTNM-koder kan tilføjes i forbindelse med aktivitet, hvor cancer senere konstateres.

Ved fund af metastaser hvor primær tumor ikke kan findes, men histologisk profil tyder på udgangspunkt i nedre GI, kodes som ukendt primær tumor (DC80.0). Disse patienter indgår ikke i databasen.

+--------------------------------------------------------------------------------------------------------------------------------+
|   ---------------------------------------------------------------------------------------------------------------------------- |
|   **Kliniske T-stadie \[P\]**   **Resultatindberetning-kode**   **Kommentarer**                                                |
|   ----------------------------- ------------------------------- -------------------------------------------------------------- |
|   cT0                           AZCD10                          Primær tumor kan ikke erkendes                                 |
|                                                                                                                                |
|   cT1                           AZCD13                          Tumor vokser ned i submucosa, men ikke i muscularis propria    |
|                                                                                                                                |
|   cT2                           AZCD14                          Tumor vokser ned i muscularis propria men ikke igennem         |
|                                                                                                                                |
|   cT3                           AZCD15                          Vokser igennem muscularis propria til subserosa (Anvend A/B)   |
|                                                                                                                                |
|   cT3a                          AZCD15A                         Nedvækst op til 1 mm igennem muscularis propria                |
|                                                                                                                                |
|   cT3b                          AZCD15B                         Nedvækst 2 til 5 mm igennem muscularis propria                 |
|                                                                                                                                |
|   cT3c                          AZCD15C                         Nedvækst 6 til 15 mm igennem muscularis propria                |
|                                                                                                                                |
|   cT3d                          AZCD15D                         Nedvækst \>15 mm igennem muscularis propria                    |
|                                                                                                                                |
|   cT4                           AZCD16                          Tumor genembryder serosa  (Anvend A/B)                         |
|                                                                                                                                |
|   cT4a                          AZCD16A                         Gennembryder serosa til viscerale peritoneum                   |
|                                                                                                                                |
|   cT4b                          AZCD16B                         Indvækst i tilstødende organ eller struktur                    |
|                                                                                                                                |
|   cTx                           AZCD19                          Bør ikke anvendes (se ovenfor).                                |
|   ---------------------------------------------------------------------------------------------------------------------------- |
+--------------------------------------------------------------------------------------------------------------------------------+

### Klinisk N kategori 

N kategori tilføjes i forbindelse med diagnosen.

cNx klassifikation benyttes kun, når der ikke foreligger nogen undersøgelser på patient.

Se TNM vejledning på dccg.dk

+----------------------------------------------------------------------------------------------------------+
|   ------------------------------------------------------------------------------------------------------ |
|   **Kliniske N-stadie \[P\]**   **Resultatindberetning-kode**   **Kommentarer**                          |
|   ----------------------------- ------------------------------- ---------------------------------------- |
|   cN0                           AZCD30                          Ingen regionale lymfeknudemetastaser     |
|                                                                                                          |
|   cN1                           AZCD31                          1-3 suspekte lymfeknuder                 |
|                                                                                                          |
|   cN2                           AZCD32                          4+ suspekte lymfeknuder                  |
|                                                                                                          |
|   cNx                           AZCD39                          Bør ikke anvendes (se ovenfor).          |
|   ------------------------------------------------------------------------------------------------------ |
+----------------------------------------------------------------------------------------------------------+

### Klinisk M kategori 

M kategori tilføjes i forbindelse med diagnosen.

cMx klassifikation eksisterer ikke.

Organ specifikke lokalisationskoder for metastaser angives som tillægskode til cancerkoden.

TNM indsamles i forbindelse med indrapportering til cancerregistret

+-----------------------------------------------------------------------------------------------------------------------+
|   ------------------------------------------------------------------------------------------------------------------- |
|   **Kliniske M-stadie \[P\]**   **Resultatindberetning-kode**   **Kommentarer**                                       |
|   ----------------------------- ------------------------------- ----------------------------------------------------- |
|   cM0                           AZCD40                          cM0: Ingen fjernmetastaser                            |
|                                                                                                                       |
|   cM1a                          AZCD41A                         cM1a: Fjernmetastase i et organ system                |
|                                                                                                                       |
|   cM1b                          AZCD41B                         cM1b: Fjernmetastase i flere organsystemer            |
|                                                                                                                       |
|   cM1c                          AZCD41C                         cM1c: Fjernmetastase i peritoneum +/- andre organer   |
|   ------------------------------------------------------------------------------------------------------------------- |
+-----------------------------------------------------------------------------------------------------------------------+

### MDT-konference

DCCG-databasen indsamler/anvender koder for

- Behandlingsbesluttende MDT
- Postoperativ opfølgnings MDT
- National MDT.

For at koderne skal anvendes, skal betingelserne under beskrivelsen være opfyldt.

Der kan afholdes flere behandlingsbesluttende MDT'er i et patientforløb.

Der bør kun optræde en behandlingsbesluttende MDT forud for en DCCG-procedure, men hvis klinisk relevant kan flere anvendes.

Yderligere behandlingsbesluttende MDT'er må gerne kodes ved behandlingsintentions-skifte eller ændringer i planlagte procedurer.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| +--------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------+ |
| | **MDT_konference \[P\]** | **Procedurekode** | **Kommentarer**                                                                                                         | |
| +:=========================+:==================+:========================================================================================================================+ |
| | Behandlingsbesluttende   | ZZ0190D1          | Kræver minimum deltagelse af kirurg, onkolog, patolog samt radiolog.                                                    | |
| |                          |                   |                                                                                                                         | |
| |                          |                   | Kræver MDT foretager beslutning om behandlingsstrategi samt der foreligger tilfredsstillende diagnostiske undersøgelser | |
| +--------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------+ |
| | Postoperativ opfølgning  | ZZ0190D2          | Der foretages systematisk audit af det operativ forløb med henblik på efterforløb samt kvalitetssikring.                | |
| +--------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------+ |
| | National                 | ZZ0190D3          | Afholdes på højtspecialiseret afdeling med deltagelse af nationale centre                                               | |
| +--------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------+ |
| | MDT                      | ZZ0190D           | MDT hvor der ikke kan foretages endelig behandlingsbeslutning                                                           | |
| +--------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------+ |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+