# filedialog.askopenfilename() -> é utilizado para aparecer aquele menu de seleção
# ele devolver uma string que contém o caminho do ficheiro
from compressor import *
from cv2 import destroyWindow, trace
from img import *
from sound import *
from tkinter import *
from tkinter import filedialog

def music_menu():
    menu = Tk()
    menu.title("🤖Python Music")
    menu.geometry("390x215")
    
    lable_bost = Label(menu, text = "Bost - >").place(x = 95,y = 0)
    lable_inicio = Label(menu, text = "Inicio do audio - >").place(x = 30,y = 30)
    lable_fim = Label(menu, text = "Fim do audio - >").place(x = 38,y = 60)
    lable_frame = Label(menu, text = "Frame do audio - >").place(x = 27,y = 90)
    lable_save = Label(menu, text = "Nome do audio a salvar - >").place(x = 8,y = 120)
    
    text_box = Entry(menu, width = 25)
    text_box.place(x = 155, y = 0)
    
    text1_box = Entry(menu,width=25)
    text1_box.place(x = 155, y = 30)
    
    text2_box = Entry(menu,width=25)
    text2_box.place(x = 155, y = 60)
    
    text3_box = Entry(menu,width=25)
    text3_box.place(x = 155, y = 90)
    
    text4_box = Entry(menu,width=25)
    text4_box.place(x = 155, y = 120)
    
    btn_ok = Button(menu, text="Ok", command=lambda: music(filedialog.askopenfilename(), int(text_box.get()), int(text1_box.get()), int(text2_box.get()), int(text3_box.get()), text4_box.get()))
    btn_ok.place(x = 195, y = 185)
    
    
    menu.mainloop()

def start_menu():
    menu = Tk()
    menu.title("🤖Python Image")
    menu.geometry("500x350")
    menu.configure(background='blue4')

    # Button:
    btn_black = Button(menu, text="Black image", command=lambda: [black(filedialog.askopenfilename())], bg='light blue', borderwidth = 0)
    btn_red = Button(menu, text="Red channel", command=lambda: red(filedialog.askopenfilename()), bg='light blue', borderwidth = 0)
    btn_add = Button(menu, text="Add image", command=lambda: add(filedialog.askopenfilename(), filedialog.askopenfilename()), bg='light blue', borderwidth = 0)
    btn_sub = Button(menu, text="Sub image", command=lambda: sub(filedialog.askopenfilename(), filedialog.askopenfilename()), bg='light blue', borderwidth = 0)
    btn_log = Button(menu, text="Image A AND Image B", command=lambda: log(filedialog.askopenfilename(), filedialog.askopenfilename()), bg='light blue', borderwidth = 0)
    btn_log1 = Button(menu, text="Image B XOR Image B", command=lambda: log1(filedialog.askopenfilename(), filedialog.askopenfilename()), bg='light blue', borderwidth = 0)
    btn_movie = Button(menu, text="Black movie", command=lambda: movie(filedialog.askopenfilename(), 1), bg='red', borderwidth = 0)
    btn_halfmovie = Button(menu, text="Half black movie", command=lambda: movie(filedialog.askopenfilename(), 2), bg='red', borderwidth = 0)
    btn_music = Button(menu, text="Play music", command=lambda: music_menu(), bg="MediumPurple1", borderwidth = 0)
    btn_compressor = Button(menu, text="RLE compressor", command=lambda: openfile(filedialog.askopenfilename()), bg ="light green", borderwidth = 0)
    btn_black.place(x=115, y=50)
    btn_red.place(x=115, y=100)
    btn_add.place(x=115, y=150)
    btn_sub.place(x=315, y=50)
    btn_log.place(x=315, y=100)
    btn_movie.place(x=310, y=200)
    btn_music.place(x=210, y=250)
    btn_log1.place(x=315, y=150)
    btn_halfmovie.place(x=110, y=200)
    btn_compressor.place(x=197, y=300)

    menu.mainloop()    
start_menu()