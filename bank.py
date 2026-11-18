def bankOper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposite
    updatedBal = totalBal - withdraw


    return totalBal, updatedBal

if __name__ == "__main__":
    initialBal = int(sys.argv[1])
    deposite = int(sys.argv[2])
    withdraw = int(sys.srgv[3])

    totalBal, updateBal = bankOper(initialBal, deposite, withdraw)

    print("Total Balance: ", totalBal)
    print("update Balance ", updateBal)