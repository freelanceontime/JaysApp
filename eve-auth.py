import requests
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import csv
import os


### Global Variables ###

### Functions ###

### Main ###

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        #self.geometry("400x400")
        self.title("Jays App")

        container = Frame(self)
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, LiveFeed):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def GetAuth():
            urltest = "https://login.eveonline.com/oauth/authorize?response_type=code&redirect_uri=https://oauth.pstmn.io/v1/callback&client_id=ce0b56d4274e4e78bdd689efbfe30614&scope=esi-characters.read_corporation_roles.v1 esi-corporations.read_corporation_membership.v1 esi-corporations.read_divisions.v1 esi-corporations.read_facilities.v1 esi-corporations.read_starbases.v1 esi-corporations.read_structures.v1 esi-industry.read_character_mining.v1 esi-industry.read_corporation_mining.v1 esi-search.search_structures.v1 esi-universe.read_structures.v1"
            webbrowser.open_new(urltest)

        def getToken():
            try:
                code = inputCC1.get()

                headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic Y2UwYjU2ZDQyNzRlNGU3OGJkZDY4OWVmYmZlMzA2MTQ6bWVLVkhnS29MZExPMFlyQ2F3MGdnc3U4bmdlM0V1SmdvRDZSRjB0cg==',
                'User-Agent': 'My User Agent 1.0',
                }

                data = '{"grant_type":"authorization_code", "redirect_uri": "https://oauth.pstmn.io/v1/callback", "client_id": "ce0b56d4274e4e78bdd689efbfe30614", "code":"' + code + '"}'

                response = requests.post('https://login.eveonline.com/oauth/token', headers=headers, data=data)
                code = response.json()

                StartPage.token = code['access_token']

                print(StartPage.token)

            except KeyError:
                messagebox.showerror("Oops", "That Key is Incorrect or the has already been used")

        
        def chosen(event):
            myLabel = Label(self, text=clickedRss.get())
            if clickedRss.get() == StartPage.observernames[0]:
                StartPage.selected = StartPage.observeritems[0]

            elif clickedRss.get() == StartPage.observernames[1]:
                StartPage.selected = StartPage.observeritems[1]

            elif clickedRss.get() == StartPage.observernames[2]:
                StartPage.selected = StartPage.observeritems[2]

            elif clickedRss.get() == StartPage.observernames[3]:
                StartPage.selected = StartPage.observeritems[3]

            elif clickedRss.get() == StartPage.observernames[4]:
                StartPage.selected = StartPage.observeritems[4]

            elif clickedRss.get() == StartPage.observernames[5]:
                StartPage.selected = StartPage.observeritems[5]

            elif clickedRss.get() == StartPage.observernames[6]:
                StartPage.selected = StartPage.observeritems[6]

            elif clickedRss.get() == StartPage.observernames[7]:
                StartPage.selected = StartPage.observeritems[7]

            elif clickedRss.get() == StartPage.observernames[8]:
                StartPage.selected = StartPage.observeritems[8]

            elif clickedRss.get() == StartPage.observernames[9]:
                StartPage.selected = StartPage.observeritems[9]

            elif clickedRss.get() == StartPage.observernames[10]:
                StartPage.selected = StartPage.observeritems[10]

            elif clickedRss.get() == StartPage.observernames[11]:
                StartPage.selected = StartPage.observeritems[11]

            elif clickedRss.get() == StartPage.observernames[12]:
                StartPage.selected = StartPage.observeritems[12]

            elif clickedRss.get() == StartPage.observernames[13]:
                StartPage.selected = StartPage.observeritems[13]

            elif clickedRss.get() == StartPage.observernames[14]:
                StartPage.selected = StartPage.observeritems[14]

            elif clickedRss.get() == StartPage.observernames[15]:
                StartPage.selected = StartPage.observeritems[15]

            elif clickedRss.get() == StartPage.observernames[16]:
                StartPage.selected = StartPage.observeritems[16]

            elif clickedRss.get() == StartPage.observernames[16]:
                StartPage.selected = StartPage.observeritems[16]

            elif clickedRss.get() == StartPage.observernames[17]:
                StartPage.selected = StartPage.observeritems[17]

            elif clickedRss.get() == StartPage.observernames[18]:
                StartPage.selected = StartPage.observeritems[18]

            elif clickedRss.get() == StartPage.observernames[19]:
                StartPage.selected = StartPage.observeritems[19]

            elif clickedRss.get() == StartPage.observernames[20]:
                StartPage.selected = StartPage.observeritems[20]

            elif clickedRss.get() == StartPage.observernames[21]:
                StartPage.selected = StartPage.observeritems[21]

            elif clickedRss.get() == StartPage.observernames[22]:
                StartPage.selected = StartPage.observeritems[22]

            elif clickedRss.get() == StartPage.observernames[23]:
                StartPage.selected = StartPage.observeritems[23]

            elif clickedRss.get() == StartPage.observernames[24]:
                StartPage.selected = StartPage.observeritems[24]

            elif clickedRss.get() == StartPage.observernames[25]:
                StartPage.selected = StartPage.observeritems[25]

            return StartPage.selected

        def observersnew():    
            try:
                url1 = "https://esi.evetech.net/latest/corporation/" + str(inputCC2.get()) + "/mining/observers?datasource=tranquility&token=" + StartPage.token

                page = requests.get(url1)
                data = page.json()

                StartPage.observeritems = []
                StartPage.observernames = []

                observers = 0
                for x in data:
                    structureid = str(data[observers]['observer_id'])
                    url2 = "https://esi.evetech.net/latest/universe/structures/" + structureid + "/?datasource=tranquility&language=en&page=1&token=" + StartPage.token
                    Structures = requests.get(url2)
                    Structuresdata = Structures.json()
                    StartPage.observernames.append(Structuresdata['name'])
                    StartPage.observeritems.append(data[observers]['observer_id'])
                    observers = observers + 1

                print(StartPage.observeritems)

                global clickedRss
                clickedRss = StringVar()
                clickedRss.set(StartPage.observernames[0])
                drop2 = OptionMenu(self, clickedRss, *StartPage.observernames, command=chosen)
                drop2.config(width=32)
                drop2.grid(row=10, column=0, padx=10, pady=10)

                label = Label(self, text="Please Select One of the Below Observers")
                label.grid(row=9, column=0, padx=10, pady=10)

            except KeyError:
                messagebox.showerror("Oops", "You are not allowed to see this Data or you Key has expired")
            except AttributeError:
                messagebox.showerror("Oops", "You have not entered a Key")      

        def miners():
            my_progress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='indeterminate')
            my_progress.start(30)
            my_progress.grid(row=13, column=0, padx=10, pady=20) 


            try:        
                url2 = "https://esi.evetech.net/latest/corporation/" + str(inputCC2.get()) + "/mining/observers/" + str(StartPage.selected) +"?datasource=tranquility&token=" + str(StartPage.token)

                page2 = requests.get(url2)
                StartPage.data2 = page2.json()

                StartPage.observerid = clickedRss.get()

                characters = 0
                placedrt2 = {}
                case_changeme1 = []
                case_changeme2 = []
                case_changeme3 = []
                case_changeme4 = []
                case_changeme5 = []
                case_changeme6 = []
                placedrt2 = {}


                for x in StartPage.data2:
                    try:
                        self.update()

                        characterName = requests.get("https://esi.evetech.net/latest/characters/" + str(StartPage.data2[(characters)]['character_id']) + "/?datasource=tranquility")
                        nameData = characterName.json()

                        pagecontents = nameData['name']

                        characterName = requests.get("https://esi.evetech.net/latest/universe/types/" + str(StartPage.data2[(characters)]['type_id']) + "/?datasource=tranquility")
                        OreData = characterName.json()

                        pagecontents2 = OreData['name']

                        case2 = placedrt2["Character"] = pagecontents
                        case_changeme1.append(case2)

                        case4 = placedrt2["CharacterID"] = StartPage.data2[(characters)]['character_id']
                        case_changeme2.append(case4)

                        case6 = placedrt2["Quantity"] = StartPage.data2[(characters)]['quantity']
                        case_changeme3.append(case6)

                        case8 = placedrt2["Item"] = pagecontents2
                        case_changeme4.append(case8)

                        case9 = placedrt2["ItemID"] = StartPage.data2[(characters)]['type_id']
                        case_changeme5.append(case9)                        

                        case10 = placedrt2["last_updated"] = StartPage.data2[(characters)]['last_updated']
                        case_changeme6.append(case10)

                        characters = characters +1
                    except ValueError:
                        continue
                
            except KeyError:
                messagebox.showerror("Oops", "You have not Obtained the Observers, Or your Key has Expired")
            except NameError:
                messagebox.showerror("Oops", "You have not Obtained the Observers, Or your Key has Expired")
            

            with open(os.environ["HOMEPATH"] + '\Desktop\MiningData_' + str(clickedRss.get()) + '.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)  
                writer.writerow(['Character Name', 'Character ID', 'Amount Mined', 'Item ID', 'Item Name', 'Last Updated', 'Moon Name']) 
                for v,u,g,h,a,m in (zip(case_changeme1,case_changeme2,case_changeme3,case_changeme5,case_changeme4,case_changeme6)):
                    writer.writerow([v,u,g,h,a,m,str(StartPage.observerid)]) 

            print("Completed Data Export Succesfully")
            my_progress.destroy()

        label = Label(self, width=50, text="Please follow the below steps")
        label.grid(row=1, column=0, padx=10, pady=10)

        Character = Button(self, width=20, text="1. Get Auth Token", command=GetAuth)
        Character.grid(row=2, column=0, padx=10, pady=10)

        label = Label(self, text="Please Input The Token from the URL e.g'code=[token]'")
        label.grid(row=3, column=0, padx=10, pady=10)

        inputCC1 = Entry(self, font=('Helvetica',10))
        inputCC1.grid(row=4, column=0, padx=10, pady=0) 

        Character = Button(self, width=20, text="2. Submit", command=getToken)
        Character.grid(row=5, column=0, padx=10, pady=10)

        label = Label(self, text="Please Input Your Corperation ID")
        label.grid(row=6, column=0, padx=10, pady=10)

        inputCC2 = Entry(self, font=('Helvetica',10))
        inputCC2.grid(row=7, column=0, padx=10, pady=0) 

        Character = Button(self, width=20, text="3. Get Observers", command=observersnew)
        Character.grid(row=8, column=0, padx=10, pady=10)

        label = Label(self, wraplength=250, text="Please Note the application will appear to stop responding while it gets the information \n\n Please Find the file on your Desktop after you 'Get mining Data'")
        label.grid(row=11, column=0, padx=10, pady=10)

        Character = Button(self, width=20, text="4. Get mining Data", command=miners)
        Character.grid(row=12, column=0, padx=10, pady=10)

        WithoutJ = Button(self, width=20, text="Character Name Finder", command=lambda:controller.show_frame(LiveFeed))
        WithoutJ.grid(row=13, column=0, padx=10, pady=10)

class LiveFeed(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def getChar():
                characterName = requests.get("https://esi.evetech.net/latest/characters/" + str(inputCC3.get()) + "/?datasource=tranquility")
                nameData = characterName.json()

                name = nameData['name']

                print(name + " " + str(inputCC3.get()))

                inputCC4 = Entry(self, width=20, text="", font=('Helvetica',10))
                inputCC4.grid(row=4, column=0, padx=10, pady=0) 

                inputCC4.insert(0, name)


        label = Label(self, width=50, text="Chracter ID Finder")
        label.grid(row=1, column=0, padx=10, pady=10)

        label = Label(self, text="Please Input The Character ID")
        label.grid(row=2, column=0, padx=10, pady=10)

        inputCC3 = Entry(self, font=('Helvetica',10))
        inputCC3.grid(row=3, column=0, padx=10, pady=0) 

        Character = Button(self, width=20, text="Submit", command=getChar)
        Character.grid(row=5, column=0, padx=10, pady=10)

        back = Button(self, width=20, text="Back", command=lambda:controller.show_frame(StartPage))
        back.grid(row=6, column=0, padx=10, pady=10)


app = App()
app.mainloop()
