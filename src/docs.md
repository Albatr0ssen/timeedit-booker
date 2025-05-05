Plan
- Skapa ett användargränssnitt (webb? discord-bot?)
 - Webb: klassiker, lätt att hantera
 - Discord: lätt att skicka påminnelse om att uppdatera token
- Logga in automatiskt med sparade användarnamn och lösenord i klartext (färre manuella inloggningar)
- Bygga systemet så att flera olika bokningar kan planeras parallellt
- Hämta alla lediga rum under en viss tidsperiod
- Kontinuerligt kolla om ett rum blir ledigit under en viss tidsperiod och boka det
- Flera olika personers timmar kan användas 
- Kolla hur många bokade timmar någon har
- Kolla om en viss bokning har blivit avbokad (kollar om någon avbokar en bokning som skett genom programmet)


Schemagenerator
- https://cloud.timeedit.net/liu/web/schema/sid=3&l=sv_SE

Hämta bokning för specifikt id
- https://cloud.timeedit.net/liu/web/schema/s.html?sid=3&id=3597816
- https://cloud.timeedit.net/liu/web/wr_stud/ri.html?id=3597407

Hämta alla grupprum på valla
- https://cloud.timeedit.net/liu/web/schema/s.html?i=66YXQ55Y9Z59QmYa05yYY6y6Yv204dgYu3a5gQG07d7gYZjZZZX5jyuY549Y7Q7

Få lokaler och användare oautentiserat 
- https://cloud.timeedit.net/liu/web/schema/objects.json?l=sv_SE&types=195&sid=3&search_text=fe
- https://cloud.timeedit.net/liu/web/schema/objects.json?l=sv_SE&types=184&sid=3&search_text=Axel%20Berg

Exempel på något
- https://cloud.timeedit.net/liu/web/wr_stud/objects.json?max=50&fr=f&part=t&partajax=t&im=f&step=1&sid=4&l=sv_SE&ohg=0&types=195&subtypes=230&fe=23.Valla&fe=160.Studbok-grupprum-24h

Något annat
- https://cloud.timeedit.net/liu/web/wr_stud/ri.html?h=t&sid=4&objects=510070.195%2C510073.195%2C510074.195%2C510076.195%2C510079.195%2C598024.195%2C598070.195%2C598071.195%2C264253.195%2C264280.195%2C264281.195%2C264457.195%2C264459.195%2C264461.195%2C264463.195%2C264477.195%2C264478.195%2C264479.195%2C264480.195%2C264481.195%2C264482.195%2C264497.195%2C264499.195%2C553662.195%2C553663.195%2C546745.195%2C546746.195%2C264562.195%2C264563.195%2C&ox=0&types=0&fe=0&part=f&tg=-1&se=f&exw=t&rr=1


