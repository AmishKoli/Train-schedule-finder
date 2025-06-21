import requests
class IRCTC:
    def __init__(self):
        user_input=input('''Enter the choice:
        1 TO CHECK PRN NUMBER
        2 TO FIND ROUTE
                ''')
        if user_input=='1':
            print("Prn number is checked")
        elif(user_input=='2'):
            print("Whats your train number")
            self.find_route()
        else:
            print("Invalid choice")
    def find_route(self):
        train_number = input("Enter the train number: ")
        self.fetch(train_number)

    def fetch(self,train_number):
        response=requests.get("http://indianrailapi.com/api/v2/TrainSchedule/apikey/d571b2f477c4fa9c3cce3dc675b02471/TrainNumber/{}".format(train_number))
        data = response.json()  # ✅ This converts it to a dictionary
        for i in data['Route']:
            print(i['StationName'],'||',i['ArrivalTime'],'||',i['DepartureTime'],"||",i['Distance'])
obj=IRCTC()
#indian railways se api use kiya
#json viewer se dat ko samja
