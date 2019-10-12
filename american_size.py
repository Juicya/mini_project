# Don't you know your american size jeans and shoes? I can fix it.

# Accept user input for sex, weight, height, and European shoe size.
sex = input('Укажите Ваш пол (м или ж): ')
waist = float(input('Укажите Ваш объем талии в сантиметрах: '))
height = float(input('Укажите Ваш рост в сантиметрах: '))
shoe_size = int(input('Укажите российский (европейский) размер обуви: '))

print('Ваш американский размер джинсов: ', end='')

# Estimate American jeans length by height.
if 155 <= height < 162:
    print('L28', end=' ')
elif 162 <= height <170:
    print('L30', end=' ')
elif 170 <= height < 178:
    print('L32', end=' ')
elif 178 <= height < 188:
    print('L34', end=' ')
elif 188 <= height < 200:
    print('L36', end=' ')
else:
    print('нестандартный рост')

# Estimate American waist size by waist and gender.
if sex == 'ж':
    if 58 <= waist <= 60:
        print('W24')
    elif 60 < waist <= 63:
        print('W25')
    elif 63 < waist <= 65:
        print('W26')
    elif 65 < waist <= 68:
        print('W27')
    elif 68 < waist <= 70:
        print('W28')
    elif 70 < waist <= 73:
        print('W29')
    elif 73 < waist <= 75:
        print('W30')
    elif 75 < waist <= 79:
        print('W31')
    elif 79 < waist <= 82:
        print('W32')
    elif 82 < waist <= 87:
        print('W33')
    elif 87 < waist <= 92:
        print('W34')
    elif 92 < waist <= 97:
        print('W35')
    elif 97 < waist <= 102:
        print('W36')
    elif 102 < waist <= 107:
        print('W38')
    else:
        print('нестандартная талия')
elif sex == 'м':
    if 70 <= waist <= 72:
        print('W28')
    elif 72 < waist <= 75:
        print('W29')
    elif 75 < waist <= 77:
        print('W30')
    elif 77 < waist <= 80:
        print('W31')
    elif 80 < waist <= 82:
        print('W32')
    elif 82 < waist <= 85:
        print('W34')
    elif 85 < waist <= 87:
        print('W34')
    elif 87 < waist <= 92:
        print('W35')
    elif 92 < waist <= 95:
        print('W36')
    elif 95 < waist <= 99:
        print('W38')
    elif 99 < waist <= 103:
        print('W40')
    elif 103 < waist <= 108:
        print('W42')
    elif 108 < waist <= 113:
        print('W44')
    else:
        print('нестандартная талия')
else:
    print('неверно выбран пол')

# Estimate American shoe size by European shoe size.
print('Ваш американский размер обуви: ', end='')

if sex == 'ж':
    if shoe_size == 34:
        print('4')
    elif shoe_size == 35:
        print('5')
    elif shoe_size == 36:
        print('6')
    elif shoe_size == 37:
        print('6,5')
    elif shoe_size == 38:
        print('7,5')
    elif shoe_size == 39:
        print('8')
    elif shoe_size == 40:
        print('9')
    elif shoe_size == 41:
        print('9,5')
    elif shoe_size == 42:
        print('10,5')
    elif shoe_size == 43:
        print('11,5')
    elif shoe_size == 44:
        print('12')
    else:
        print('нестандартный размер ноги')
elif sex == 'м':
    if shoe_size == 34:
        print('3')
    elif shoe_size == 35:
        print('4')
    elif shoe_size == 36:
        print('5')
    elif shoe_size == 37:
        print('5,5')
    elif shoe_size == 38:
        print('6,5')
    elif shoe_size == 39:
        print('7')
    elif shoe_size == 40:
        print('8')
    elif shoe_size == 41:
        print('8,5')
    elif shoe_size == 42:
        print('9,5')
    elif shoe_size == 43:
        print('10,5')
    elif shoe_size == 44:
        print('11')
    elif shoe_size == 45:
        print('12')
    elif shoe_size == 46:
        print('12,5')
    elif shoe_size == 47:
        print('13,5')
    elif shoe_size == 48:
        print('14')
    elif shoe_size == 49:
        print('15')
    else:
        print('нестандартный размер ноги')
else:
    print('неверно выбран пол')
