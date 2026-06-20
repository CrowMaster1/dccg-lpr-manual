---
title: Kirurgiske Procedurer
nav_order: 7
layout: default
---

# Kodning ved Kirurgiske Procedurer på kolorektalcancerpatienter

## Proceduresigte ved det kirurgiske indgreb

Proceduresigtet defineres som den endelige intention bag proceduren.

Den er ikke nødvendigvis bestemt forud for en procedure. Dvs. en planlagt kurativ procedure, der slutteligt (umiddelbart efter proceduren er udført) er palliativ, skal kodes som palliativ. Koden skal ikke ændres senere hvis der meget senere ændres intention.

Eksempel: en operation vurderes at kunne udføres med kurativt sigte på MDT, desværre under operation findes udbredt karcinose. Man vælger dog at foretage resektion af primær tumor. Her er koden palliativ.

Bridge-to-surgery indgreb: Stent anlæggelser eller stomianlæggelser i hvor der senere påtænkes at der skal udføres et kurativt indgreb/behandling intentions kodes som kurativ.

  -----------------------------------------------------------------------
  **Procedurens intention \[P\]**    **Tillægskode til procedurekode**
  ---------------------------------- ------------------------------------
  Diagnostisk                        ZPZA01

  Intenderet kurativ behandling      ZPZA02C

  Palliativ                          ZPZA05
  -----------------------------------------------------------------------

## Prioritet 

En akut operation defineres som en procedure, der ikke kan afvente regelret udredningsprogram. Dette kan være på forløb der er akutte eller elektive. Det er operatørens vurdering der gælder.

+------------------------------------------------------------------------------+---+
|   -------------------------------------------------------------------------- |   |
|   **Akut udført operation \[non-P\]**   **Tillægskode til procedurekode**    |   |
|   ------------------------------------- ------------------------------------ |   |
|   Udført Akut                           ZPTP01                               |   |
|                                                                              |   |
|   -------------------------------------------------------------------------- |   |
+==============================================================================+===+

Ved akut operation anføres tilstande, der fører til den akutte indikation som bi-diagnoser f.eks. ileus, perforation etc.

## Konvertering 

Der er foretaget konvertering hvis et indgreb var intenderet laparoskopisk og anden minimal invasiv kirurgi, men grundet tekniske eller intraoperative komplikationer må konverteres til åben kirurgi.

  -----------------------------------------------------------------------------------------------------------
  **Konvertering af indgrebstype \[non-P\]**   **Tillægskode til procedurekode**   
  -------------------------------------------- ----------------------------------- --------------------------
  Anden konvertering til åbent indgreb         KZYK96                              Anvendes i alle tilfælde

  -----------------------------------------------------------------------------------------------------------

## Robot assisteret 

Hvis et indgreb har involveret anvendelse af robot, uafhængig af tid.

  --------------------------------------------------------------------------------------------------
  **Anvendelse af robot \[non-P\]**   **Tillægskode til procedurekode**   
  ----------------------------------- ----------------------------------- --------------------------
  Robot assisteret                    KZXX00                              Anvendes i alle tilfælde

  --------------------------------------------------------------------------------------------------

## Resektionstype

Se vejledning på DCCG.dk, her også tolkning ift. definition for CME-kirurgi.

  -----------------------------------------------------------------------------------------------
  **Resektionstype**                                                            **Tillægskode**
  ----------------------------------------------------------------------------- -----------------
  D0: ukomplet excision af tumornære lymfeknuder                                KZLG00D0

  D1: komplet excision af tumornære lymfeknuder                                 KZLG00D1

  D2: komplet excision af tumornære lymfeknuder og intermediære lymfeknuder     KZLG00D2

  D3: komplet excision af tumornære lymfeknuder og alle regionale lymfeknuder   KZLG00D3

  D9: ingen oplysninger om excision af tumornære lymfeknuder                    KZLG00D9
  -----------------------------------------------------------------------------------------------