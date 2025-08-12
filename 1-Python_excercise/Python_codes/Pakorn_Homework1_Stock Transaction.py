# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Pakorn sagulkoo 6380064520
# 1. Stock Transaction Program

Shares_buy = int(input("์Number of shares which are bought: ")) #ปริมาณหุ้นที่ซื้อ
Cost_buy = 40                                                  #ราคาซื้อหุ้นต่อหน่วย
Total_buy = Shares_buy * Cost_buy                              #ราคาซื้อหุ้น

print("Money paid for buying the stock: $",Total_buy, sep='')

Comiss_buy_rate = 3/100                                        #อัตราค่าคอมมิสชันในการซื้อหุ้น
Comiss_buy = Total_buy * Comiss_buy_rate                       #ค่าคอมมิสชันในการซื้อหุ้น

print("Commission paid when bought stock: $", Comiss_buy, sep='')

Shares_sale = int(input("์Number of shares which are sold: "))  #ปริมาณหุ้นที่ขาย
Cost_sale = 42.75                                              #ราคาขายหุ้นต่อหน่วย
Total_sale = Shares_sale * Cost_sale                           #ราคาขายหุ้น

print("Money recieved from selling the stock: $",Total_sale, sep='')

Comiss_sale_rate = 3/100                                       #อัตราค่าคอมมิสชันในการขายหุ้น
Comiss_sale = Total_sale * Comiss_sale_rate                    #ค่าคอมมิสชันในการขายหุ้น

print("Commission paid when sold stock: $", Comiss_sale, sep='')

Net_income = Total_sale - Total_buy - Comiss_buy - Comiss_sale #กำไรสุทธิจากการขายหุ้น

print("Money left: $",Net_income, sep='')

