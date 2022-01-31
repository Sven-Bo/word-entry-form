from pathlib import Path
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "my_word_template.docx"
doc = DocxTemplate(document_path)
context = {"NAME": "Sven"}
doc.render(context)
doc.save(Path(__file__).parent / "generated_doc.docx")