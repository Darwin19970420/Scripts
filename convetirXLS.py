import xlrd
import  json
import couchdb

#Open couchdb
couch = couchdb.Server('http://Darwin:12345@localhost:5984') # conexión a la bd
db = couch['empresastec_xls'] #base en la cual se guardara

# Abrir los archivos xlsx
wb = xlrd.open_workbook('Datos_XLS.xlsx')
# crear json para guardar
jsonFile ="JsonExcel.json"

sh = wb.sheet_by_index(0)

# crear diccionario


# Abrir el json donde se guardar
with open (jsonFile, "w") as jsonFile:

    # pasar por las colunmas de manera iteractiva
    for rownum in range(1, sh.nrows):
        doc = {}
        #variable para leer las columnas
        row_values = sh.row_values(rownum)
        #crear el diccionario
        doc['tecnologia'] = {'id':row_values[0],
                          'cibercafe':row_values[1],
                          'provincia':row_values[2],
                          'catón':row_values[3],
                          'dirección':row_values[4],
                          'ingres':row_values[5],
                          'egresos':row_values[6],
                          'usuarios':row_values[7],
                          'saldos':row_values[8],
                          'software':row_values[9],
                          'equipos':row_values[10]
                          } 
        #guardar en couchdb
        db.save(doc)

        #guardar en json
        jsonFile.write (json.dumps(doc,indent =4))

        #verificarformato json
        print (doc)
    




