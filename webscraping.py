#!/usr/bin/python
from __future__ import print_function
import sys,re, smtplib
import abuseipdb, ipvoid, sans, myIPwhois, xforceIBM

def webscraping():
    myIPvoidPrint1 = ''
    mySansPrint2 = ''
    myAbuseIPDBPrint3 = ''
    myXForcePrint4 = ''

    if len(sys.argv) <= 2:
        print('>>>>> Welcome to my WebScraping Tool <<<<<')
        print('     Usage: python webscraping.py [x.x.x.x | domain]')
    else:
        print('>>>>> Welcome to WebScraping Tool <<<<<')

        # regular expression for IP
        re_ip = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

        i = 1
        while i < len(sys.argv):
            print("")
            print("Now checking " + sys.argv[i] + " ...")
            print("")

            # If the IP format is valid:
            if re_ip.match(sys.argv[i]):
                # Call myIPwhois.py
                # myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[i])

                # Call ipvoid.py
                myIPvoidPrint1 = ipvoid.ipvoidChecker(sys.argv[i])

                # Call sans.py
                mySansPrint2 = sans.sansChecker(sys.argv[i])

                # Call abuseipdb.py
                myAbuseIPDBPrint3 = abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[i])

                # Call xforceIBM.py
                myXForcePrint4 = xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/ipr/" + sys.argv[i])


            # If the input is a domain or other strings, let the website validate then ...
            else:
                #Call myIPwhois.py
                # myIPwhois.IPWhoisChecker("https://www.abuseipdb.com/whois/" + sys.argv[i])

                # Call sans.py
                # sans.sansChecker("https://isc.sans.edu/api/ip/" + sys.argv[1])
                sans.sansChecker(sys.argv[i])

                # Call abuseipdb.py
                abuseipdb.abuseipdbChecker("https://www.abuseipdb.com/check/" + sys.argv[i])

                # Call xforceIBM.py
                # Check the domain
                xforceIBM.myXForceChecker("https://api.xforce.ibmcloud.com/url/" + sys.argv[i])



            print ("------------", sys.argv[i], "------------")
            message = "[.] IPVoid Result: " + myIPvoidPrint1 + '\n' +\
                      "[.] SANS Result: " + ' | '.join(mySansPrint2) + '\n' +\
                      "[.] AbuseIPDB Result: " + myAbuseIPDBPrint3 + '\n' +\
                      "[.] XForce Result:  " + ' | '.join(myXForcePrint4)
            print (message)

            i += 1
"""
    sendemail(from_addr='xxx@gmail.com',
              to_addr_list=['xxx@xx.co.nz'],
              cc_addr_list=['xxx@xx.co.nz'],
              subject='Some Testing Shxxt',
              message= message,
              login='xxx',
              password='xxx!')
"""


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems



if __name__ == '__main__':
    webscraping()