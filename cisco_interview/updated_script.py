from get_input  import csv_file
import json

class  citrix_interview_find_average:

    def __init__(self):
        csv_filee=csv_file
        if str(csv_filee)[-3:]== 'csv':
            if csv_filee is not None:
                total_months_avlabule = []
                total_years_avalibule = []
                with open(csv_file, 'r+') as file:
                    data = file.readlines()
                    for j in data:
                        total_months_avlabule.append(j.split(',')[0][:2])
                        total_years_avalibule.append(j.split(',')[0][-4:])

                    self.main_years = sorted(list(set(total_years_avalibule[1:])))
                    self.main_months = sorted(list(set(total_months_avlabule[1:])))
                str_months='january february march april may june july august september october november december'.split()
                string_months={str_months[h]:'0'+str(h+1) for h in range(0,len(str_months))}
                year_data={}
                months_data={}
                def total_years_average():
                    for years in self.main_years:
                        year_data.update(self.yearly_find_average(csv_filee,years))
                    json_data = json.dumps(year_data)
                    return json_data
                print(total_years_average())
                def total_months_averages():
                    for key,value in string_months.items():
                        if len(value)==3:
                            pp=''.join(list(value[1:]))
                            months_data.update(self.monthly_find_average(csv_filee,pp))
                        else:
                            months_data.update(self.monthly_find_average(csv_filee,value))
                    json_data_month=json.dumps(months_data)
                    return json_data_month
                print(total_months_averages())

            else:
                print('please provid INPUT CSV FILE {0}'.format(csv_filee))
        else:
            print('please provide CSV file format  \nyour provided file format {0} '.format(csv_filee))


    def monthly_find_average(self,csv_file,month):

        if month and csv_file is not None:
            with open(csv_file, 'r+') as file:
                data = file.readlines()
                average_monthly = []
                count = 0
                if month in self.main_months:
                    for h in data:
                        list_data = str(h).split(',')
                        if list_data[0][0:2] == month:
                            average_monthly.append(list_data[1][2:])
                            count = count + float(list_data[1][2:])
                    ff = count / len(average_monthly)

                    return {'{0} mothly average'.format(month):ff}
                else:
                    print('please provoide vaild MONTH\nyour provide month {0} \navalabule months {1}'.format(month, self.main_months))
        else:
            print('please provide YEAR AND INPUT CSV FILE')


    def yearly_find_average(self,csv_file,year):

        if year and csv_file is not None:
            with open(csv_file, 'r+') as file:
                data = file.readlines()
                average_yearly = []
                count = 0
                if year in self.main_years:
                    for h in data:
                        list_data = str(h).split(',')
                        if list_data[0][-4:] == year:
                            average_yearly.append(list_data[0][-4:])
                            count = count + float(list_data[1][2:])
                    year_average = count / len(average_yearly)
                    return {'{0} Year average'.format(year):year_average}
                else:
                    print('please provoide vaild year\nyour provide year {0} \nthese are the avalabule years {1}'.format(year,
                                                                                                              self.main_years))
        else:
            print('please provide YEAR AND INPUT CSV FILE')



average_object=citrix_interview_find_average()
