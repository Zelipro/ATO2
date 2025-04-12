from kivymd.app import MDApp
from kivy.lang import  Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from kivy.core.window import Window
from kivy.graphics import RoundedRectangle,Color

from Les_Bases import base_10_k , base_k_10
from kivy.clock import Clock
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

#Window.size = [380,620]

Style = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDBoxLayout:
    orientation:"vertical"
    #La page 
    MDFloatLayout:
        size_hint:(1,.09)
        MDTopAppBar:
            id: TopBar
            title:"ATO"
            left_action_items:[["weather-night" , lambda x : app.ChangeMode()]]
            pos_hint:{"top":1}
            elevation:3
        
        MDCard:
            size_hint:(None,None)
            height:TopBar.height-5
            width:TopBar.height-5
            md_bg_color:(1,1,1,1)
            elevation:3
            pos_hint:{"top":1,"right":1}
            radius:[(TopBar.height-5)/2]
            
            AsyncImage:
                size_hint:(None,None)
                source : "Img.png"
                size:(TopBar.height-5,TopBar.height-15)
                pos_hint:{"center_y":.55}
    

    
    ScreenManager:
        id:cr
        transition:NoTransition()
        MDScreen:
            name:'Page_1'
            MDBoxLayout:
                id : Main
                orientation:'vertical'
                size_hint:(1,None)
                spacing:15
                pos_hint:{"center_x":.9}
                MDLabel:
                    text : "Bienvenu M.Elisée"
                    bold:True
                    size_hint:(None,1)
                    width:TopBar.width-25
                    pos_hint: {"center_x":.41}

                MDBoxLayout:
                    id:Placer
                    orientation:"vertical"
                    spacing:15
                    size_hint:(None,None)
                    width:TopBar.width
                    pos_hint: {"center_x":.1}
                    padding:[5,5,5,5]
                    MDRaisedButton:
                        id:But1
                        text:"[b]Conversion de Base[/b]"
                        size_hint:(None,1)
                        md_bg_color:(0,0,1,1)
                        width:TopBar.width-25
                        pos_hint: {"center_x":.5}
                        on_release : app.Appui2(self)
                    MDRaisedButton:
                        id:But2
                        text:"[b]Ascci[/b]"
                        size_hint:(None,1)
                        width:TopBar.width-25
                        md_bg_color:(0,0,1,1)
                        pos_hint: {"center_x":.5}
                        on_release:app.Appui2(self)
                        makup:True
        MDScreen:
            name:'Page_2'
            MDBoxLayout:
                id:Page2
                orientation:"vertical"
                pos_hint:{"center_x":.5,'center_y':.5}
                spacing:50
                MDLabel:
                    text:'Veuillez entrer un Nombre'
                    id:Lab_Page2 
                    bold:True
                    size_hint :(1,.1)
                    color : (1,0,0,1)
                MDScrollView:
                    do_scroll_x:False
                    do_scroll_y:True
                    MDGridLayout:
                        id:Grd
                        cols:1
                        adaptive_height:True
                MDRaisedButton:
                    text : "[b]Retour[/b]"
                    md_bg_color : (1,0,0,1)
                    size_hint_x : None
                    width : TopBar.width - 20
                    pos_hint :  {"center_x":.5}
                    makup : True
                    on_release : app.ret1(self)
                        
        MDScreen:
            name:"Page_3"
            MDBoxLayout:
                id:Page3
                orientation:"vertical"
                size_hint_y:None
                width:TopBar.width-20
                pos_hint:{"center_x":.5,"center_y":.5}
                spacing:50
                MDBoxLayout:
                    id:Contenant
                    orientation:"vertical"
                    size_hint_x:None
                    width:TopBar.width - 2
                    pos_hint:{"center_x":.5}
                    spacing:20
                    MDRaisedButton:
                        id:But
                        text:"[b]Votre Choix SVP [/b]"
                        on_release : app.Option(self)
                        size_hint_x:None
                        width:TopBar.width - 10
                        pos_hint:{"center_x":.5}
                        makup:True
                    MDTextField:
                        id:Input
                        hint_text : "Entrez une Valeur.........."
                        halign:'center'
                        size_hint_x:None
                        width:TopBar.width - 10
                        pos_hint:{"center_x":.5}
                    MDLabel:
                        id:Rep
                        bold:True
                        halign:"center"
                        
                MDRaisedButton:
                    id:"Retour"
                    text:"[b]Retour[/b]"
                    makup:True
                    size_hint_x:None
                    width:TopBar.width - 10
                    pos_hint:{"center_x":.5}
                    md_bg_color:(1,0,0,1)
                    on_release : app.ret2(self)
"""
class ATOApp(MDApp):
    def build(self):
        self.Mode = "Light"
        self.conv = False #cA JA l'ai utiliser plus tard dans Valider2
        self.Deja = False #Comme j'ai utiliser Clock.schedule_once dedans ca permet de voir si le truc est deja utiliser ou pas
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        MAIN = Builder.load_string(Style)
        main = MAIN.ids.Main
        self.Place(MAIN)
        main.padding = [0,0,0,Window.height/2-10]
        return MAIN
    
    def Place(self, MAIN):
        placer = MAIN.ids.Placer
        with placer.canvas.before:
            Color(1, 1, 0, 1)  # Couleur du rectangle
            rect = RoundedRectangle(pos=placer.pos, size=placer.size, radius=[20])
        placer.bind(
            pos=lambda instance, value: self._update(instance, rect),
            size=lambda instance, value: self._update(instance, rect),
        )

    def _update(self, instance, rect):
        rect.pos = instance.pos
        rect.size = instance.size

    def ChangeMode(self):
        if self.Mode == "Light":
            self.Mode = "Dark"
            self.theme_cls.primary_palette = "Yellow"
            self.Icon = "weather-sunny"
        else:
            self.Mode = "Light"
            self.theme_cls.primary_palette = "DeepPurple"
            self.Icon = "weather-night"

        self.theme_cls.theme_style = self.Mode
        self.root.ids.Lab_Page2.color = (1,0,0,1)
        self.root.ids.TopBar.left_action_items = [[self.Icon , lambda x : self.ChangeMode()]]

    def Appui2(self,Button):
        dic = {"[b]Conversion de Base[/b]" : ["Page_2",self.Page2],"[b]Ascci[/b]":["Page_3"]}
        self.root.ids.cr.current = dic.get(Button.text)[0]
        try:
            do = dic.get(Button.text)[1]
            if self.Deja:
                try:
                   self.Conv()
                except:
                    self.root.ids.cr.current = "Page_1"
            else:
                self.Deja = True
                do()
        except:
            pass


    def Page2(self):
        Lay = self.root.ids.Grd
        self.Entry = []
        for i in range(2,17):
              #Creation et ajout de MDTextField(Entry)
              Text = MDTextField(
                   hint_text = f'Base {i}',
                   multiline = False,
                   halign = "center",
                   size_hint_y = None,
                )
              #Text.bind(on_focus = lambda instance ,value : self.Conv(instance,value))
              Lay.add_widget(Text)
              self.Entry.append(Text)
        self.Conv()

    def Conv(self):
        self.Tr = True
        for Enty in self.Entry:
            if Enty.text != "":
                try:
                    Ent = Enty
                    val = Enty.text
                    for i,Entry in enumerate(self.Entry):
                        Avant = Entry.text
                        Rep = str(base_10_k(base_k_10(val,self.Entry.index(Ent)+2),i+2))  #ici j'ai ajouter 2 car enumarate commance par 0 or nous on travail de 2 a 16 
                        print(Rep,Avant)
                        if Avant == "":
                            Entry.text = Rep 
                        elif Avant != Rep:
                            val = Avant 
                            Ent = Entry
                            self.Prend_et_fait(Ent)
                    
                except:
                    self.Err = Ent
                    self.Tr = False
                    
                    self.rep = self.show_error(title = "Error",Message = "Entrez invalide ! ",fonct = self.Ok)
        
        if self.Tr:
            self.action = Clock.schedule_once(lambda dt : self.Conv(), 2)

    def Prend_et_fait(self,Entry):
        val = Entry.text
        for i,Enty in enumerate(self.Entry):
            Enty.text = str(base_10_k(base_k_10(val,self.Entry.index(Entry)+2),i+2))  #ici j'ai ajouter 2 car enumarate commance par 0 or nous on travail de 2 a 16 

    def show_error(self,title,Message,fonct):
        Diag = MDDialog(
            title = title,
            text = Message,
            buttons = [
                MDRaisedButton(
                      text = "Ok",
                      on_release = fonct
                    )
            ]
            )
        Diag.open()
        return Diag

    def Ok(self,instance):
        self.Err.text = ""
        self.rep.dismiss()
        self.Conv()
        
    def Option(self,instance):
        self.Menu = MDDropdownMenu(
            caller = self.root.ids.But,
            items = [
                {
                    "text":"De Carateres en ascii",
                    "viewclass":"OneLineListItem",
                    "on_release":lambda x = "De Carateres en ascii":self.Appui(x)
                    },
                
                {
                    "text": "De ascii en Carateres",
                    "viewclass":"OneLineListItem",
                    "on_release":lambda x = "De ascii en Carateres":self.Appui(x)
                    },
            ],
            width_mult = 4,
        )
        
        self.Menu.open()
    
    def Appui(self,x):
        self.root.ids.But.text = f'[b]{x}[/b]'
        self.root.ids.But.size_hint_x = None
        self.root.ids.But.width = self.root.ids.TopBar.width - 10
        self.root.ids.But.pos_hint = {"center_x":.5}
        self.Menu.dismiss()
        if not self.conv:
            self.Valider2()
    
    
    def Valider2(self):
        Text = self.root.ids.Input
        self.con = True
        But = self.root.ids.But
        if Text.text == "" or But.text not in [f'[b]{elmt}[/b]' for elmt in ["De ascii en Carateres","De Carateres en ascii"]]:
            #self.Opt = self.show_error(title = "Error",Message="Tous les champs ne sont pas remplit !",fonct = self.Vali)
            if Text.text == "":
                self.root.ids.Rep.text = ""
            pass
        
        else:
            Val = Ascci(Text,But).Appui()
            self.root.ids.Rep.text = str(Val)
        
        Clock.schedule_once(lambda dt : self.Valider2() , .2)
            

    def ret1(self,instance):
        #self.root.ids.Page2.clear_widgets()
        Clock.unschedule(self.action)
        self.root.ids.cr.current = "Page_1"
        
    
    def ret2(self,instance):
        #self.root.ids.Page3.clear_widgets()
        self.root.ids.cr.current = "Page_1"
        
    def Vali(self,instance):
        self.Opt.dismiss()

class Ascci:
    def __init__(self,Entry,Choix):
        self.Entry = Entry.text
        self.Choix = Choix.text
        self.ascii_dict = {
        "00": "NUL",
        "01": "SOH",
        "02": "STX",
        "03": "ETX",
        "04": "EOT",
        "05": "ENQ",
        "06": "ACK",
        "07": "BEL",
        "08": "BS",
        "09": "HT",
        "0A": "LF",
        "0B": "VT",
        "0C": "FF",
        "0D": "CR",
        "0E": "SO",
        "0F": "SI",
        "10": "DLE",
        "11": "DC1",
        "12": "DC2",
        "13": "DC3",
        "14": "DC4",
        "15": "NAK",
        "16": "SYN",
        "17": "ETB",
        "18": "CAN",
        "19": "EM",
        "1A": "SUB",
        "1B": "ESC",
        "1C": "FS",
        "1D": "GS",
        "1E": "RS",
        "1F": "US",
        "20": " ",
        "21": "!",
        "22": "\"",
        "23": "#",
        "24": "$",
        "25": "%",
        "26": "&",
        "27": "'",
        "28": "(",
        "29": ")",
        "2A": "*",
        "2B": "+",
        "2C": ",",
        "2D": "-",
        "2E": ".",
        "2F": "/",
        "30": "0",
        "31": "1",
        "32": "2",
        "33": "3",
        "34": "4",
        "35": "5",
        "36": "6",
        "37": "7",
        "38": "8",
        "39": "9",
        "3A": ":",
        "3B": ";",
        "3C": "<",
        "3D": "=",
        "3E": ">",
        "3F": "?",
        "40": "@",
        "41": "A",
        "42": "B",
        "43": "C",
        "44": "D",
        "45": "E",
        "46": "F",
        "47": "G",
        "48": "H",
        "49": "I",
        "4A": "J",
        "4B": "K",
        "4C": "L",
        "4D": "M",
        "4E": "N",
        "4F": "O",
        "50": "P",
        "51": "Q",
        "52": "R",
        "53": "S",
        "54": "T",
        "55": "U",
        "56": "V",
        "57": "W",
        "58": "X",
        "59": "Y",
        "5A": "Z",
        "5B": "[",
        "5C": "\\",
        "5D": "]",
        "5E": "^",
        "5F": "_",
        "60": "`",
        "61": "a",
        "62": "b",
        "63": "c",
        "64": "d",
        "65": "e",
        "66": "f",
        "67": "g",
        "68": "h",
        "69": "i",
        "6A": "j",
        "6B": "k",
        "6C": "l",
        "6D": "m",
        "6E": "n",
        "6F": "o",
        "70": "p",
        "71": "q",
        "72": "r",
        "73": "s",
        "74": "t",
        "75": "u",
        "76": "v",
        "77": "w",
        "78": "x",
        "79": "y",
        "7A": "z",
        "7B": "{",
        "7C": "|",
        "7D": "}",
        "7E": "~",
        "7F": "DEL"
    }
        self.nbr_transf = {y:x for x,y in self.ascii_dict.items()} #Valeur inverse
    
    def Appui(self):
        if self.Choix == "[b]De Carateres en ascii[/b]":
            val_reture = ""
            dic2 = { 
                    x: "e" for x in ["é", "è", "ê"]
                }
            dic2.update({ 
                    r: "a" for r in ["à", "â", "å"]
                })
            dic2.update({ 
                    x: "y" for x in ["ý", "ŷ"]
                })
            dic2.update({ 
                    w: "E" for w in ["Ê", "É", "È"]
                })
            dic2.update({ 
                    x: "A" for x in ["À", "Ê", "Å"]
                })
            dic2.update({ 
                    x: "Y" for x in ["Ý", "Ŷ"]
                })
            dic2.update({ 
                    x: "\"" for x in ["«", "»"]
                })
            dic2.update({ 
                    "ç": "c", "î": "i", "ô": "o", "û": "u", 
                    "Ç": "C", "Î": "I", "Ô": "O", "Û": "U"
                })



            for x in self.Entry:
                    for elmt in dic2.keys():
                        if x in elmt:
                            x = dic2.get(elmt)
                    val_reture += str(self.nbr_transf.get(x))+" "
        else:
            val_reture = ""
            self.Entry = self.Entry.split(" ")
            Li = ["«","»"]
            rep = 0
            for x in self.Entry:
                if x == "22":
                    val_reture += Li[rep]
                    rep = 0 if rep == 1 else 1
                else:
                    val_reture += str(self.ascii_dict.get(x))
                    
        return val_reture
ATOApp().run()