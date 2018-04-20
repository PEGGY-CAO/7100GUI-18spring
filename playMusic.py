import pygame, sys
from pygame.locals import *
import time

import tkinter, tkFileDialog
import json
import datetime
from collections import OrderedDict

root = tkinter.Tk()
filez = tkFileDialog.askopenfilenames(parent=root, title='Choose a file')
fileList = root.tk.splitlist(filez)
numOfSong = len(fileList)

data = {}
writeToFile = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.json'
pygame.init()

width = 800
height = 500
button_width = 80
button_height = 30
margin = 30
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Designed for EEG experiments")
background_colour = (255, 255, 255) # white
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
grey = (110, 110, 110)

# # three button
# pygame.draw.rect(window, blue, [120, 140 + margin, button_width, button_height])
# pygame.draw.rect(window, green, [120, 200 + margin, button_width, button_height])
# pygame.draw.rect(window, red, [400, 140 + margin, button_width, button_height])
# initial music module
pygame.mixer.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 26)
myfont1 = pygame.font.SysFont('Comic Sans MS', 20)

#pygame.mixer.music.play(0, 0.0)
pygame.display.flip()


grid = 20





def firstPage():
    window.fill(background_colour)
    global music_pause, music_playing, first_page
    pygame.draw.circle(window, grey, (width / 2, height / 2), height / 4, 2)
    playTriangle = [[width / 2 - width / 16, height / 3], [width / 2 - width / 16, height / 3 * 2], [width / 2 + width / 14 + grid, height / 2]]
    pygame.draw.polygon(window, grey, playTriangle)
    playbox = pygame.Rect(width / 2 - width / 16, height / 3, width / 6, height / 3)

    data[title[-1]] = []
    #draw text
    titleforsong = myfont.render('music\'s name: ' + title[-1], True, black)
    textsurface = myfont.render('Press the button for playing music', True, black)
    # textGreenB = myfont.render('Press the green button to pause or unpause.', True, black)
    # textPrompt = myfont.render('Press the red button when finished listening.', True, black)
    textsurface1 = myfont.render('Press space bar as long as you are intrigued by the music.', False, black)
    textsurface2 = myfont.render('Press stop to go next.', False, black)
    window.blit(titleforsong, (0, 0))
    # window.blit(textGreenB, (0, 33))
    # window.blit(textPrompt, (0, 66))
    window.blit(textsurface, (0, 33))
    window.blit(textsurface1, (0, 66))
    window.blit(textsurface2, (0, 99))
    timeText = myfont1.render('Time:', True, (0, 0, 0))
    window.blit(timeText, (width / 4 * 3, height / 4))

    numOfSpace = 0

    while first_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playbox.collidepoint(event.pos):
                    if not music_playing:
                        pygame.draw.rect(window, background_colour, playbox, 0)
                        long = height / 4
                        pygame.draw.rect(window, grey, [width / 2 - long / 2, height / 2 - long / 2, long, long], 0)
                        pygame.mixer.music.play(0, 0)
                        music_playing = True
                        now = datetime.datetime.now()
                        dateandtime = now.strftime("%Y-%m-%d %H:%M")
                        print(dateandtime)
                        data[title[-1]].append({
                            'date and time': dateandtime
                        })
                    else:
                        pygame.mixer.music.stop()
                        first_page = False
                    # if music_playing:
                    # active = True
                    # color_textbox = color_active

                #print(event.pos)
                # if 120 < event.pos[0] < (120 + button_width) and 140 + margin < event.pos[1] < (140 + button_height + margin):
                #     if music_playing:
                #         pygame.mixer.music.play(-1, 0)
                #         #pygame.mixer.music.set_pos(5)
                #         # time.sleep(5)
                #         # pygame.mixer.music.pause()
                #         # pygame.mixer.music.play(-1, 50)
                #         music_playing = False
                #     else:
                #         pygame.mixer.music.stop()
                #         #pygame.mixer.music.unpause()
                #         music_playing = True
                # if 120 < event.pos[0] < (120 + button_width) and 200 + margin < event.pos[1] < (200 + button_height + margin):
                #     if music_pause:
                #         pygame.mixer.music.unpause()
                #         music_pause = False
                #     else:
                #         pygame.mixer.music.pause()
                #         music_pause = True
                #
                # # turn into a new page
                # if 400 < event.pos[0] < (400 + button_width) and 140 + margin < event.pos[1] < (140 + button_height + margin):
                #     first_page = False
            elif event.type ==KEYDOWN:

                if event.key == K_SPACE:
                    numOfSpace = numOfSpace + 1
                    #print(numOfSpace)
                    #print("space bar")
                    #print(pygame.mixer.music.get_pos()/10)
                    t = float(pygame.mixer.music.get_pos()/10)/100
                    timeString = myfont1.render(str(t), True, (0, 0, 0))
                    window.blit(timeString, (width / 4 * 3, height / 4 + numOfSpace * margin))
                    timeList.append(t)
                    print(timeList)

        pygame.display.flip()


# def second_page():
#     # global timeList
#     l = len(timeList)
#     #print(len(timeList))
#     window.fill(background_colour)
#     pos = 'Positive'
#     neu = 'Neutral'
#     neg = 'Negative'
#     myfont2 = pygame.font.SysFont('Comic Sans MS', 20)
#     myfont2S = pygame.font.SysFont('Comic Sans MS', 15)
#     page2text0 = myfont2.render('There are ' + str(len(timeList)) + ' markers in total.', True, (0, 0, 0))
#     page2text = myfont2.render('Check each box according to your feeling when hear it.', False, (0, 0, 0))
#     window.blit(page2text0, (0, 0))
#     window.blit(page2text, (0, margin))
#
#     page2pos = myfont2S.render(pos, False, black)
#     page2neu = myfont2S.render(neu, False, black)
#     page2neg = myfont2S.render(neg, False, black)
#
#     lineSeg = 3
#     # draw for user
#     for i in range(l):
#         pointTriangle = [[width / 8, margin * (i + 2)], [width / 8, margin * (i + 2) + grid],
#                          [width / 8 + grid, margin * (i + 2) + grid / 2]]
#         pygame.draw.polygon(window, red, pointTriangle)
#         pygame.draw.rect(window, black, (width / 4, margin * (i + 2), grid, grid), lineSeg)
#         window.blit(page2pos, (width / 4 + margin, margin * (i + 2)))
#         pygame.draw.rect(window, black, (width / 2, margin * (i + 2), grid, grid), lineSeg)
#         window.blit(page2neu, (width / 2 + margin, margin * (i + 2)))
#         pygame.draw.rect(window, black, (width / 4 * 3, margin * (i + 2), grid, grid), lineSeg)
#         window.blit(page2neg, (width / 4 * 3 + margin, margin * (i + 2)))
#     pygame.display.flip()
#     while True:
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 start = time.clock()
#                 print(start)
#                 x = event.pos[0] * 8 / width
#                 y = event.pos[1] / margin - 2
#                 print(x)
#                 print(y)
#                 if x == 1:
#                     print(timeList[y])
#                     pygame.mixer.music.stop()
#                     pygame.mixer.music.play(0, 0)
#                     if timeList[0] < 5:
#                         pygame.mixer.music.play(0, 0)
#                     else:
#                     #pygame.mixer.music.rewind()
#                         pygame.mixer.music.play(-1, timeList[y] - 5)
#                     #print(pygame.mixer.music.get_pos())
#                     time.sleep(5)
#                     pygame.mixer.music.stop()
#                     # if time.clock() - start >= 5:
#                     #     pygame.mixer.music.stop()

checkboxText = ['Idea', 'Reflection', 'Insight', 'Cringe']


def checkbox(n):
    myfont0 = pygame.font.SysFont('Comic Sans MS', 18)
    for i in range(n):
        checkbox = pygame.Rect(margin * 4 + 150 * i, margin * 6, grid, grid)
        pygame.draw.rect(window, black, checkbox, 2)
        page2checktext = myfont0.render(checkboxText[i], True, (0, 0, 0))
        window.blit(page2checktext, (margin * 5 + 150 * i, margin * 6))
        #input_box = pygame.Rect(width / 4, margin * 4, width / 2, margin)


def nextPage(i):
    clock = pygame.time.Clock()
    l = len(timeList)
    window.fill(background_colour)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 20)
    myfont0 = pygame.font.SysFont('Comic Sans MS', 18)
    # draw title
    page2text0 = myfont2.render('Marking ' + str(i + 1) + ' / ' + str(l) + ': ', True, (0, 0, 0))
    window.blit(page2text0, (margin, margin))
    #draw play button
    pointTriangle = [[width / 2, margin], [width / 2, margin + grid], [width / 2 + grid, margin + grid / 2]]
    pygame.draw.polygon(window, red, pointTriangle)
    #draw "when" text
    page2text1 = myfont2.render('When?', True, (0, 0, 0))
    window.blit(page2text1, (width / 2 - margin, margin * 3))
    #draw input textbox
    input_box = pygame.Rect(width / 4, margin * 4, width / 2, margin)
    active = False
    color_inactive = black
    color_active = (0, 255, 255)
    color_textbox = color_inactive
    text = ''
    #draw "what" text
    page2text2 = myfont2.render('What?', True, (0, 0, 0))
    window.blit(page2text2, (width / 2 - margin, margin * 5))
    #pygame.draw.rect(window, black, input_box, 2)
    #pygame.draw.rect(window, black, (width / 4, margin * (i + 4), width / 2, margin), 2)
    #draw Next button and text
    nextX = width - button_width - margin
    nextY = height - button_height - margin
    pygame.draw.rect(window, blue, [nextX, nextY, button_width, button_height])
    buttonnext = myfont0.render('Next', True, (0, 0, 0))
    window.blit(buttonnext, (nextX + grid, nextY))
    # draw checkbox
    checkbox(4)
    # prepare for checkbox's check or not, 0 = unchecked
    checklist = [False, False, False, False]
    # draw Feeling text for radio box
    page2text3 = myfont2.render('Feeling?', True, (0, 0, 0))
    window.blit(page2text3, (width / 2 - margin, margin * 7))
    radioTextList = ['Negative', 'Neutral', 'Positive']
    for j in range(3):
        radioText = myfont0.render(radioTextList[j], True, black)
        window.blit(radioText, (width / 4 * (j + 1), margin * 8))
        pygame.draw.circle(window, black, (width / 4 * (j + 1) - grid, margin * 8 + margin / 2), 10, 2)
    radioList = [0, 0, 0]
    # draw Strength text for radio box
    page2text4 = myfont2.render('Strength?', True, (0, 0, 0))
    window.blit(page2text4, (width / 2 - margin, margin * 9))
    radioTextList2 = ['Little', 'Medium', 'A lot']
    for j in range(3):
        radioText = myfont0.render(radioTextList2[j], True, black)
        window.blit(radioText, (width / 4 * (j + 1), margin * 10))
        pygame.draw.circle(window, black, (width / 4 * (j + 1) - grid, margin * 10 + margin / 2), 10, 2)
    radioList2 = [0, 0, 0]
    # draw Describe text
    page2text5 = myfont2.render('Describe: (Why?)', True, (0, 0, 0))
    window.blit(page2text5, (width / 2 - margin, margin * 11))
    # draw textbox2
    input_box2 = pygame.Rect(width / 4, margin * 12, width / 2, margin)
    activetwo = False
    color_textbox2 = color_inactive
    text2 = ''


    nextP = True
    while nextP:
        pygame.draw.rect(window, color_textbox, input_box, 2)
        pygame.draw.rect(window, color_textbox2, input_box2, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print(x)
                # for input box
                if input_box.collidepoint(event.pos):
                    active = True
                    color_textbox = color_active
                else:
                    active = False
                    color_textbox = color_inactive
                if input_box2.collidepoint(event.pos):
                    activetwo = True
                    color_textbox2 = color_active
                else:
                    activetwo = False
                    color_textbox2 = color_inactive
                # for "Play" button
                if width / 2 < event.pos[0] < width / 2 + grid and margin < event.pos[1] < margin + grid:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(0, 0)
                    if timeList[0] < 5:
                        pygame.mixer.music.play(0, 0)
                    else:
                        # pygame.mixer.music.rewind()
                        pygame.mixer.music.play(-1, timeList[i] - 5)
                    # print(pygame.mixer.music.get_pos())
                    time.sleep(5)
                    pygame.mixer.music.stop()
                # for "Next" button to next page
                elif nextX < event.pos[0] < (nextX + button_width) and nextY < event.pos[1] < (nextY + button_height):
                    nextP = False
                #elif width / 2 < event.pos[0] < width / 2 + grid and margin < event.pos[1] < margin + grid:

                #for checkbox
                if margin * 6 < event.pos[1] < margin * 6 + grid: # y are in this range
                    x = (event.pos[0] - margin * 4) / 150
                    if not checklist[x]:
                        start_x1 = margin * 4 + 150 * x + 5
                        start_y1 = margin * 6 + 5
                        end_x1 = margin * 4 + 150 * x + grid - 5
                        end_y1 = margin * 6 + grid - 5
                        start_x2 = end_x1
                        start_y2 = start_y1
                        end_x2 = start_x1
                        end_y2 = end_y1
                        pygame.draw.line(window, black, (start_x1, start_y1), (end_x1, end_y1), 2)
                        pygame.draw.line(window, black, (start_x2, start_y2), (end_x2, end_y2), 2)
                        print(event.pos)
                        checklist[x] = True
                    else:
                        pygame.draw.rect(window, background_colour, [margin * 4 + 150 * x + 4, margin * 6 + 4, grid - 6, grid - 6])
                        checklist[x] = False
                        print(checklist)

                # for radio box
                if margin * 8 < event.pos[1] < margin * 8 + grid: # y are in this range
                    print(event.pos)
                    feelingNumber = (event.pos[0] + margin) * 4 / width - 1
                    # 0 for Negative, 1 for Neutral, 2 for Positive
                    print(feelingNumber)
                    if feelingNumber == 0:
                        radioList[feelingNumber] = 1
                        radioList[1] = 0
                        radioList[2] = 0
                    elif feelingNumber == 1:
                        radioList[feelingNumber] = 1
                        radioList[0] = 0
                        radioList[2] = 0
                    else:
                        radioList[feelingNumber] = 1
                        radioList[0] = 0
                        radioList[1] = 0

                # for radio box2
                if margin * 10 < event.pos[1] < margin * 10 + grid:  # y are in this range
                    print(event.pos)
                    strengthNumber = (event.pos[0] + margin) * 4 / width - 1
                    # 0 for Little, 1 for Medium, 2 for A lot
                    #print(feelingNumber)
                    if strengthNumber == 0:
                        radioList2[strengthNumber] = 1
                        radioList2[1] = 0
                        radioList2[2] = 0
                    elif strengthNumber == 1:
                        radioList2[strengthNumber] = 1
                        radioList2[0] = 0
                        radioList2[2] = 0
                    else:
                        radioList2[strengthNumber] = 1
                        radioList2[0] = 0
                        radioList2[1] = 0

            #read text
            elif event.type == pygame.KEYDOWN:
                char = chr(event.key)
                print(char)
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        # text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        pygame.draw.rect(window, background_colour,
                                         [width / 4 + 2, margin * 4 + 2, width / 2 - 4, margin - 4], 0)
                        text = text[:-1]
                    else:
                        text += char
                if activetwo:
                    if event.key == pygame.K_RETURN:
                        print(text2)
                        # text2 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        pygame.draw.rect(window, background_colour, [width / 4 + 2, margin * 12 + 2, width / 2 - 4, margin - 4], 0)
                        text2 = text2[:-1]
                    else:
                        text2 += char
        #show text for question 1
        page2Answer1 = myfont0.render(text, True, (0, 0, 0))
        window.blit(page2Answer1, (width / 4 + 5, margin * 4 + 5))

        # show text for question 2
        page2Answer2 = myfont0.render(text2, True, (0, 0, 0))
        window.blit(page2Answer2, (width / 4 + 5, margin * 12 + 5))

        #print(radioList)
        #draw radio box - checked/unchecked
        for r in range(3):
            if radioList[r] == 0:
                pygame.draw.rect(window, background_colour, [width / 4 * (r + 1) - grid - 2, margin * 8 + margin / 2 - 2, 4, 4])
            else:
                pygame.draw.circle(window, black, (width / 4 * (r + 1) - grid, margin * 8 + margin / 2), 2 * radioList[r], 0)
        for rl in range(3):
            if radioList2[rl] == 0:
                pygame.draw.rect(window, background_colour, [width / 4 * (rl + 1) - grid - 2, margin * 10 + margin / 2 - 2, 4, 4])
            else:
                pygame.draw.circle(window, black, (width / 4 * (rl + 1) - grid, margin * 10 + margin / 2), 2 * radioList2[rl], 0)
        pygame.display.flip()
        clock.tick(30)

    checklistToWrite = []
    for numOfT in range(4):
        if checklist[numOfT]:
            checklistToWrite.append(checkboxText[numOfT])
    print(checklistToWrite)

    d = OrderedDict({
        timeList[i]: {
            "When": text,
            "What": checklistToWrite,
            "Feeling": radioTextList[feelingNumber],
            "Strength": radioTextList2[strengthNumber],
            "Why": text2
        }
    })

    data[title[-1]].append(d)
    with open(writeToFile, 'w')as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


def takeabreak():
    window.fill(background_colour)
    myfont0 = pygame.font.SysFont('Comic Sans MS', 18)
    # draw text
    textsur = myfont.render('Take a break', False, black)
    textsur1 = myfont.render('Press next when ready for next song', False, black)
    window.blit(textsur, (width / 3, height / 3))
    window.blit(textsur1, (width / 4, height / 3 + margin))
    # draw Next button and text
    nextX = width - button_width - margin
    nextY = height - button_height - margin
    pygame.draw.rect(window, blue, [nextX, nextY, button_width, button_height])
    buttonnextb = myfont0.render('Next', True, (0, 0, 0))
    window.blit(buttonnextb, (nextX + grid, nextY))

    pygame.display.flip()
    readytogo = True
    while readytogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if nextX < event.pos[0] < (nextX + button_width) and nextY < event.pos[1] < (nextY + button_height):
                    readytogo = False


def generatePage():
    pages = len(timeList)
    for i in range(pages):
        nextPage(i)


#initialAll()
for numofs in range(numOfSong):

    file = fileList[numofs]
    title = file.split('/')
    print(title[-1])
    pygame.mixer.music.load(file)
    first_page = True

    timeList = []
    music_playing = False
    music_pause = False

    firstPage()
    generatePage()
    if numofs < numOfSong - 1:
        takeabreak()
# second_page()
