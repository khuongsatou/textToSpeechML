import gtts  
from playsound import playsound  
from datetime import datetime
import os
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com','translate.google.com','translate.google.co.kr'])
# lang = translator.detect("who are you ?")


path = os.path.dirname(os.path.abspath(__file__))

random_date = datetime.now()
date = datetime.today().strftime("%Y-%m-%d")
print(date)
file_name = 'script.txt'
f = None
# Ý tưởng cho 1 đoạn văn -> kết quả cho ra số file tương ứng với câu.

# mỗi đoạn sẽ có 5 dòng chữ và khoảng cách với nhau bởi 1 dòng và kết thúc là dấu chấm mỗi dòng.

# 1 câu sẽ ra 5 dòng tương ứng.
# ______
# B1. Tách ra đấu (.)
# B2. Lấy 1 dòng *5. và 3 dòng sẽ ra 15 dòng.
# B3. Lấy 5 dòng trùng nhau tạo ra 1 file 1x và 0.6x.
# B4. Save lại file mp3 và đặt tên với dạng.  

def create_folder():
    try:
        os.mkdir(path+"/"+str(date))
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


def write_file(text):
    try:

        f = open(file_name, 'w')
        f.write(text)
        # print(f.read())
        
        f.close()
        
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


def x5(str):
    result = ''
    for i in range(5):
        result += str.strip() +".\n\n"
    # print(result,end='\n')
    return result


def textToSpeech(str,slow):
    return gtts.gTTS(text=str, lang=language, slow=slow)

def saveSpeech(speech,i,speed):
    return speech.save(str(date)+"/"+str(i)+"_"+str(speed)+"_"+str(random_date.time())+".mp3")

def translateVi(text):
    print(text)
    result = translator.translate(str(text), src='en', dest='vi')
    print(result)
    return result.text

#---- Config ----
text_val = 'i am impressed by your contributions to society every year and i want to become a volunteer in those meaning activities. I also like the ways you support your employees. I know that you pay for employees to develop the new techniques and skills. I think that really helps to build employee satisfaction and loyalty'  

language = 'en' 
slow = True 


# tách data ra
data = text_val.split('.')
_len = len(data)

# tạo thư mục chứa
create_folder()
list_text  = '' + str(random_date)+'\n' + "\n----------------------\n"

for row in range(_len):
    # duplicate lên 5 lần
    text = x5(data[row])
    for col in range(2):
        # đưa vào đọc xử lý
        speech = textToSpeech(text,col == 0)
        # save lại
        saveSpeech(speech,row,'0.6x' if col == 0 else '1x')
    list_text += str(text) + "\n----------------------\n\n"

print(list_text)
tran = translateVi(list_text)
write_file(list_text+""+ tran)




# # play the audio file  
# playsound("welcome.mp3")  