import csv
import json
import couchdb

couch = couchdb.Server('http://Darwin:12345@localhost:5984') # conexión a la bd

db = couch['productoselectronicos_csv'] #base en la cual se guardara


csvFilePath = "DatafinitiElectronicsProductsPricingData.csv" #nombre del csv y csv debe estar en la misma carpeta
jsonFilePath = "JsonCsv.json" #donde se guardara los json


with open (jsonFilePath, "w") as jsonFile: # abrir el json para guardar
    with open (csvFilePath) as csvFile:
        
        csvReader = csv.DictReader (csvFile)
        for csvRow in csvReader:
            data = {}
            date = csvRow ["id"] # columna principal o id del csv
            data['tecnologia'] = csvRow #envia el json del csv
            db.save(data)
            root = {}
            root["JsonCsv.json"] = data
            print (data)

            #escribe en json
            jsonFile.write (json.dumps(data,indent =4))







