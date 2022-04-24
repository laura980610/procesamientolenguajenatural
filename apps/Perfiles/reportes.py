from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (
        Paragraph,
        Table,
        SimpleDocTemplate,
        Spacer,
        TableStyle,
        Paragraph)

from .models import historico

class ReportePersona(object):

    def __init__(self):
        self.buf = BytesIO()

    def run(self):
        self.doc = SimpleDocTemplate(self.buf)
        self.story = []
        self.encabezado()
        self.crearTabla()
        self.doc.build(self.story, onFirstPage=self.numeroPagina,
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        p = Paragraph("Reporte Personas", self.estiloPC())
        self.story.append(p)
        self.story.append(Spacer(1,0.5*inch))

    def crearTabla(self):
        data = [["busqueda","perfiles"]] \
            +[[x.busqueda, x.perfiles]
                for x in historico.objects.all()]

        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN',(2,2),(-1,-1),'CENTER'),
            ('VALIGN',(0,2),(-1,-1),'MIDDLE')])

        t = Table(data)
        t.setStyle(style)
        self.story.append(t)

    def estiloPC(self):
        return ParagraphStyle(name="centrado", alignment=TA_CENTER)

    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Pagina %s" % num
        canvas.drawRightString(10*mm, 10*mm, text)