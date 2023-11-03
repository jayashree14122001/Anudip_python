def discount():
    print("1. For Battery based Toys")
    print("2. For Key based Toys")
    print("3. Electrical charging based Toys")
    opt = int(input("Enter the product code (1,2 or 3):"))
    amount = int(input("Enter the order amount(Rs.):"))
    if opt==1:
        if amount>1000:
            dis = amount * 0.1
        else:
            dis = 0
    elif opt==2:
        if amount>100:
            dis = amount * 0.05
        else:
            dis=0
    elif opt==3:
        if amount>500:
            dis = amount*0.1
        else:
            dis = 0
    else:
        print("Wrong Choice, Please Enter Right Choice")
    bill_amount = amount - dis                 
    print("Customer has to pay:",bill_amount)
discount()