create view ultimasAnotaciones as
SELECT FECHA, printf("%.2f",BAJADA) bajada, printf("%.2f",SUBIDA) subida, round(PING) ping
from anotacion
order by id desc;
