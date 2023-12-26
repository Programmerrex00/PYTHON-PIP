import random

#Usando Tuplas


def choise(a):
  if a == 'piedra':
    return ('piedra')
  elif a == 'papel':
    return ('papel')
  elif a == 'tijera':
    return ('tijera')
  else:
    return ('perder')


def mensaje(usuario, pc):
  print(f'\nHas elegido: {choise(usuario)}')
  print(f'El PC ha elegido: {choise(pc)}')


def select_user_and_machine():
  option = ('piedra', 'papel', 'tijera')
  pc = random.choice(option)
  usuario = input(
      '\n1) piedra 🗿\n2) papel 📄 \n3) tijera ✂️\n =>').lower().strip()
  return pc, usuario


def check_rules(usuario, pc, cont_maquina, cont_usuario):
  if choise(pc) == usuario:
    mensaje(usuario, pc)
    print('Empate!')
  elif (usuario == 'piedra'
        and pc == 'tijera') or (usuario == 'papel'
                                and pc == 'piedra') or (usuario == 'tijera'
                                                        and pc == 'papel'):
    mensaje(usuario, pc)
    print('User Gana!!')
    cont_usuario += 1
  elif usuario != 'papel' and usuario != 'piedra' and usuario != 'tijera':
    print('Opcion incorrecta\n')
  else:
    mensaje(usuario, pc)
    print('Has Perdido!!')
    cont_maquina += 1
  return cont_maquina, cont_usuario


# Con exit salimos directamente del programa
def check_wins(cont_maquina, cont_usuario):

  print(f'''🤖 Computer wins: {cont_maquina} \n🙋 User wins: {cont_usuario}''')

  if cont_maquina == 3:
    print('\n🎖️ El ganador es Computer 🎖️')
    exit()

  if cont_usuario == 3:
    print('\n🎖️ El ganador es User 🎖️')
    exit()


print("""
[ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
            >>> Ingresa una opción <<<
""")
print('\t***' * 10)
print('\t\t\t\tAl mejor de 3')
print('\t***' * 10)


def run_game():
  cont_maquina = 0
  cont_usuario = 0
  rounds = 1

  while True:
    print('***' * 10)
    print('Round ', rounds)
    print('***' * 10)
    rounds += 1

    pc, usuario = select_user_and_machine()

    cont_maquina, cont_usuario = check_rules(usuario, pc, cont_maquina,
                                             cont_usuario)

    check_wins(cont_maquina, cont_usuario)


run_game()