import pygame
import random
from Button import Button,text1,Color_button,Image_button,blue_button

upper = []
outer = []
bottom = []
shoe = []
rando={'command':""}
tempo={'command':"",'parts':"",'type':"",'color':''}




screen = pygame.display.set_mode((504, 780))
pygame.display.set_caption("Fashionism")
list=["While shopping, always buy the basic item not the trending one!",
      "Try new color blocking method everyday",
      "Never wear crocs in any circumstances :)"]
probablity=random.randint(0,len(list)-1)
tips=str(list[probablity])

# for i in range(0,len(upper)-1):
#     print(upper[i].type,upper[i].color)


pygame.init()

class Cloth():
    def __init__(self, type, color):
        self.type = type
        self.color = color


def read():
    file = open("Upper.txt", "r")
    for row in file:
        variable = row.split(",")
        upper.append(Cloth(variable[0], variable[1]))
    file.close()
    out = open("outer.txt", "r")
    for row in out:
        variable = row.split(",")
        outer.append(Cloth(variable[0], variable[1]))

    out.close()
    pant = open("pants.txt", "r")
    for row in pant:
        variable = row.split(",")

        bottom.append(Cloth(variable[0], variable[1]))
    pant.close()


    shoee = open("shoes.txt", "r")
    for row in shoee:
        variable = row.split(",")

        shoe.append(Cloth(variable[0], variable[1]))
    shoee.close()

def randomized_each():
    probability = random.randint(0, len(upper) - 1)
    u = upper[probability].color[:len(upper[probability].color)-1] + " " + upper[probability].type

    probability1 = random.randint(0, len(outer) - 1)
    o = outer[probability1].color[:len(outer[probability1].color)-1] + " " + outer[probability1].type

    probability2 = random.randint(0, len(bottom) - 1)
    b = bottom[probability2].color[:len(bottom[probability2].color)-1] + " " + bottom[probability2].type

    probability3 = random.randint(0, len(shoe) - 1)
    s = shoe[probability3].color[:len(shoe[probability3].color)-1] + " " + shoe[probability3].type
    dicttu = {'top': u,'outer': o,'bottom': b,'shoes': s}
    return dicttu

def write():
    if tempo["parts"]=="upper" and tempo['command']=='append':
        temp=""
        file= open("Upper.txt","w")
        for row in upper:
            temp+=row.type+","+row.color
        temp+= '\n'

        file.write(temp)
        file.close()
    elif tempo["parts"]=="outer" and tempo['command']=='append':
        temp=""
        file= open("outer.txt","w")
        for row in outer:
            temp+=row.type+","+row.color
        temp+= '\n'

        file.write(temp)
        file.close()
    elif tempo['parts']=="bottom" and tempo['command']=='append':
        temp=""
        file= open("pants.txt","w")
        for row in bottom:
            temp+=row.type+","+row.color
        temp+= '\n'
        file.write(temp)
        file.close()
    elif tempo['parts']=="shoes" and tempo['command']=='append':
        temp=""
        file= open("shoes.txt","w")
        for row in shoe:
            temp+=row.type+","+row.color
        temp+= '\n'
        file.write(temp)
        file.close()

def randomized():
    if rando["command"]=="pure":
        tmp = {"u": "", "o": "", "b": "", "s": ""}
        while True:
            probability = random.randint(0, len(upper) - 1)
            u = (upper[probability].color[:len(upper[probability].color) - 1] + " " + upper[probability].type)
            if 'Shirt' in u or 'Polo Shirt' in u:
                tmp["u"] = "shirt"
                break
            elif 'T-Shirt' in u or 'Long-Sleeve T' in u:
                tmp["u"] = "tshirt"
                break
            elif 'Hoodie' in u or "Sweater" in u:
                tmp["u"] = 'hoodie'
                break

        while True:
            probability1 = random.randint(0, len(outer) - 1)
            o = (outer[probability1].color[:len(outer[probability1].color) - 1] + " " + outer[probability1].type)
            if tmp["u"] == "shirt":
                if "flannel" in o or "sport jacket" in o or 'zipped hoodie' in o:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "hoodie":
                if "zipped hoodie" in o:
                    print("", end="")
                else:
                    break
            else:
                break

        while True:
            probability2 = random.randint(0, len(bottom) - 1)
            b = (bottom[probability2].color[:len(bottom[probability2].color) - 1] + " " + bottom[probability2].type)
            if tmp["u"] == "shirt":
                if "jogger" in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "tshirt":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "hoodie":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
        while True:
            probability3 = random.randint(0, len(shoe) - 1)
            s = (shoe[probability3].color[:len(shoe[probability3].color) - 1] + " " + shoe[probability3].type)
            if tmp["u"] == "shirt":
                if "sports shoes" in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "tshirt":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "hoodie":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break
        while True:

                dictt = {'top': u, 'jacket': o, 'pants': b, 'shoes': s}
                return dictt
    elif rando['command'] == 'formal':
        tmp = {"u": "", "o": "", "b": "", "s": ""}
        while True:
            probability = random.randint(0, len(upper) - 1)
            u = (upper[probability].color[:len(upper[probability].color) - 1] + " " + upper[probability].type)
            if 'Shirt' in u or 'Polo Shirt' in u:
                tmp["u"] = "shirt"
                break
            elif 'T-Shirt' in u or 'Long-Sleeve T' in u:
                print("",end="")

            elif 'Hoodie' in u or "Sweater" in u:
                print("",end="")


        while True:
            probability1 = random.randint(0, len(outer) - 1)
            o = (outer[probability1].color[:len(outer[probability1].color) - 1] + " " + outer[probability1].type)
            if tmp["u"] == "shirt":
                if "flannel" in o or "sport jacket" in o or 'zipped hoodie' in o:
                    print("", end="")
                else:
                    break

            else:
                break

        while True:
            probability2 = random.randint(0, len(bottom) - 1)
            b = (bottom[probability2].color[:len(bottom[probability2].color) - 1] + " " + bottom[probability2].type)
            if tmp["u"] == "shirt":
                if "jogger" in b or 'shorts' in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "tshirt":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "hoodie":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
        while True:
            probability3 = random.randint(0, len(shoe) - 1)
            s = (shoe[probability3].color[:len(shoe[probability3].color) - 1] + " " + shoe[probability3].type)
            if tmp["u"] == "shirt":
                if "sports shoes" in s or 'sneaker' in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "tshirt":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "hoodie":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break
        while True:
            dictt = {'top': u, 'jacket': o, 'pants': b, 'shoes': s}
            return dictt

    elif rando['command'] == 'casual':
        tmp = {"u": "", "o": "", "b": "", "s": ""}
        while True:
            probability = random.randint(0, len(upper) - 1)
            u = (upper[probability].color[:len(upper[probability].color) - 1] + " " + upper[probability].type)
            if 'Shirt' in u or 'Polo Shirt' in u:
                tmp["u"] = "shirt"
                break
            elif 'T-Shirt' in u or 'Long-Sleeve T' in u:
                tmp["u"] = "tshirt"
                break
            elif 'Hoodie' in u or "Sweater" in u:
                tmp["u"] = 'hoodie'
                break

        while True:
            probability1 = random.randint(0, len(outer) - 1)
            o = (outer[probability1].color[:len(outer[probability1].color) - 1] + " " + outer[probability1].type)
            if tmp["u"] == "shirt":
                if "flannel" in o or "sport jacket" in o or 'zipped hoodie' in o:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "hoodie":
                if "zipped hoodie" in o:
                    print("", end="")
                else:
                    break
            else:
                break

        while True:
            probability2 = random.randint(0, len(bottom) - 1)
            b = (bottom[probability2].color[:len(bottom[probability2].color) - 1] + " " + bottom[probability2].type)
            if tmp["u"] == "shirt":
                if "jogger" in b or 'trouser' in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "tshirt":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
            elif tmp["u"] == "hoodie":
                if 'trouser' in b:
                    print("", end="")
                else:
                    break
        while True:
            probability3 = random.randint(0, len(shoe) - 1)
            s = (shoe[probability3].color[:len(shoe[probability3].color) - 1] + " " + shoe[probability3].type)
            if tmp["u"] == "shirt":
                if "sports shoes" in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "tshirt":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break

            elif tmp["u"] == "hoodie":
                if 'dress shoes' in s or 'loafer' in s:
                    print("", end="")
                else:
                    break
        while True:
            dictt = {'top': u, 'jacket': o, 'pants': b, 'shoes': s}
            return dictt


    elif rando['command']=='sport':
        tmp = {"u": "", "o": "", "b": "", "s": ""}
        while True:
            probability = random.randint(0, len(upper) - 1)
            u = (upper[probability].color[:len(upper[probability].color) - 1] + " " + upper[probability].type)
            if 'Shirt' in u or 'Polo Shirt' in u:
                print("",end="")
            elif 'T-Shirt' in u or 'Long-Sleeve T' in u:
                tmp["u"] = "tshirt"
                break
            elif 'Hoodie' in u or "Sweater" in u:
                tmp["u"] = 'hoodie'
                break

        while True:
            probability1 = random.randint(0, len(outer) - 1)
            o = (outer[probability1].color[:len(outer[probability1].color) - 1] + " " + outer[probability1].type)
            if tmp["u"] == "hoodie":
                if "zipped hoodie" in o:
                    print("", end="")
                else:
                    break
            else:
                break

        while True:
            probability2 = random.randint(0, len(bottom) - 1)
            b = (bottom[probability2].color[:len(bottom[probability2].color) - 1] + " " + bottom[probability2].type)
            if "trouser" in b or "chino" in b or "jeans" in b:
                print("",end="")
            else:
                break
        while True:
            probability3 = random.randint(0, len(shoe) - 1)
            s = (shoe[probability3].color[:len(shoe[probability3].color) - 1] + " " + shoe[probability3].type)

            if "dress shoes" in s or "loafer" in s:
                print("",end="")
            else:
                break

        while True:
            dictt = {'top': u, 'jacket': o, 'pants': b, 'shoes': s}
            return dictt

def main_page():


    randomized_button= Button(screen,"RANDOMIZE",252,315)
    customized_button= Button(screen,"CUSTOMIZE",252,395)
    new_button= Button(screen,"INSERT NEW ITEM",252,475)
    delete_button = Button(screen, "DELETE ITEM", 252, 555)
    exit_button = Button(screen, "EXIT", 252, 635)
    tips_button = text1(screen,tips,252,715)
    run = True
    while run:

        background = pygame.image.load("background_main.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img,(0,0))

        randomized_button.draw_button()
        customized_button.draw_button()
        new_button.draw_button()
        delete_button.draw_button()
        exit_button.draw_button()
        tips_button.draw_button()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                randomized_button_hover=randomized_button.rect.collidepoint(mouse_x,mouse_y)
                customized_button_hover = customized_button.rect.collidepoint(mouse_x, mouse_y)
                new_button_hover = new_button.rect.collidepoint(mouse_x, mouse_y)
                delete_button_hover = delete_button.rect.collidepoint(mouse_x, mouse_y)
                exit_button_hover = exit_button.rect.collidepoint(mouse_x, mouse_y)
                if randomized_button_hover==True:
                    randomized_button.mouse_hover(screen,'RANDOMIZE OUTFIT!',252,315)
                if randomized_button_hover==False:
                    randomized_button.mouse_back(screen,'RANDOMIZE',252,315)
                if customized_button_hover == True:
                    customized_button.mouse_hover(screen,"CHOOSE OCCASION",252,395)
                if customized_button_hover == False:
                    customized_button.mouse_back(screen,"CUSTOMIZE",252,395)
                if new_button_hover==True:
                    new_button.mouse_hover(screen,"INSERT NEW ITEM",252,475)
                if new_button_hover==False:
                    new_button.mouse_back(screen,"INSERT NEW ITEM",252,475)
                if delete_button_hover==True:
                    delete_button.mouse_hover(screen, "DELETE ITEM", 252, 555)
                if delete_button_hover==False:
                    delete_button.mouse_back(screen, "DELETE ITEM", 252, 555)
                if exit_button_hover==True:
                    exit_button.mouse_hover(screen, "EXIT NOW?", 252, 635)
                if exit_button_hover==False:
                    exit_button.mouse_back(screen, "EXIT", 252, 635)


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                randomized_button_clicked= randomized_button.rect.collidepoint(mouse_x,mouse_y)
                customized_button_clicked = customized_button.rect.collidepoint(mouse_x, mouse_y)
                new_button_clicked = new_button.rect.collidepoint(mouse_x, mouse_y)
                delete_button_clicked = delete_button.rect.collidepoint(mouse_x, mouse_y)
                exit_button_clicked = exit_button.rect.collidepoint(mouse_x, mouse_y)
                if randomized_button_clicked==True:
                    randomized_button.sound.play()
                    run = False
                    rando["command"]="pure"
                    second_screen()

                if customized_button_clicked==True:
                    customized_button.sound.play()
                    customized()
                    pass
                if new_button_clicked==True:
                    new_button.sound.play()
                    tempo['command'] = 'append'
                    input_page()

                    run= False

                if delete_button_clicked==True:
                    delete_button.sound.play()
                    tempo['command'] = 'delete'
                    delete_page()
                    run=False


                if exit_button_clicked==True:
                    exit_button.sound.play()
                    exit()

                    pass

def second_screen():
    randomized()
    x=randomized()

    random_upper = Button(screen, x['top'], 320, 260)
    random_jacket = Button(screen, x['jacket'], 320, 370)
    random_pants = Button(screen, x['pants'], 320, 480)
    random_shoes = Button(screen, x['shoes'], 320, 590)
    re_randomized = Button(screen, "RE-RANDOMIZED", 140, 725)
    wear_this = blue_button(screen, "WEAR THIS", 380, 725)
    run2 = True
    while run2:
        randomized_each()
        y = randomized_each()
        s_page = pygame.image.load("second_page.png")
        screen.blit(s_page, (0, 0))
        random_upper.draw_button()
        random_jacket.draw_button()
        random_pants.draw_button()
        random_shoes.draw_button()
        re_randomized.draw_button()
        wear_this.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                random_upper_hover=random_upper.rect.collidepoint(mouse_x,mouse_y)
                random_jacket_hover = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_hover = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_hover = random_shoes.rect.collidepoint(mouse_x, mouse_y)
                re_randomized_hover = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_hover= wear_this.rect.collidepoint(mouse_x,mouse_y)
                if random_upper_hover==True:
                    random_upper.mouse_hover(screen, x['top'], 320, 260)
                if random_upper_hover==False:
                    random_upper.mouse_back(screen, x['top'], 320, 260)

                if random_jacket_hover== True:
                    random_jacket.mouse_hover(screen, x['jacket'], 320, 370)
                if random_jacket_hover == False:
                    random_jacket.mouse_back(screen, x['jacket'], 320, 370)

                if random_pants_hover==True:
                    random_pants.mouse_hover(screen, x['pants'], 320, 480)
                if random_pants_hover==False:
                    random_pants.mouse_back(screen, x['pants'], 320, 480)

                if random_shoes_hover==True:
                    random_shoes.mouse_hover(screen, x['shoes'], 320, 590)
                if random_shoes_hover==False:
                    random_shoes.mouse_back(screen, x['shoes'], 320, 590)

                if re_randomized_hover==True:
                    re_randomized.mouse_hover(screen, "RE-RANDOMIZED", 140, 725)
                if re_randomized_hover==False:
                    re_randomized.mouse_back(screen, "RE-RANDOMIZED", 140, 725)

                if  wear_this_hover==True:
                    wear_this.mouse_hover(screen, "MAIN MENU", 380, 725)
                if  wear_this_hover==False:
                    wear_this.mouse_back(screen, "WEAR THIS", 380, 725)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                re_randomized_button_clicked = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_clicked = wear_this.rect.collidepoint(mouse_x, mouse_y)
                random_upper_clicked = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_clicked = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_clicked = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_clicked = random_shoes.rect.collidepoint(mouse_x, mouse_y)

                if re_randomized_button_clicked == True:
                    re_randomized.sound.play()
                    second_screen()
                    run2 = False
                    pass
                if wear_this_clicked == True:
                    wear_this.sound.play()
                    main_page()
                    run2 = False
                if random_upper_clicked == True:
                    random_upper.sound.play()
                    random_upper = Button(screen, y['top'], 320, 260)
                    pass
                if random_jacket_clicked == True:
                    random_jacket.sound.play()
                    random_jacket = Button(screen, y['outer'], 320, 370)
                    pass
                if random_pants_clicked == True:
                    random_pants.sound.play()
                    random_pants = Button(screen, y['bottom'], 320, 480)
                    pass
                if random_shoes_clicked == True:
                    random_shoes.sound.play()
                    random_shoes = Button(screen, y['shoes'], 320, 590)
                    pass

def customized():


    formal_button= Button(screen,"FORMAL LOOK",252,315)

    casual_button= Button(screen,"STREET LOOK",252,475)

    sport_button = Button(screen, "SPORT LOOK", 252, 635)
    previous_page = Button(screen, "MAIN MENU", 380, 725)
    run = True
    while run:

        background = pygame.image.load("background_main.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img,(0,0))

        formal_button.draw_button()
        casual_button.draw_button()
        sport_button.draw_button()
        previous_page.draw_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                formal_button_hover=formal_button.rect.collidepoint(mouse_x,mouse_y)
                casual_button_hover = casual_button.rect.collidepoint(mouse_x, mouse_y)
                sport_button_hover = sport_button.rect.collidepoint(mouse_x, mouse_y)
                previous_page_hover = previous_page.rect.collidepoint(mouse_x, mouse_y)

                if formal_button_hover==True:
                    formal_button.mouse_hover(screen,"FORMAL LOOK",252,315)
                if formal_button_hover==False:
                    formal_button.mouse_back(screen,"FORMAL LOOK",252,315)
                if casual_button_hover == True:
                    casual_button.mouse_hover(screen,"STREET LOOK",252,475)
                if casual_button_hover == False:
                    casual_button.mouse_back(screen,"STREET LOOK",252,475)
                if sport_button_hover==True:
                    sport_button.mouse_hover(screen, "SPORT LOOK", 252, 635)
                if sport_button_hover==False:
                    sport_button.mouse_back(screen, "SPORT LOOK", 252, 635)
                if previous_page_hover==True:
                    previous_page.mouse_hover(screen, "MAIN MENU", 380, 725)
                if previous_page_hover==False:
                    previous_page.mouse_back(screen, "MAIN MENU", 380, 725)


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                formal_button_clicked= formal_button.rect.collidepoint(mouse_x,mouse_y)
                casual_button_clicked = casual_button.rect.collidepoint(mouse_x, mouse_y)
                sport_button_clicked = sport_button.rect.collidepoint(mouse_x, mouse_y)
                previous_page_clicked = previous_page.rect.collidepoint(mouse_x, mouse_y)

                if formal_button_clicked==True:
                    formal_button.sound.play()
                    rando["command"] = "formal"
                    formal_look()
                    run = False

                if casual_button_clicked==True:
                    casual_button.sound.play()
                    rando["command"] = "casual"
                    casual_look()
                    run=False

                if sport_button_clicked==True:
                    sport_button.sound.play()
                    rando["command"] = "sport"
                    sport_look()
                    run= False
                    pass
                if previous_page_clicked==True:
                    previous_page.sound.play()
                    main_page()
                    run=False

def formal_look():
    randomized()
    x = randomized()

    random_upper = Button(screen, x['top'], 320, 260)
    random_jacket = Button(screen, x['jacket'], 320, 370)
    random_pants = Button(screen, x['pants'], 320, 480)
    random_shoes = Button(screen, x['shoes'], 320, 590)
    re_randomized = Button(screen, "RE-RANDOMIZED", 140, 725)
    wear_this = blue_button(screen, "WEAR THIS", 380, 725)
    run2 = True
    while run2:
        randomized_each()
        y = randomized_each()
        s_page = pygame.image.load("second_page.png")
        screen.blit(s_page, (0, 0))
        random_upper.draw_button()
        random_jacket.draw_button()
        random_pants.draw_button()
        random_shoes.draw_button()
        re_randomized.draw_button()
        wear_this.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                random_upper_hover = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_hover = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_hover = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_hover = random_shoes.rect.collidepoint(mouse_x, mouse_y)
                re_randomized_hover = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_hover = wear_this.rect.collidepoint(mouse_x, mouse_y)
                if random_upper_hover == True:
                    random_upper.mouse_hover(screen, x['top'], 320, 260)
                if random_upper_hover == False:
                    random_upper.mouse_back(screen, x['top'], 320, 260)

                if random_jacket_hover == True:
                    random_jacket.mouse_hover(screen, x['jacket'], 320, 370)
                if random_jacket_hover == False:
                    random_jacket.mouse_back(screen, x['jacket'], 320, 370)

                if random_pants_hover == True:
                    random_pants.mouse_hover(screen, x['pants'], 320, 480)
                if random_pants_hover == False:
                    random_pants.mouse_back(screen, x['pants'], 320, 480)

                if random_shoes_hover == True:
                    random_shoes.mouse_hover(screen, x['shoes'], 320, 590)
                if random_shoes_hover == False:
                    random_shoes.mouse_back(screen, x['shoes'], 320, 590)

                if re_randomized_hover == True:
                    re_randomized.mouse_hover(screen, "RE-RANDOMIZED", 140, 725)
                if re_randomized_hover == False:
                    re_randomized.mouse_back(screen, "RE-RANDOMIZED", 140, 725)

                if wear_this_hover == True:
                    wear_this.mouse_hover(screen, "MAIN MENU", 380, 725)
                if wear_this_hover == False:
                    wear_this.mouse_back(screen, "WEAR THIS", 380, 725)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                re_randomized_button_clicked = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_clicked = wear_this.rect.collidepoint(mouse_x, mouse_y)
                random_upper_clicked = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_clicked = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_clicked = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_clicked = random_shoes.rect.collidepoint(mouse_x, mouse_y)

                if re_randomized_button_clicked == True:
                    re_randomized.sound.play()
                    formal_look()
                    run2 = False
                    pass
                if wear_this_clicked == True:
                    wear_this.sound.play()
                    customized()
                    run2 = False
                if random_upper_clicked == True:
                    random_upper.sound.play()
                    random_upper = Button(screen, y['top'], 320, 260)
                    pass
                if random_jacket_clicked == True:
                    random_jacket.sound.play()
                    random_jacket = Button(screen, y['outer'], 320, 370)
                    pass
                if random_pants_clicked == True:
                    random_pants.sound.play()
                    random_pants = Button(screen, y['bottom'], 320, 480)
                    pass
                if random_shoes_clicked == True:
                    random_shoes.sound.play()
                    random_shoes = Button(screen, y['shoes'], 320, 590)
                    pass

def casual_look():
    randomized()
    x = randomized()

    random_upper = Button(screen, x['top'], 320, 260)
    random_jacket = Button(screen, x['jacket'], 320, 370)
    random_pants = Button(screen, x['pants'], 320, 480)
    random_shoes = Button(screen, x['shoes'], 320, 590)
    re_randomized = Button(screen, "RE-RANDOMIZED", 140, 725)
    wear_this = blue_button(screen, "WEAR THIS", 380, 725)
    run2 = True
    while run2:
        randomized_each()
        y = randomized_each()
        s_page = pygame.image.load("second_page.png")
        screen.blit(s_page, (0, 0))
        random_upper.draw_button()
        random_jacket.draw_button()
        random_pants.draw_button()
        random_shoes.draw_button()
        re_randomized.draw_button()
        wear_this.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                random_upper_hover = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_hover = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_hover = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_hover = random_shoes.rect.collidepoint(mouse_x, mouse_y)
                re_randomized_hover = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_hover = wear_this.rect.collidepoint(mouse_x, mouse_y)
                if random_upper_hover == True:
                    random_upper.mouse_hover(screen, x['top'], 320, 260)
                if random_upper_hover == False:
                    random_upper.mouse_back(screen, x['top'], 320, 260)

                if random_jacket_hover == True:
                    random_jacket.mouse_hover(screen, x['jacket'], 320, 370)
                if random_jacket_hover == False:
                    random_jacket.mouse_back(screen, x['jacket'], 320, 370)

                if random_pants_hover == True:
                    random_pants.mouse_hover(screen, x['pants'], 320, 480)
                if random_pants_hover == False:
                    random_pants.mouse_back(screen, x['pants'], 320, 480)

                if random_shoes_hover == True:
                    random_shoes.mouse_hover(screen, x['shoes'], 320, 590)
                if random_shoes_hover == False:
                    random_shoes.mouse_back(screen, x['shoes'], 320, 590)

                if re_randomized_hover == True:
                    re_randomized.mouse_hover(screen, "RE-RANDOMIZED", 140, 725)
                if re_randomized_hover == False:
                    re_randomized.mouse_back(screen, "RE-RANDOMIZED", 140, 725)

                if wear_this_hover == True:
                    wear_this.mouse_hover(screen, "MAIN MENU", 380, 725)
                if wear_this_hover == False:
                    wear_this.mouse_back(screen, "WEAR THIS", 380, 725)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                re_randomized_button_clicked = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_clicked = wear_this.rect.collidepoint(mouse_x, mouse_y)
                random_upper_clicked = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_clicked = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_clicked = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_clicked = random_shoes.rect.collidepoint(mouse_x, mouse_y)

                if re_randomized_button_clicked == True:
                    re_randomized.sound.play()
                    casual_look()
                    run2 = False
                    pass
                if wear_this_clicked == True:
                    wear_this.sound.play()
                    customized()
                    run2 = False
                if random_upper_clicked == True:
                    random_upper.sound.play()
                    random_upper = Button(screen, y['top'], 320, 260)
                    pass
                if random_jacket_clicked == True:
                    random_jacket.sound.play()
                    random_jacket = Button(screen, y['outer'], 320, 370)
                    pass
                if random_pants_clicked == True:
                    random_pants.sound.play()
                    random_pants = Button(screen, y['bottom'], 320, 480)
                    pass
                if random_shoes_clicked == True:
                    random_shoes.sound.play()
                    random_shoes = Button(screen, y['shoes'], 320, 590)
                    pass

def sport_look():
    randomized()
    x = randomized()

    random_upper = Button(screen, x['top'], 320, 260)
    random_jacket = Button(screen, x['jacket'], 320, 370)
    random_pants = Button(screen, x['pants'], 320, 480)
    random_shoes = Button(screen, x['shoes'], 320, 590)
    re_randomized = Button(screen, "RE-RANDOMIZED", 140, 725)
    wear_this = blue_button(screen, "WEAR THIS", 380, 725)
    run2 = True
    while run2:
        randomized_each()
        y = randomized_each()
        s_page = pygame.image.load("second_page.png")
        screen.blit(s_page, (0, 0))
        random_upper.draw_button()
        random_jacket.draw_button()
        random_pants.draw_button()
        random_shoes.draw_button()
        re_randomized.draw_button()
        wear_this.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                random_upper_hover = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_hover = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_hover = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_hover = random_shoes.rect.collidepoint(mouse_x, mouse_y)
                re_randomized_hover = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_hover = wear_this.rect.collidepoint(mouse_x, mouse_y)
                if random_upper_hover == True:
                    random_upper.mouse_hover(screen, x['top'], 320, 260)
                if random_upper_hover == False:
                    random_upper.mouse_back(screen, x['top'], 320, 260)

                if random_jacket_hover == True:
                    random_jacket.mouse_hover(screen, x['jacket'], 320, 370)
                if random_jacket_hover == False:
                    random_jacket.mouse_back(screen, x['jacket'], 320, 370)

                if random_pants_hover == True:
                    random_pants.mouse_hover(screen, x['pants'], 320, 480)
                if random_pants_hover == False:
                    random_pants.mouse_back(screen, x['pants'], 320, 480)

                if random_shoes_hover == True:
                    random_shoes.mouse_hover(screen, x['shoes'], 320, 590)
                if random_shoes_hover == False:
                    random_shoes.mouse_back(screen, x['shoes'], 320, 590)

                if re_randomized_hover == True:
                    re_randomized.mouse_hover(screen, "RE-RANDOMIZED", 140, 725)
                if re_randomized_hover == False:
                    re_randomized.mouse_back(screen, "RE-RANDOMIZED", 140, 725)

                if wear_this_hover == True:
                    wear_this.mouse_hover(screen, "MAIN MENU", 380, 725)
                if wear_this_hover == False:
                    wear_this.mouse_back(screen, "WEAR THIS", 380, 725)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                re_randomized_button_clicked = re_randomized.rect.collidepoint(mouse_x, mouse_y)
                wear_this_clicked = wear_this.rect.collidepoint(mouse_x, mouse_y)
                random_upper_clicked = random_upper.rect.collidepoint(mouse_x, mouse_y)
                random_jacket_clicked = random_jacket.rect.collidepoint(mouse_x, mouse_y)
                random_pants_clicked = random_pants.rect.collidepoint(mouse_x, mouse_y)
                random_shoes_clicked = random_shoes.rect.collidepoint(mouse_x, mouse_y)

                if re_randomized_button_clicked == True:
                    re_randomized.sound.play()
                    sport_look()
                    run2 = False
                    pass
                if wear_this_clicked == True:
                    wear_this.sound.play()
                    customized()
                    run2 = False
                if random_upper_clicked == True:
                    random_upper.sound.play()
                    random_upper = Button(screen, y['top'], 320, 260)
                    pass
                if random_jacket_clicked == True:
                    random_jacket.sound.play()
                    random_jacket = Button(screen, y['outer'], 320, 370)
                    pass
                if random_pants_clicked == True:
                    random_pants.sound.play()
                    random_pants = Button(screen, y['bottom'], 320, 480)
                    pass
                if random_shoes_clicked == True:
                    random_shoes.sound.play()
                    random_shoes = Button(screen, y['shoes'], 320, 590)
                    pass

def input_page():
    upper_button = Button(screen, "UPPER", 252, 320)
    outer_button = Button(screen, "OUTER", 252, 420)
    bottom_button = Button(screen, "BOTTOM", 252, 520)
    shoes_button = Button(screen, "SHOES", 252, 620)
    main_menu_button = Button(screen, "MAIN MENU", 380, 725)
    run2 = True
    while run2:
        s_page = pygame.image.load("input-page.png")
        screen.blit(s_page, (0, 0))
        upper_button.draw_button()
        outer_button.draw_button()
        bottom_button.draw_button()
        shoes_button.draw_button()
        main_menu_button.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                upper_button_hover=upper_button.rect.collidepoint(mouse_x,mouse_y)
                outer_button_hover = outer_button.rect.collidepoint(mouse_x, mouse_y)
                bottom_button_hover = bottom_button.rect.collidepoint(mouse_x, mouse_y)
                shoes_button_hover = shoes_button.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_hover = main_menu_button.rect.collidepoint(mouse_x, mouse_y)
                if upper_button_hover==True:
                    upper_button.mouse_hover(screen, "INPUT UPPER", 252, 320)
                if upper_button_hover==False:
                    upper_button.mouse_back(screen, "UPPER", 252, 320)

                if outer_button_hover == True:
                    outer_button.mouse_hover(screen, "INPUT OUTER", 252, 420)
                if outer_button_hover == False:
                    outer_button.mouse_back(screen, "OUTER", 252, 420)

                if bottom_button_hover==True:
                    bottom_button.mouse_hover(screen, "INPUT BOTTOM", 252, 520)
                if bottom_button_hover==False:
                    bottom_button.mouse_back(screen, "BOTTOM", 252, 520)

                if shoes_button_hover==True:
                    shoes_button.mouse_hover(screen, "INPUT SHOES", 252, 620)
                if shoes_button_hover==False:
                    shoes_button.mouse_back(screen, "SHOES", 252, 620)

                if main_menu_button_hover==True:
                    main_menu_button.mouse_hover(screen, "EXIT NOW?", 380, 725)
                if main_menu_button_hover==False:
                    main_menu_button.mouse_back(screen, "MAIN MENU", 380, 725)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                upper_button_clicked = upper_button.rect.collidepoint(mouse_x, mouse_y)
                outer_button_clicked = outer_button.rect.collidepoint(mouse_x, mouse_y)
                bottom_button_clicked = bottom_button.rect.collidepoint(mouse_x, mouse_y)
                shoes_button_clicked = shoes_button.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_clicked = main_menu_button.rect.collidepoint(mouse_x, mouse_y)

                if upper_button_clicked == True:
                    upper_button.sound.play()
                    tempo['parts']="upper"
                    input_upper()
                    run2=False


                if outer_button_clicked == True:
                    outer_button.sound.play()
                    tempo['parts'] = "outer"
                    input_outer()
                    run2 = False
                if bottom_button_clicked == True:
                    bottom_button.sound.play()
                    tempo['parts'] = "bottom"
                    input_bottom()
                    run2= False

                if shoes_button_clicked == True:
                    shoes_button.sound.play()
                    tempo['parts'] = "shoes"
                    input_shoes()
                    run2 = False

                if main_menu_button_clicked == True:
                    main_menu_button.sound.play()
                    main_page()
                    tempo['command']="append"
                    run2 = False

def delete_page():
    upper_button = Button(screen, "UPPER", 252, 320)
    outer_button = Button(screen, "OUTER", 252, 420)
    bottom_button = Button(screen, "BOTTOM", 252, 520)
    shoes_button = Button(screen, "SHOES", 252, 620)
    main_menu_button = Button(screen, "MAIN MENU", 380, 725)
    run2 = True
    while run2:
        s_page = pygame.image.load("delete-page.png")
        screen.blit(s_page, (0, 0))
        upper_button.draw_button()
        outer_button.draw_button()
        bottom_button.draw_button()
        shoes_button.draw_button()
        main_menu_button.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                upper_button_hover = upper_button.rect.collidepoint(mouse_x, mouse_y)
                outer_button_hover = outer_button.rect.collidepoint(mouse_x, mouse_y)
                bottom_button_hover = bottom_button.rect.collidepoint(mouse_x, mouse_y)
                shoes_button_hover = shoes_button.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_hover = main_menu_button.rect.collidepoint(mouse_x, mouse_y)
                if upper_button_hover == True:
                    upper_button.mouse_hover(screen, "DELETE UPPER?", 252, 320)
                if upper_button_hover == False:
                    upper_button.mouse_back(screen, "UPPER", 252, 320)
                if outer_button_hover == True:
                    outer_button.mouse_hover(screen, "DELETE OUTER?", 252, 420)
                if outer_button_hover == False:
                    outer_button.mouse_back(screen, "OUTER", 252, 420)
                if bottom_button_hover == True:
                    bottom_button.mouse_hover(screen, "DELETE BOTTOM?", 252, 520)
                if bottom_button_hover == False:
                    bottom_button.mouse_back(screen, "BOTTOM", 252, 520)
                if shoes_button_hover == True:
                    shoes_button.mouse_hover(screen, "DELETE SHOES?", 252, 620)
                if shoes_button_hover == False:
                    shoes_button.mouse_back(screen, "SHOES", 252, 620)
                if main_menu_button_hover == True:
                    main_menu_button.mouse_hover(screen, "EXIT NOW?", 380, 725)
                if main_menu_button_hover == False:
                    main_menu_button.mouse_back(screen, "MAIN MENU", 380, 725)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                upper_button_clicked = upper_button.rect.collidepoint(mouse_x, mouse_y)
                outer_button_clicked = outer_button.rect.collidepoint(mouse_x, mouse_y)
                bottom_button_clicked = bottom_button.rect.collidepoint(mouse_x, mouse_y)
                shoes_button_clicked = shoes_button.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_clicked = main_menu_button.rect.collidepoint(mouse_x, mouse_y)

                if upper_button_clicked == True:
                    upper_button.sound.play()
                    tempo['parts']='upper'
                    input_upper()
                    run2 = False

                if outer_button_clicked == True:
                    outer_button.sound.play()
                    tempo['parts'] = 'outer'
                    input_outer()
                    run2 = False
                if bottom_button_clicked == True:
                    bottom_button.sound.play()
                    tempo['parts'] = 'bottom'
                    input_bottom()
                    run2=False
                if shoes_button_clicked == True:
                    shoes_button.sound.play()
                    tempo['parts'] = 'shoes'
                    input_shoes()
                    run2 = False

                if main_menu_button_clicked == True:
                    main_menu_button.sound.play()
                    main_page()
                    run2 = False

def input_upper():

    TShirt_button= Button(screen,"T-Shirt",252,240)
    Shirt_button= Button(screen,"Shirt",252,320)
    Polo_shirt_button= Button(screen,"Polo Shirt",252,400)
    Long_Sleeve_button = Button(screen, "Long-Sleeve T", 252, 480)
    Sweater_button = Button(screen, "Sweater", 252, 560)
    Hoodie_button = Button(screen,"Hoodie",252,640)
    previous_button =Button(screen,"PREVIOUS PAGE",380,725)
    run = True
    while run:

        background = pygame.image.load("background_input.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img,(0,0))
        TShirt_button.draw_button()
        Shirt_button.draw_button()
        Polo_shirt_button.draw_button()
        Long_Sleeve_button.draw_button()
        Sweater_button.draw_button()
        Hoodie_button.draw_button()
        previous_button.draw_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                TShirt_button_hover = TShirt_button.rect.collidepoint(mouse_x, mouse_y)
                Shirt_button_hover = Shirt_button.rect.collidepoint(mouse_x, mouse_y)
                Polo_shirt_button_hover = Polo_shirt_button.rect.collidepoint(mouse_x, mouse_y)
                Long_Sleeve_button_hover=Long_Sleeve_button.rect.collidepoint(mouse_x,mouse_y)
                Sweater_button_hover = Sweater_button.rect.collidepoint(mouse_x, mouse_y)
                Hoodie_button_hover = Hoodie_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_hover = previous_button.rect.collidepoint(mouse_x, mouse_y)
                if TShirt_button_hover == True:
                    TShirt_button.mouse_hover(screen,"T-Shirt",252,240)
                if TShirt_button_hover == False:
                    TShirt_button.mouse_back(screen,"T-Shirt",252,240)
                if Shirt_button_hover == True:
                    Shirt_button.mouse_hover(screen,"Shirt",252,320)
                if Shirt_button_hover == False:
                    Shirt_button.mouse_back(screen,"Shirt",252,320)
                if Polo_shirt_button_hover == True:
                    Polo_shirt_button.mouse_hover(screen,"Polo Shirt",252,400)
                if Polo_shirt_button_hover == False:
                    Polo_shirt_button.mouse_back(screen,"Polo Shirt",252,400)
                if Long_Sleeve_button_hover == True:
                    Long_Sleeve_button.mouse_hover(screen, "Long-Sleeve T", 252, 480)
                if Long_Sleeve_button_hover == False:
                    Long_Sleeve_button.mouse_back(screen, "Long-Sleeve T", 252, 480)
                if Sweater_button_hover == True:
                    Sweater_button.mouse_hover(screen, "Sweater", 252, 560)
                if Sweater_button_hover == False:
                    Sweater_button.mouse_back(screen, "Sweater", 252, 560)
                if Hoodie_button_hover == True:
                    Hoodie_button.mouse_hover(screen,"Hoodie",252,640)
                if Hoodie_button_hover == False:
                    Hoodie_button.mouse_back(screen,"Hoodie",252,640)
                if previous_button_hover == True:
                    previous_button.mouse_hover(screen,"PREVIOUS PAGE",380,725)
                if previous_button_hover == False:
                    previous_button.mouse_back(screen,"PREVIOUS PAGE",380,725)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                TShirt_button_clicked= TShirt_button.rect.collidepoint(mouse_x,mouse_y)
                Shirt_buttton_clicked = Shirt_button.rect.collidepoint(mouse_x, mouse_y)
                Polo_shirt_button_clicked = Polo_shirt_button.rect.collidepoint(mouse_x, mouse_y)
                Long_Sleeve_button_clicked = Long_Sleeve_button.rect.collidepoint(mouse_x, mouse_y)
                Sweater_button_clicked = Sweater_button.rect.collidepoint(mouse_x, mouse_y)
                Hoodie_button_clicked = Hoodie_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_clicked = previous_button.rect.collidepoint(mouse_x, mouse_y)

                if TShirt_button_clicked==True:
                    TShirt_button.sound.play()
                    tempo["type"]="T-shirt"
                    color()
                    run=False

                if Shirt_buttton_clicked==True:
                    Shirt_button.sound.play()
                    tempo["type"] = "Shirt"
                    color()
                    run = False

                if Polo_shirt_button_clicked==True:
                    Polo_shirt_button.sound.play()
                    tempo["type"] = "Polo shirt"
                    color()
                    run=False

                if Long_Sleeve_button_clicked==True:
                    Long_Sleeve_button.sound.play()
                    tempo["type"] = "Long_Sleeve"
                    color()
                    run=False

                if Sweater_button_clicked==True:
                    Sweater_button.sound.play()
                    tempo["type"] = "Sweater"
                    color()
                    run=False

                if Hoodie_button_clicked == True:
                    Hoodie_button.sound.play()
                    tempo["type"] = "Hoodie"
                    color()
                    run=False

                if previous_button_clicked == True:
                    previous_button.sound.play()
                    if tempo['command'] == 'append':
                        input_page()
                        run = False


                    elif tempo["command"]=='delete':
                        delete_page()

                        run=False

def input_outer():

    Flannel_button= Button(screen,"Flannel",252,240)
    Leather_button= Button(screen,"Leather Jacket",252,320)
    Bomber_button= Button(screen,"Bomber Jacket",252,400)
    Zipped_hoodie_button = Button(screen, "Zipped Hoodie", 252, 480)
    Sport_jacket_button = Button(screen, "Sport Jacket", 252, 560)
    Coat_button = Button(screen,"Coat",252,640)
    previous_button =Button(screen,"PREVIOUS PAGE",380,725)
    run = True
    while run:

        background = pygame.image.load("background_input.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img,(0,0))
        Flannel_button.draw_button()
        Leather_button.draw_button()
        Bomber_button.draw_button()
        Zipped_hoodie_button.draw_button()
        Sport_jacket_button.draw_button()
        Coat_button.draw_button()
        previous_button.draw_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Flannel_button_hover = Flannel_button.rect.collidepoint(mouse_x, mouse_y)
                Leather_button_hover = Leather_button.rect.collidepoint(mouse_x, mouse_y)
                Bomber_button_hover = Bomber_button.rect.collidepoint(mouse_x, mouse_y)
                Zipped_hoodie_button_hover=Zipped_hoodie_button.rect.collidepoint(mouse_x,mouse_y)
                Sport_jacket_button_hover = Sport_jacket_button.rect.collidepoint(mouse_x, mouse_y)
                Coat_button_hover = Coat_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_hover = previous_button.rect.collidepoint(mouse_x, mouse_y)
                if Flannel_button_hover == True:
                    Flannel_button.mouse_hover(screen,"Flannel",252,240)
                if Flannel_button_hover == False:
                    Flannel_button.mouse_back(screen,"Flannel",252,240)
                if Leather_button_hover == True:
                    Leather_button.mouse_hover(screen,"Leather Jacket",252,320)
                if Leather_button_hover == False:
                    Leather_button.mouse_back(screen,"Leather Jacket",252,320)
                if Bomber_button_hover == True:
                    Bomber_button.mouse_hover(screen,"Bomber Jacket",252,400)
                if Bomber_button_hover == False:
                    Bomber_button.mouse_back(screen,"Bomber Jacket",252,400)
                if Zipped_hoodie_button_hover == True:
                    Zipped_hoodie_button.mouse_hover(screen, "Zipped Hoodie", 252, 480)
                if Zipped_hoodie_button_hover == False:
                    Zipped_hoodie_button.mouse_back(screen, "Zipped Hoodie", 252, 480)
                if Sport_jacket_button_hover == True:
                    Sport_jacket_button.mouse_hover(screen, "Sport Jacket", 252, 560)
                if Sport_jacket_button_hover == False:
                    Sport_jacket_button.mouse_back(screen, "Sport Jacket", 252, 560)
                if Coat_button_hover == True:
                    Coat_button.mouse_hover(screen,"Coat",252,640)
                if Coat_button_hover == False:
                    Coat_button.mouse_back(screen,"Coat",252,640)
                if previous_button_hover == True:
                    previous_button.mouse_hover(screen,"PREVIOUS PAGE",380,725)
                if previous_button_hover == False:
                    previous_button.mouse_back(screen,"PREVIOUS PAGE",380,725)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                Flannel_button_clicked= Flannel_button.rect.collidepoint(mouse_x,mouse_y)
                Leather_button_clicked = Leather_button.rect.collidepoint(mouse_x, mouse_y)
                Bomber_button_clicked = Bomber_button.rect.collidepoint(mouse_x, mouse_y)
                Zipped_hoodie_button_clicked = Zipped_hoodie_button.rect.collidepoint(mouse_x, mouse_y)
                Sport_jacket_button_clicked = Sport_jacket_button.rect.collidepoint(mouse_x, mouse_y)
                Coat_button_clicked = Coat_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_clicked = previous_button.rect.collidepoint(mouse_x, mouse_y)

                if Flannel_button_clicked==True:
                    Flannel_button.sound.play()
                    tempo['type']='flannel'
                    color()
                    run=False
                if Leather_button_clicked==True:
                    Leather_button.sound.play()
                    tempo['type']='leather jacket'

                    color()
                    run=False

                if Bomber_button_clicked==True:
                    Bomber_button.sound.play()
                    tempo['type']='bomber'

                    color()
                    run=False

                if Zipped_hoodie_button_clicked==True:
                    Zipped_hoodie_button.sound.play()
                    tempo['type']='zipped hoodie'

                    color()
                    run=False

                if Sport_jacket_button_clicked==True:
                    Sport_jacket_button.sound.play()
                    tempo['type']='sports jacket'

                    color()
                    run=False

                if Coat_button_clicked == True:
                    Coat_button.sound.play()
                    tempo['type']='coat'

                    color()
                    run=False

                if previous_button_clicked == True:
                    previous_button.sound.play()
                    if tempo['command']=='append':
                        input_page()

                        run=False
                    elif tempo["command"]=='delete':
                        delete_page()
                        run=False

def input_bottom():

    Short_button= Button(screen,"Shorts",252,255)
    Chino_button= Button(screen,"Chino Pants",252,350)
    Jeans_button= Button(screen,"Jeans",252,445)
    Trouser_button = Button(screen, "Trouser", 252, 540)
    Jogger_button = Button(screen, "Jogger pants", 252, 635)
    previous_button =Button(screen,"PREVIOUS PAGE",380,725)
    run = True
    while run:

        background = pygame.image.load("background_input.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img,(0,0))
        Short_button.draw_button()
        Chino_button.draw_button()
        Jeans_button.draw_button()
        Trouser_button.draw_button()
        Jogger_button.draw_button()
        previous_button.draw_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Short_button_hover = Short_button.rect.collidepoint(mouse_x, mouse_y)
                Chino_button_hover = Chino_button.rect.collidepoint(mouse_x, mouse_y)
                Jeans_button_hover =Jeans_button.rect.collidepoint(mouse_x, mouse_y)
                Trouser_button_hover=Trouser_button.rect.collidepoint(mouse_x,mouse_y)
                Jogger_button_hover = Jogger_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_hover = previous_button.rect.collidepoint(mouse_x, mouse_y)
                if Short_button_hover == True:
                    Short_button.mouse_hover(screen,"Shorts",252,255)
                if Short_button_hover == False:
                    Short_button.mouse_back(screen,"Shorts",252,255)
                if Chino_button_hover == True:
                    Chino_button.mouse_hover(screen,"Chino Pants",252,350)
                if Chino_button_hover == False:
                    Chino_button.mouse_back(screen,"Chino Pants",252,350)
                if Jeans_button_hover == True:
                    Jeans_button.mouse_hover(screen,"Jeans",252,445)
                if Jeans_button_hover == False:
                    Jeans_button.mouse_back(screen,"Jeans",252,445)
                if Trouser_button_hover == True:
                    Trouser_button.mouse_hover(screen, "Trouser", 252, 540)
                if Trouser_button_hover == False:
                    Trouser_button.mouse_back(screen, "Trouser", 252, 540)
                if Jogger_button_hover == True:
                    Jogger_button.mouse_hover(screen, "Jogger pants", 252, 635)
                if Jogger_button_hover == False:
                    Jogger_button.mouse_back(screen, "Jogger pants", 252, 635)

                if previous_button_hover == True:
                    previous_button.mouse_hover(screen,"PREVIOUS PAGE",380,725)
                if previous_button_hover == False:
                    previous_button.mouse_back(screen,"PREVIOUS PAGE",380,725)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                Short_button_clicked= Short_button.rect.collidepoint(mouse_x,mouse_y)
                Chino_button_clicked = Chino_button.rect.collidepoint(mouse_x, mouse_y)
                Jeans_button_clicked = Jeans_button.rect.collidepoint(mouse_x, mouse_y)
                Trouser_button_clicked = Trouser_button.rect.collidepoint(mouse_x, mouse_y)
                Jogger_button_clicked = Jogger_button.rect.collidepoint(mouse_x, mouse_y)
                previous_button_clicked = previous_button.rect.collidepoint(mouse_x, mouse_y)

                if Short_button_clicked==True:
                    Short_button.sound.play()
                    tempo['type']='Shorts'
                    color()
                    run=False

                if Chino_button_clicked==True:
                    Chino_button.sound.play()
                    tempo['type'] = 'chino'
                    color()
                    run=False

                if Jeans_button_clicked==True:
                    Jeans_button.sound.play()
                    tempo['type'] = 'jeans'
                    color()
                    run=False

                if Trouser_button_clicked==True:
                    Trouser_button.sound.play()
                    tempo['type'] = 'trouser'
                    color()
                    run=False

                if Jogger_button_clicked==True:
                    Jogger_button.sound.play()
                    tempo['type'] = 'jogger'
                    color()
                    run=False

                if previous_button_clicked == True:
                    previous_button.sound.play()
                    if tempo['command']=='append':
                        input_page()

                        run=False
                    elif tempo["command"]=='delete':
                        delete_page()
                        run=False

def input_shoes():
    sneaker_button = Button(screen, "Sneaker", 252, 320)
    sport_shoes_button = Button(screen, "Sport shoes", 252, 420)
    loafer_button = Button(screen, "Loafer", 252, 520)
    dress_shoes_button = Button(screen, "Dress shoes", 252, 620)
    main_menu_button = Button(screen, "PREVIOUS PAGE", 380, 725)
    run2 = True
    while run2:
        s_page = pygame.image.load("background_input.png")
        screen.blit(s_page, (0, 0))
        sneaker_button.draw_button()
        sport_shoes_button.draw_button()
        loafer_button.draw_button()
        dress_shoes_button.draw_button()
        main_menu_button.draw_button()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                sneaker_button_hover = sneaker_button.rect.collidepoint(mouse_x, mouse_y)
                sport_shoes_button_hover = sport_shoes_button.rect.collidepoint(mouse_x, mouse_y)
                loafer_button_hover =loafer_button.rect.collidepoint(mouse_x, mouse_y)
                dress_shoes_button_hover=dress_shoes_button.rect.collidepoint(mouse_x,mouse_y)
                main_menu_button_hover = main_menu_button.rect.collidepoint(mouse_x, mouse_y)
                if sneaker_button_hover == True:
                    sneaker_button.mouse_hover(screen, "Sneaker", 252, 320)
                if sneaker_button_hover == False:
                    sneaker_button.mouse_back(screen, "Sneaker", 252, 320)
                if sport_shoes_button_hover == True:
                    sport_shoes_button.mouse_hover(screen, "Sport shoes", 252, 420)
                if sport_shoes_button == False:
                    sport_shoes_button.mouse_back(screen, "Sport shoes", 252, 420)
                if loafer_button_hover == True:
                    loafer_button.mouse_hover(screen, "Loafer", 252, 520)
                if loafer_button_hover == False:
                    loafer_button.mouse_back(screen, "Loafer", 252, 520)
                if dress_shoes_button_hover == True:
                    dress_shoes_button.mouse_hover(screen, "Dress shoes", 252, 620)
                if dress_shoes_button_hover == False:
                    dress_shoes_button.mouse_back(screen, "Dress shoes", 252, 620)
                if main_menu_button_hover == True:
                    main_menu_button.mouse_hover(screen,"PREVIOUS PAGE",380,725)
                if main_menu_button_hover == False:
                    main_menu_button.mouse_back(screen,"PREVIOUS PAGE",380,725)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                sneaker_button_clicked = sneaker_button.rect.collidepoint(mouse_x, mouse_y)
                sport_shoes_button_clicked = sport_shoes_button.rect.collidepoint(mouse_x, mouse_y)
                loafer_button_clicked = loafer_button.rect.collidepoint(mouse_x, mouse_y)
                dress_shoes_button_clicked = dress_shoes_button.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_clicked = main_menu_button.rect.collidepoint(mouse_x, mouse_y)

                if sneaker_button_clicked == True:
                    sneaker_button.sound.play()
                    tempo['type']='sneaker'
                    color()

                    run2 = False

                if sport_shoes_button_clicked == True:
                    sneaker_button.sound.play()
                    tempo['type'] = 'sports shoes'
                    color()

                    run2 = False
                if loafer_button_clicked == True:
                    sneaker_button.sound.play()
                    tempo['type'] = 'loafer'
                    color()

                if dress_shoes_button_clicked == True:
                    loafer_button.sound.play()
                    tempo['type'] = 'dress shoes'
                    color()

                    run2 = False

                if main_menu_button_clicked == True:
                    main_menu_button.sound.play()
                    if tempo['command']=='append':
                        input_page()
                        run2=False
                    elif tempo["command"]=='delete':
                        delete_page()
                        run2=False

def color():

    run = True
    while run:
        background = pygame.image.load("color-page.png")
        img = pygame.transform.scale(background, (504, 780))
        screen.blit(img, (0, 0))
        white = Color_button(screen,(255,255,255), 46.5, 346)
        black = Color_button(screen,(5,5,5), 128.5, 346)
        red = Color_button(screen,(255,0,0), 210.5, 346)
        maroon = Color_button(screen,(204,51,51), 292.5, 346)
        grey = Color_button(screen,(153,153,153), 374.5, 346)
        light_grey = Color_button(screen,(204,204,204), 456.5, 346)
        blue = Color_button(screen,(51,153,204), 46.5, 459)
        navy_blue = Color_button(screen,(51,0,102), 128.5, 459)
        green = Color_button(screen,(51,204,51), 210.5, 459)
        olive = Color_button(screen,(0,104,55), 292.5, 459)
        brown = Color_button(screen,(102,51,0), 374.5, 459)
        orange = Color_button(screen,(255,102,51), 456.5, 459)
        yellow = Color_button(screen,(255,253,0), 46.5, 572)
        purple = Color_button(screen,(102,51,153), 128.5, 572)
        khaki = Color_button(screen,(204,153,102), 210.5, 572)
        pink = Color_button(screen,(255,0,255), 292.5, 572)
        colorful = Image_button(screen,"colorful.png", 374.5, 572)
        camo = Image_button(screen,"camo.png", 456.5, 572)
        main_menu_button = Button(screen, "PREVIOUS PAGE", 140, 725)
        save_button = blue_button(screen, "PROCEED",380, 725 )



        for event in pygame.event.get():
            background = pygame.image.load("color-page.png")
            img = pygame.transform.scale(background, (504, 780))
            screen.blit(img, (0, 0))
            white.draw_button()
            black.draw_button()
            red.draw_button()
            maroon.draw_button()
            grey.draw_button()
            light_grey.draw_button()
            blue.draw_button()
            navy_blue.draw_button()
            green.draw_button()
            olive.draw_button()
            brown.draw_button()
            orange.draw_button()
            yellow.draw_button()
            purple.draw_button()
            khaki.draw_button()
            pink.draw_button()
            colorful.draw_button()
            camo.draw_button()
            main_menu_button.draw_button()
            save_button.draw_button()
            pygame.display.flip()


            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                main_menu_button_hover=main_menu_button.rect.collidepoint(mouse_x,mouse_y)
                save_button_hover=save_button.rect.collidepoint(mouse_x,mouse_y)


                if main_menu_button_hover == True:
                    main_menu_button.mouse_back(screen, "PREVIOUS PAGE", 140, 725)
                if main_menu_button_hover == False:
                    main_menu_button.mouse_back(screen, "PREVIOUS PAGE", 140, 725)


                if save_button_hover == True:
                    save_button.mouse_hover(screen, "TO MAIN MENU?",380, 725)
                if save_button_hover == False:
                    save_button.mouse_back(screen, "PROCEED",380, 725)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                white_clicked = white.rect.collidepoint(mouse_x, mouse_y)
                black_clicked = black.rect.collidepoint(mouse_x, mouse_y)
                red_clicked = red.rect.collidepoint(mouse_x, mouse_y)
                maroon_clicked = maroon.rect.collidepoint(mouse_x, mouse_y)
                grey_clicked = grey.rect.collidepoint(mouse_x, mouse_y)
                light_grey_clicked = light_grey.rect.collidepoint(mouse_x, mouse_y)
                blue_clicked = blue.rect.collidepoint(mouse_x, mouse_y)
                navy_blue_clicked = navy_blue.rect.collidepoint(mouse_x, mouse_y)
                green_clicked = green.rect.collidepoint(mouse_x, mouse_y)
                olive_clicked = olive.rect.collidepoint(mouse_x, mouse_y)
                brown_clicked = brown.rect.collidepoint(mouse_x, mouse_y)
                orange_clicked = orange.rect.collidepoint(mouse_x, mouse_y)
                yellow_clicked = yellow.rect.collidepoint(mouse_x, mouse_y)
                purple_clicked = purple.rect.collidepoint(mouse_x, mouse_y)
                khaki_clicked = khaki.rect.collidepoint(mouse_x, mouse_y)
                pink_clicked = pink.rect.collidepoint(mouse_x, mouse_y)
                colorful_clicked = colorful.rect.collidepoint(mouse_x, mouse_y)
                camo_clicked = camo.rect.collidepoint(mouse_x, mouse_y)
                main_menu_button_clicked=main_menu_button.rect.collidepoint(mouse_x,mouse_y)
                save_button_clicked=save_button.rect.collidepoint(mouse_x,mouse_y)

                if white_clicked==True:
                    white.sound.play()
                    tempo['color']="white"
                if black_clicked==True:
                    black.sound.play()
                    tempo['color']="black"
                if red_clicked==True:
                    red.sound.play()
                    tempo['color']="red"
                if maroon_clicked==True:
                    maroon.sound.play()
                    tempo['color']="maroon"
                if grey_clicked==True:
                    grey.sound.play()
                    tempo['color']="grey"
                if light_grey_clicked==True:
                    light_grey.sound.play()
                    tempo['color']="light_grey"
                if blue_clicked==True:
                    blue.sound.play()
                    tempo['color']="blue"
                if navy_blue_clicked==True:
                    navy_blue.sound.play()
                    tempo['color']="navy_blue"
                if green_clicked==True:
                    green.sound.play()
                    tempo['color']="green"
                if olive_clicked==True:
                    olive.sound.play()
                    tempo['color']="olive"
                if brown_clicked==True:
                    brown.sound.play()
                    tempo['color']="brown"
                if orange_clicked==True:
                    orange.sound.play()
                    tempo['color']="orange"
                if yellow_clicked==True:
                    yellow.sound.play()
                    tempo['color']="yellow"
                if purple_clicked==True:
                    purple.sound.play()
                    tempo['color']="purple"
                if khaki_clicked==True:
                    khaki.sound.play()
                    tempo['color']="khaki"
                if pink_clicked==True:
                    pink.sound.play()
                    tempo['color']="pink"
                if colorful_clicked==True:
                    colorful.sound.play()
                    tempo['color']="colorful"
                if camo_clicked==True:
                    colorful.sound.play()
                    tempo['color']="camo"

                if main_menu_button_clicked==True:
                    main_menu_button.sound.play()
                    if tempo['parts']=='upper':
                        input_upper()
                        run=False
                    elif tempo['parts']=='outer':
                        input_outer()
                        run=False
                    elif tempo['parts']=='bottom':
                        input_bottom()
                        run=False
                    elif tempo['parts']=='shoes':
                        input_shoes()
                        run=False


                if save_button_clicked==True:

                    if tempo['command']=='append':
                        if tempo['parts']=='upper':
                            upper.append(Cloth(tempo['type'],tempo['color']))
                        elif tempo['parts']=='outer':
                            outer.append(Cloth(tempo['type'], tempo['color']))
                        elif tempo['parts']=='bottom':
                            bottom.append(Cloth(tempo['type'], tempo['color']))
                        elif tempo['parts']=='shoes':
                            shoe.append(Cloth(tempo['type'], tempo['color']))

                    if tempo['command']=='delete':
                        if tempo['parts']=='upper':
                            for cloth in upper:
                                if cloth.type==tempo['type']:
                                    if cloth.color==tempo['color']:
                                        del upper[cloth]
                                    else:
                                        pass
                                else:
                                    pass


                        elif tempo['parts']=='outer':
                            for cloth in outer:
                                if cloth.type==tempo['type']:
                                    if cloth.color==tempo['color']:
                                        del outer[cloth]
                                    else:
                                        pass
                                else:
                                    pass
                        elif tempo['parts']=='bottom':
                            for cloth in bottom:
                                if cloth.type==tempo['type']:
                                    if cloth.color==tempo['color']:
                                        del bottom[cloth]
                                    else:
                                        pass
                                else:
                                    pass
                        elif tempo['parts']=='shoes':
                            for cloth in shoe:
                                if cloth.type==tempo['type']:
                                    if cloth.color==tempo['color']:
                                        del shoe[cloth]
                                    else:
                                        pass
                                else:
                                    pass

                    write()
                    main_page()
                    run=False

read()
main_page()