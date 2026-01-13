import logging
import sys

logging.basicConfig(level=logging.DEBUG)

numbers = []
try: 
    choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie"))
    if choice in [1,3]:
        many = int(input("Na ilu liczbach chcesz wykonać obliczenia? :"))
        for i in range(many):
            next_number = float(input("Podaj składnik %s" % (i+1)))
            numbers.append(next_number)
    else:     
        a = float(input("Podaj składnik 1."))
        b  = float(input("Podaj składnik 2."))
except ValueError:
    logging.warning("Nie podałeś liczby !")
    sys.exit(0)


def operation(choice, *args):
    """
    Function operation takes three positional parameters. The user's selection causes the main information available in the search results to be displayed
    
    :param choice: User's can choose addition(1), subtraction(2), multiplication(3), division(4)
    :param a: number 1
    :param b: number 2
    """
    if choice == 1: 
        logging.info("Dodaję : %s", args)
        return sum(args)
    elif choice == 2:
        logging.info("Odejmuję : %s i %s", a,b)
        return a - b
    elif choice == 3:
        logging.info("Mnożę : %s i %s", a,b)
        return a * b
    elif choice == 4:
        if b == 0:
            logging.warning("Nie dzielimy przez 0")
            return None
        else:
            logging.info("Dzielę : %s i %s", a,b)
            return a / b


wynik = operation(choice,*numbers)
if wynik is not None:
    print("Wynik to :", wynik)