# 1. จงเขียนโปรแกรมคํานวณ ด้วยภาษาต่อไปนี้(java,python,php หรือ javascript) 
# เลือกมา 1ภาษาที่ตัวเองถนัด โดยมีโจทย์ดังนี้
# ให้เขียนโปรแกรมเครื่องขายนํ้าผลไม้แห่งหนึ่ง สามารถหยอดเหรียญ 1 2 5 10 บาท มีสินค้าและ
# ราคาดังนี้นํ้าส้ม ราคา 13 บาท ,นํ้าแอปเปิล ราคา 15 บาท และนํ้ากีวีราคา 22 บาท ต้องการให้
# เขียนโปรแกรมรับจํานวนเหรียญ กับสินค้าที่เลือก แล้วแสดงผลลัพธ์ เป็น เงินทอน ที่ใช้จํานวน
# เหรียญให้น้อยที่สุด

class Juice:
    # setup
    def __init__(self):
        self.juice = {'orange':1}
        self.coin = {'a':1, 'b':2, 'c':5, 'd':10}
        self.juice_price = {1: 13, 2: 15, 3:22} 
        self.coin_convert = { self.coin[k]:k for k in self.coin } # {1: 'a', 2: 'b', 5: 'c', 10: 'd'}
        self.sum_coin = {}
        self.state = False 

    # นับจำนวนเหรียญที่ใส่เข้ามา
    def count_coin(self, input_coin):
        amount = 0
        for in_c in input_coin:
            if in_c in self.coin.keys():
                amount += self.coin[in_c]
            else:
                print("not coin")
        print(f"Your amount is {amount} bath.")
        return amount

    # คิดราคาน้ำผลไม้ที่เลือก
    def chose_juice(self, input_juice):
        price = 0
        for in_j in input_juice:
            if in_j in self.juice_price.keys():
                price += self.juice_price[in_j]
            else:
                print("don't have : ", in_j)
        print(f"Price of juice is {price} bath.")
        return price

    # คิดเงินทอนจากเครื่อง
    # amount เงินที่ใส่ในเครื่อง, price ราคาน้ำผลไม้ที่ต้องจ่าย
    def calculate_price(self, amount, price):
        t = 0
        if amount < price:
            t = price - amount
            print(f"Plase add your coin {t} bath") 
        elif amount > price:
            t = amount - price
            print(f"Change {t} baht")
            self.state = True
        elif amount - price == 0:
            print("just right!")
            self.state = True
        return self.calculat_coin_change(t)

    # คำนวณหาค่าเหรียญเงินทอน
    def calculat_coin_change(self, change):

        if self.state == True:
            num = max(self.coin_convert.keys())
            if change == 1 :
                self.sum_coin[1] = 1
                print(self.sum_coin)
            elif change == 2 :
                self.sum_coin[2] = 1
                print(self.sum_coin)
            elif change == 5 :
                self.sum_coin[5] = 1
                print(self.sum_coin)
            elif change == 10 :
                self.sum_coin[10] = 1
                print(self.sum_coin)
            else:
                coin_out = change//num
                other = change%num
                self.sum_coin[num] = coin_out
                del self.coin_convert[num]
                if other != 0:
                    return self.calculat_coin_change(other)
                print(self.sum_coin)
        else:
            pass

# ตัวอย่างง 
# Input เลือกนํ้าผลไม้ (1= นํ้าส้ม, 2=นํ้าแอปเปิล, 3=นํ้ากีวี): 1,1 >>> น้ำส้ม 2 ชิ้น = 26 บาท
# Input หยอดเหรียญ (a=1,b=5,c=10): c,c,c >>> เหรียญ 10 บาท 3 เหรียญ = 30 บาท
# Output: 1.เงินทอนคือ 4 บาท >>> 30-26 = 4
# ● เหรียญสองบาท 2เหริยญ

if __name__ == '__main__':

    input1 = 1,2
    input2 = 'd','d','d','d'
    call = Juice()
    value_juice = call.chose_juice(input1)
    value_coin = call.count_coin(input2)
    call.calculate_price(value_coin, value_juice)
    