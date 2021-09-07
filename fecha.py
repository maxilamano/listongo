from datetime import datetime, timedelta
from pytz import timezone
import pytz

def fechaActual():
    timeZone = pytz.timezone('Chile/Continental') #zona horaria chile

    fecha = datetime.now(timeZone) #obtener fecha

    fechaString = fecha.strftime("%d/%m/%Y %H:%Mhrs") #convertir a string

    return fechaString

def fechaFile():
    timeZone = pytz.timezone('Chile/Continental') #zona horaria chile

    fecha = datetime.now(timeZone) #obtener fecha

    fechaString = fecha.strftime("%d-%m-%Y_%H-%Mhrs") #convertir a string

    return fechaString
