''' Developed By - Parv Narang '''
import speech_recognition as sr
import playsound
import time

r = sr.Recognizer()

with sr.Microphone() as source:

    while True:
        playsound.playsound('listen.mp3', True)
        print("What do you want to listen to : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('you said: {}'.format(text))

            if text == "donkey story":
                print("The foolish donkey")
                playsound.playsound('donkey.mp3', True)
                time.sleep(50)

                while True:
                    try:
                        playsound.playsound('ques.mp3', True)
                        print("Any questions")
                        #time.sleep(5)
                        audio1 = r.listen(source)
                        text1 = r.recognize_google(audio1)
                        print('Q. {}'.format(text1))
                        #time.sleep(1)
                        if text1 == 'what is this' or text1 == 'what is the story about':
                            print("this is a story about a foolish donkey.")
                            playsound.playsound('sfd.mp3',True)

                        elif text1 == 'what trick did he play' or text1 == 'which trick':
                            print("the donkey used to tumble down the stream and the salt bag also fell into the water. The salt dissolved in the water and hence the bag became very light to carry.")
                            playsound.playsound('trick.mp3',True)

                        elif text1 == 'what did he load on the donkey' or text1 == 'what he loaded':
                            print("He loaded a cotton bag on the donkey.")
                            playsound.playsound('load.mp3',True)


                        elif text1 == 'what is the moral' or text1 == 'what is the moral of the story':
                            print("Luck won’t favor always.")
                            playsound.playsound('luck_moral.mp3',True)

                        elif text1 == 'how did the bag become very light':
                            print("The salt dissolved in the water hence the bag became very light")
                            playsound.playsound('salt.mp3',True)

                        elif text1 == 'no questions' or text1 == 'nothing' or text1 == 'no':
                            print("Okay")
                            playsound.playsound('ok.mp3',True)
                            break

                        else:
                            print("Sorry please say it again")
                            playsound.playsound('sorry_please.mp3',True)
                    except:
                        print("Sorry ask again")
                        playsound.playsound('sorry_ask.mp3',True)            

            elif text == "the old man" or text == "old man":
                print("The old man")
                playsound.playsound('man.mp3', True)
                time.sleep(5)

                while True:
                    try:
                        playsound.playsound('ques.mp3', True)
                        print("Any questions")
                        #time.sleep(5)
                        audio2 = r.listen(source)
                        text2 = r.recognize_google(audio2)
                        print('Q.{}'.format(text2))
                        time.sleep(1)
                        if text2 == 'what is this' or text2 == 'what is the story about':
                            print("This is a story about an old man")
                            playsound.playsound('old.mp3',True)

                        elif text2 == 'what is the moral' or text2 == 'what is the moral of the story':
                            print("Don't chase happiness enjoy your life")
                            playsound.playsound('old_moral.mp3',True)
                        
                        elif text2 == 'how old was the man' or text2 == 'what is the age of the man':
                            print("He is 80 years old")
                            playsound.playsound('age.mp3',True)

                        elif text2 == 'what was the rumour':
                            print("The rumour was that the old man was happy on that day")
                            playsound.playsound('rumour.mp3',True)

                        elif text2 == 'no questions' or text2 == 'nothing' or text2 == 'no':
                            print("Okay")
                            playsound.playsound('ok.mp3',True)
                            break

                        else:
                            print("Sorry please say it again")
                            playsound.playsound('sorry_please.mp3',True)

                    except:
                        print("Sorry ask again")
                        playsound.playsound('sorry_ask.mp3',True)


            elif text == "a song" or text == "some songs" or text == "songs" or text == "song":
                print("Which one do you want to listen to ")
                print("I have kalimba, sleep away, maid with flaxen hair and the mashup")
                playsound.playsound('whsong.mp3',True)

                while True:
                    try:
                        playsound.playsound('whsng.mp3', True)
                        print("so which song you want to listen to")
                        audio3 = r.listen(source)
                        text3 = r.recognize_google(audio3)
                        print('{}'.format(text3))
                        time.sleep(1)
                        if text3 == 'kalimba' or text3 == 'i want to listen to kalimba':
                            print("Playing kalimba")
                            playsound.playsound('kalimba.mp3', True)
                            playsound.playsound('whatdo.mp3', True)
                            print("what do you want to do now")
                            audio4 = r.listen(source)
                            text4 = r.recognize_google(audio4)
                            print('{}'.format(text4))
                            if text4 == 'exit' or text4 == 'i want to exit' or text4 == 'leave':
                                print("Okay")
                                playsound.playsound('ok.mp3',True)
                                break
                            else:
                                continue

                        elif text3 == 'sleep away' or text3 == 'i want to listen to sleep away' or text3 == 'away' or text3 == 'sleep':
                            print("Playing sleep away")
                            playsound.playsound('sleep.mp3', True)
                            playsound.playsound('whatdo.mp3', True)
                            print("what do you want to do now")
                            audio4 = r.listen(source)
                            text4 = r.recognize_google(audio4)
                            print('{}'.format(text4))
                            if text4 == 'exit' or text4 == 'i want to exit' or text4 == 'leave':
                                print("Okay")
                                playsound.playsound('ok.mp3',True)
                                break
                            else:
                                continue


                        elif text3 == 'maid with' or text3 == 'maid with flaxen hair':
                            print("Playing maid with flaxen hair")
                            playsound.playsound('mfh.mp3', True)
                            playsound.playsound('whatdo.mp3', True)
                            print("what do you want to do now")
                            audio4 = r.listen(source)
                            text4 = r.recognize_google(audio4)
                            print('{}'.format(text4))
                            if text4 == 'exit' or text4 == 'i want to exit' or text4 == 'leave':
                                print("Okay")
                                playsound.playsound('ok.mp3',True)
                                break
                            else:
                                continue


                        elif text3 == 'mashup' or text3 == 'the mashup' or text3 == 'i want to listen to the mashup':
                            print("Playing the mashup")
                            playsound.playsound('song4.mp3', True)
                            playsound.playsound('whatdo.mp3', True)
                            print("what do you want to do now")
                            audio4 = r.listen(source)
                            text4 = r.recognize_google(audio4)
                            print('{}'.format(text4))
                            if text4 == 'exit' or text4 == 'i want to exit' or text4 == 'leave':
                                print("Okay")
                                playsound.playsound('ok.mp3',True)
                                break
                            else:
                                continue


                        elif text3 == 'exit' or text3 == 'i want to exit':
                            print("Okay")
                            playsound.playsound('ok.mp3',True)
                            break

                        else:
                            print("Sorry please say it again")
                            playsound.playsound('sorry_please.mp3',True)

                    except:
                        print("Sorry ask again")
                        playsound.playsound('sorry_ask.mp3',True)

            else:
                print("Sorry not in the list")
                playsound.playsound('sorry_list.mp3',True)
        
        except:
            print("Sorry could not recognize")
            playsound.playsound('sorry_recog.mp3',True)
