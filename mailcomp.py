from paper_db import paper_db

class MailComponent:

    def __init__(self,mail_type,**kwargs):

        ##Initialize instance of the paper_db class
        self.paperDB = paper_db()

        self.mail_type = mail_type

        options = {
            'width' : None,
            'height' : None,
            'paper_name' : None,
            }

        options.update(kwargs)

        self.width = options.get('width')
        self.height = options.get('height')
        self.paper_name = options.get('paper_name')
        self.paper_type = self.paperDB.get_paper_type(self.paper_name)
        self.paper_weight = self.paperDB.get_paper_weightLB(self.paper_name)

    def __str__(self):
        ##return (str(self.width) + "x" + str(self.height) + "-" + mail_type + " " + paper_weight + " " + paper_type
        return("{}x{} - {} - {}".format(str(self.width),str(self.height),str(self.paper_name),str(self.mail_type)))

    def __repr__(self):
        return self.__str__()

    def get_caliper(self):
        return(self.paperDB.get_paper_caliper(self.paper_name))

    def get_weight(self):
        sq_in = self.width * self.height
        sq_m = sq_in/1550
        gsm_per_sheet = sq_m * self.paperDB.get_paper_gsm(self.paper_name)

        weight_oz = gsm_per_sheet * .03527396195

        return(round(weight_oz,2))


    
