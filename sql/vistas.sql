/* [https://goo.gl/vXiUZZ] Manejo de fechas en SQLITE*/

select max(ping) max_ping, avg(ping) ping, min(ping) min_ping, avg(bajada) bajada, avg(subida) subida from anotacion;
select * from anotacion order by ping desc;

select 
	max(ping) max_ping, avg(ping) ping, min(ping) min_ping, 
	max(bajada) max_bajada, avg(bajada) bajada, min(bajada) min_bajada, 
	max(subida) max_subida, avg(subida) subida, min(subida) min_subida
from (
	select 
		cast(ping as decimal) ping,
		cast(bajada as decimal) bajada,
		cast(subida as decimal) subida
	from anotacion
);

select fecha  from anotacion where cast(fecha as datetime)>=strftime(date('now'));
select date('now');



SELECT date(fecha) dia, strftime('%H',fecha) hora,* from anotacion where fecha>=datetime('now','start of day') and fecha<=datetime('now','start of day','+24 hours','-1 seconds'); 

// Datos de la semana que ha pasado 

create view velocidadesSemanales as
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

select 
	
	case cast (strftime('%w', 'now') as integer)
		  when 0 then 'D'
		  when 1 then 'L'
		  when 2 then 'M'
		  when 3 then 'X'
		  when 4 then 'J'
		  when 5 then 'V'
		  else 'S' 
	end  as dia;
	
 select 
	case strftime('%m', 'now') 
		when '01' then 'Ene' 
		when '02' then 'Feb' 
		when '03' then 'Mar' 
		when '04' then 'Abr' 
		when '05' then 'May' 
		when '06' then 'Jun' 
		when '07' then 'Jul' 
		when '08' then 'Ago' 
		when '09' then 'Sep'
		when '10' then 'Oct' 
		when '11' then 'Nov' 
		when '12' then 'Dic' 
		else '' 
	end as month ;	
	
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
		
delete from anotacion where fecha like '2017-02-13%';		

select datetime('now','start of day','-1 seconds','-7 days'),datetime('now','start of day','-1 seconds');
