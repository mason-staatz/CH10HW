class Procedure:
    def __init__(self, proc_name, proc_date, proc_doc, proc_cost, patientID):
        self.__proc_name = proc_name
        self.__proc_date = proc_date
        self.__proc_doc = proc_doc
        self.__proc_cost = proc_cost
        self.__patientID = patientID

    def get_proc_name(self):
        return self.__proc_name

    def get_proc_date(self):
        return self.__proc_date

    def get_proc_doc(self):
        return self.__proc_doc

    def get_proc_cost(self):
        return self.__proc_cost

    def get_patientID(self):
        return self.__patientID
