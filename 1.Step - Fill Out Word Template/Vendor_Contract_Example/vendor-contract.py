from pathlib import Path
import datetime
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / "vendor-contract.docx"
doc = DocxTemplate(document_path)

client = "Sven"
vendor = "Tutorial Ltd."
amount = 2105
non_refundable = round(amount * 0.2, 2)
line1 = "Some text goes here"
line2 = "...and here goes some more text"
today = datetime.datetime.today()
today_in_one_week = today + datetime.timedelta(days=7)

context = {
    "CLIENT": client,
    "VENDOR": vendor,
    "LINE1": line1,
    "LINE2": line2,
    "AMOUNT": amount,
    "NONREFUNDABLE": non_refundable,
    "TODAY": today.strftime("%Y-%m-%d"),
    "TODAY_IN_ONE_WEEK": today_in_one_week.strftime("%Y-%m-%d"),
}

doc.render(context)
doc.save(Path(__file__).parent / f"{vendor}-contract.docx")