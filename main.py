import math
import os

import tkinter
from tkinter import filedialog

from PIL import Image

from functools import partial

print(str(os.getcwd()))
# tkinter 정의
window = tkinter.Tk()

# 창 생성
window.title('오픈마켓 썸네일 사이즈 조절')
window.geometry('640x400+200+200')

# 선택된 파일 저장 튜플
files = ()

# 파일 선택 함수
def fileChoose():
    global files
    files = filedialog.askopenfilenames(title="select a file",
                          filetypes =(('png files', '*.png'),
                          ('jpg files', '*.jpg'),
                          ('jpeg files', '*jpeg')))

    imageCountLabel.config(text="'"+str(len(files))+"'"+'개의 파일 선택됨.')

# 파일 선택 버튼
fileBtn = tkinter.Button(window, text='파일선택', command=fileChoose)
fileBtn.pack(pady=30)


# 선택된 사진 텍스트
imageCountLabel = tkinter.Label(window, text='')
imageCountLabel.pack()

# 오픈마켓 리스트
openMarketList = [
    '**한꺼번에**',
    '네이버 스토어팜',
    '쿠팡',
    '쿠팡(로켓)',
    '11번가',
    'G마켓 / 옥션',
    # '옥션',
    '자사몰',
    '학교장터',
    '네이버 가격비교',
]

# 확인 라벨 초기화
def labelInit():
    commitLabel.config(text='')

# 이미지 변경 함수
def imageResize(openMarket, type, extention):
    
    print('파일 갯수 : ', len(files))
    # 파일 갯수만큼 반복
    for file in files:
        print('파일 명 : ', file)
        
        # filedialog로 가져온 경로를 pillow image로 open
        image=Image.open(file)
        print('원래 사이즈 : ', image.size)
        
        # 파일명 추출
        fileName = os.path.split(file)[1]
        fileName = fileName.split('.')[0]

        # 원본 이미지 사이즈를 x,y로 저장
        originSizeX = image.size[0]
        originSizeY = image.size[1]

        # 변환된 이미지 변수 정의
        resizedImage = ''

        # 썸네일이 선택 되었다면 학교장터와 나머지로 나눔

        if type == '썸네일':
            # 한꺼번에하면 하나씩 모두 저장
            if openMarket == '**한꺼번에**':

                # 네이버 스토어팜
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'네이버 스토어팜'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'네이버 스토어팜'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 쿠팡
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 쿠팡(로켓)
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡(로켓)'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡(로켓)'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 11번가
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'11번가'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'11번가'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # G마켓 / 옥션
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'G마켓'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'G마켓'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 옥션
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'옥션'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'옥션'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 자사몰
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'자사몰'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'자사몰'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 학교장터
                resizedImage = image.resize((262, 262))
                # 학교장터는 jpg로만 저장
                # JPG로 저장 할 때는 RGB로 변경
                resizedImage = resizedImage.convert('RGB')
                resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'학교장터'+'.jpg', quality=100)

                # 가격비교
                resizedImage = image.resize((1000, 1000))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'가격비교'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'가격비교'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                commitLabel.config(text='변환 완료!')
            
            # 여기까지 한번에 뽑기
            #---------------------------------------------------------------------------#

            # 썸네일은 학교장터와 나머지만 구분
            elif openMarket == '학교장터':
                resizedImage = image.resize((262, 262))
                commitLabel.config(text='변환 완료!')
            else:
                resizedImage = image.resize((1000, 1000))
                commitLabel.config(text='변환 완료!')


        #-------------------------------------------------------------------------------#
        # 여기부터 상세페이지

        # 상세 페이지가 선택 되었으면 각 오픈마켓의 기준 x크기를 가져옴
        # 원본 x크기와 기준 x크기를 나누고, y에 결과를 곱합
        elif type == '상세페이지':
            # 한꺼번에하면 하나씩 모두 저장
            if openMarket == '**한꺼번에**':
                # 네이버 스토어팜
                targetSizeX = 860
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'네이버 스토어팜'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'네이버 스토어팜'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 쿠팡
                targetSizeX = 780
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 쿠팡(로켓)
                targetSizeX = 780
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡(로켓)'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'쿠팡(로켓)'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 11번가
                targetSizeX = 800
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'11번가'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'11번가'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # G마켓 / 옥션
                resizedImage = image.resize((860, 2580))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'G마켓'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'G마켓'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # # 옥션
                # resizedImage = image.resize((860, 2580))
                # # 선택된 확장자에 따라 저장
                # if extention == '.jpg':
                # JPG로 저장 할 때는 RGB로 변경
                resizedImage = resizedImage.convert('RGB')
                #     resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'옥션'+'.jpg', quality=100)
                # elif extention == '.png':
                #     resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'옥션'+'.png')

                # print('변환된 사이즈 : ', resizedImage.size)

                # 자사몰
                targetSizeX = 1000
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))
                # 선택된 확장자에 따라 저장
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'자사몰'+'.jpg', quality=100)
                elif extention == '.png':
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'자사몰'+'.png')

                print('변환된 사이즈 : ', resizedImage.size)

                # 학교장터
                targetSizeX = 680
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

                # JPG로 저장 할 때는 RGB로 변경
                # 학교장터는 jpg로만 저장
                resizedImage = resizedImage.convert('RGB')
                resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'학교장터'+'.jpg', quality=100)

                print('변환된 사이즈 : ', resizedImage.size)

                commitLabel.config(text='변환 완료!')

                # 가격비교
                targetSizeX = 750
                calc =  targetSizeX / originSizeX
                resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

                # JPG로 저장 할 때는 RGB로 변경
                resizedImage = resizedImage.convert('RGB')
                resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+'학교장터'+'.jpg', quality=100)

                print('변환된 사이즈 : ', resizedImage.size)

                commitLabel.config(text='변환 완료!')

            # 여기까지 한꺼번에 뽑기    
            #---------------------------------------------------------------------------#
            else:
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

                elif openMarket == 'G마켓 / 옥션':
                    resizedImage = image.resize((860, 2580))

                # elif openMarket == '옥션':
                #     targetSizeX = 860
                #     calc =  targetSizeX / originSizeX
                #     resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

                elif openMarket == '자사몰':
                    targetSizeX = 1000
                    calc =  targetSizeX / originSizeX
                    resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

                elif openMarket == '학교장터':
                    targetSizeX = 680
                    calc =  targetSizeX / originSizeX
                    resizedImage = image.resize((targetSizeX, round(originSizeY*calc)))

                # 선택된 확장자에 따라 저장, 학교장터는 jpg만 저장할 수 있도록 함
                if extention == '.jpg':
                    # JPG로 저장 할 때는 RGB로 변경
                    resizedImage = resizedImage.convert('RGB')
                    resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+str(openMarket)+'.jpg', quality=100)
                    commitLabel.config(text='변환 완료!')
                elif extention == '.png':
                    if openMarket != '학교장터':
                        resizedImage.save(str(os.getcwd())+'/resized'+str(fileName)+str(openMarket)+'.png')
                        commitLabel.config(text='변환 완료!')
                    else:
                        commitLabel.config(text='학교장터는 jpg만 사용 가능합니다!')

        print('변환된 사이즈 : ', resizedImage.size)
        
        window.after(4000, labelInit)

# 선택된 옵션을 표시해줌
def showSelect(event=None):
    selectLabel.config(text=openMarketSelect.get()+'  '+radioSelect.get()+'을(를) ' + extentionSelect.get()+'로 변환 합니다.')

# 오픈마켓 선택
openMarketSelect = tkinter.StringVar(window)
openMarketSelect.set(openMarketList[0])
openMarketMenu = tkinter.OptionMenu(window, openMarketSelect, *openMarketList, command=showSelect)
openMarketMenu.config(width=10)
openMarketMenu.pack(pady=20)

# 이미지 종류 선택
radioSelect = tkinter.StringVar()
thumbRadio = tkinter.Radiobutton(window, text="썸네일", value='썸네일', variable=radioSelect, command=showSelect)
thumbRadio.select()
thumbRadio.place(x=230, y=180)
pageRadio = tkinter.Radiobutton(window, text="상세페이지", value='상세페이지', variable=radioSelect, command=showSelect)
pageRadio.place(x=340, y=180)

# 확장자 선택
extentionSelect = tkinter.StringVar()
jpgRadio = tkinter.Radiobutton(window, text="JPG", value='.jpg', variable=extentionSelect, command=showSelect)
jpgRadio.select()
jpgRadio.place(x=230, y=210)
pngRadio = tkinter.Radiobutton(window, text="PNG", value='.png', variable=extentionSelect, command=showSelect)
pngRadio.place(x=340, y=210)

# 완료 텍스트
commitLabel = tkinter.Label(window, text='')
commitLabel.pack(side='bottom')

# 확인 버튼
commitBtn = tkinter.Button(window, text='확인', command=lambda:imageResize(openMarketSelect.get(), radioSelect.get(), extentionSelect.get()))
commitBtn.pack(side='bottom', pady=20)

# 선택 확인 텍스트
selectLabel = tkinter.Label(window, text='None')
selectLabel.pack(side='bottom')


showSelect()

window.mainloop()