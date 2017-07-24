import sqlite3
class paper_db:
    
    def __init__(self):

        self.my_conn = sqlite3.Connection('paper.db')

        self.c = self.my_conn.cursor()
##c.execute('SELECT * FROM paper WHERE paper_type = "TEXT"')
##rows = c.fetchall()

    def get_papers(self,paper_type='ALL',paper_weight='ALL'):

        if paper_type == 'ALL' and paper_weight == 'ALL':
            query = 'SELECT paper_name FROM paper'
        elif paper_type != 'ALL' and paper_weight == 'ALL':
            query = 'SELECT paper_name FROM paper WHERE paper_type ="' + paper_type + '"'
        elif paper_type == 'ALL' and paper_weight != 'ALL':
            query = 'SELECT paper_name FROM paper WHERE weight_lb ="' + paper_weight + '"'
        else:
            query = 'SELECT paper_name FROM paper WHERE paper_type ="' + paper_type + '" AND weight_lb="' + paper_weight + '"'
            
        self.c.execute(query)
        results = self.c.fetchall()

        paper_list= []
        for item in results:
            paper_list.append(item[0])
        
        return(paper_list)

    ##GET PAPER TYPE - USED TO GET BASIS SIZE FOR PAPER WEIGHT IN GSM FUNC

    def get_paper_type(self,paper_name):

        query = 'SELECT paper_type FROM paper WHERE paper_name = "' + paper_name + '"'

        self.c.execute(query)
        result = self.c.fetchall()

        paper_type = result[0][0]

        return(paper_type)

    ## GET UNIQUE PAPER TYPES

    def get_unique_paper_type(self):

        query = 'SELECT DISTINCT paper_type FROM paper'

        self.c.execute(query)
        results = self.c.fetchall()

        paper_types = []

        for item in results:
            paper_types.append(item[0].title())

        return(paper_types)

     ## GET UNIQUE PAPER WEIGHTS

    def get_unique_paper_weight(self):

        query = 'SELECT DISTINCT weight_lb FROM paper'

        self.c.execute(query)
        results = self.c.fetchall()

        paper_weights = []

        for item in results:
            paper_weights.append(item[0])

        return(paper_weights)

    ##GET PAPER WEIGHT_LB - USED TO GET BASIS SIZE FOR PAPER WEIGHT IN GSM FUNC

    def get_paper_weightLB(self,paper_name):

        query = 'SELECT weight_lb FROM paper WHERE paper_name = "' + paper_name + '"'

        self.c.execute(query)
        result = self.c.fetchall()

        paper_weightLB = result[0][0]

        return(paper_weightLB)
    
    ##GET PAPER CALIPER

    def get_paper_caliper(self,paper_name):

        query = 'SELECT caliper FROM paper WHERE paper_name = ' + '"' + paper_name + '"'

        self.c.execute(query)
        result = self.c.fetchall()

        caliper = result[0][0]

        return(caliper)
    
    ##GET PAPER WEIGHT IN GSM - REQUIRES CALCULATION
    def get_paper_gsm(self,paper_name):

        paper_type = self.get_paper_type(paper_name)

        ##Get the width and height of the basis size to calculate basis_weight(width*height)

        query = 'SELECT width,height FROM basis_weight WHERE paper_type = "' + paper_type + '"'

        self.c.execute(query)
        results = self.c.fetchall()
        basis_size = results[0][0] * results[0][1]
        basis_weight = self.get_paper_weightLB(paper_name)

        gsm = (basis_weight * 1406.5) / basis_size
        gsm = round(gsm,2)

        return(gsm)


    def get_envelopes(self):

        query = 'SELECT env_name FROM envelope'

        self.c.execute(query)
        results = self.c.fetchall()

        env_list = []
        for item in results:
            env_list.append(item[0])

        return(env_list)

    def get_env_weight(self,env_name):

        query = 'SELECT weight_oz FROM envelope WHERE env_name="' + env_name + '"'

        self.c.execute(query)
        results = self.c.fetchall()

        return(results[0][0])

    ##GET ENVELOPE CALIPER

    def get_env_caliper(self,paper_name):

        query = 'SELECT caliper FROM envelope WHERE env_name = ' + '"' + paper_name + '"'

        self.c.execute(query)
        result = self.c.fetchall()

        caliper = result[0][0]

        return(caliper)
        
        

##paperDB = paper_db()
##
##papers = paperDB.get_papers()
##paper_type = paperDB.get_paper_type('Tango C2S - 14pt')
##caliper = paperDB.get_paper_caliper('Tango C2S - 14pt')
##paper_gsm = paperDB.get_paper_gsm('Tango C2S - 14pt')
##print(paper_gsm)
