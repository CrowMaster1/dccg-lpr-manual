---
title: Onkologi
nav_order: 13
layout: default
---

# Onkologi

Patienter, der ses på en onkologisk afdeling uden at være set forud på en kirurgisk afdeling, skal have registreret basis værdier som beskrevet tidligere.

### Kodning af onkologisk forløb

Patienter, der ses på en onkologisk afdeling, registreres med behandling intention og performance status ved hvert behandlingsskifte. I modsætning til kirurgiske procedure behøves disse koder ikke at blive påført ved hver procedure (medicingivning/strålebehandlingsfraktioner), men i starten af behandlingen. Dvs. at der ikke er krav om intention ved enkelte fraktioner eller serier.

### Performance Status

Se under basis skema for koder

### Lokalisations angivelse ved stråleterapi

Ved stråleterapi ønskes oplyst hvilket organ, behandling blev givet imod. I praksis vil det kun være rektumcancerpatienter hvor pallierende stråleterapi kan retters mod enten primær tumor eller metastaser.

Hvis behandling kobles på metastase lokalisation som A-diagnose, er det ikke nødvendigt at angive yderligere. Hvis pallierende behandling rettes mod andet organ, ønskes oplyst anatomisk lokalisation sideløbende.

### Proceduresigte/behandlingsintention

Proceduresigtet defineres ved onkologisk behandling som den intention behandlingen initialt bliver givet ved. Dette adskiller sig fra den kirurgiske definition.

Intention kan ideelt tilføjes hver enkelt kemoterapi procedure, alternativt skal denne tilføjes ved start og ved skift i behandling. Kan tilføjes i forbindelse med journaloptagelses aktivitet etc.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Onkologisk behandlingsintention**   **Tillægskode til procedurekode**   **Kommentar**
  ------------------------------------- ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Adjuverende behandling                ZPZA02A                             Behandling af patient med mulig mikroskopisk sygdom, forudgået af en kurativ procedure -- resektion.

  Neoadjuverende behandling             ZPZA02B                             Behandling af resektabel sygdom, hvor resektion er mulig, men hvor patient kan have gavn af behandling forud for resektionsforsøg

  Intenderet kurativ behandling         ZPZA02C                             Procedure der i sig selv kan opnå chance for helbredelse - uden anvendelse af ekstra modalitet (stråleterapi, onkologi etc) og tilstedeværelse af makroskopisk sygdom

  Downstaging                           ZPZA02E                             Behandling af non-resektabel sygdom, hvor skrumpning kan give mulighed for resektion

  Palliativ                             ZPZA05                              Behandling hvor det ikke anses sandsynlig (90%+) at der kan opnås anden intenderet kurativ behandling ved effekt

  Ingen behandling                      ZWCM8                               
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Hjælpesektion for Medicinsk Onkologi

#### Antineoplastisk behandling

Antineoplastisk behandling skal kodes så ensartet som muligt så behandlingsregimet fremstår.

Behandling kodes med kombinationskoder hvis muligt. Ellers kodes de indgivne enkelte stoffer.

Optræder det indgivne stof ikke i SKS, kodes enten simpel eller kompleks kemoterapi, med SKS ATC-koden (M\*\*\*).

Kombinationsbehandling

  ---------------------------------------------------------------------------------------------------
  **Kombinations koder**                                   **Procedurekode**   **Kommentar**
  -------------------------------------------------------- ------------------- ----------------------
  Behandling med capecitabin+oxaliplatin                   BWHA222             CapOx

  Behandling med 5-fluorouracil+oxaliplatin                BWHA231             FOLFOX

  Behandling med 5-fluorouracil+irinotecan                 BWHA233             FOLFIRI

  Behandling med fluorouracil + irinotecan + oxaliplatin   BWHA234             FOLFOXIRI/FOLFIRINOX
  ---------------------------------------------------------------------------------------------------

Enkeltstofbehandling

  ------------------------------------------------------------------------
  **Enkelt stof koder**                **Procedurekode**   **Kommentar**
  ------------------------------------ ------------------- ---------------
  Behandling med oxaliplatin           BWHA108             

  Behandling med 5-fluorouracil        BWHA110             

  Behandling med capecitabin           BWHA123             

  Behandling med irinotecan            BWHA212             

  Behandling med cetuximab             BOHJ17              

  Behandling med bevacizumab           BOHJ19B1            

  Behandling med panitumumab           BOHJ19C2            

  Behandling med encorafenib           BWHA446             

  Behandling med pembrolizumab         BOHJ19J3            

  Behandling med tegafur/uracil        BWHA141             
  ------------------------------------------------------------------------

Behandling med Trifluridin ellerTegafur:

  ------------------------------------------------------------------------
  **Behandling med Trifluridin/Tegafur**    **ATC-kode**   **Kommentar**
  ----------------------------------------- -------------- ---------------
  Trifluridin, kombinationer                ML01BC59       Lonsurf

  Tegafur, kombinationer                    ML01BC53       S1
  ------------------------------------------------------------------------

#### Behandling af knoglemetastaser

  -------------------------------------------------------------------------
  **Behandling af knoglemetastaser**    **Procedurekode**   **Kommentar**
  ------------------------------------- ------------------- ---------------
  Behandling med bisfosfonat            BWHB40              

  Behandling med zoledronsyre           BWHB40A             

  Behandling med ibandronsyre           BWHB40B             

  Behandling med pamidronat             BWHB40C             

  Behandling med denosumab              BWHB42              
  -------------------------------------------------------------------------

Hjælpesektion for radioterapi

### Hjælpe sektion til Strålebehandlingsprocedure

  -----------------------------------------------------------------------
  **Strålingstype (ikke udtømmende)**               **Procedurekode**
  ------------------------------------------------- ---------------------
  Konventionel ekstern strålebehandling             BWGC1

  Intensitetsmoduleret radioterapi (IMRT)           BWGC4

  Individuel konform strålebehandling               BWGC

  MR-vejledt strålebehandling                       BWGC8
  -----------------------------------------------------------------------

Gives palliativ bestråling ønskes opgivet lokalisation, hvis denne ikke fremgår af den tilknyttede aktionsdiagnose.

  -----------------------------------------------------------------------
  **Bestrålet lokalisation**                **Topografikode**
  ----------------------------------------- -----------------------------
  Rektum                                    T000751

  Cerebrum                                  T001076

  Lunge                                     T000398

  Lever                                     T000607

  Knogle                                    T000224

  Hud                                       T000010
  -----------------------------------------------------------------------

#### Ablative/kurative hypofraktioneret behandling

Gives hypofraktioneret kurativt anlagt behandling tilføjes/anvendes

  -----------------------------------------------------------------------
  **Stereotaktisk strålebehandling**                **Procedurekode**
  ------------------------------------------------- ---------------------
  Stereotaktisk strålebehandling af lever           BWGC22

  Stereotaktisk strålebehandling af lunger          BWGC23

  Cerebral stereotaktisk strålebehandling           BWGC21
  -----------------------------------------------------------------------