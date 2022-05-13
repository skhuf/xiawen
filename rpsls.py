#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：夏文
日期：2022-5-13
"""
#程序目的：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克）
# 计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
        number=0
    elif name=='史波克':
        number=1
    elif name=='纸':
        number=2
    elif name=='蜥蜴':
        number=3
    elif name=='剪刀':
        number=4
    else:
        number=5
    return number




def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number == 0:
        name = '石头'
    elif number == 1:
        name='史波克'
    elif number == 2:
        name = '纸'
    elif number == 3:
        name = '蜥蜴'
    elif number == 4:
        name = '剪刀'
    else:
        name=''
    return name




def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==5:
        print('Error:No Correct Name')
        return
    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    comp_number=random.randrange(5)
    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    comp_name=number_to_name(comp_number)

    # 在屏幕上显示计算机选择的随机对象
    print("计算机的选择为:", comp_name)
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    i=player_choice_number
    if comp_number in [i+1,i+2]:
        print('机器赢了！')
    elif comp_number==player_choice_number:
        print('您和计算机出的一样呢')
    else:
        print('您赢了')




# 对程序进行测试
print("欢迎使用RPSLS游戏")
# 输出"-------- "进行分割
print("--------")
# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
choice_name= input('请输入您的选择\n')
# print("----------------")
# print("请输入您的选择:")
# choice_name=input()
rpsls(choice_name)


