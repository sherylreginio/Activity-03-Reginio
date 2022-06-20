import Reginio_Script_2_EV as EV
import Reginio_Script_1_Stat as ST
import math

def ContinueOrExit():
    option = int(input("\nDo you want to try again? \n[1] Yes  [2] No \nOption: "))
    if option == 1: main()
    elif option == 2: exit()
    else: 
        print("INVALID...")
        ContinueOrExit()
        

def main():

    print("******************Welcome To Pokemon STAT & EV Calculator******************\n\n")
    while True:
        ba = int ( input ("Base HP: "))
        lvl = int ( input ("Level: "))
        ev = int ( input ("EV must be [0 - 255] \nEV: "))
        iv = int ( input ("IV must be [0 - 31] \nIV: "))
            
        if iv > 31:
            print("IV exceeds!\n")  
            main() 

        if ev > 255:
            print("EV exceeds!\n") 
            main()

        else:    
            print("Proceeding...")
            break

    while True:
        print("\nChoose Pokemon Calculator Type \n[1] EV Calculator \n[2] Stat Calculator ")
        choice = int(input("\nInput your choice: "))
    
        if choice == 1:
            stats = int(input("Stats: "))
            pk = int(input("[1] Beneficial [2] Hindering \nModifier: "))
            if pk == 1:
                modi = 1.1

            elif pk == 2:
                modi = 0.9

            else:
                print("Invalid Input!")
            
            TotalEV = EV.EVCalculation.computeEV(ba, iv, ev, lvl, modi, stats)
            if TotalEV <=500:
                print("Total EV:", TotalEV)
            
            else:
                print("Pokemon's Total EV Exceeds!")
            ContinueOrExit()
        

        elif choice == 2:
            op = int(input("\nCompute other stats? \n[1] Yes [2] No \nSelect: "))
            if op == 1: 
                opt = str(input("\n[attck] [def] [spattck] [spdef] [spd]\nWhat Stat would you like to compute?: "))    
                if opt == 'attck': 
                    sta = 'Attack'   
                    opti = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if opti == 1:
                        ntr = 1.1

                    elif opti == 2:
                        ntr = 0.9
                
                if opt == 'def':
                    sta = 'Defense'    
                    opti = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if opti == 1:
                        ntr = 1.1

                    elif opti == 2:
                        ntr = 0.9
                
                if opt == 'spattck':  
                    sta = 'Special Attack'  
                    opti = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if opti == 1:
                        ntr = 1.1

                    elif opti == 2:
                        ntr = 0.9

                if opt == 'spdef':  
                    sta = 'Special Defense'  
                    opti = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if opti == 1:
                        ntr = 1.1

                    elif opti == 2:
                        ntr = 0.9

                if opt == 'spd':    
                    sta = 'Speed'
                    opti = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if opti == 1:
                        ntr = 1.1

                    elif opti == 2:
                        ntr = 0.9
                
                other = ST.StatCalculation.OtherStat(ba, ev, lvl, iv, ntr)
                if other <= 510:
                    print("\nComputing", sta,"Value =", other)
                
                else:
                    print("Pokemon's Total EV Exceeds...")
                ContinueOrExit()

            elif op == 2:
                chp = ST.StatCalculation.Health(ba, ev, lvl, iv)
                if chp <= 510:
                    print ("HP Value:", chp)
                else:
                    print("Pokemon's Total EV Exceeds!")
                ContinueOrExit()

            else:
                print("INVALID INPUT!")
                       
        else:
            print("INVALID INPUT!")

main()