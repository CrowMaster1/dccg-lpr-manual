---
title: Patient oplysninger
nav_order: 4
layout: default
---

# Patient oplysninger

## Performance Status 

Performance status (ECOG) oplyses som den, der danner grundlag for behandlingsbeslutningen.

Der bør ikke foretages vurdering ud fra journal gennemgang. Her bør anvendes performance status ukendt. Hvis der i databasen/LPR findes flere værdier vælges sidste inden proceduren.

  --------------------------------------------------------------------------------------
  **Vurdering \[P\]**         **Procedurekode**   **Kommentar**
  --------------------------- ------------------- --------------------------------------
  Performance Status 0        ZZV020U0            

  Performance Status 1        ZZV020U1            

  Performance Status 2        ZZV020U2            

  Performance Status 3        ZZV020U3            

  Performance Status 4        ZZV020U4            

  Performance Status 5        ZZV020U5            Død

  Performance Status ukendt   ZZV020U9            Oplysning ikke tilgængelig i journal
  --------------------------------------------------------------------------------------

## ASA-klassifikation 

ASA-score oplyses som den, der danner grundlag for behandlingsbeslutningen. Der bør ikke foretages vurdering iht. journalvurdering. Her bør anvendes ASA ukendt. Patienter der ikke får foretaget resektion skal også have indrapporteret ASA, da grundet til fravalg af resektion kan være for høj score (forklarende variabel).

Det foretrækkes at ASA registreres på procedurekoden i forbindelse med vurdering af patient -- dvs. tilknyttes operation eller anden kontrolbesøg/indlæggelse

Ved flere opgivne vælges sidste inden proceduren

  ----------------------------------------------------------------------------------------------
  **Vurdering \[ikke-P\]**              **Tillægskode**   **Kommentar**
  ------------------------------------- ----------------- --------------------------------------
  ASA funktionsniveau, ASA 1            EZA1              

  ASA funktionsniveau, ASA 2            EZA2              

  ASA funktionsniveau, ASA 3            EZA3              

  ASA funktionsniveau, ASA 4            EZA4              

  ASA funktionsniveau, ASA 5            EZA5              

  ASA funktionsniveau, ASA 6            EZA6              

  ASA funktionsniveau, ASA Ukendt (9)   EZA9              Oplysning ikke tilgængelig i journal
  ----------------------------------------------------------------------------------------------

## Alkohol indtag 

Enkelt eller begge kan anvendes

  ----------------------------------------------------------------------------------
  **Alkoholforbrug**                              **diagnosekode**   **Kommentar**
  ----------------------------------------------- ------------------ ---------------
  Alkohol \>10 genstande ugentligt                DZ721C             

  Alkoholindtag overskrider 4 genstande dagligt   DZ721D             
  ----------------------------------------------------------------------------------

## Tobak anvendelse 

  -----------------------------------------------------------------------------------------------------
  **Nuværende rygestatus \[P\]**   **Pseudo- procedurekode**   **Kommentar**
  -------------------------------- --------------------------- ----------------------------------------
  Ryger                            ZZP01A1A                    Ryger (Inden for seneste 8 uger)

  Tidligere ryger                  ZZP01A1B2                   Ikke røget de seneste 8 uger

  Aldrig ryger                     ZZP01A1B3                   Ingen eller minimalt tidligere forbrug

  Rygestopper                      ZZP01A1B1                   Anvendes ikke
  -----------------------------------------------------------------------------------------------------

## Højde & Vægt 

  ----------------------------------------------------------------------------------------------------
  **Patientens højde og vægt\[P\]**   **Pseudo-procedurekode**   **Kommentar**
  ----------------------------------- -------------------------- -------------------------------------
  Legemshøjde (cm)                    ZZ0241+ VPH####            I tillægskoden angives højden i cm.

  Legemsvægt (kg)                     ZZ0240+ VPH####            I tillægskoden angives vægten i kg.
  ----------------------------------------------------------------------------------------------------