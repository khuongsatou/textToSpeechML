import gtts  
from playsound import playsound  

# Ý tưởng cho 1 đoạn văn -> kết quả cho ra số file tương ứng với đâu. 
text_val = 'i am impressed by your contributions to society every year and i want to become a volunteer in those meaning activities. I also like the ways you support your employees. I know that you pay for employees to develop the new techniques and skills. I think that really helps to build employee satisfaction and loyalty'  

language = 'en'  


print(text_val.split('.'))

# obj = gtts.gTTS(text=text_val, lang=language, slow=True)  

# # save the audio file  
# obj.save("welcome.mp3")   

# # play the audio file  
# playsound("welcome.mp3")  