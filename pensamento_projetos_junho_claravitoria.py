'''
um bloco de comentarios.
para explicar o que o codgo faz,ou para deixar anotaçoes para o programador.
>>projeto barbearia:

>PO(como dono do negocio:quero um sistema de vendas para minha barbearia,
para que eu possa controlar as vendas e os produtos.)

>QA(como cliente:quero um sistema de agendamento de horario, para que eu possa agendar meus horarios
disponiveis de forma rapida e facil)

>tech (como programador:quero um sistema de agendamento de horario para minha barbearia,para que eu possa
desenvolver um software eficiente e funcional para o negocio.)

>dey(como programador:quero um sistema de agendamento de horarios para minha barbearia ,para que eu possa
implenmentar as funcionalidades necessarias para atender as necessidades do negocio e dos clientes.)

>ux (como designer de experiencia do usuario:quero um sistema de agedamento de horarios para minha barbearia,
para que eu possa criar uma interface intuitiva e agradavel para os usuarios,garantindo uma experiencia de
agendamento satisfatorio.)

>IA(como analista de dados:quero um sistema de agendamento de horarios para minha barbearia para que eu possa
coletar e analisar os dados armazenados,ajudando a identificar um padrao de cada cliente e otimizar as 
estrategicas de marketing)

    if opcao == '1':
 printi('Opção 1 - Cadastrando produtos...')

nome_produto = input('digite o nome do produto:')

quantidade_estoque int(input'Digite a quantidade em estoque: *))

preco_produto float(input('10,00: '))

validade_produto input('22:')

descricao_produto input('Digite a descrição do produto: ')
'''


print('olá, mundo!')
print('/n----------------------------------------------------------------------------')
print('bem vido ao sistema de vendas - barbearia')
print('1 - selecionar sua necessidade')
print('2 - escolha o melhor horario')
print('3 - realizar agendamento')
print('0 - sair')
print('/n-----------------------------------------------------------------------------')

while True:
    print('-' * 48 + '/n')
    print("=== BARBEARIA DOS SANTOS ===")
    nome = input( "Digite seu nome : " )        
    email = input ("Digite seu email : " )
    print("3 - print("Qual serviço deseja agendar")')
    print("1 - Corte de cabelo")
    print("2 - Barba")
    print("3 - Sombrancelha")
    print("4 - Corte de cabelo + barba")
    serviço = input ("Escolha o serviço desejado:")

opçao = incut('digite a opcao desejada:')

if opcao == '1':
    print('1 - Cortes e estilos')

elif opcao == '2':
    print('2 - Agendar horário')

elif opcao == '3':
    print('3 - Tabela de preços')

elif opcao == '4':
    print('4 - Realizar pagamento')

elif opcao == '5':
    print('5 - Nossos serviços')

elif opcao == '6':
    print('6 - Nossas unidades')

elif opcao == '7':
    print('7 - Contato e suporte')

elif opcao == '8':
    print('8 - Escolher unidade para atendimento')

elif opcao == '9':
    print('9 - Feedback e reclamações')

elif opcao == '0':
    print('0 - Sair')






