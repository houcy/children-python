'''
程序：饮料换购
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''饮料换购'''
    t = int(input('请输入开始买了多少瓶饮料？'))
    g = t
    while g >= 3:
        h = g // 3
        g = h + g % 3
        t += h
    print('一共喝到%d瓶饮料' % t)

if __name__ == '__main__':
    main()
