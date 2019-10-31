from .models import DebtorData
import csv
import io

def update_or_create_debtordata(file):
    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string, delimiter=',', quotechar='"')
    next(reader)
    for fields in reader:
        print(fields)
        print('fields: ', fields)
        print(len(fields))
        if len(fields) > 4:
            data_dict = {}
            data_dict['company'] = fields[0]
            data_dict['oarex_rating'] = fields[1]
            data_dict['pay_terms'] = fields[2]
            data_dict['jurisdiction'] = fields[3]
            data_dict['ownership'] = fields[4]
            print('data_dict', data_dict)
            try:
                print('im trying')
                DebtorData.objects.update_or_create(company=data_dict['company'], defaults=data_dict)
            except:
                print('i am in continue')
                continue
        else:
            print('im break')
            break
        

    