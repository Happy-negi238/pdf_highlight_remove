import fitz

doc = fitz.open("pdf.pdf")

start_page = 23  # page 25
OPTIONS_X0 = 450  # tuned value

for page_num in range(start_page, doc.page_count):
    page = doc[page_num]
    annots = page.annots()

    if annots:
        for annot in list(annots):
            if annot.type[0] == 8:
                rect = annot.rect

                center_x = (rect.x0 + rect.x1) / 2
                overlap = rect.x1 - max(rect.x0, OPTIONS_X0)

                # Condition 1: center in options
                cond1 = center_x >= OPTIONS_X0

                # Condition 2: >40% highlight in options area
                cond2 = overlap > (rect.width * 0.4)

                if cond1 or cond2:
                    page.delete_annot(annot)

doc.save("output_options_only.pdf")
print("Options column highlights removed (robust mode) ✅")

# import fitz 

# doc = fitz.open("almost_correct.pdf")   

# page_num = 35
# page = doc[page_num]

# # 🔹 Left block ke exact text (jaisa PDF me hai)
# TARGET_TEXTS = [
#     "Macros can be stored in ----------- locations"
# ]

# for text in TARGET_TEXTS:
#     areas = page.search_for(text)
#     for rect in areas:
#         highlight = page.add_highlight_annot(rect)
#         highlight.update()

# doc.save("output_page36_text_highlighted.pdf")
# print("Page 36 text-only highlight restored ✅")
