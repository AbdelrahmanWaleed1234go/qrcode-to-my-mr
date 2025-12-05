from flet import *
import qrcode

def main(page:Page):
    wel=Text("Welcome in qrcode for school app")

    ti=TextField("Enter your grade level and your name")

    def create(e):
        img = qrcode.make(ti.value)
        img.save("your_qr.ico")
        img.show()

    e=ElevatedButton("create your qrcode",on_click=create)

    page.add(wel,ti,e)

app(main,view=WEB_BROWSER)
    

