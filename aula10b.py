n1 =  float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota : '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua Media foi boa ! Parabens')
#else:
 #   print('sua media foi ruim! ESTUDE MAIS!')

print('Parabens'if m>=6 else 'Estude Mais!')