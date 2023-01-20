import pyttsx3
engine = pyttsx3.init() 


rate = engine.getProperty('rate')   
                      
engine.setProperty('rate', 180)     
#print (rate)  

volume = engine.getProperty('volume')   
                         

engine.setProperty('volume',6.0)    
#print (volume) 

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)   
text_one = input('Enter a text to convert to speech: ')
engine.say(text_one)
engine.save_to_file(text_one,'text_to_speech.mp3')
# engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()


engine.runAndWait()
