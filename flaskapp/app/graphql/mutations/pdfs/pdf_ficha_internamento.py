import datetime
from PyPDF2  import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

template_directory = "./graphql/mutations/pdfs/pdfs_templates/ficha_de_internamento_hmlem.pdf"


def fill_pdf_ficha_internamento(datetime:datetime, patient_name:str, patient_cns:int, patient_birthday:datetime):

    packet = io.BytesIO()
    #Create canvas and add data
    c = canvas.Canvas(packet, pagesize=letter)
    #Writing all data in respective fields
    c = add_data(canvas=c, data=patient_name, pos=(27, 673))

    # create a new PDF with Reportlab
    c.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read the template pdf 
    template_pdf = PdfFileReader(open(template_directory, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = template_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    return output
    

def add_data(canvas:canvas.Canvas, data:str, pos:tuple):
    """Add data in pdf using canvas object

    Args:
        canvas (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
    """    
    canvas.drawString(pos[0], pos[1], data)
    return canvas


def write_newpdf(newpdf:PdfFileWriter, new_directory:str):
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    """    
    outputFile = open(new_directory, 'wb')
    newpdf.write(outputFile)
    outputFile.close()


if __name__ == "__main__":
    output = fill_pdf_ficha_internamento(
        datetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now()
        )
    
    
    write_newpdf(output, "./graphql/mutations/pdfs/ficha_teste.pdf")
    