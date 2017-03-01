CREATE VIEW velocidadesSemanales as
select 
	dia,
	max(ping) max_ping, avg(ping) avg_ping, min(ping) min_ping, 
	max(bajada) max_bajada, avg(bajada) avg_bajada, min(bajada) min_bajada, 
	max(subida) max_subida, avg(subida) avg_subida, min(subida) min_subida 
from 
(
	select 
		date(fecha) dia, 
		cast(ping as decimal) ping,
		cast(bajada as decimal) bajada,
		cast(subida as decimal) subida
	from anotacion 
	where 
		fecha>=datetime('now','start of day','-7 days') and fecha<=datetime('now','start of day')
)
group by dia;