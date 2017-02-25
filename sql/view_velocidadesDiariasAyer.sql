CREATE VIEW velocidadesDiariasAyer as
select 
	date(fecha) dia, 
	strftime('%H:%M',fecha) hora,
	cast(ping as decimal) ping,
	cast(bajada as decimal) bajada,
	cast(subida as decimal) subida
from anotacion 
where 
	fecha>=datetime('now','start of day','-1 seconds','-24 hours') and fecha<=datetime('now','start of day','-1 seconds')
order by id;