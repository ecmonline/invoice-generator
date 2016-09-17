ecm.online invoice-generator
======

Generate invoices using python, weasyprint and yaml.
Just add your data to `documents/invoice/data.yml` and run the `./buildpdf.py` script.

Current template looks like this:

![rendered invoice](https://raw.githubusercontent.com/ecmonline/invoice-generator/master/pdf.png)

Usage see `./buildpdf.py --help`:


    usage: buildpdf.py [-h] [--template TEMPLATE] [--yaml_file YAML_FILE]
                    [--output_pdf OUTPUT_PDF] [--locale LOCALE]

    Convert HTML template to pdf with data from yaml

    optional arguments:
    -h, --help            show this help message and exit
    --template TEMPLATE   The name of the template to use (e.g. invoice)
    --yaml_file YAML_FILE
                            The yaml file to use for data
    --output_pdf OUTPUT_PDF
                            The output pdf file
    --locale LOCALE       The locale to use