import tkinter
from tkinter import filedialog
from PIL import Image
from functools import partial
    

window = tkinter.Tk()

window.title('오픈마켓 썸네일 사이즈 조절')
window.geometry('640x400+200+200')

files = ()

def fileChoose():
    global files
    files = filedialog.askopenfilenames(title="select a file",
                          filetypes =(('png files', '*.png'),
                          ('jpg files', '*.jpg')))


    print(files)


fileBtn = tkinter.Button(window, text='파일선택', command=fileChoose)
fileBtn.pack(pady=20)

openMarketList = [
    '**한꺼번에**',
    '네이버 스토어팜',
    '쿠팡',
    '쿠팡(로켓)',
    '11번가',
    'G마켓',
    '자사몰',
    '학교장터',
]

def showSelect(event=None):
    label.config(text=openMarketSelect.get()+'  '+radioSelect.get()+'를' +  ' ' + extentionSelect.get()+'로 변환 합니다.')

def imageResize(openMarket, type, extention):
    print('파일 갯수 : ', len(files))
    for file in files:
        print('파일 명 : ', file)
        image=Image.open(file)

        if type == '썸네일':
            if openMarket == '학교장터':
                image.resize(('262x262'))
            else:
                image.resize(('1000x1000'))
        elif type == '상세페이지':
            pass
            
        if extention == '.jpg':
            image.save('asd.jpg', 'JPG')
            print('jpg로 저장함!~')
        elif extention == 'png':
            image.save('asd.png', 'PNG')
            print('png로 저장함!~')

# 오픈마켓 선택
openMarketSelect = tkinter.StringVar(window)
openMarketSelect.set(openMarketList[0])
openMarketMenu = tkinter.OptionMenu(window, openMarketSelect, *openMarketList, command=showSelect)
openMarketMenu.config(width=10)
openMarketMenu.pack()

# 이미지 종류 선택
radioSelect = tkinter.StringVar()
thumbRadio = tkinter.Radiobutton(window, text="썸네일", value='썸네일', variable=radioSelect, command=showSelect)
thumbRadio.place(x=230, y=120)
pageRadio = tkinter.Radiobutton(window, text="상세페이지", value='상세페이지', variable=radioSelect, command=showSelect)
pageRadio.place(x=340, y=120)

# 확장자 선택
extentionSelect = tkinter.StringVar()
jpgRadio = tkinter.Radiobutton(window, text="JPG", value='.jpg', variable=extentionSelect, command=showSelect)
jpgRadio.place(x=230, y=150)
pngRadio = tkinter.Radiobutton(window, text="PNG", value='.png', variable=extentionSelect, command=showSelect)
pngRadio.place(x=340, y=150)


commitBtn = tkinter.Button(window, text='확인', command=lambda:imageResize(openMarketSelect.get(), radioSelect.get(), extentionSelect.get()))
commitBtn.pack(side='bottom', pady=20)

# 선택 확인 텍스트
label = tkinter.Label(window, text="None", height=5)
label.pack(side='bottom')


window.mainloop()