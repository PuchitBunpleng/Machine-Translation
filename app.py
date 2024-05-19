from tkinter import *
from tkinter import ttk
from idlelib.tooltip import Hovertip


# Change Here
def ThaiToEng(thai):
    eng = thai + ' --> Thai to Eng'  # Change this Line
    return eng


# เปลี่ยนตรงนี้
def EngToThai(eng):
    thai = eng + ' --> อังกฤษเป็นไทย'  # เปลี่ยนบรรทัดนี้
    return thai


# use for get model name
def getModel():
    if modelCombo.current() == 0:
        return 'Transformer'
    elif modelCombo.current() == 1:
        return 'mBART'


def swapLang():
    print(getModel())
    global curLang
    inText.delete('1.0', END)
    outputText = outText.get(1.0, "end-1c")
    inText.insert(INSERT, outputText)
    outText.config(state=NORMAL)
    outText.delete('1.0', END)
    outText.config(state=DISABLED)
    if curLang == 'Thai':
        langLabel.configure(text='English:')
        inFlag.configure(image=engFlag)
        outFlag.configure(image=thaiFlag)
        curLang = 'Eng'
    elif curLang == 'Eng':
        langLabel.configure(text='Thai:')
        inFlag.configure(image=thaiFlag)
        outFlag.configure(image=engFlag)
        curLang = 'Thai'
    else:
        print('Something Wrong')


def translate():
    if inText.get(1.0, "end-1c"):
        outText.delete('1.0', END)
        inputText = inText.get(1.0, "end-1c")
        outText.config(state=NORMAL)
        if curLang == 'Thai':
            translatedTextEng = ThaiToEng(inputText)
            outText.delete('1.0', END)
            outText.insert(INSERT, translatedTextEng)
        elif curLang == 'Eng':
            translatedTextThai = EngToThai(inputText)
            outText.delete('1.0', END)
            outText.insert(INSERT, translatedTextThai)
        else:
            print('Something Wrong')
        outText.config(state=DISABLED)


root = Tk()
root.title('Capstone Project')
root.minsize(800, 600)
root.geometry('800x600')
root.configure(bg='#DBEEFC')
frame = Frame(root)
frame.pack()

curLang = 'Thai'

# Banner
Label(root, text='Machine Translation Application', font=('JetBrains Mono', 32), bg='#17ACFF')\
    .place(x=0, y=0, width=800, height=90)

# Model Selection Text
Label(root, text='Model:', font=('JetBrains Mono', 16), bg='#DBEEFC').place(x=271, y=118, width=58, height=21)

# Model Selection Combobox
modelStr = StringVar()
modelCombo = ttk.Combobox(root, textvariable=modelStr, font=('JetBrains Mono', 16))
modelCombo['values'] = ('Transformer', 'mBART')
modelCombo.place(x=338, y=110, width=182, height=40)
modelCombo.current(0)

# Input Label
langLabel = Label(root, text='Thai:', font=('JetBrains Mono', 20), anchor=W, bg='#DBEEFC')
langLabel.place(x=70, y=134, width=96, height=26)

# Input Flag
thaiFlag = PhotoImage(file='src/images/ThaiFlag.png').subsample(12, 12)
inFlag = Label(root, image=thaiFlag, bg='#DBEEFC')
inFlag.place(x=690, y=130, width=40, height=40)

# Input Textbox
inText = Text(root, font=('JetBrains Mono', 14))
scroll1 = Scrollbar(inText)
inText.configure(yscrollcommand=scroll1.set)
inText.place(x=70, y=170, width=660, height=125)
scroll1.config(command=inText.yview)
scroll1.pack(side=RIGHT, fill=Y)

# Translate Button
transB = Button(root, text='Translate', bg='#17ACFF', font=('JetBrains Mono', 20), command=translate)
transB.place(x=264, y=315, width=200, height=44)

# Swap Language Button
swapICO = PhotoImage(file='src/images/Swap.png').subsample(21, 21)
swapB = Button(root, image=swapICO, command=swapLang)
swapB.place(x=494, y=315, width=44, height=44)
Hovertip(swapB, 'Change Language')

# Output Label
Label(root, text='Translated:', font=('JetBrains Mono', 20), bg='#DBEEFC').place(x=70, y=359, width=132, height=26)

# Output Flag
engFlag = PhotoImage(file='src/images/EngFlag.png').subsample(13, 13)
outFlag = Label(root, image=engFlag, bg='#DBEEFC')
outFlag.place(x=690, y=355, width=40, height=40)

# Output Textbox
outText = Text(root, font=('JetBrains Mono', 14), state='disabled')
scroll2 = Scrollbar(outText)
outText.configure(yscrollcommand=scroll2.set)
outText.place(x=70, y=395, width=660, height=125)
scroll2.config(command=outText.yview)
scroll2.pack(side=RIGHT, fill=Y)


root.mainloop()