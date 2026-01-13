import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def input_numbers():

    try:
        numbers = []
        choice = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie"))
        if choice in [1,3]:
            many = int(input("Na ilu liczbach chcesz wykonać obliczenia? :"))
            for i in range(many):
                next_number = float(input("Podaj składnik %s: "% (i+1)))
                numbers.append(next_number)
            return choice, numbers
        elif choice in [2,4]:
            for y in range(2):
                next_number = float(input("Podaj składnik %s: "% (y+1)))
                numbers.append(next_number)
            return choice, numbers
    except ValueError:
        logging.warning("Nie podałeś liczby !")
        sys.exit(0)


def operation(choice, *args):
    """
    Function operation takes two positional parameters. Whoever *args create possibility to takes more arguments. The user's selection causes the main information available in the search results to be displayed
    
    :param choice: User's can choose addition(1), subtraction(2), multiplication(3), division(4)
    :param a: number 1
    :param b: number 2
    Description multiplication : Variable "handy" is very useful because she add possibility to multiply every element of tuple without a problem. It must have be "1" because if i would choose another number it would give me bad result. For example "0" and my result would be "0" and this isnt truth.
    """
    if choice == 1: 
        logging.info("Dodaję liczby%s ", ", ".join(str(x) for x in args))
        return sum(args)
    elif choice == 2:
        logging.info("Odejmuję liczby %s ", ", ".join(str(x) for x in args))
        return numbers[0] - numbers[1]
    elif choice == 3:
        logging.info("Mnożę liczby %s",", ".join(str(x) for x in args))
        handy= 1
        for z in args:
            handy = handy * z
        return handy
    elif choice == 4:
        if numbers[1] == 0:
            logging.warning("Nie dzielimy przez 0")
            return None
        else:
            logging.info("Dzielę liczby %s", ", ".join(str(x) for x in args))
            return numbers[0] / numbers[1]

if __name__ == "__main__":
    choice, numbers = input_numbers()
    wynik = operation(choice,*numbers)
if wynik is not None:
    print("Wynik to :", wynik)