import requests
import json
from tkinter import *
from tkinter import ttk
from random import *
from tkinter.font import Font

url="https://api.orhanaydogdu.com.tr/deprem/kandilli/live" 

payload = {}
headers = {}

response = requests.request("GET", url)
result = json.loads(response.text)

#!Window
window = Tk()
window.geometry("1700x1000+200+20")
window.title("Deprem")

frame1 = Frame(window, height=200, width=200, bg = 'red')
frame1.pack(pady = 50)

#>Table
table = ttk.Treeview(window, columns = ("tarih", "bolge", "buyukluk", "derinlik"), show = "headings")
table.heading("tarih", text = "Tarih")
table.heading("bolge", text = "Bolge")
table.heading("buyukluk", text = "Buyukluk")
table.heading("derinlik", text = "Derinlik")
table.pack(fill = "both", expand = False)

style = ttk.Style()
style.theme_use("vista")
style.configure("Treeview", background = "#D3D3D3", foreground = "black", columwidth = 500,rowheight = 80, fieldbackground = "D3D3D3", font = ("Helvetica 15"))
style.map("Treeview", background = [("selected", "green")])

#>Labels
font = "Helvetica 20"
tarih = Label(frame1, text = "Tarih", font = font)
bolge = Label(frame1, text = "Bolge", font = font)
buyukluk = Label(frame1, text = "Buyukluk", font = font)
derinlik = Label(frame1, text = "Derinlik", font = font)
padVAR = 25
tarih.pack(side = "left", padx = padVAR)
bolge.pack(side = "left", padx = padVAR)
buyukluk.pack(side = "left", padx = padVAR)
derinlik.pack(side = "left", padx = padVAR)


#print(result)
count = 0
print("{:<24} {:<39}  {:<12} {:<12}".format("Tarih", "Bolge", "Buyukluk", "Derinlik"))

for i in result["result"]:
    if(count >= 10):
        break
    
    if(i["mag"] > 3):
        dataList = i["date"], i["title"], i["mag"], i["depth"]
        tarih = i["date"]
        bolge = i["title"]
        buyukluk = i["mag"]
        derinlik = i["depth"]
        datas = (tarih, bolge, buyukluk, derinlik)
        table.insert(parent = '', index = 0, values = datas)
        
        print("{:<24} {:<39}  {:<12} {:<12}".format(i["date"], i["title"], i["mag"], i["depth"]))
        count += 1

def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])
        
table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))
table.bind('<<TreeviewSelect>>', item_select)


window.mainloop()