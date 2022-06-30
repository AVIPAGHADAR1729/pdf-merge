from flask import Flask, render_template, request, Response
from PyPDF2 import PdfFileMerger
from io import BytesIO


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pdfmerge", methods=["POST"])
def upload_files():
    if request.method == "POST":
        print("POST")
        files = request.files.getlist("file")
        print(files)
        if files and all([file.filename.endswith(".pdf") for file in files]):
            print("PDF")
            pdf_merge = PdfFileMerger()
            for pos, file in enumerate(files):
                pdf_merge.merge(pos, file)

            # out_file_name = datetime.now().strftime('%Y%m%d%H%M%S') + '.pdf'
            # with open(out_file_name,'wb') as pdf:
            #     pdf_merge.write(pdf)

            # with open(out_file_name,'rb') as read_file:
            #     return Response(BytesIO(read_file.read()),mimetype="application/pdf", direct_passthrough=True)

            _byteio = BytesIO()
            pdf_merge.write(_byteio)
            _byteio.seek(0)

            return Response(
                _byteio, mimetype="application/pdf", direct_passthrough=True
            )

            # return send_file(out_file_name,mimetype='application/pdf',as_attachment=True)

        else:
            print("Err")
            return {"Err": "Err...."}


if __name__ == "__main__":
    app.run(debug=True)
