#!/usr/bin/env python2

import codecs
import yaml
import locale

from pybars import Compiler
from weasyprint import HTML

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

template = 'invoice'

document_url = 'documents/'+template
base_url = document_url+'/template'

index_html = base_url+'/index.html'
data_yml = document_url+'/data.yml'
output_pdf = 'pdf.pdf'

with codecs.open(data_yml, encoding="utf-8") as yml_file:
    document_data = yaml.load(yml_file)

pos_number = 1
document_data['totals'] = {
    'netto' : 0,
    'brutto': 0,
    'tax': 0        
}
for pos in document_data['positions']:
    if not 'tax_rate' in pos:
        pos['tax_rate'] = document_data['tax_rate']

    pos['pos_number'] = pos_number
    pos['total_netto_price'] = pos['netto_price'] * pos['amount']
    pos['total_tax'] = pos['total_netto_price'] * (pos['tax_rate'] / float(100))
    pos['total_brutto_price'] = pos['total_netto_price'] + pos['total_tax']

    document_data['totals']['netto'] += pos['total_netto_price']
    document_data['totals']['brutto'] += pos['total_brutto_price']
    document_data['totals']['tax'] += pos['total_tax']

    pos['amount'] = locale.format("%.2f", pos['amount'])
    pos['tax_rate'] = locale.format("%.2f", pos['tax_rate'])
    pos['netto_price'] = locale.format("%.2f", pos['netto_price'])
    pos['total_netto_price'] = locale.format("%.2f", pos['total_netto_price'])
    pos['text'] = pos['text'].replace('\n', '<br>')

    pos_number += 1

document_data['totals']['netto'] = locale.format("%.2f", document_data['totals']['netto'])
document_data['totals']['brutto'] = locale.format("%.2f", document_data['totals']['brutto'])
document_data['totals']['tax'] = locale.format("%.2f", document_data['totals']['tax'])

with codecs.open(index_html, encoding="utf-8") as index_file:
    html_text = index_file.read()
    
    compiler = Compiler()
    template = compiler.compile(html_text)

    html_text = template(document_data)

    weasytemplate = HTML(string=html_text, base_url=base_url)
    weasytemplate.write_pdf(output_pdf)

