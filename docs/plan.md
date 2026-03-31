## Idevumu izsekotājs
Idevumu izsekotājs ir python programma, kas ļauj lietotājam viegi un ērti reģistrēt ikdienas izdevumus. Programma atļauj sdalīt izdevumus pa kategorijām, apskatīt kategoriju un vai mēnešu kopsummas, kā arī eksportēt datus CSV failā.

### Datu struktūra 
Viens izdevuma ieraksts sastāvēs no kategorijas, summas, datuma un komentāra. Ieraksts izskatītos apmēram šādi
   Datums   |    Kategorija   |       Komentārs     |    Summa    |
 YYYY-MM-DD |     Ēdiens      |   darba pusdienas   |   XXX.XX€   |

Lietotājs ievadīs informāciju šādā kārtībā
1.Datums
2.Kategorija
3.Komentārs
4.Summa

Es izvēlējos šādu struktūru, jo skatoties uz citiem izdevumu izekotājiem tie izmanto līdzīgu struktūru šim, kā arī izmantojot šo informācijas ievadīšanas kārtību to būs vieglāk izveidot un apstrādāt.

### Moduļu plāns
Programma sastāvēs no 4 python scripta failiem un vienu JSON failu.
app.py būs galvenā programma ko vajadzēs palaist.
storage.py būs python scripts kas veiks JSON operācijas.
logic.py būs scripts kas veiks visu filtrēšanu un kopsavilkšanu.
export.py eksportēs CSV failu.
expenses.json fails kas turēs visus izdevumus.

### Lietotāja scenāriji
1. Lietotājs ievada derīgus izdevuma datus - Programma tad uzņems tos datus un saglabās tos JSON failā ar JSON struktūru.
2. Lietotājs ievada nederīgu izdevuma datu vienību - Programma parādīs kļūdu un atļaus ievadīt to atkārtoti.
3. Lietotājs izvēlas parādīt izdevumus - Programma apkopos visus eksistējošos izdevumus un izdrukās visu sarakstu jaukā formātā un parādīs visu izdevumu summu.

### Robežgadījumi
Ja expenses.json neeksistē programma paprasīs vai izveidot jaunu failu un ja lietotājs piekritīs tam tad to izveidos, un ja nepiekritīs tad programma izslēgsies.
Ja lietotājs ievadīs kādu no datu vienībām nepareizi (piem. neeksistējošu datumu, negatīvu summu) tad programma iedos kļūdu un atļaus lietotājam ievadīt datu vienību vēlreiz.
Ja lietotājs ievadīs tukšu komentāru tad programma to saglabās kā NULL vērtību.
Ja lietotājs izvēlēsies parādīt izdevumus, bet nevieni izdevumi neeksistēs tad programma Iedos kļūdu sakot ka nav nevienu izdevumu.

