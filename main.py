import requests
from colorama import Fore

def send_text():
    
    mas = '+'
    
    print('Escribe el número al que deseas enviar el mensaje:')
    in_num = input()
    print('Escribe el mensaje que deseas enviar:')
    in_men = input()

    # Comprueba si los datos son válidos antes de enviar el mensaje
    if not in_num or not in_men:
        print('Debes proporcionar un número de teléfono y un mensaje.')
        return
    
    if '+' in in_num:
        num = in_num
    else:
        num = mas + in_num

    # Envía la solicitud POST
    resp = requests.post('https://textbelt.com/text', {
    'phone': num,
    'message': in_men,
    'key': 'textbelt',
    })

    # Imprime la respuesta de la solicitud
    if resp.json() ==  ({'success': False, 'error': 'Your phone number was not provided in E.164 format, or free SMS are disabled for this country'}):
        print(Fore.RED + 'Mira si el numero esta bien escrito o si esta en un pais disponible')
        print(Fore.RESET)
        
    elif resp.json() == ({'success': False, 'error': 'Only one test text message is allowed per day.', 'quotaRemaining': 0}):
        print(Fore.RED + 'Espera 24 horas para enviar otro mensaje')
        print(Fore.RESET)
    else:
        print(Fore.RED + 'error')
        print(Fore.RESET)
        
        

        
    print(resp.json())

send_text()