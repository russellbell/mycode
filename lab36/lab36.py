import pyexcel


def get_ip_data():
    input_ip = input("\nWhat is the IP address ")
    input_driver = input("What is the drive associated with this devices? ")
    input_device_type = input("What kind of device is this?")
    input_device_owner = input("Who owns this devices? ")
    d = {'IP': input_ip, 'driver': input_driver, 'device': input_device_type, 'owner': input_device_owner}
    return d


mylistdict = []

print("hHello! This program will make you a *.xls file")

while True:
    try:
        mylistdict.append(get_ip_data())
        keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
        if keep_going.lower() == 'q':
            break
    except:
        filename = input("\nWhat is the name of the *.xls file? ")

        pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

        print(f"The file {filename}.xls should be in your local directory")
