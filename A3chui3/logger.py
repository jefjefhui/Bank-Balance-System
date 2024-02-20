#A3,Chi Heng Jeffrey Hui,CIS 345, T TH 12:00 PM
import csv
def log_transactions(log):
    with open('my.csv','w',newline='') as fp:
        writer=csv.writer(fp)
        writer.writerows(log)


def format_money(value):
    return f'$ {value:,.2f}'


