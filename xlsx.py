#funcion de creacion de doxumento excel xlsx

import xlsxwriter

def createXlsxFile(fileName,serverName,listaUsers,listaBots):
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet(serverName)

    boldFormat = workbook.add_format({
      'bold': True,
      'fg_color': 'gray',
      'border': 1
      })

    cellFormat = workbook.add_format({
      'text_wrap': True,
      'align': 'top',
      'align': '=left'
    })

    #formato merge
    mergeFormat = workbook.add_format({
      'bold': True,
      'border': 1,
      'align': 'center',
      'valign': 'vcenter',
      'fg_color': 'orange'
    })

    worksheet.merge_range('A1:B1', serverName, mergeFormat)

    worksheet.write('A2','Usuarios', boldFormat) #lista Usuarios
    rowIndex = 3
    for i in range(len(listaUsers)):
        worksheet.write('A'+ str(rowIndex), listaUsers[i],cellFormat)
        rowIndex += 1

    worksheet.write('B2','Bots',boldFormat, ) #lista de Bots
    rowIndex = 3
    for i in range(len(listaBots)):
        worksheet.write('B'+ str(rowIndex), listaBots[i], cellFormat)
        rowIndex += 1

    worksheet.set_column(0,0,width=60) #Tamaño lista Usuarios
    worksheet.set_column(1,1,width=20) #Tamaño lista Bots
    workbook.close()
