#!/usr/bin/env python3


#Dictionary: keys are donors and values are lists of donations
donor_data = {"Allen, Paul": [1000000.00, 50000.00, 300000.00], 
                    "Gates, Bill": [5000000.00, 80000.00, 700000.00], 
                    "Bezos, Jeff": [30000.00], 
                    "Musk, Elon": [1000000.00, 30000.00], 
                    "Zuckerberg, Mark":[10000.00, 50000.00, 2000.00, 400000.00]
                    }


def show_donor_list():
    donor_list = []
    for donor in donor_data:
        donor_list.append(donor)
    sort_donors = sorted(donor_list)
    for donor in sort_donors:
        print(donor)


def get_donor(name):
    """
    retieve donor form donor_data list
    :param: name of donor
    :returns: donor tuple
    """
    for donor in donor_data:
        if name.strip().lower() == donor.lower():
            return donor
    return None


def make_donor_email(donor_dict):
    """
    Make a thank you email for the donor
    :param: donor tuple
    returns: string containing text of email
    """
    #for donor, amt in donor_data.items():
    return '''\n
        Dear {name}, 
        Thank you for your donation of ${amt:.2f}.
        You are a good person.
                            Sincerely,
                            -Me
        '''.format(**donor_dict)
        #.format(donor, donor_data[donor][-1])


def send_donor_email():
    donor_dict = {}
    while True:
        name = input("Please enter a donor's name in the form of 'Last name, First name'"
            "(or 'list' to see a list of all donors, or 'menu' to exit)> ").strip()
        if name == "list":
            show_donor_list()
        elif name == "menu":
            return None
        else:
            break
    while True:
        amount_str = input("Please enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return None
        else:
            amount = float(amount_str)
        donor = get_donor(name)
        if donor is None:
             donor_dict["name"] = name
        donor_dict["amt"] = amount
        #donor[name].append(amount)
            #donor_data.setdefault(name, [])
        #donor_data[name].append(amount)
        break
    print(make_donor_email(donor_dict))


def sort_key(donor):
    return donor[1]


def make_report():
    rows = []
    for donor in donor_data:
        total = sum(donor_data[donor])
        num = len(donor_data[donor])
        avg = total / num
        rows.append((donor, total, num, avg))
    rows.sort(key=sort_key, reverse=True)
    print("{:20s}{:15s}{:15s}{:12s}".format(
        "Donor Name", "|  Total Given", "|  Num Gifts", "|  Average Gift"))
    print("_" * 67)
    for row in rows:
        print('{:20s}{:15.2f}{:^15d}{:12.2f}'.format(*row))


def quit():
    print("Quitting this menu now")
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "exit menu":
            break


#def init_prompt():
init_prompt = ('''\n
                            Would you like to: 
                            '1' - Send a Thank You 
                            '2' - Create a Report 
                            '3' - Quit
                            > ''')
    #return response.strip()


main_dispatch = {"1": send_donor_email,
                                   "2": make_report,
                                   "3": quit}


if __name__ == "__main__":
    menu_selection(init_prompt, main_dispatch)

'''
    running = True
    while running:
        selection = init_prompt()
        if  selection == "1":
            send_donor_email()
        elif selection == "2":
            make_report()
        elif selection == "3":
            running = False
        else:
            print("error: please make a valid selection!")
'''

