#!/usr/bin/env python3

pdf_objects = []

pdf_objects.append(
    b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
)

pdf_objects.append(
    b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
)

pdf_objects.append(
    b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n"
)

content_stream = b"BT\n/F1 24 Tf\n100 700 Td\n(This is a sample PDF.) Tj\nET"

pdf_objects.append(
    b"4 0 obj\n<< /Length " + str(len(content_stream)).encode("ascii") + b" >>\nstream\n" + content_stream + b"\nendstream\nendobj\n"
)

pdf_objects.append(
    b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n"
)

pdf_header = b"%PDF-1.1\n"

offsets = []
current_offset = len(pdf_header)
for obj in pdf_objects:
    offsets.append(current_offset)
    current_offset += len(obj)

xref = b"xref\n0 " + str(len(pdf_objects)+1).encode("ascii") + b"\n0000000000 65535 f \n"
for off in offsets:
    xref += ("%010d" % off).encode("ascii") + b" 00000 n \n"

xref += b"trailer\n<< /Root 1 0 R /Size " + str(len(pdf_objects)+1).encode("ascii") + b" >>\nstartxref\n" + str(current_offset).encode("ascii") + b"\n%%EOF\n"

with open("docs/pdfs/sample.pdf", "wb") as f:
    f.write(pdf_header)
    for obj in pdf_objects:
        f.write(obj)
    f.write(xref)
