import barcode 
from barcode.writer import ImageWriter

def createBarcode(number, name): 
    path = '/Users/nicholaslamprecht/GitHub/nictec_website2.0/nictecsite/storage/static/storage/Barcodes/'
    f = open(path + name, 'wb')
    code = barcode.get('code39', number, writer=ImageWriter())
    code.write(f) 
    return
    
