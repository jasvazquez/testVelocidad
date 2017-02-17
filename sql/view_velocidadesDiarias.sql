create view velocidadesDiarias as
select 
	date(fecha) dia, 
	strftime('%H:%M',fecha) hora,
	cast(ping as decimal) ping,
	cast(bajada as decimal) bajada,
	cast(subida as decimal) subida
from anotacion 
where 
	fecha>=datetime('now','start of day','-1 seconds') and fecha<=datetime('now','start of day','+24 hours')
	order by id;
