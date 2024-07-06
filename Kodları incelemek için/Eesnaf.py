#-------------------------(modules)----------------------------#
#from multiprocessing import Process                           #
#import multiprocessing
#import threading
#import square.client                                          #
import smtplib                                                 #
from email.mime.multipart import MIMEMultipart                 #
from email.mime.text import MIMEText                           #
import ursina                                                  #
import os                                                      #
import sys                                                     #
import pygame                                                  #
pygame.init()                                                  #
#--------------------------------------------------------------#

#--------------------------------------------------------------
my_name = "Taha Mert Savaş"
my_mail = "taha.mert.savas@gmail.com"
token = "---------------------------------------------------------"
print("{0}\nOwner of the project: {1}\nYou can reach me here: {2}\n{0}".format(token,my_name,my_mail))
#--------------------------------------------------------------

#-------------------------(screen)-----------------------------#
screen_width,screen_height = 1920,1080                         #
screen = pygame.display.set_mode((screen_width,screen_height)) #
#--------------------------------------------------------------#



#-------------------------(img and mask)-----------------------#
mouse_mask = pygame.mask.from_surface(pygame.Surface((1,1)))
#------#                          #------#                                  #------#
login_page_bg = pygame.image.load("Login Page Materials/login_page_bg.png")

login_button_off = pygame.image.load("Login Page Materials/login_button_off.png")
login_button_on = pygame.image.load("Login Page Materials/login_button_on.png")
login_button_mask = pygame.mask.from_surface(login_button_off)

universty_logo = pygame.image.load("Login Page Materials/şeyhedebaliüniversitesi_logo.png")
universty_logo_mask = pygame.mask.from_surface(universty_logo)
exit_logo = pygame.image.load("Login Page Materials/exit_logo.png")
#------#                          #------#                                  #------#
shopping_page_bg = pygame.image.load("Shopping Page Materials/shopping_page_bg.png")
shopping_page_top_bg = pygame.image.load("Shopping Page Materials/shopping_page_top_bg.png")
product_choice = pygame.image.load("Shopping Page Materials/product_choice.png")
num_bg = pygame.image.load("Shopping Page Materials/number_bg.png")
basket_orange = pygame.image.load("Shopping Page Materials/basket_orange.png")
basket_orange_mask = pygame.mask.from_surface(basket_orange)
basket_blue = pygame.image.load("Shopping Page Materials/basket_blue.png")

person_logo = pygame.image.load("Shopping Page Materials/person_logo.png")
mandarin_logo = pygame.image.load("Shopping Page Materials/mandarin_logo.png")

product_list = []
product_name_list = []
product_folder = "Products"
product_files = os.listdir(product_folder)
for filename in product_files:
    if filename.endswith(".png") or filename.endswith(".jpg"):
        product_image = pygame.image.load(os.path.join(product_folder, filename))
        product_list.append(product_image)
        product_name_list.append(filename)
#------#                          #------#                                  #------#
order_page_bg = pygame.image.load("Order Page Materials/order_page_bg.png")
wait = pygame.image.load("Order Page Materials/wait2.png")
products_bg = pygame.image.load("Order Page Materials/products_bg.png")
products_bg = pygame.transform.scale(products_bg,(products_bg.get_width(),products_bg.get_height()+10))
product_bg = pygame.image.load("Order Page Materials/product_bg.png")
products_bg_bg = pygame.image.load("Order Page Materials/products_bg_bg.png")
delete_red = pygame.image.load("Order Page Materials/delete_red.png")
delete_white = pygame.image.load("Order Page Materials/delete_white.png")

data_bg = pygame.image.load("Order Page Materials/data_bg.png")
adress_button_green = pygame.image.load("Order Page Materials/adress.png")
tel_no_button_green = pygame.image.load("Order Page Materials/telefon_no.png")
e_mail_button_green = pygame.image.load("Order Page Materials/e-posta.png")
adress_button_white = pygame.image.load("Order Page Materials/adress_white.png")
tel_no_button_white = pygame.image.load("Order Page Materials/telefon_no_white.png")
e_mail_button_white = pygame.image.load("Order Page Materials/e-posta_white.png")
e_esnaf_logo = pygame.image.load("Order Page Materials/logo.png")
confirmation_button_black = pygame.image.load("Order Page Materials/confirmation_button_black.png")
confirmation_button_white = pygame.image.load("Order Page Materials/confirmation_button_white.png")
#--------------------------------------------------------------#

def shopping_product(screen, product, x, y, delete_img):
    screen.blit(product_bg, (x, y))
    screen.blit(product, (x + 17.3, y + product_bg.get_height() / 2 - 173.2 / 2))
    screen.blit(delete_img, (x + 600, y + 15))

n = 0
def wait_func(wait,n,event):
    while not event.is_set():
        print("A")
        screen.blit(wait_bg,(screen_width/2-wait_bg.get_width()/2,screen_height/2-wait_bg.get_height()/2))
        wait = pygame.transform.rotate(wait, n)
        screen.blit(wait,(screen_width/2-wait.get_width()/2,screen_height/2-wait.get_height()/2))
        print("a")

def send_mail(mail_num):

    # E-posta içeriği
    content = f"E-mail:{e_mail_text}\nTel no:{tel_no_text}\nAdres:{address_text}\n\n"+del_png
    sender = 'göndereceğinoutlokhesabı@outlook.com'
    password = 'şifresi'
    to = "gönderiyialıcakgmailveyahesap"

    # E-posta oluşturma
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = "E-esnaf -SİPARİŞLER-"
    msg.attach(MIMEText(content, 'plain'))

    server = None

    try:
        if mail_num == 0:
            # SMTP sunucusuna bağlanma ve mail gönderme
            server = smtplib.SMTP("smtp-mail.outlook.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            text = msg.as_string()
            server.sendmail(sender, to, text)
            print("Mail başarıyla gönderildi.")
            mail_num += 1

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Hatası: {e.smtp_code} - {e.smtp_error.decode('utf-8')}")
    except smtplib.SMTPConnectError as e:
        print(f"SMTP Bağlantı Hatası: {e.smtp_code} - {e.smtp_error.decode('utf-8')}")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"SMTP Alıcı Reddedildi: {e.recipients}")
    except smtplib.SMTPSenderRefused as e:
        print(f"SMTP Gönderen Reddedildi: {e.smtp_code} - {e.smtp_error.decode('utf-8')}")
    except smtplib.SMTPDataError as e:
        print(f"SMTP Veri Hatası: {e.smtp_code} - {e.smtp_error.decode('utf-8')}")
    except smtplib.SMTPException as e:
        print(f"SMTP Hatası: {str(e)}")
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")
    finally:
        if server is not None:
            try:
                server.quit()
            except smtplib.SMTPServerDisconnected:
                print("Server already disconnected.")


#------------------------(positions)---------------------------#
login_button_xpos,login_button_ypos= 653.6,403.9               #
product_xpos,product_ypos = 108,167.7                          #
#--------------------------------------------------------------#


#----------------------------(keys)----------------------------#
LOGIN_PAGE = True                                              #
SHOPPING_PAGE = False                                          #
ORDER_PAGE = False
ADDRESS_INPUT = False
E_MAIL_INPUT = False
TEL_NO_INPUT = False
tel_lock = True
mail_lock = True
adress_lock = True

#--------------------------------------------------------------#
j=0
mail_num = 0

address_text = ""
e_mail_text = ""
tel_no_text = ""

cursor_visible = True
cursor_timer = pygame.time.get_ticks()

shopping_list = []
shopping_name_list = []
del_png = ""
FPS = 60
clock = pygame.time.Clock()
while True:
    #--------------------------------------------------------------#
    #clock.tick(FPS)                                                #
    keys = pygame.key.get_pressed()                                #
    mouse_xpos,mouse_ypos = pygame.mouse.get_pos()                 #
    left_click_up = False                                          #
    left_click = False                                             #
    scroll_wheel_up = False                                        #
    scroll_wheel_down = False                                      #
    one_down = False                                               #
    key_name = None                                                #
    for event in pygame.event.get():                               #
        if (event.type == pygame.MOUSEBUTTONDOWN):                 #
            if event.button == 1:                                  #
                left_click = True                                  #
            if event.button == 4:                                  #
                scroll_wheel_up = True                             #
            if event.button == 5:                                  #
                scroll_wheel_down = True                           #
        if (event.type == pygame.MOUSEBUTTONUP):                   #
            if event.button == 1:                                  #
                left_click_up = True                               #
        if (event.type == pygame.KEYDOWN):                         #
            one_down = True                                        #
            key_name = pygame.key.name(event.key)                  #
            if ADDRESS_INPUT == True and adress_lock == True:
                if key_name == 'backspace':
                    address_text = address_text[:-1]
                elif key_name == 'return':
                    ADDRESS_INPUT = False
                else:
                    address_text += event.unicode
                    print("harf eklendi")
            if E_MAIL_INPUT == True and mail_lock == True:
                if key_name == 'backspace':
                    e_mail_text = e_mail_text[:-1]
                elif key_name == 'return':
                    E_MAIL_INPUT = False
                else:
                    e_mail_text += event.unicode
                    print("harf eklendi")

            if TEL_NO_INPUT == True and tel_lock == True:
                if key_name == 'backspace':
                    tel_no_text = tel_no_text[:-1]
                elif key_name == 'return':
                    TEL_NO_INPUT = False
                else:
                    tel_no_text += event.unicode
                    print("harf eklendi")
        if (event.type == pygame.QUIT) or key_name == "escape":    #
            pygame.quit()                                          #
            sys.exit()                                             #
    #--------------------------------------------------------------#

    # -------------------------------------------------(Login Page)----------------------------------------------------#
    if LOGIN_PAGE == True:                                                                                             #
        screen.blit(login_page_bg,(0,0))                                                                               #
        login_button = login_button_off                                                                                #
        if login_button_mask.overlap(mouse_mask, (mouse_xpos - login_button_xpos, mouse_ypos - login_button_ypos)):    #
            login_button = login_button_on                                                                             #
            if left_click_up == True:                                                                                  #
                LOGIN_PAGE = False                                                                                     #
                SHOPPING_PAGE = True                                                                                   #
        screen.blit(login_button, (login_button_xpos,login_button_ypos))                                               #
    # -----------------------------------------------------------------------------------------------------------------#

    # ------------------------------------------------(Shopping Page)--------------------------------------------------#
    min_product_ypos = -(len(product_list) // 6 * 325) + shopping_page_top_bg.get_height() + product_list[0].get_height()/3
    max_product_ypos = 167.7

    if SHOPPING_PAGE == True:
        screen.blit(shopping_page_bg, (0, 0))
        for index, product in enumerate(product_list):
            row = index // 6
            col = index % 6
            product_x = product_xpos + col * 300
            product_y = product_ypos + row * 325

            product_mask = pygame.mask.from_surface(product)
            if product_mask.overlap(mouse_mask, (mouse_xpos - product_x, mouse_ypos - product_y)) and (mouse_ypos > shopping_page_top_bg.get_height()):
                screen.blit(product_choice, (product_x-((product_choice.get_width()-product.get_width())/2), product_y-((product_choice.get_height()-product.get_height())/2)))
                if left_click == True :
                    shopping_list.append(product)
                    shopping_name_list.append(product_name_list[product_list.index(product)])

                    product_name = product_name_list[product_list.index(product)]
                    product_name = product_name.replace(".png", "")
                    del_png = del_png+product_name+"\n"

            screen.blit(product, (product_x, product_y))

        # Mouse tekerleği yukarı kaydırıldığında
        if (scroll_wheel_down == True) and product_ypos > min_product_ypos:
            product_ypos -= 100

        # Mouse tekerleği aşağı kaydırıldığında
        elif (scroll_wheel_up == True) and product_ypos < max_product_ypos:
            product_ypos += 100

        screen.blit(shopping_page_top_bg, (0, 0))

        font = pygame.font.SysFont("Arial", 20,bold=True)
        num_products = font.render(f"{len(shopping_list)}", 1, (0, 0, 0))
        screen.blit(num_bg, (1778, 77))
        screen.blit(num_products,(1782,77))
        basket_logo = basket_orange
        if basket_orange_mask.overlap(mouse_mask, (mouse_xpos - 1665, mouse_ypos - 27)):
            basket_logo = basket_blue
            if left_click == True:
                """
                event = multiprocessing.Event()  # E-posta gönderme işleminin bitip bitmediğini takip eden olay

                mail_process = multiprocessing.Process(target=send_mail, args=(mail_num, event))
                mail_process.start()

                wait_func(wait,n,event)

                mail_process.join()
                """
                SHOPPING_PAGE = False
                ORDER_PAGE = True
        screen.blit(basket_logo, (1665, 27))

        screen.blit(mandarin_logo, (1802, 26))

        screen.blit(person_logo, (386, 30))


    # -----------------------------------------------------------------------------------------------------------------#

    # ------------------------------------------------(Order Page)-----------------------------------------------------#
    if ORDER_PAGE == True:
        screen.blit(order_page_bg,(0,0))
        screen.blit(products_bg, (108, 108))

        m = 131+j
        for index, original_product in enumerate(shopping_list):
            scaled_product = pygame.transform.scale(original_product, (175.8, 173.2))
            delete_img = delete_red

            if pygame.mask.from_surface(delete_red).overlap(mouse_mask,(mouse_xpos - (118 + 600), mouse_ypos - (m + 15))):
                delete_img = delete_white
                if left_click:
                    shopping_list.remove(original_product)  # Orijinal ürünü kaldırın
                    continue  # Döngünün bu turunu atlayarak listede değişiklik olduğunda hatalardan kaçının


            if (scroll_wheel_down == True) :
                j -= 10

            # Mouse tekerleği aşağı kaydırıldığında
            elif (scroll_wheel_up == True) :
                j += 10
            shopping_product(screen, scaled_product, 118, m, delete_img)
            m += 100 + product_bg.get_height()
            screen.blit(products_bg_bg, (108,0))

        # -------------------------------------------------#

        screen.blit(data_bg,(1374,108))
        screen.blit(e_esnaf_logo, (1473.6, 633.6))

        e_mail_button = e_mail_button_green
        if pygame.mask.from_surface(e_mail_button).overlap(mouse_mask, (mouse_xpos - (1416.9), mouse_ypos - (187))):
            e_mail_button = e_mail_button_white
            if left_click:
                E_MAIL_INPUT = True
                mail_lock = True
        else:
            if left_click:
                mail_lock = False
        tel_no_button = tel_no_button_green
        if pygame.mask.from_surface(tel_no_button).overlap(mouse_mask, (mouse_xpos - (1416.9), mouse_ypos - (355.6))):
            tel_no_button = tel_no_button_white
            if left_click:
                TEL_NO_INPUT = True
                tel_lock = True
        else:
            if left_click:
                tel_lock = False
        adress_button = adress_button_green
        if pygame.mask.from_surface(adress_button).overlap(mouse_mask, (mouse_xpos - (1416.9), mouse_ypos - (524.3))):
            adress_button = adress_button_white
            if left_click:
                ADDRESS_INPUT = True
                adress_lock = True
        else:
            if left_click:
                adress_lock = False

        confirmation_button = confirmation_button_black
        if pygame.mask.from_surface(confirmation_button_black).overlap(mouse_mask,
                                                                       (mouse_xpos - (1416.9), mouse_ypos - (845.6))):
            confirmation_button = confirmation_button_white
            if left_click:
                screen.blit(wait, (screen_width / 2 - wait.get_width() / 2, screen_height / 2 - wait.get_height() / 2))
                send_mail(mail_num)

        screen.blit(e_mail_button, (1416.9, 187))
        screen.blit(tel_no_button, (1416.9, 355.6))
        screen.blit(adress_button, (1416.9, 524.3))
        screen.blit(confirmation_button, (1416.9, 845.6))
        #-------------------------------------------------#

        if ADDRESS_INPUT:
            font = pygame.font.SysFont("Arial", 25)
            address_rect = pygame.Rect(1416.9+170, 524.3-55 + adress_button.get_height() , 250, 30)
            pygame.draw.rect(screen, (255, 255, 255), address_rect)
            screen.blit(font.render(address_text, True, (0, 0, 0)), (address_rect.x + 5, address_rect.y + 5))

            if pygame.time.get_ticks() - cursor_timer >= 500:
                cursor_timer = pygame.time.get_ticks()
                cursor_visible = not cursor_visible

            if cursor_visible == True and adress_lock == True:
                cursor_pos = font.size(address_text)[0]
                pygame.draw.line(screen, (0, 0, 0), (address_rect.x + 5 + cursor_pos, address_rect.y + 5),(address_rect.x + 5 + cursor_pos, address_rect.y + 25), 2)
        
        if E_MAIL_INPUT:
            font = pygame.font.SysFont("Arial", 25)
            address_rect = pygame.Rect(1416.9+170, 187-55 + adress_button.get_height() , 250, 30)
            pygame.draw.rect(screen, (255, 255, 255), address_rect)
            screen.blit(font.render(e_mail_text, True, (0, 0, 0)), (address_rect.x + 5, address_rect.y + 5))

            if pygame.time.get_ticks() - cursor_timer >= 500:
                cursor_timer = pygame.time.get_ticks()
                cursor_visible = not cursor_visible

            if cursor_visible == True and mail_lock == True:
                cursor_pos = font.size(e_mail_text)[0]
                pygame.draw.line(screen, (0, 0, 0), (address_rect.x + 5 + cursor_pos, address_rect.y + 5),(address_rect.x + 5 + cursor_pos, address_rect.y + 25), 2)


        if TEL_NO_INPUT:
            font = pygame.font.SysFont("Arial", 25)
            address_rect = pygame.Rect(1416.9+170, 355.6-55 + adress_button.get_height() , 250, 30)
            pygame.draw.rect(screen, (255, 255, 255), address_rect)
            screen.blit(font.render(tel_no_text, True, (0, 0, 0)), (address_rect.x + 5, address_rect.y + 5))

            if pygame.time.get_ticks() - cursor_timer >= 500:
                cursor_timer = pygame.time.get_ticks()
                cursor_visible = not cursor_visible

            if cursor_visible == True and tel_lock == True:
                cursor_pos = font.size(tel_no_text)[0]
                pygame.draw.line(screen, (0, 0, 0), (address_rect.x + 5 + cursor_pos, address_rect.y + 5),(address_rect.x + 5 + cursor_pos, address_rect.y + 25), 2)



    # -----------------------------------------------------------------------------------------------------------------#





    top_left_logo = universty_logo
    if universty_logo_mask.overlap(mouse_mask, (mouse_xpos - 6, mouse_ypos - 20)):
        top_left_logo = exit_logo
        if left_click == True:
            pygame.quit()
            sys.exit()
    screen.blit(top_left_logo,(6,20))
    pygame.display.flip()




