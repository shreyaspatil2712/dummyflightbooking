def payment(board):
    ans = input("How would you like to pay?(enter netbanking):" )
    if ans == "netbanking":
        acn = input("Enter your account number(enter random numbers): ")
        email = input("Enter your email adress(eneter a real email as the script will send you an email): ")
        global seatsn
        cost = seatsn * 100
        print("____SUMMARY____")
        print("cost perseat - 100$")
        print("Number of seats booked -", seatsn)
        print("Total cost of booking -", cost ,"$")
        ans3 = input("Would you like to proceed (y/n)" )
        if ans3 == "y" :
            print("You will reciveve an email on the email adress", email)
            from selenium import webdriver   # for webdriver
            from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
            from selenium.webdriver.chrome.options import Options  # for suppressing the browser
            import time

            option = webdriver.ChromeOptions() # setting up in a way that chrome wont open
            option.add_argument('headless')
            web = webdriver.Chrome(options=option)

            web.get('https://emkei.cz/')  ## fake email sender , cant affrod a paid service :)

            time.sleep(2) ## some time to load

            ### senders name
            fromName = "Egale Airlines"
            from_name = web.find_element_by_xpath('//*[@id="fromname"]')
            from_name.send_keys(fromName)

            ### senders email
            fromMail = "bookings@eagleairlines.com"
            from_mail = web.find_element_by_xpath('//*[@id="from"]')
            from_mail.send_keys(fromMail)

            ## recervers mail
            toMail = email
            to_mail = web.find_element_by_xpath('//*[@id="rcpt"]')
            to_mail.send_keys(toMail)

            ## subject
            sbj = "booking confirmation"
            sb_j = web.find_element_by_xpath('//*[@id="subject"]')
            sb_j.send_keys(sbj)

            ## main body
            counter1 = str(seatsn)
            cost1 = str(cost)
            mainbody = "Dear Customer, Your flight booking's' from  " + location + "  for the date  " + date + " have been confirmed. " + counter1 + " seats have been booked. Total cost of your booking is  " + cost1  + "$"
            main_body = web.find_element_by_xpath('//*[@id="text"]')
            main_body.send_keys(mainbody)

            ## submit
            submit = web.find_element_by_xpath('//*[@id="sendfrm"]/table[3]/tbody/tr[4]/td[2]/input[2]')
            submit.click()

        else :
            print("Payment Cancelled")
