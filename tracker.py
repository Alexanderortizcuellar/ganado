import sqlite3

con = sqlite3.connect("ganado.db")
cursor = con.cursor()
cols = ['Numero', 'Fecha_nacimiento', 'Marca', 'Sexo', 'Dueño', 'Mama', 'Descripcion', 'Comprado', 'Precio_compra', 'Vendedor', 'Fecha_compra', 'Criadero', 'Procedencia_otro', 'Procedencia_otro_cual', 'Procedencia_otro_notas', 'Vendida', 'Vendida_comprador', 'Vendida_precio', 'Vendida_fecha', 'Muerta', 'Muerta_causa', 'Muerta_fecha']
query = """ 
CREATE TABLE IF NOT EXISTS ganado(Numero INT,Fecha_nacimiento TEXT,
                                    Marca TEXT,Sexo TEXT,Dueno TEXT,
                                    Mama INT,Descripcion TEXT,Comprado TEXT,
                                    Precio_compra REAL,Vendedor TEXT,Fecha_compra TEXT,
                                    Criadero TEXT,Procedencia_otro TEXT,Procedencia_otro_cual TEXT,
                                    Procedencia_otro_notas TEXT,Vendida TEXT,Vendida_comprador TEXT,
                                    Vendida_precio REAL,Vendida_fecha TEXT,Muerta TEXT,Muerta_causa TEXT,
                                    Muerta_fecha TEXT)
"""

cursor.execute(query)

query2 = """
CREATE TABLE IF NOT EXISTS vacunas(Numero INT,Tipo TEXT,Fecha TEXT)
"""
cursor.execute(query2)
con.commit()
con.close()