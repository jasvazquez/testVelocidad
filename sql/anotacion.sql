-- Describe ANOTACION
CREATE TABLE anotacion (
"ID" INTEGER PRIMARY KEY AUTOINCREMENT , 
    "fecha" TEXT,
    "ping" TEXT,
    "bajada" TEXT,
    "subida" TEXT,
     "server" TEXT);
     
-- Describe TRG_ANOTACION
CREATE TRIGGER trg_Anotacion after INSERT ON Anotacion
for each row
BEGIN
  UPDATE anotacion set fecha = DATETIME('NOW') where id=new.id;
END;     