# coding: utf-8

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高

于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提

成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于

40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于

100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

'''


def get_money():
    '''
    计算利润
    '''
    i = input('请输入利润：').strip()
    if i.isdigit():
        i = int(i)
        money = None
        if i<= 100000:
            money = i*0.1
        elif i <=200000:
            money = 10000 + (i-100000)*0.075
        elif i <= 400000:
            money = 10000+7500+(i-200000)*0.05
        elif i<= 600000:
            money = 10000+7500+ 200000*0.05 + (i-400000)*0.03
        elif i <= 1000000:
            money = 100000 + 7500 + 200000*0.05 + 200000*0.03 + (i-600000)*0.015
        else:
            money = 100000 + 7500 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (i-1000000)*0.01
        return money
    else:
        print('请重新输入')






