import random
from tkinter import *

#bookname  
book1 = ['Foreigner ', 'Alien ', 'Phantoms ', 'Traitors ', 'Friend ', 'Edge ', 'Sword ', 'Priest ', 'Witch ', 'Criminals ', 'Losers ', 'Lords ', 'Robots ', 'Owl ', 'Army ', 'Gods ', 'Slaves ', 'Guardians ', 'Spiders ', 'Lions ', 'Soldiers ']
book2 = ['Of The ', 'Of The ', 'With ', 'Without ']
book3 = ['Ascension', 'Time', 'Sea', 'Curse', 'Invaders', 'Gold', 'Dungeons', 'Water', 'Utopia', 'Night', 'Knights', 'Invaders', 'Imagination', 'Ancients', 'Mountain', 'Waves', 'Home', 'Dreams', 'End', 'Ocean', 'Direction']
bookname = random.choice(book1)+random.choice(book2)+random.choice(book3)

#name
firstname = ['Nos ', 'Lavort ', 'Muckie ', 'Dauvoos ', 'Mashun ', 'Wer ', 'Ozaa ', 'Jakhi ', 'Niulapam ', 'Zhuzang ', 'Civio ', 'Frasi ', 'Mochlort ', 'Lodulin ', 'Leclat ', 'Umohtup ', 'Tantapia ', 'Uggat ', 'Yagut ', 'Ipsaus ', 'Scistell ', 'Cheeck ', 'Tosuq ']
middleyn = ['yes', 'no']
middleyn1 = random.choice(middleyn)
middle = ['Bervock ', 'Chuongjam ', 'Shupoun ', 'Rouve ', 'Oipzaib ', 'Ubafid ', 'Bikchot ', 'Bi ', 'Motte ', 'Shifaafum ', 'Achun ', 'Wharkezz ', 'Jeintsan ', 'Oxi ', 'Dougenq ', 'Si ', 'Datti ', 'Ubbud ', 'Az ', 'Ummi ', 'Davor ', 'Ampoz ', 'Thall ', 'Buuzom ', 'Yengxai ', 'Hiyyauk ', 'Potholl ']
surname_male = ['Zoolu', 'Youmar', 'Treovos', 'Ron', 'Uf', 'Oim', 'Oothung', 'Wizti', 'Shujin', 'Sesourx', 'Hugudrio', 'Sabag', 'Topuz', 'Tludhub', 'Soprogg', 'Tave', 'Boni', 'Deikai', 'Baglopt', 'Qauthaap', 'Yabannin', 'Sajun', 'Iser', 'Gu', 'Maadchosh', 'Mawokhom']
surname_male1 = random.choice(surname_male)
surname_female = ['Shoshee', 'Ziqah', 'Luse', 'Abviusce', 'Ann', 'Voecemplis', 'Jaamma', 'Dioci', 'Thenkash', 'Bzuxach', 'Edauk', 'Tlijghoa', 'Abb', 'Thusnum', 'Ugoh', 'Tilsequuo', 'Aepio', 'Hiasor', 'Gzux', 'Wuyauzh', 'Psatu', 'Binigra', 'Gizizah']
surname_female1 = random.choice(surname_female)


#surname_pick
pick_surname1 = ['male', 'female']
pick_surname = random.choice(pick_surname1)
if pick_surname == 'male':
    sur_data = surname_male1
if pick_surname == 'female':
    sur_data = surname_female1
    
#gender
if pick_surname == 'male':
    gender = 'Male'
if pick_surname == 'female':
    gender = 'Female'

#gender_character
if pick_surname == 'male':
    gender_ch = 'man'
if pick_surname == 'female':
    gender_ch = 'woman'

#type
type = ['Young Adult', 'Adult', 'Elderly Adult', 'Child', 'Adolescent', 'Old Adult']
type1 = random.choice(type)

#nationality
nationality = ['Duyisish', 'Touhaimese', 'Zammanish', 'Siwahic', 'Tolberian']
nationality1 = random.choice(nationality)

#city
cityDuyisish = ['Khumaggas, ', 'Chuong, ', 'Khazudha, ', 'Quya, ', 'Morfort, ', 'Meoxpiam, ', 'Beinwai, ', 'Ahshokh, ']
cityTouhaimese = ['Wressey, ', 'Zroxrora, ', 'Flifchester, ', 'Zrirphia, ', 'Grora, ', 'Yheim, ', 'Ordtol, ', 'Ariopus, ']
cityZammanish = ['Diburgh, ', 'Striby, ', 'Zhosham, ', 'Frauxmery, ', 'Yubert, ', 'Hok, ', 'Mey, ', 'Sreka, ', 'Oremery, ', 'Ordburg, ']
citySiwahic = ['Godence, ', 'Zlaport, ', 'Yritginia, ', 'Zrueron, ', 'Ulale, ', 'Strento, ', 'Glagos, ', 'Akalas, ', 'Aresgas, ']
cityTolberian = ['Udesgend, ', 'Gidsea, ', 'Fohgas, ', 'Fruostin, ', 'Xico, ', 'Cosa, ', 'Zrok, ', 'Aleson, ']

#nationality
if nationality1 == 'Duyisish':
    cityDuyisish1 = random.choice(cityDuyisish)
    location = cityDuyisish1+'Duysis'
if nationality1 == 'Touhaimese':
    cityTouhaimese1 = random.choice(cityTouhaimese)
    location = cityTouhaimese1+'Touhai'
if nationality1 == 'Zammanish':
    cityZammanish1 = random.choice(cityZammanish)
    location = cityZammanish1+'Zamman'
if nationality1 == 'Siwahic':
    citySiwahic1 = random.choice(citySiwahic)
    location = citySiwahic1+'Siwah'
if nationality1 == 'Tolberian':
    cityTolberian1 = random.choice(cityTolberian)
    location = cityTolberian1+'Tolberia'

#language
if nationality1 == 'Duyisish':
    language = 'Duyiush'
if nationality1 == 'Touhaimese':
    language = 'Touhaleze'
if nationality1 == 'Zammanish':
    language = 'Zaleze'
if nationality1 == 'Siwahic':
    language = 'Surewa'
if nationality1 == 'Tolberian':
    language = 'Tolbese'

#age
if type1 == 'Child':
    age = random.randint(6, 14)
if type1 == 'Adolescent':
    age = random.randint(15, 17)
if type1 == 'Young Adult':
    age = random.randint(18, 25)
if type1 == 'Adult':
    age = random.randint(26, 58)
if type1 == 'Elderly Adult':
    age = random.randint(59, 75)
if type1 == 'Old Adult':
    age = random.randint(76, 96)

#birth
birthmonthh = ['January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'November ', 'December ']
birthmonth = random.choice(birthmonthh)
leapyearr = ['yes', 'no']
leapyear = random.choice(leapyearr)
if birthmonth == 'January ':
    birthday = random.randint(1, 31)
if birthmonth == 'February ':
    if leapyear == 'yes':
        birthday = random.randint(1, 29)
    if leapyear == 'no':
        birthday = random.randint(1, 28)
if birthmonth == 'March ':
    birthday = random.randint(1, 31)
if birthmonth == 'April ':
    birthday = random.randint(1, 30)
if birthmonth == 'May ':
    birthday = random.randint(1, 31)
if birthmonth == 'June ':
    birthday = random.randint(1, 30)
if birthmonth == 'July ':
    birthday = random.randint(1, 31)
if birthmonth == 'August ':
    birthday = random.randint(1, 31)
if birthmonth == 'September ':
    birthday = random.randint(1, 30)
if birthmonth == 'October ':
    birthday = random.randint(1, 31)
if birthmonth == 'November ':
    birthday = random.randint(1, 30)
if birthmonth == 'December ':
    birthday = random.randint(1, 31)

#height
if type1 == 'Child':
    height = random.randint(95, 161)
if type1 == 'Adolescent':
    height = random.randint(162, 172) 
if type1 == 'Young Adult':
    height = random.randint(173, 175)
if type1 == 'Adult':
    height = random.randint(175, 180)
if type1 == 'Elderly Adult':
    height = random.randint(170, 175)
if type1 == 'Old Adult':
    height = random.randint(160, 170)

#weight
if type1 == 'Child':
    weight = random.randint(22, 52)
if type1 == 'Adolescent':
    weight = random.randint(53, 66)
if type1 == 'Young Adult':
    weight = random.randint(67, 72)
if type1 == 'Adult':
    weight = random.randint(73, 87)
if type1 == 'Elderly Adult':
    weight = random.randint(71, 78)
if type1 == 'Old Adult':
    weight = random.randint(78, 80)

#deathdate
deathmonthh = ['January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'November ', 'December ']
deathmonth = random.choice(deathmonthh)
deathleapyearr = ['yes', 'no']
deathleapyear = random.choice(deathleapyearr)
if deathmonth == 'January ':
    deathday = random.randint(1, 31)
if deathmonth == 'February ':
    if deathleapyear == 'yes':
        deathday = random.randint(1, 29)
    if deathleapyear == 'no':
        deathday = random.randint(1, 28)
if deathmonth == 'March ':
    deathday = random.randint(1, 31)
if deathmonth == 'April ':
    deathday = random.randint(1, 30)
if deathmonth == 'May ':
    deathday = random.randint(1, 31)
if deathmonth == 'June ':
    deathday = random.randint(1, 30)
if deathmonth == 'July ':
    deathday = random.randint(1, 31)
if deathmonth == 'August ':
    deathday = random.randint(1, 31)
if deathmonth == 'September ':
    deathday = random.randint(1, 30)
if deathmonth == 'October ':
    deathhday = random.randint(1, 31)
if deathmonth == 'November ':
    deathday = random.randint(1, 30)
if deathmonth == 'December ':
    deathday = random.randint(1, 31)

#causeofdeath
causedeathh = ['Skin Disease', 'Diabetes', 'Digestive Disease', 'Suicide', 'Stroke', 'Stomach Cancer', 'Violence', 'Covid-19', 'Malaria', 'Rabies', 'Yellow Fever', 'Ebola', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis E', 'Heart Disease', 'Liver Cancer', 'Pancreatic Cancer', 'Kidney Cancer', 'Brain and nervous system cancer', 'Asthma', 'Alzheimer Disease', 'Parkinson Disease', 'Epilepsy', 'Drug Use Disorder', 'Bacterial Skin Disease', 'Down Syndrome', 'Pedestrian Road Injuries', 'Cyclist Road Injuries', 'Motorcyclist Road Injuries', 'Motor Vehicle Road Injuries', 'Drowning', 'Poisoning']
causedeath = random.choice(causedeathh)

#pronoun
if type1 == 'Child':
    if gender == 'Male':
        pronoun = 'child'
    if gender == 'Female':
        pronoun = 'child'
#teenager
if type1 == 'Adolescent':
    if gender == 'Male':
        pronoun = 'teen boy'
    if gender == 'Female':
        pronoun = 'teen girl'
#young adult
if type1 == 'Young Adult':
    if gender == 'Male':
        pronoun = 'young man'
    if gender == 'Female':
        pronoun = 'young girl'
#adult
if type1 == 'Adult':
    if gender == 'Male':
        pronoun = 'man'
    if gender == 'Female':
        pronoun = 'woman'
#elder adult
if type1 == 'Elderly Adult':
    if gender == 'Male':
        pronoun = 'old man'
    if gender == 'Female':
        pronoun = 'old woman'
#very old adult
if type1 == 'Old Adult':
    if gender == 'Male':
        pronoun = 'very old man'
    if gender == 'Female':
        pronoun = 'very old woman'

#he_she
if gender == 'Male':
    he_she = 'he'
if gender == 'Female':
    he_she = 'she'

#he_she2
if gender == 'Male':
    he_she2 = 'He'
if gender == 'Female':
    he_she2 = 'She'

#him_her
if gender == 'Male':
    him_her = 'him'
if gender == 'Female':
    him_her = 'her'

#his_her
if gender == 'Male':
    his_her = 'his'
if gender == 'Female':
    his_her = 'her'

#a_an
if type1 == 'Elderly Adult':
    a_an = 'an '
else:
    a_an = 'a '

#king_queen
if gender == 'Male':
    king_queen = 'king'
if gender == 'Female':
    king_queen = 'queen'
    
#storyparts
bornstory = ['In the day ' + str(he_she) + ' was born, ', 'On the timeline ' + str(he_she) + ' was born, ', 'In the generation ' + str(he_she) + ' was born, ', 'In the time ' + str(he_she) + ' was born, ', 'In the year ' + str(he_she) + ' was born, ', 'In the month ' + str(he_she) + ' was born, ']
bornstory_how = ['the sun was lighting the houses full of young, dark magic.', 'the flowers were all dead trying to escape from the magic of the new-born wizard.', 'the sky was full of grey clouds and witches who were cheering for the new ' + str(king_queen) + '.', 'no human was able to escape the hands of ' + str(sur_data) + '.', 'no living creature could escape the filthy hands of ' + str(sur_data) + '.', 'the creatures were all hiding from the evil hands of ' + str(sur_data) + '.']
story_start = [' Once upon a time, ', ' From the day god created the modern human, ', ' In the past, ', ' Way long ago, ', ' Many years ago, ', ' When the flowers were not touched by anyone, ', ' A long time ago, ', ' When the sky was full of joy, ', ' When you were not born yet, ', ' A long, long time ago, ', ' In the time the Earth did not exist, ', ' When kings and queens ruled the world, ']
character_male =  ['there was a king.', 'there was an evil ' + str(pronoun) + '.', 'there was ' + str(a_an) + str(pronoun) + ', named ' + str(sur_data) + '.', 'there was an ordinary farmer', 'there was ' + str(a_an) + str(pronoun) + ' who was working for the royal family.']
character_female = ['there was a queen.', 'there was an evil ' + str(pronoun) + '.', 'there was ' + str(a_an) + str(pronoun) + ', named ' + str(sur_data) + '.', 'there was an ordinary maid', 'there was ' + str(a_an) + str(pronoun) + ' who was working for the royal family.']
time = [' One day, ', ' One afternoon, ', ' One full-moon night, ', ' One night, ', ' One evening, ', ' One not special day, ', ' One not that special day, ', ' One very cold night, ', ' One very sunny day, ', ' One cloudy day, ', ' One miserable day, ', ' One peaceful day, ']
story_plot = [str(he_she2) + ' was going for a walk next to ', str(he_she2) + ' was passing by ', str(he_she2) + ' was enjoying the day next to ', str(he_she2) + ' was looking at ', str(he_she2) + ' was enjoying the day by ', str(he_she2) + ' was going for a walk next to ']
place = ['the garden. ', 'the castle. ', 'the mountains. ', 'the great village of El. ', 'the wizarding school. ', 'the witches college. ', 'the royal mansion. ', 'the town of Igu. ', 'the time department. ', 'the great wizard valley. ', 'the full blood container. ', 'the evil witch house. ']
second_character = [str(he_she2) + ' saw a man ', str(he_she2) + ' saw a girl ', str(he_she2) + ' saw a little girl ', str(he_she2) + ' saw a young boy ', str(he_she2) + ' saw an old man ', str(he_she2) + ' saw an old lady ', str(he_she2) + ' saw a very old man ', str(he_she2) + ' saw a very old lady ', str(he_she2) + ' saw a little boy ']
second_what = ['who seemed very angry, ', 'who was looking at the sky, ', 'who was suspicious, ', 'who was odd, ', 'who seemed, very, very happy, ', 'who was enjoying the day, ']
second_work = ['choking on something. ', 'searching something. ', 'flying. ', 'not respecting the orders. ', 'transforming into something. ', 'disappearing and reappearing. ', 'filming something. ', 'spitting something. ', 'trading something. ', 'making something. ', 'doing something. ']
first_ask_second = [str(he_she2) + ' asked the human, "What are you doing, bloody human?".', str(he_she2) + ' punched the human and said to the creature, "No more doing useless stuff, get to work!".', str(he_she2) + ' scared the human and said: "Get to work, you useless creature!".', str(he_she2) + ' ignored the human and leaved him there.', str(he_she2) + ' killed the human and said to the others, "You want this? Get back to work or you will end up like this useless human!".', str(he_she2) + ' tortured the human and asked him, "Want more? Get back to work or else I will come back to you!".']
response_second = [' The other humans said, "Please, leave us alone!".', ' "Do not torture us, please, we are not many!".', ' ' + str(he_she2) + ' laughed while the other humans stared at ' + str(him_her) + ' with fear in their eyes.', 'The other humans stared at ' + str(him_her) + ' while ' + str(he_she) + ' was laughing.']
leave_character_first = [' ' + str(he_she2) + ' left the humans there and went into ' + str(his_her) + ' office.', ' ' + str(he_she2) + ' was leaving while the humans were looking at him angry.', ' ' + str(he_she2) + ' was killing other innocent living creatures. No one could get off ' + str(his_her) + ' hand.']
endstory = [' ' + str(he_she2) + ' was doing bad stuff, now ' + str(he_she) + ' is dead, no one rules the witches and wizards now.', ' ' + str(he_she2) + ' will never ever rule the world again. ' + str(he_she) + ' is gone...', ' Witches and wizards will never rule the world again. They are nowhere to be found...']        

#character-pick
if gender == 'Male':
    charact_fin = character_male
else:
    charact_fin = character_female
character = charact_fin

#the-story-bot

final_story = random.choice(bornstory)+random.choice(bornstory_how)+random.choice(story_start)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_character)+random.choice(second_what)+random.choice(second_work)+random.choice(first_ask_second)+random.choice(response_second)+random.choice(leave_character_first)+random.choice(endstory)
finalstory = final_story

#print
import sys

orig_stdout = sys.stdout
f = open('story.txt', 'w')
sys.stdout = f

if middleyn1 == 'yes':
    namewmiddle = random.choice(firstname)+random.choice(middle)+sur_data
    print('------------------------------')
    print('Bookname: ', bookname)
    print('Character name: ', namewmiddle)
    print('Gender: ', gender)
    print('Type: ', type1)
    print('Nationality: ', nationality1)
    print('Location: ', location)
    print('Language: ', language)
    print('Age: ', age)
    print('Birthday: ', str(birthmonth) + str(birthday))
    print('Height: ', str(height) + ' cm')
    print('Weight: ', str(weight) + ' kg')
    print('Deathdate: ', str(deathmonth) + str(deathday))
    print('Cause of Death: ', causedeath)
    print('Story: ', finalstory)
    
if middleyn1 == 'no':
    namewomiddle = random.choice(firstname)+sur_data
    print('------------------------------')
    print('Bookname: ', bookname)
    print('Character name: ', namewomiddle)
    print('Gender: ', gender)
    print('Pronoun: ', pronoun)
    print('Type: ', type1)
    print('Nationality: ', nationality1)
    print('Location: ', location)
    print('Language: ', language)
    print('Age: ', age)
    print('Birthday: ', str(birthmonth) + str(birthday))
    print('Height: ', str(height) + ' cm')
    print('Weight: ', str(weight) + ' kg')
    print('Deathdate: ', str(deathmonth) + str(deathday))
    print('Cause of Death: ', causedeath)
    print('Story: ', finalstory)

sys.stdout = orig_stdout
f.close()

print('Sur_Data: ' + str(sur_data))
print('Pronoun: ' + str(pronoun))
print('Final Story: ' + str(finalstory))














    

 
    

