# Ler area e saber quanto de tinta precisa para pintar

print('Esse programa calcula a partir da altura e largura em metros de uma parede e devolve a área\nAlém disso, informa a quantidade de tinta necessária para pintá-la.')

a = int(input('Qual a altura da parede?'))
l = int(input('Qual a largura da parede?'))  # noqa: E741

ae = a * l
t = int(ae / 2)

print('A área da parede é {}m²\nSerá necessario {}l de tinta para pintar a parede.'.format(ae, t))
