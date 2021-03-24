import math

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
                          ('jpg files', '*.jpg'),
                          ('jpeg files', '*jpeg')))

    imageCountLabel.config(text="'"+str(len(files))+"'"+'개의 파일 선택됨.')


fileBtn = tkinter.Button(window, text='파일선택', command=fileChoose)
fileBtn.pack(pady=20)

openMarketList = [
    '**한꺼번에**',
    '네이버 스토어팜',
    '쿠팡',
    '쿠팡(로켓)',
    '11번가',
    'G마켓',
    '옥션',
    '자사몰',
    '학교장터',
]

def labelInit():
    commitLabel.config(text='')


def imageResize(openMarket, type, extention):

    print('파일 갯수 : ', len(files))
    for file in files:
        print('파일 명 : ', file)
        
        image=Image.open(file)
        print('원래 사이즈 : ', image.size)
        originSizeX = image.size[0]
        originSizeY = image.size[1]

        resizedImage = ''

        if type == '썸네일':
            if openMarket == '학교장터':
                resizedImage = image.resize((262, 262))
            else:
                resizedImage = image.resize((1000, 1000))
        elif type == '상세페이지':
            if openMarket == '네이버 스토어팜':
                targetSizeX = 860
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

            elif openMarket == '쿠팡':
                targetSizeX = 780
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                
            elif openMarket == '쿠팡(로켓)':
                targetSizeX = 780
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

            elif openMarket == '11번가':
                targetSizeX = 800
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

            elif openMarket == 'G마켓':
                resizedImage = image.resize((1000, 1000))

            elif openMarket == '옥션':
                targetSizeX = 860
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

            elif openMarket == '자사몰':
                targetSizeX = 1000
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

            elif openMarket == '학교장터':
                targetSizeX = 680
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

        if extention == '.jpg':
            resizedImage.save('aaaa.jpg', quality=100)
        elif extention == '.png':
            resizedImage.save('aaaa.png')

        print('변환된 사이즈 : ', resizedImage.size)

        commitLabel.config(text='변환 완료!')
        window.after(1000, labelInit)

def showSelect(event=None):
    selectLabel.config(text=openMarketSelect.get()+'  '+radioSelect.get()+'을(를) ' + extentionSelect.get()+'로 변환 합니다.')

# 오픈마켓 선택
openMarketSelect = tkinter.StringVar(window)
openMarketSelect.set(openMarketList[0])
openMarketMenu = tkinter.OptionMenu(window, openMarketSelect, *openMarketList, command=showSelect)
openMarketMenu.config(width=10)
openMarketMenu.pack()

# 이미지 종류 선택
radioSelect = tkinter.StringVar()
thumbRadio = tkinter.Radiobutton(window, text="썸네일", value='썸네일', variable=radioSelect, command=showSelect)
thumbRadio.select()
thumbRadio.place(x=230, y=120)
pageRadio = tkinter.Radiobutton(window, text="상세페이지", value='상세페이지', variable=radioSelect, command=showSelect)
pageRadio.place(x=340, y=120)

# 확장자 선택
extentionSelect = tkinter.StringVar()
jpgRadio = tkinter.Radiobutton(window, text="JPG", value='.jpg', variable=extentionSelect, command=showSelect)
jpgRadio.select()
jpgRadio.place(x=230, y=150)
pngRadio = tkinter.Radiobutton(window, text="PNG", value='.png', variable=extentionSelect, command=showSelect)
pngRadio.place(x=340, y=150)

# 완료 텍스트
commitLabel = tkinter.Label(window, text='')
commitLabel.pack(side='bottom')

# 확인 버튼
commitBtn = tkinter.Button(window, text='확인', command=lambda:imageResize(openMarketSelect.get(), radioSelect.get(), extentionSelect.get()))
commitBtn.pack(side='bottom', pady=20)

# 선택 확인 텍스트
selectLabel = tkinter.Label(window, text='None')
selectLabel.pack(side='bottom')

# 선택된 사진 텍스트
imageCountLabel = tkinter.Label(window, text='')
imageCountLabel.pack(side='bottom')

showSelect()

window.mainloop()