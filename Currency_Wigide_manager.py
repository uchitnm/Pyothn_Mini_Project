from tkinter import *
import json
import requests

with open('data.json', 'r', encoding="utf8") as fileObj:
    choices = json.load(fileObj)
    fileObj.close()

def DETAILS():
    global choices
    info_wid=Tk()
    s=""
    for i in choices:
        s+=f"{choices[i]:<35}\t{':' :^2}\t{i:>35}\n"
    T=Text(master=info_wid)
    T.insert(INSERT, s)
    T.configure(state='disabled')
    T.pack()

    info_wid.mainloop()


def convert(amt,wid_name,result,toChoice):
    # print(str(choice_to.get()))
    if str(amt.get()) == "Currency value.":
        amt.set("1")
    con_url = f"https://api.apilayer.com/fixer/convert?to={str(toChoice.get())}&from={str(toChoice.get())}&amount={str(amt.get())}"
    symbolsCurrencyJson = requests.get(
        "https://gist.githubusercontent.com/ksafranski/2973986/raw/5fda5e87189b066e11c1bf80bbfbecb556cf2cc1/Common-Currency.json").json()

    headers = {"apikey": "gibY1ggFgTfO5XY02pF69ZWZLYaOTFec"}

    response = requests.request("GET", con_url, headers=headers)

    result = response.json()
    Label(wid_name, text="Converted Amount: ").grid(
        row=2, column=0, columnspan=2, sticky="W")
    result.config(text=symbolsCurrencyJson[str(toChoice.get())]["symbol"]+" "+str(result["result"]))


def click(event,field_name):
    if field_name.get() == 'Currency value.':
        field_name.config(state=NORMAL)
        field_name.delete(0, END)
    else:
        field_name.config(state=NORMAL)


def unclick(event,field_name):
    if field_name.get() == '':
        field_name.delete(0, END)
        field_name.insert(0, 'Currency value.')
        field_name.config(state=DISABLED)
    else:
        field_name.config(state=DISABLED)