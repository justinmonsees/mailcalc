import tkinter
from tkinter import messagebox
from mailcomp import MailComponent
from paper_db import paper_db

DEFAULT_GAP = 100

class MailCalc:
    def __init__(self,master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master,bg="white")
        self.mainframe.pack(fill=tkinter.BOTH,expand=True)


        ##Initialize instance of the paper_db class
        self.paperDB = paper_db()

        
        ##initialize the list of components
        self.mail_comps = []

##        self.timer_text = tkinter.StringVar()
##        self.timer_text.trace('w',self.build_timer)
##        self.time_left = tkinter.IntVar()
##        self.time_left.set(DEFAULT_GAP)
##        self.time_left.trace('w',self.alert)
##        self.running = False
        
        self.build_grid()
        self.build_banner()
        self.build_sm_grid()
        self.build_calc()
        
#        self.build_buttons()
##        self.build_timer()

##        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.rowconfigure(0,weight=1)
        self.mainframe.rowconfigure(1,weight=4)
        self.mainframe.rowconfigure(2,weight=4)

    def build_banner(self):

        banner_frame = tkinter.Frame(self.mainframe)
        banner_frame.grid(row=0,column=0,sticky="nsew")
        banner_frame.columnconfigure(0,weight=1)
        banner_frame.rowconfigure(0,weight=1)
        banner_frame.rowconfigure(1,weight=1)

        COMP_TYPES = ["Self Mailer","Insert","Booklet","Envelope"]

        self.banner = tkinter.Label(
            banner_frame,
            background="black",
            text="Mailpiece Weight & Thickness Calculator",
            fg="white",
            font=("Helvetica",24)
            )

        self.comp_type_label = tkinter.Label(
            banner_frame,
            text = "Choose your mail component"
            )

        self.comp_type_val = tkinter.StringVar()
        self.comp_type_val.set(COMP_TYPES[0])
    
        self.comp_type =tkinter.OptionMenu(
            banner_frame,
            self.comp_type_val,
            *COMP_TYPES,
            command=self.comp_type_changed
            )

        self.banner.grid(
            row=0,column=0,
            sticky="nsew",
            padx=10,pady=10,
            columnspan=2
            )

        self.comp_type_label.grid(row=1,column=0,sticky="nsew")
        self.comp_type.grid(row=1,column=1,sticky="nsew")
        
 ##--------------------SELF MAILER GRID--------------------------------------       

    def build_sm_grid(self):
        calc_frame = tkinter.Frame(self.mainframe)
        calc_frame.grid(row=1,column=0,sticky="nsew",padx=40)
        calc_frame.columnconfigure(0,weight=1)
        calc_frame.rowconfigure(0,weight=1)
        calc_frame.rowconfigure(1,weight=1)
        calc_frame.rowconfigure(2,weight=1)
        calc_frame.rowconfigure(3,weight=1)

        size_frame = tkinter.Frame(calc_frame)
        size_frame.grid(row=1,column=0,sticky="nsew")
        size_frame.columnconfigure(0,weight=15)
        size_frame.columnconfigure(1,weight=3)
        size_frame.columnconfigure(2,weight=1)
        size_frame.columnconfigure(3,weight=3)
        size_frame.rowconfigure(0,weight=1)
        size_frame.rowconfigure(1,weight=1)

        self.width = tkinter.DoubleVar()
        self.height = tkinter.DoubleVar()

        self.lbl_flat_size = tkinter.Label(
            size_frame,
            bg="white",
            text="Flat Size:",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_height = tkinter.Label(
            size_frame,
            bg="white",
            text="H",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_X = tkinter.Label(
            size_frame,
            bg="white",
            text="X",
            fg="black",
            font=("Helvetica",14)
            )

        self.lbl_width = tkinter.Label(
            size_frame,
            bg="white",
            text="W",
            fg="black",
            font=("Helvetica",14)
            )

        self.height = tkinter.DoubleVar()
        self.height.set(0)
        
        self.ent_height =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.height
            )

        self.width = tkinter.DoubleVar()
        self.width.set(0)
        
        self.ent_width =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.width
            )

        self.lbl_flat_size.grid(row=1,column=0,sticky="ew")
        self.lbl_width.grid(row=0,column=1,sticky="ew")
        self.ent_width.grid(row=1,column=1,sticky="ew")
        self.lbl_X.grid(row=1,column=2,sticky="ew")
        self.lbl_height.grid(row=0,column=3,sticky="ew")
        self.ent_height.grid(row=1,column=3,sticky="ew")

##PAPER GRID SECTION

        paper_frame = tkinter.Frame(calc_frame)
        paper_frame.grid(row=2,column=0,sticky="nsew")
        paper_frame.columnconfigure(0,weight=10)
        paper_frame.columnconfigure(1,weight=10)
        paper_frame.columnconfigure(2,weight=10)
        paper_frame.columnconfigure(3,weight=10)
        paper_frame.rowconfigure(0,weight=1)
        paper_frame.rowconfigure(1,weight=1)
        paper_frame.rowconfigure(2,weight=1)
        paper_frame.rowconfigure(3,weight=1)

        

        PAPER_NAMES = self.paperDB.get_papers()
        PAPER_WEIGHTS = self.paperDB.get_unique_paper_weight()
        PAPER_WEIGHTS.insert(0,'ALL')
        PAPER_TYPES = self.paperDB.get_unique_paper_type()
        PAPER_TYPES.insert(0,'ALL')

        self.lbl_paper_name = tkinter.Label(
            paper_frame,
            bg="white",
            text="Paper:",
            fg="black",
            font=("Helvetica",14),
            )
        self.lbl_num_panels = tkinter.Label(
            paper_frame,
            bg="white",
            text="Number of panels:",
            fg="black",
            font=("Helvetica",14),
            )

        self.num_panels = tkinter.DoubleVar()
        self.num_panels.set(1)
        
        self.ent_num_panels =tkinter.Entry(
            paper_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.num_panels
            )

##        self.lbl_paper_type = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Type",
##            fg="black",
##            font=("Helvetica",14),
##            )
##
##        self.lbl_paper_weight = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Weight",
##            fg="black",
##            font=("Helvetica",14)
##            )


        self.paper_name = tkinter.StringVar()
        self.paper_name.set(PAPER_NAMES[0])

        self.opt_paper_name =tkinter.OptionMenu(
            paper_frame,
            self.paper_name,
            *PAPER_NAMES
            )

        self.paper_type = tkinter.StringVar()
        self.paper_type.set(PAPER_TYPES[0])
     
##        self.opt_paper_type =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_type,
##            *PAPER_TYPES,
##            command = self.refresh_paper_list
##            )
##
##        self.paper_weight = tkinter.StringVar()
##        self.paper_weight.set(PAPER_WEIGHTS[0])       
##
##        self.opt_paper_weight =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_weight,
##            *PAPER_WEIGHTS,
##            command = self.refresh_paper_list
##            )


        self.lbl_paper_name.grid(row=0,column=0,sticky="ew")
        self.opt_paper_name.grid(row=0,column=1,sticky="ew",columnspan=2)
        self.lbl_num_panels.grid(row=2,column=0,sticky="ew")
        self.ent_num_panels.grid(row=2,column=1,sticky="ew")
##        self.lbl_paper_type.grid(row=2,column=0,sticky="ew",columnspan=2)
##        self.opt_paper_type.grid(row=3,column=0,sticky="ew",columnspan=2)
##        self.lbl_paper_weight.grid(row=2,column=2,sticky="ew",columnspan=2)
##        self.opt_paper_weight.grid(row=3,column=2,sticky="ew",columnspan=2)        

 ##--------------------INSERTS GRID--------------------------------------       

    def build_insert_grid(self):
        calc_frame = tkinter.Frame(self.mainframe)
        calc_frame.grid(row=1,column=0,sticky="nsew",padx=40)
        calc_frame.columnconfigure(0,weight=1)
        calc_frame.rowconfigure(0,weight=1)
        calc_frame.rowconfigure(1,weight=1)
        calc_frame.rowconfigure(2,weight=1)
        calc_frame.rowconfigure(3,weight=1)

        size_frame = tkinter.Frame(calc_frame)
        size_frame.grid(row=1,column=0,sticky="nsew")
        size_frame.columnconfigure(0,weight=15)
        size_frame.columnconfigure(1,weight=3)
        size_frame.columnconfigure(2,weight=1)
        size_frame.columnconfigure(2,weight=13)
        size_frame.rowconfigure(0,weight=1)
        size_frame.rowconfigure(1,weight=1)

        self.width = tkinter.DoubleVar()
        self.height = tkinter.DoubleVar()

        self.lbl_flat_size = tkinter.Label(
            size_frame,
            bg="white",
            text="Flat Size:",
            fg="black",
            font=("Helvetica",14),
            )
        
        self.lbl_height = tkinter.Label(
            size_frame,
            bg="white",
            text="H",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_X = tkinter.Label(
            size_frame,
            bg="white",
            text="X",
            fg="black",
            font=("Helvetica",14)
            )

        self.lbl_width = tkinter.Label(
            size_frame,
            bg="white",
            text="W",
            fg="black",
            font=("Helvetica",14)
            )

        self.height = tkinter.DoubleVar()
        self.height.set(0)
        
        self.ent_height =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.height
            )

        self.width = tkinter.DoubleVar()
        self.width.set(0)
        
        self.ent_width =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.width
            )

        self.lbl_flat_size.grid(row=1,column=0,sticky="ew")
        self.lbl_width.grid(row=0,column=1,sticky="ew")
        self.ent_width.grid(row=1,column=1,sticky="ew")
        self.lbl_X.grid(row=1,column=2,sticky="ew")
        self.lbl_height.grid(row=0,column=3,sticky="ew")
        self.ent_height.grid(row=1,column=3,sticky="ew")

##PAPER GRID SECTION

        paper_frame = tkinter.Frame(calc_frame)
        paper_frame.grid(row=2,column=0,sticky="nsew")
        paper_frame.columnconfigure(0,weight=10)
        paper_frame.columnconfigure(1,weight=10)
        paper_frame.columnconfigure(2,weight=10)
        paper_frame.columnconfigure(3,weight=10)
        paper_frame.rowconfigure(0,weight=1)
        paper_frame.rowconfigure(1,weight=1)
        paper_frame.rowconfigure(2,weight=1)
        paper_frame.rowconfigure(3,weight=1)

        

        PAPER_NAMES = self.paperDB.get_papers()
        PAPER_WEIGHTS = self.paperDB.get_unique_paper_weight()
        PAPER_WEIGHTS.insert(0,'ALL')
        PAPER_TYPES = self.paperDB.get_unique_paper_type()
        PAPER_TYPES.insert(0,'ALL')

        self.lbl_paper_name = tkinter.Label(
            paper_frame,
            bg="white",
            text="Paper:",
            fg="black",
            font=("Helvetica",14),
            )
        self.lbl_num_panels = tkinter.Label(
            paper_frame,
            bg="white",
            text="Number of panels:",
            fg="black",
            font=("Helvetica",14),
            )
        self.lbl_num_pages = tkinter.Label(
            paper_frame,
            bg="white",
            text="Number of pages:",
            fg="black",
            font=("Helvetica",14),
            )

        self.num_panels = tkinter.DoubleVar()
        self.num_panels.set(1)
        
        self.ent_num_panels =tkinter.Entry(
            paper_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.num_panels
            )

        self.num_pages = tkinter.DoubleVar()
        self.num_pages.set(1)
        
        self.ent_num_pages =tkinter.Entry(
            paper_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.num_pages
            )

##        self.lbl_paper_type = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Type",
##            fg="black",
##            font=("Helvetica",14),
##            )
##
##        self.lbl_paper_weight = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Weight",
##            fg="black",
##            font=("Helvetica",14)
##            )


        self.paper_name = tkinter.StringVar()
        self.paper_name.set(PAPER_NAMES[0])

        self.opt_paper_name =tkinter.OptionMenu(
            paper_frame,
            self.paper_name,
            *PAPER_NAMES
            )

        self.paper_type = tkinter.StringVar()
        self.paper_type.set(PAPER_TYPES[0])
     
##        self.opt_paper_type =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_type,
##            *PAPER_TYPES,
##            command = self.refresh_paper_list
##            )
##
##        self.paper_weight = tkinter.StringVar()
##        self.paper_weight.set(PAPER_WEIGHTS[0])       
##
##        self.opt_paper_weight =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_weight,
##            *PAPER_WEIGHTS,
##            command = self.refresh_paper_list
##            )


        self.lbl_paper_name.grid(row=0,column=0,sticky="ew")
        self.opt_paper_name.grid(row=0,column=1,sticky="ew",columnspan=2)
        self.lbl_num_panels.grid(row=1,column=0,sticky="ew")
        self.ent_num_panels.grid(row=1,column=1,sticky="ew")
        self.lbl_num_pages.grid(row=2,column=0,sticky="ew")
        self.ent_num_pages.grid(row=2,column=1,sticky="ew")
##        self.lbl_paper_type.grid(row=2,column=0,sticky="ew",columnspan=2)
##        self.opt_paper_type.grid(row=3,column=0,sticky="ew",columnspan=2)
##        self.lbl_paper_weight.grid(row=2,column=2,sticky="ew",columnspan=2)
##        self.opt_paper_weight.grid(row=3,column=2,sticky="ew",columnspan=2)

 ##--------------------BOOKLETS GRID--------------------------------------       

    def build_booklet_grid(self):
        calc_frame = tkinter.Frame(self.mainframe)
        calc_frame.grid(row=1,column=0,sticky="nsew",padx=40)
        calc_frame.columnconfigure(0,weight=1)
        calc_frame.rowconfigure(0,weight=1)
        calc_frame.rowconfigure(1,weight=1)
        calc_frame.rowconfigure(2,weight=1)
        calc_frame.rowconfigure(3,weight=1)

        size_frame = tkinter.Frame(calc_frame)
        size_frame.grid(row=1,column=0,sticky="nsew")
        size_frame.columnconfigure(0,weight=10)
        size_frame.columnconfigure(1,weight=1)
        size_frame.columnconfigure(2,weight=10)
        size_frame.rowconfigure(0,weight=1)
        size_frame.rowconfigure(1,weight=1)

        self.width = tkinter.DoubleVar()
        self.height = tkinter.DoubleVar()

        self.lbl_finished_size = tkinter.Label(
            size_frame,
            bg="white",
            text="Finished Size:",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_height = tkinter.Label(
            size_frame,
            bg="white",
            text="H",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_X = tkinter.Label(
            size_frame,
            bg="white",
            text="X",
            fg="black",
            font=("Helvetica",14)
            )

        self.lbl_width = tkinter.Label(
            size_frame,
            bg="white",
            text="W",
            fg="black",
            font=("Helvetica",14)
            )

        self.height = tkinter.DoubleVar()
        self.height.set(0)
        
        self.ent_height =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.height
            )

        self.width = tkinter.DoubleVar()
        self.width.set(0)
        
        self.ent_width =tkinter.Entry(
            size_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.width
            )

        self.lbl_finished_size.grid(row=1,column=0,sticky="ew")
        self.lbl_width.grid(row=0,column=1,sticky="ew")
        self.ent_width.grid(row=1,column=1,sticky="ew")
        self.lbl_X.grid(row=1,column=2,sticky="ew")
        self.lbl_height.grid(row=0,column=3,sticky="ew")
        self.ent_height.grid(row=1,column=3,sticky="ew")

##PAPER GRID SECTION

        paper_frame = tkinter.Frame(calc_frame)
        paper_frame.grid(row=2,column=0,sticky="nsew")
        paper_frame.columnconfigure(0,weight=10)
        paper_frame.columnconfigure(1,weight=10)
        paper_frame.columnconfigure(2,weight=10)
        paper_frame.columnconfigure(3,weight=10)
        paper_frame.rowconfigure(0,weight=1)
        paper_frame.rowconfigure(1,weight=1)
        paper_frame.rowconfigure(2,weight=1)
        paper_frame.rowconfigure(3,weight=1)

        

        PAPER_NAMES = self.paperDB.get_papers()
        PAPER_WEIGHTS = self.paperDB.get_unique_paper_weight()
        PAPER_WEIGHTS.insert(0,'ALL')
        PAPER_TYPES = self.paperDB.get_unique_paper_type()
        PAPER_TYPES.insert(0,'ALL')

        self.lbl_is_self_cover = tkinter.Label(
            paper_frame,
            bg="white",
            text="Self cover?",
            fg="black",
            font=("Helvetica",14),
            )
                
        self.lbl_cvr_paper_name = tkinter.Label(
            paper_frame,
            bg="white",
            text="Cover Paper",
            fg="black",
            font=("Helvetica",14),
            )
        self.lbl_txt_paper_name = tkinter.Label(
            paper_frame,
            bg="white",
            text="Text Paper",
            fg="black",
            font=("Helvetica",14),
            )

        self.lbl_num_pages = tkinter.Label(
            paper_frame,
            bg="white",
            text="Number of pages",
            fg="black",
            font=("Helvetica",14),
            )

        self.num_pages = tkinter.DoubleVar()
        self.num_pages.set(8)
        
        self.ent_num_pages =tkinter.Entry(
            paper_frame,
            bg="white",
            fg="black",
            width=10,
            justify=tkinter.CENTER,
            textvariable=self.num_pages
            )

##        self.lbl_paper_type = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Type",
##            fg="black",
##            font=("Helvetica",14),
##            )
##
##        self.lbl_paper_weight = tkinter.Label(
##            paper_frame,
##            bg="white",
##            text="Paper Weight",
##            fg="black",
##            font=("Helvetica",14)
##            )


        self.cvr_paper_name = tkinter.StringVar()
        self.cvr_paper_name.set(PAPER_NAMES[0])

        self.opt_cvr_paper_name =tkinter.OptionMenu(
            paper_frame,
            self.cvr_paper_name,
            *PAPER_NAMES
            )

        self.txt_paper_name = tkinter.StringVar()
        self.txt_paper_name.set(PAPER_NAMES[0])

        self.opt_txt_paper_name =tkinter.OptionMenu(
            paper_frame,
            self.txt_paper_name,
            *PAPER_NAMES
            )

        self.is_self_cover = tkinter.StringVar()
        self.is_self_cover.set("No")


        self.opt_is_self_cover = tkinter.OptionMenu(
            paper_frame,
            self.is_self_cover,
            "No",
            "Yes",
            command = self.toggle_cover_option
            )
        
##        self.paper_type = tkinter.StringVar()
##        self.paper_type.set(PAPER_TYPES[0])
     
##        self.opt_paper_type =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_type,
##            *PAPER_TYPES,
##            command = self.refresh_paper_list
##            )
##
##        self.paper_weight = tkinter.StringVar()
##        self.paper_weight.set(PAPER_WEIGHTS[0])       
##
##        self.opt_paper_weight =tkinter.OptionMenu(
##            paper_frame,
##            self.paper_weight,
##            *PAPER_WEIGHTS,
##            command = self.refresh_paper_list
##            )

        self.lbl_is_self_cover.grid(row=0,column=0,sticky="ew")
        self.opt_is_self_cover.grid(row=0,column=1,sticky="ew")
        self.lbl_cvr_paper_name.grid(row=1,column=0,sticky="ew")
        self.opt_cvr_paper_name.grid(row=1,column=1,sticky="ew",columnspan=2)
        self.lbl_txt_paper_name.grid(row=2,column=0,sticky="ew")
        self.opt_txt_paper_name.grid(row=2,column=1,sticky="ew",columnspan=2)
        self.lbl_num_panels.grid(row=3,column=0,sticky="ew")
        self.ent_num_panels.grid(row=3,column=1,sticky="ew")
        self.lbl_num_pages.grid(row=4,column=0,sticky="ew")
        self.ent_num_pages.grid(row=4,column=1,sticky="ew")
##        self.lbl_paper_type.grid(row=2,column=0,sticky="ew",columnspan=2)
##        self.opt_paper_type.grid(row=3,column=0,sticky="ew",columnspan=2)
##        self.lbl_paper_weight.grid(row=2,column=2,sticky="ew",columnspan=2)
##        self.opt_paper_weight.grid(row=3,column=2,sticky="ew",columnspan=2) 

##-----------------------ENVELOPE GRID SECTION--------------------------------------------------
    def build_envelope_grid(self):

        calc_frame = tkinter.Frame(self.mainframe)
        calc_frame.grid(row=1,column=0,sticky="nsew",padx=40)
        calc_frame.columnconfigure(0,weight=1)
        calc_frame.rowconfigure(0,weight=1)

        paper_frame = tkinter.Frame(calc_frame)
        paper_frame.grid(row=0,column=0,sticky="nsew")
        paper_frame.columnconfigure(0,weight=1)
        paper_frame.columnconfigure(1,weight=1)
        paper_frame.columnconfigure(2,weight=1)
        paper_frame.columnconfigure(3,weight=1)
        paper_frame.columnconfigure(4,weight=1)
        paper_frame.rowconfigure(0,weight=1)
        paper_frame.rowconfigure(1,weight=1)

        PAPER_NAMES = self.paperDB.get_envelopes()
        
        self.lbl_paper_name = tkinter.Label(
            paper_frame,
            bg="white",
            text="Envelope Type",
            fg="black",
            font=("Helvetica",14),
            )

        self.paper_name = tkinter.StringVar()

        if len(PAPER_NAMES) > 0:
            self.paper_name.set(PAPER_NAMES[0])
    
        self.opt_paper_name =tkinter.OptionMenu(
            paper_frame,
            self.paper_name,
            *PAPER_NAMES
            )

        self.lbl_paper_name.grid(row=0,column=2,sticky="ew")
        self.opt_paper_name.grid(row=1,column=1,sticky="ew",columnspan=3)
           

##-------------------BUTTON GRID SECTION---------------------------------
        
    def build_calc(self):
        
        button_frame = tkinter.Frame(self.mainframe)
        button_frame.grid(row=2,column=0,sticky="nsew")
        button_frame.columnconfigure(0,weight=1)
        button_frame.columnconfigure(1,weight=1)
        button_frame.columnconfigure(2,weight=1)
        button_frame.columnconfigure(3,weight=1)
        button_frame.columnconfigure(4,weight=1)
        button_frame.rowconfigure(0,weight=1)
        button_frame.rowconfigure(1,weight=1)
        button_frame.rowconfigure(2,weight=1)
        button_frame.rowconfigure(3,weight=1)
        button_frame.rowconfigure(4,weight=1)

        self.add_button = tkinter.Button(
            button_frame,
            text="Add",
            command=self.add_component
            )

        self.remove_button = tkinter.Button(
            button_frame,
            text="Remove",
            command=self.remove_component
            )

        self.component_list = tkinter.Listbox(
            button_frame
            )

        self.calc_button = tkinter.Button(
            button_frame,
            text="Calculate",
            command=self.calculate
            )
         

        self.lbl_weight_oz = tkinter.Label(
            button_frame,
            bg="white",
            text="Weight(oz):",
            fg="black",
            font=("Helvetica",14),
            )
        
        self.lbl_thickness_in = tkinter.Label(
            button_frame,
            bg="white",
            text="Thickness(in):",
            fg="black",
            font=("Helvetica",14),
            )

        self.weight_oz = tkinter.DoubleVar()
        self.weight_oz.set(0)
        
        self.lbl_calculated_weight = tkinter.Label(
            button_frame,
            bg="white",
            textvariable = self.weight_oz,
            fg="black",
            font=("Helvetica",14),
            )

        self.thickness_in = tkinter.DoubleVar()
        self.thickness_in.set(0)
        
        self.lbl_calculated_thickness = tkinter.Label(
            button_frame,
            bg="white",
            textvariable= self.thickness_in,
            fg="black",
            font=("Helvetica",14),
            )
        
         

        self.add_button.grid(row=0,column=1,sticky="ew")
        self.remove_button.grid(row=0,column=3,sticky="ew")
        self.component_list.grid(row=1,column=1,sticky="ew",columnspan=3)
        self.calc_button.grid(row=2,column=1,sticky="ew",columnspan=3)
        self.lbl_weight_oz.grid(row=3,column=1,sticky="ew")
        self.lbl_calculated_weight.grid(row=4,column=1,sticky="ew")
        self.lbl_thickness_in.grid(row=3,column=3,sticky="ew")
        self.lbl_calculated_thickness.grid(row=4,column=3,sticky="ew")
        


    def add_component(self):

        cur_comp_type = self.comp_type_val.get()
        ##ADD SOME INPUT VALIDATION TO NOT COMPONENTS WITH INVALID WIDTH OR HEIGHT
        
        if cur_comp_type.lower() == "self mailer":
            cur_width = self.width.get()
            cur_height = self.height.get()
            cur_paper_name = self.paper_name.get()
            cur_paper_type = self.paperDB.get_paper_type(cur_paper_name)
            cur_paper_weight = self.paperDB.get_paper_weightLB(cur_paper_name)
            cur_num_panels = self.num_panels.get()

            mail_comp = MailComponent(cur_comp_type,width=cur_width,height=cur_height,paper_name=cur_paper_name)
            self.mail_comps.append((mail_comp.get_weight(),mail_comp.get_caliper()*cur_num_panels))
            self.component_list.insert(tkinter.END,mail_comp)

        elif cur_comp_type.lower() == "envelope":
            env_paper_name = self.paper_name.get()
            env_mail_comp = MailComponent(cur_comp_type,paper_name=env_paper_name)
            self.mail_comps.append((env_mail_comp.get_weight(),env_mail_comp.get_caliper()))
            self.component_list.insert(tkinter.END,env_mail_comp)

        elif cur_comp_type.lower() == "insert":

            cur_width = self.width.get()
            cur_height = self.height.get()
            cur_paper_name = self.paper_name.get()
            cur_num_panels = self.num_panels.get()
            cur_num_pages = self.num_pages.get()

            mail_comp = MailComponent(cur_comp_type,width=cur_width,height=cur_height,paper_name=cur_paper_name)
            self.mail_comps.append((mail_comp.get_weight()*cur_num_pages,mail_comp.get_caliper()*cur_num_panels*cur_num_pages))
            self.component_list.insert(tkinter.END,mail_comp)
        ##  print(env_mail_comp.get_weight())

        elif cur_comp_type.lower() == "booklet":

            is_self_cover = self.is_self_cover.get()
            cur_width = self.width.get() * 2
            cur_height = self.height.get()
            cur_num_pages = self.num_pages.get() / 4 ##Calculate number of sheets for the booklet

            if is_self_cover.lower() == "no":
                cur_cvr_paper_name = self.cvr_paper_name.get()
                cover_mail_comp = MailComponent(cur_comp_type + " Cover",width=cur_width,height=cur_height,paper_name=cur_cvr_paper_name)
                self.mail_comps.append((cover_mail_comp.get_weight(),cover_mail_comp.get_caliper()*2))
                self.component_list.insert(tkinter.END,cover_mail_comp)
                cur_num_pages -=1 

            cur_txt_paper_name = self.txt_paper_name.get()
            text_mail_comp = MailComponent(cur_comp_type + " Text",width=cur_width,height=cur_height,paper_name=cur_txt_paper_name)
            self.mail_comps.append((text_mail_comp.get_weight()*cur_num_pages,text_mail_comp.get_caliper()*cur_num_pages*2))
            self.component_list.insert(tkinter.END,text_mail_comp)
                
                

    def remove_component(self):

        cur_selection = self.component_list.curselection()
        try:
            print(cur_selection[0])
            ##delete the component from the list box
            self.component_list.delete(cur_selection[0])
            ##delete the component from the list of weights/thicknesses
            del self.mail_comps[cur_selection[0]]
        ##if someone hits the remove button but no item in the list box is selected
       ##just ignore the error and don't do anything
        except IndexError:
             pass
            
    def comp_type_changed(self,*args):
        self.component_type = args[0]

        if self.component_type == "Envelope":
            self.build_envelope_grid()
        elif self.component_type == "Self Mailer":
            self.build_sm_grid()
        elif self.component_type == "Insert":
            self.build_insert_grid()
        elif self.component_type == "Booklet":
            self.build_booklet_grid()
        
        print(self.component_type)

    def refresh_paper_list(self,*args):

        self.paper_arg = args[0]
        
        paper_type = self.paper_type.get()
        paper_weight = self.paper_weight.get()

        menu = self.opt_paper_name.children["menu"]
        self.paper_name.set('')
        menu.delete(0, 'end')
        
        PAPER_NAMES = self.paperDB.get_papers(paper_type.upper(),paper_weight)

        for paper in PAPER_NAMES:
                menu.add_command(label=paper,command=tkinter._setit(self.paper_name,paper))


        if len(PAPER_NAMES) > 0:
            self.paper_name.set(PAPER_NAMES[0])

    def toggle_cover_option(self,*args):

        is_self_cover = args[0]

        if is_self_cover.lower() == "yes":
            self.opt_cvr_paper_name.config(state="disabled")
        elif is_self_cover.lower() == "no":
            self.opt_cvr_paper_name.config(state="enabled")

    def calculate(self,*args):

        total_weight = 0
        total_thickness = 0

        for weight,thickness in self.mail_comps:
            total_weight += weight
            total_thickness += thickness

        self.weight_oz.set(total_weight)
        self.thickness_in.set(total_thickness)
        
        print(self.mail_comps)

        
if __name__ == '__main__':
    
    root = tkinter.Tk()
    root.title("Mail Piece Calculator")
    MailCalc(root)
    
    root.mainloop()
