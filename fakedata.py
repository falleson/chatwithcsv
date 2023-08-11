import random
import datetime
import pandas as pd

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

start_date = datetime.datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
end_date = datetime.datetime.strptime('2022-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

saleorderid = [i for i in range(1, 101)]
userid = [random.randint(1, 10) for i in range(100)]
productid = [random.randint(1, 5) for i in range(100)]
flavor = ['原味', '烧烤', '五香', '麻辣', '孜然']
saledate = [random_date(start_date, end_date) for i in range(100)]
saleamount = [round(random.uniform(50, 500), 2) for i in range(100)]
discountrate = [round(random.uniform(0.8, 0.95), 2) for i in range(100)]

data = {'saleorderid': saleorderid, 'userid': userid, 'productid': productid, 'flavor': flavor, 'saledate': saledate, 'saleamount': saleamount, 'discountrate': discountrate}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)

print(df.head())