from ast import Bytes
from cgitb import html
from io import BytesIO
from django.http import HttpResponse
from xhtml2pdf import pisa    
from django.template.loader import get_template

class Gerar_Pdf:

    def render_pdf(self, endereco_template, context_dict={}):
        template = get_template(endereco_template)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.enconde("")), result)
        return HttpResponse(result.getvalue(),
                            content_type= 'application/pdf')


