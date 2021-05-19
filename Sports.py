import random
from PIL import Image
print('This program will ask a series of questions, all of which you should answer \'Yes\' or \'No\'.\nThe main focus of this program is to find your favorite sport and tell you little about it.\n')
answer = str(input('Would you like to see if we can guess what sport you are thinking of? '))
if answer.lower() == 'yes':
    print('Please answer \'Yes\' or \'No\' for the following questions\n')
    question1 = str(input('Do they use a ball for this sport? '))
    question2 = str(input('Do you score in a net? '))
    question3 = str(input('Is this a team sport? '))
    question4 = str(input('Do you shoot to score? '))
    question5 = str(input('Do you play up to a set score? '))
    question6 = str(input('Do you use a stick, bat, racket, or club? '))
    question7 = str(input('Do you wear pads? '))
    question8 = str(input('Is this sport played outside? '))
    
    if question1.lower() == 'no' and question6.lower() == 'yes':
        thoughtSport = 'Hockey'
    elif question3.lower() == 'no' and question6.lower() == 'yes' and question5.lower() == 'no':
        thoughtSport = 'Golf'
    elif question8.lower() == 'yes' and question2.lower() == 'yes' and question7.lower() == 'no':
        thoughtSport = 'Soccer'
    elif question4.lower() == 'yes' and question1.lower() == 'yes':
        thoughtSport = 'Basketball'
    elif question5.lower() == 'yes' and question1.lower() == 'yes' and question8.lower() == 'no':
        thoughtSport = 'Volleyball'
    elif question6.lower() == 'yes' and question8.lower() == 'yes' and question3.lower() == 'yes':
        thoughtSport = 'Baseball'
    elif question7.lower() == 'yes' and question8.lower() == 'yes':
        thoughtSport = 'Football'
    elif question8.lower() == 'yes' and question1.lower() == 'no':
        thoughtSport = 'Ultimate Frisbee'
    elif question5.lower() == 'yes' and question8.lower() == 'yes':
        thoughtSport = 'Tennis'
    else:
        thoughtSport = 'Unknown'
    print('\nThe sport you are thinking of is %s.' % (thoughtSport))
    
favSport = str(input('\nWhat is your favorite sport? '))
sportFile = ['basketball','football','hockey','golf','tennis','volleyball','soccer','baseball','ultimate frisbee','swimming','bowling','cricket','badminton','underwater basket weaving']
while favSport.lower() not in sportFile:
    print('\nSorry we do not currently have information on that sport.')
    favSport = str(input('Please enter another sport that interest you. '))
setSport = favSport.lower()
answer = str(input('\nWould like to know a little about %s? ' % (setSport)))
sportInfo = ['You shoot a ball.','Hit people and die young.','Use your stick and fight people.','Hole in 1.','Make a grunting noise.','Make ball hit the ground.','Run a lot kick a ball.','Dinger.','Throw a disk.','Don\'t drown.','WII bowling is lit.','Indian baseball.','It\'s fun.','Weave baskets underwater.']
if answer.lower() == 'yes':
    for index in range(len(sportFile)):
        if sportFile[index] == setSport:
            saveIndex = index
    print()
    print(sportInfo[saveIndex])
    
noPic = ['football','hockey','golf','tennis','volleyball','soccer','baseball','ultimate frisbee','swimming','bowling','cricket','badminton','underwater basket weaving']
if setSport not in noPic:
    answerImg = str(input('\nWould you like to see a picture of your selected sport? '))
    
    if answerImg.lower() == 'yes':
        setImNum = str(random.randint(1,3))
        imageName = ('Sport_Images/' + setSport + setImNum + '.jpg')
        image = Image.open(imageName)
        height = image.height
        width = image.width
        pixels = image.load()
        image.show()
    
if setSport not in noPic:
    answerImg2 = str(input('\nWould like to edit the given image? '))
    while answerImg2.lower() == 'yes' and answerImg.lower() == 'yes':
        imageAnswer = str(input('\nHow would you like to edit the image? Please choose one of the following:\n Negative: shows the negative form of the image\n FlipY: flips the image over the y-axis\n FlipX: flips the image over the x-axis\n Darken: makes white spots darker\n Lighten: makes dark spots(black) lighter\n Your answer: '))
        newImage = Image.new("RGB", (width,height))
        newPixels = newImage.load()
        
        if imageAnswer.lower() == 'negative':
            for x in range(width):
                for y in range(height):
                    colors = list(pixels[x,y])
                    r = colors[0]
                    g = colors[1]
                    b = colors[2]
                    newPixels[x,y] = (255-r,255-g,255-b)
            newImage.show()
        
        elif (imageAnswer.lower() == 'flipy'):
            for x in range(width):
                for y in range(height):
                    colors = list(pixels[x,y])
                    r = colors[0]
                    g = colors[1]
                    b = colors[2]
                    newPixels[x, y] = pixels[x,height-1-y]
            newImage.show()
        
        elif (imageAnswer.lower() == 'flipx'):
            for x in range(width):
                for y in range(height):
                    colors = list(pixels[x,y])
                    r = colors[0]
                    g = colors[1]
                    b = colors[2]
                    newPixels[x, y] = pixels[width-1-x, y]
            newImage.show()
        
        elif (imageAnswer.lower() == 'darken'):
            for x in range(width):
                for y in range(height):
                    colors = list(pixels[x,y])
                    r = colors[0]
                    g = colors[1]
                    b = colors[2]
                    if(r>=155 and g>=155 and b>=155):
                        newPixels[x, y] = (0, 0, 0)
                    else:
                        newPixels[x, y] = (r, g, b)
            newImage.show()
        
        elif (imageAnswer.lower() == 'lighten'):
            for x in range(width):
                for y in range(height):
                    colors = list(pixels[x,y])
                    r = colors[0]
                    g = colors[1]
                    b = colors[2]
                    if(r<=100 and g<=100 and b<=100):
                        newPixels[x, y] = (255, 255, 255)
                    else:
                        newPixels[x, y] = (r, g, b)
            newImage.show()
        
        else:
            print('We do not support the given edit function.')
        answerImg2 = str(input('Would you like to try and edit the image again? '))