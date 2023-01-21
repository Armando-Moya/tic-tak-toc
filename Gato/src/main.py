from tkinter import *
from tkinter import ttk  
#------|constns|------#
WIDTH=768
HEIGHT=1366
GAME_ICON1='X'
GAME_ICON2='O'
GAME_ICON3='-'

#-------|statements|------#
class screen:
     def __init__(self,**kwargs):
        self.widgets=kwargs

     def clear_screen(self):
        for i in self.widgets.values():
            i.place_forget()

     def clear_element(self,element:str):
         self.widgets[element].place_forget()

     def draw_elements_range(self,min_row:int,min_column:int,max_row:int,max_column:int,*args,):
             for i in range(min_row,max_row):
                for j in range(min_column,max_column):
                     self.widgets[args[j]].grid(row=i,column=j)

     def draw_element(self,element:str,**kwargs):  
       self.widgets[element].place(x=kwargs['x'],y=kwargs['y'],width=kwargs['width'],height=kwargs['height'])

     def show_elements(self):
       for i in self.widgets.keys():
          print(i)  

def data_screen_2_jugadores(obj_act,obj_ant):
 obj_ant.clear_screen()
 obj_act.draw_element("a",x=WIDTH/2,y=HEIGHT/3,width=100,height=50)
 obj_act.draw_element("jugador_1",x=(WIDTH/2)+100,y=HEIGHT/3,width=100,height=50)
 obj_act.draw_element("icon_jugador_x_1",x=(WIDTH/2)+200,y=HEIGHT/3,width=50,height=50)
 obj_act.draw_element("icon_jugador_o_1",x=(WIDTH/2)+300,y=HEIGHT/3,width=50,height=50)
 obj_act.draw_element("b",x=WIDTH/2,y=(HEIGHT/3)+100,width=100,height=50)
 obj_act.draw_element("jugador_2",x=(WIDTH/2)+100,y=(HEIGHT/3)+100,width=100,height=50)
 obj_act.draw_element("icon_jugador_x_2",x=(WIDTH/2)+200,y=(HEIGHT/3)+100,width=50,height=50)
 obj_act.draw_element("icon_jugador_o_2",x=(WIDTH/2)+300,y=(HEIGHT/3)+100,width=50,height=50)

def data_screen_1_jugadores(obj_act,obj_ant):
   obj_ant.clear_screen()
   obj_ant.clear_screen()
   obj_act.draw_element("a",x=WIDTH/2,y=HEIGHT/3,width=100,height=50)
   obj_act.draw_element("jugador_1",x=(WIDTH/2)+100,y=HEIGHT/3,width=100,height=50)
   obj_act.draw_element("icon_jugador_x_1",x=(WIDTH/2)+200,y=HEIGHT/3,width=50,height=50)
   obj_act.draw_element("icon_jugador_o_1",x=(WIDTH/2)+300,y=HEIGHT/3,width=50,height=50)


def main():
  
 root=Tk()
 jugador_icon_1=StringVar()
 jugador_icon_2=StringVar()
 jugador_name_1=StringVar()
 jugador_name_2=StringVar() 
 root.title("Gato")
 root.geometry(str(WIDTH)+"x"+str(HEIGHT))
 #root=Labelroot(root,text="Gato")
 #root.place(x=WIDTH/2, y=HEIGHT/3)
 data1=screen(a=Label(root,text="Jugador 1"),jugador_1=Entry(root),icon_jugador_x_1=Checkbutton(root,text="X",variable=jugador_icon_1,onvalue="X"),icon_jugador_o_1=Checkbutton(root,text="O",variable=jugador_icon_1,onvalue="O"),b=Label(root,text="Jugador2"),jugador_2=Entry(root),icon_jugador_x_2=Checkbutton(root,text="X",variable=jugador_icon_2,onvalue="X"),icon_jugador_o_2=Checkbutton(root,text="O",variable=jugador_icon_2,onvalue="O"))
 data2=screen(a=Label(root,text="Jugador 1"),jugador_1=Entry(root),icon_jugador_x_1=Checkbutton(root,text="X",variable=jugador_icon_1,onvalue="X"),icon_jugador_o_1=Checkbutton(root,text="O",variable=jugador_icon_1,onvalue="O"))
 start=screen(mode_1=Button(root,text="1 Jugador",command=lambda:data_screen_1_jugadores(data2,start)),mode_2=Button(root,text="2 Jugador",command=lambda:data_screen_2_jugadores(data1,start)))
 start.draw_element("mode_1",x=WIDTH/2,y=HEIGHT/3,width=200,height=50)
 start.draw_element("mode_2",x=WIDTH/2,y=(HEIGHT/3)+100,width=200,height=50)
 root.mainloop()

if __name__ == "__main__":
    main()
