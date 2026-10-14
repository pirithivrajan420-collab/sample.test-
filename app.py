import main as ca

USER_DATA = {
    "username": "admin",
    "acc.no": 123456,
    "pin": 1234,
    "balance": 10000,
}


def user_info():
    if USER_DATA and USER_DATA["username"]:
        return f"\nHi User {USER_DATA['username']} Your Account no Is {USER_DATA['acc.no']}"
    print("User Not Found")


def deposit(deposite_amount):
    if deposite_amount:
        amount = ca.deposit_calc(USER_DATA["balance"], deposite_amount)
        USER_DATA["balance"] = amount
        return amount
    print("Amount Not Found")


def check_balance():
    return USER_DATA["balance"]


def main():
    print("Welcome to tp ATM.....")
    pin_no = int(input("Enter Your Pin Number: "))

    if USER_DATA and USER_DATA["pin"] == pin_no:
        print(user_info())
        while True:
            choice = int(input(
                "1. deposit\n"
                "2. withdraw\n"
                "3. check balance\n"
                "4. exit\n"
                "enter your choice: "
            ))

            match choice:
                case 1:
                    deposite_amount = int(input("Enter Your Deposite Amount: "))
                    print(f"Your New Balance is {deposit(deposite_amount)}")
                case 2:
                    withdraw_amount = int(input("Enter Your Withdraw Amount: "))
                    amount = ca.withdraw_calc(USER_DATA["balance"], withdraw_amount)
                    USER_DATA["balance"] = amount
                    print(f"Your New Balance is {amount}")
                case 3:
                    print(f"Your Current Balance is {check_balance()}")
                case 4:
                    print("Thank You For Using tp ATM Service")
                    break
                case _:
                    print("Invalid Choice, please select between 1 to 4")
    else:
        print("Invalid Pin No,")



        
        
        