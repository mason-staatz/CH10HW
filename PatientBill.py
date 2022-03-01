import PatientClass as pat
import ProcedureClass as pro

def main():

    ID = 1
    name = 'Matt Jones'
    address = '123 Main st, Waco TX 76706'
    phone = '254-555-7415'
    veteran_status = 'TRUE'
    patients = pat.Patient(ID, name, address, phone, veteran_status)
    
    proc_name = 'Physical Exam'
    proc_date = '2/15/2022' 
    proc_doc = 'Dr. Irvine'
    proc_cost = 250
    patientID = 1
    procedures = pro.Procedure(proc_name, proc_date, proc_doc, proc_cost, patientID)
    cost1= proc_cost

    

    print('*** Patient Bill***')
    print('Name:', patients.get_name())
    print('Address:', patients.get_address())
    print('Phone:', patients.get_phone())
    
    print('\n')


    print('Procedure:', procedures.get_proc_name())
    print('Date:', procedures.get_proc_date())
    print('Practitioner:', procedures.get_proc_doc())
    print('Charge: $', format(procedures.get_proc_cost(), ',.2f'), sep='')

    
    print('\n')
    

    procedures.set_proc_name("MRI")
    procedures.set_proc_date("2/15/2022")
    procedures.set_proc_doc('Dr. Hamilton')
    procedures.set_proc_cost(1500)
    procedures.set_patientID(1)

    print('Procedure:', procedures.get_proc_name())
    print('Date:', procedures.get_proc_date())
    print('Practitioner:', procedures.get_proc_doc())
    print('Charge: $', format(procedures.get_proc_cost(), ',.2f'), sep='')
    cost2= procedures.get_proc_cost()

    

    procedures.set_proc_name("CT Scan")
    procedures.set_proc_date("2/17/2022")
    procedures.set_proc_doc('Dr. Drey')
    procedures.set_proc_cost(1200)
    procedures.set_patientID(2)


    print('\n')


    if veteran_status == 'TRUE':
        total= (cost2+cost1)*.6
    else:
        total= cost2+cost1

    print('Total Charges: $', format(total, ',.2f'), sep='')
        

  

main()