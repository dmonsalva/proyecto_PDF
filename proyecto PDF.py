proyecto = input("DIGITA LA DESCRIPCION DEL PROYECTO: ")
horas_estimadas = input("DIGITA LA CANTIDAD DE HORAS ESTIMADAS: ")
valor_hora = input("DIGITA EL VALOR DE LA HORA TRABAJADA: ")
tiempo_estimado = input("DIGITA EL PLAZO ESTIMADO: ")
valor_total = int(horas_estimadas)*int(valor_hora)


from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("Template.png", 0 ,0)

pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, tiempo_estimado)
pdf.text(115, 205, str(valor_total))

pdf.output("presupuesto.pdf")
print("PRESUPUESTO EJECUTADO CON EXITO")