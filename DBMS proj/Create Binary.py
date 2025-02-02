import pickle
F=open("password.bin","wb")
for I in range (1):
    P=input("Enter Password:")
    pickle.dump(P,F)
F.close()
F1=open("username.bin","wb")
for I in range (1):
    U=input("Enter Username:")
    pickle.dump(U,F1)
F1.close()
