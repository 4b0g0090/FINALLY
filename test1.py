class FriedChicken:                 #建立炸雞類別
    #建構子
    def __init__(self, name, flavor, spice_level, size, price):
        self.name = name  # 名稱
        self.flavor = flavor  # 口味
        self.spice_level = spice_level  # 辣度
        self.size = size  # 尺寸
        self.price = price  # 價格
    #副函式
    def display(self):                    #列出5種屬性
        print(f"炸雞名稱：{self.name}")    
        print(f"口味：{self.flavor}")
        print(f"辣度：{self.spice_level}")
        print(f"尺寸：{self.size}")
        print(f"價格：${self.price}\n")
    #副函式
    def change_price(self, new_price):        #修改價格
        self.price = new_price                
        print(f"將 {self.name} 的價格修改為 ${self.price}")
    #副函式
    def change_spice_level(self, new_spice_level):     #修改辣度
        self.spice_level = new_spice_level
        print(f"將 {self.name} 的辣度改成 {self.spice_level}")

    #副函式
    def change_size(self,new_size):          #修改大小
        self.size = new_size        
        print(f"將 {self.name} 的大小改成 {self.size}")


# 創建4個物件
chicken1 = FriedChicken("超派炸雞", "香辣", "中辣", "大", 100)
chicken2 = FriedChicken("派克炸雞", "原味", "不辣", "中", 70)
chicken3 = FriedChicken("3Q炸雞", "泰式", "微辣", "小", 80)
chicken4 = FriedChicken("海苔炸雞", "椒麻味", "中辣", "中", 90)

# 呼叫3個副函式 4X3=12
chicken1.display()
chicken1.change_price(75)
chicken1.change_spice_level("大辣")
chicken1.change_size("小")

chicken2.display()
chicken2.change_price(75)
chicken2.change_spice_level("小辣")
chicken2.change_size("大")


chicken3.display()
chicken3.change_price(75)
chicken3.change_spice_level("大辣")
chicken3.change_size("中")

chicken4.display()
chicken4.change_price(75)
chicken4.change_spice_level("不辣")
chicken4.change_size("大")