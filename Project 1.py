import docx
for i in range(1,6):
    doc = docx.Document(str(i)+".docx")
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = docx.shared.Pt(14)
    style.paragraph_format.line_spacing = 1.5
    doc.save(str(i)+".docx")
    