from fpdf import FPDF
import json

def create_pdf(json_filename, output_pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    with open(json_filename, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for key, value in json_data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(output_pdf_path)

if __name__ == "__main__":
    input_json_filename = "input.json"
    output_pdf_path = "output.pdf"

    create_pdf(input_json_filename, output_pdf_path)
    print(f"PDF created at {output_pdf_path}")

for each key-value pair: values such as "investigations", "intervention", "treatment", "causes", and the key should be wrapped as a value mapped to a new key called: "output".  "signs", "introduction", "symptoms" should be wrapped and assigned a new key called: "input"