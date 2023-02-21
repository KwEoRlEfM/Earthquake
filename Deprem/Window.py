import requests
import json
from tkinter import *

url="https://api.orhanaydogdu.com.tr/deprem/kandilli/live" 

payload = {}
headers = {}

response = requests.request("GET", url)
result = json.loads(response.text)

#!Window
window = Tk()
window.geometry("1500x1000+200+20")
window.title("Deprem")

frame1 = Frame(window, height=200, width=200, bg = 'red')
frame1.pack(pady = 50)

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

vary = 200
def createlabels(tarih, bolge, buyukluk, derinlik):
    global vary
    newFrame = Frame(window, height=200, width=200, bg = 'blue')
    newFrame.place(x =75, y = vary)
    
    
    VARtarih = Label(newFrame, text = tarih, font = font)
    VARbolge = Label(newFrame, text = bolge, font = font)
    VARbuyukluk = Label(newFrame, text = buyukluk, font = font)
    VARderinlik = Label(newFrame, text = derinlik, font = font)
    
    varBuyukluk = Label(window, text = buyukluk, font = font, fg = 'white', bg = 'red')
    varBuyukluk.place(x = 1200, y = vary)

    padVAR = 5
    VARtarih.pack(side = "left", padx = padVAR)
    VARbolge.pack(side = "left", padx = padVAR)
    VARderinlik.pack(side = "right", padx = padVAR)
    VARbuyukluk.pack(side = "right", padx = padVAR)
    vary += 50

#print(result)
count = 0
print("{:<24} {:<39}  {:<12} {:<12}".format("Tarih", "Bolge", "Buyukluk", "Derinlik"))

for i in result["result"]:
    if(count >= 10):
        break
    
    if(i["mag"] > 3):
        createlabels(i["date"], i["title"], i["mag"], i["depth"])
        print("{:<24} {:<39}  {:<12} {:<12}".format(i["date"], i["title"], i["mag"], i["depth"]))
        count += 1

window.mainloop()