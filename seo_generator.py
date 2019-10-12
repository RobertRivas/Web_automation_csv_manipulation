from selenium import webdriver
import csv
import sys

driver = webdriver.Chrome(r"/Users/robertrivas/PycharmProjects/web_automation/csvfile_reader_manipulator/chromedriver")

maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

mobile_errors_list = []
product_ID_list = []

with open("/Users/robertrivas/PycharmProjects/web_automation/csvfile_reader_manipulator/https___www.equipdirect.com_ Mobile Usability Issue Drilldown 2019-07-18.csv", newline='', encoding='utf-8') as mobile_issues:
    mobile_issue_reader = csv.DictReader(mobile_issues)

    for index, row in enumerate(mobile_issue_reader):
        # if index == 0:
        #     print(row['URL'])

         # print(row['URL'])

        mobile_errors_list.append(row['URL'])



x = 1
y = 0
for x, url in enumerate(mobile_errors_list):
    with open("/Users/robertrivas/PycharmProjects/web_automation/csvfile_reader_manipulator/ProductExportWed-07-24-042654.CSV",
                   newline='', encoding='utf-8') as product_export:
        product_export_reader = csv.DictReader(product_export)
        for index, row in enumerate(product_export_reader):
            print(x, url)

            # if row['ProductUrl'] == mobile_errors_list:
            if row['ProductUrl'] == mobile_errors_list[x]:
                product_ID_list.append(row['ProductID'])


             #print(row['ProductID'] + ',' + row['ProductUrl'])

        for y in range(len(product_ID_list)):
            print(product_ID_list[y])



def site_login():

    driver.get('https://www.equipdirect.com/mcp/login.aspx')
    driver.find_element_by_id('txtUserName').send_keys('')
    driver.find_element_by_id('txtPassWord').send_keys('')
    driver.find_element_by_id('btnlogin').click()



site_login()


