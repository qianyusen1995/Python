#定义函数
def pet_information(animal_type,pet_name):
    #打印该动物类型
    print("It's a "+animal_type+'.')
    #打印该动物的名字，title()函数使字符串的所有单词以大写开始
    print('The '+animal_type+"'s name is "+pet_name.title()+'.')
#调用函数
pet_information('pig','marry')
#再次调用函数
pet_information ('cat','jackson')