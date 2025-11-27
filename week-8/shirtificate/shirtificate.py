from fpdf import FPDF


def main():
    convert_pdf(input('Name: '))


def convert_pdf(n):
    pdf = FPDF(orientation="portrait", unit="mm", format="A4")
    pdf.add_page()

    # title
    pdf.set_font("helvetica", style="B", size=36)
    pdf.cell(0, 20, "CS50 Shirtificate", ln= True, align='C')

    # image
    pdf.image('E:\\Python\\cs50P\\week-8\\shirtificate\\shirtificate.png' , w=200, h = 200 , x = (pdf.w-200)/2, y = (pdf.h-200)/2)

    # name
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=24)
    pdf.cell(0,pdf.h/2 +30, f'{n} took CS50', align='C')

    # output
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()  