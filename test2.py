# 建立類別
class Drinks:
    # 建構子
    def __init__(self, drink_type, temperature, sugar,money):
        self.drink_type = drink_type
        self.temperature = temperature
        self.sugar = sugar
        self.money=money

    def get_type(self):
        return self.drink_type

    def get_temperature(self):
        return self.temperature

    def get_sugar(self):
        return self.sugar
    def get_money(self):
        return self.money

# 子類別
class HotDrinks(Drinks):  # 繼承父類別
    #建構子
    def __init__(self, drink_type):
        super().__init__(drink_type, "熱飲", "3分糖","70")


# 子類別
class ColdDrinks(Drinks):  # 繼承父類別
    #建構子
    def __init__(self, drink_type):
        super().__init__(drink_type, "冷飲", "無糖","70")
    def change_price(self, new_price):        #修改價格
        self.price = new_price                
        print(f"將 {self.drink_type} 的價格修改為 ${self.price}")
    def change_sugar(self, new_sugar):       
        self.sugar = new_sugar                
        print(f"將 {self.drink_type} 的糖度修改為 ${self.sugar}")
    def change_name(self, new_name):       
        self.name = new_name                
        print(f"將 {self.drink_type} 的名稱修改為 ${self.name}")

# 輸出結果
hot_tea = HotDrinks("茶")
print("熱飲料名稱是", hot_tea.get_type())
print("飲料甜度是", hot_tea.get_sugar())


cold_juice = ColdDrinks("果汁")
print("冷飲料名稱是", cold_juice.get_type())
print("飲料溫度:", cold_juice.get_temperature())
print("飲料甜度是", cold_juice.get_sugar())
print("飲料價錢是",cold_juice.get_money())
cold_juice.change_price(75)
cold_juice.change_sugar("5分糖")
cold_juice.change_name("紅茶")


# 員工類別
class Employee:
    # 建構子
    def __init__(self, name, seniority, hours_worked, hourly_rate):
        self.name = name
        self.seniority = seniority
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_name(self):
        return self.name

    def get_seniority(self):
        return self.seniority

    def get_hours_worked(self):
        return self.hours_worked

    def money(self):
        return self.hours_worked * self.hourly_rate * 30  # 當月

    def add_work_time(self, additional_hours):
        self.hours_worked += additional_hours

    def add_year(self, additional_years):
        self.seniority += additional_years


employee1 = Employee("jason", 5, 100, 20)
employee2 = Employee("MIKE", 6, 150, 10)
employee3 = Employee("JAY", 3, 130, 15)

# 使用成員函式/方法
print("員工姓名：", employee1.get_name())
print("員工年資：", employee1.get_seniority(), "年")
print("員工工時：", employee1.get_hours_worked(), "小時")
print("員工月薪：", employee1.money(), "元")

employee1.add_work_time(10)  # 增加工時10小時
print("增加工時後的員工工時：", employee1.get_hours_worked(), "小時")

employee1.add_year(1)  # 增加年資1年
print("增加年資後的員工年資：", employee1.get_seniority(), "年")




# 使用成員函式/方法
print("員工姓名：", employee2.get_name())
print("員工年資：", employee2.get_seniority(), "年")
print("員工工時：", employee2.get_hours_worked(), "小時")
print("員工月薪：", employee2.money(), "元")

employee2.add_work_time(10)  # 增加工時10小時
print("增加工時後的員工工時：", employee2.get_hours_worked(), "小時")

employee2.add_year(1)  # 增加年資1年
print("增加年資後的員工年資：", employee2.get_seniority(), "年")



# 使用成員函式/方法
print("員工姓名：", employee3.get_name())
print("員工年資：", employee3.get_seniority(), "年")
print("員工工時：", employee3.get_hours_worked(), "小時")
print("員工月薪：", employee3.money(), "元")

employee3.add_work_time(10)  # 增加工時10小時
print("增加工時後的員工工時：", employee3.get_hours_worked(), "小時")

employee3.add_year(1)  # 增加年資1年
print("增加年資後的員工年資：", employee3.get_seniority(), "年")
