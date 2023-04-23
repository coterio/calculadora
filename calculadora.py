from time import sleep
import math
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
print(30*" " + 25*"—")
print(27*" " + 31*"—")
print(37*" " + "CALCULADORA")
print(27*" " + 31*"—")
print(30*" " + 25*"—")
nome = str(input("\n\nMuito bem vindo á minha calculadora... \nVamos começar pelo seu nome.\n"))
procede = "s"
pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094"
while(procede == "s"):
           n1 = float(input(f"{nome}... Qual o primeiro número á ser inserido?\n"))
           print(f"\n {n1}")
           op = input(f"\nQual operação iremos utilizar {nome}?\n+\n-\n*\n/\n%\n^\n√(índice)\nπ(casas d.)\n")
           if(op == "√"):
               print(GREEN + "\nselecione o índice\n" + RESET)
           print(f"{n1} {op}")
               
           n2 = float(input(f"E o último dígito.\n"))
           print("Pensando...")
           red   = "\033[1;31m"  
           BLUE  = "\033[1;34m"
           CYAN  = "\033[1;36m"
           GREEN = "\033[0;32m"
           RESET = "\033[0;0m"
           BOLD  = "\033[;1m"
           REVERSE = "\033[;7m"
           tudo = 0
           i = 0
           while(i != 4):
                 print(GREEN + tudo*" " + "PE\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "NS\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "AN\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "DO\n" + RESET)
                 sleep(0.2)
                 tudo += 5
                 i += 1
           sleep(1)
           if(op == "+"):
               resu = float(n1 + n2)
               print(f"R: {resu}\n{BLUE}[{n1} + {n2}]{RESET}")
           elif(op == "-"):
               resu = float(n1 - n2)
               print(f"R: {resu}\n{BLUE}[{n1} - {n2}]{RESET}")
           elif(op == "*"):
               resu = float(n1 * n2)
               print(f"R: {resu}\n{BLUE}[{n1} × {n2}]{RESET}")
           elif(op == "/"):
               resu = float(n1 / n2)
               print(f"R: {resu}\n{BLUE}[{n1} ÷ {n2}]{RESET}")
           elif(op == "%"):
               porca = n1 / 100
               resu = float(n2 * porca)
               print(f"{BLUE}{n1}%{RESET} de {BLUE}{n2}{RESET} equivale á {resu:.2f}")
           elif(op == "^"):
                resu = float(n1 ** n2)
                print(f"R: {resu}\n{BLUE}[{n1} ^ {n2}]{RESET}")
           elif(op == "√"):
                 resu = float(n1 ** (1/n2))
                 print(f"R: {resu}\n{BLUE}[i:{n2}]{RESET}\n{BLUE}[√{n1}]{RESET}")
           elif(op == "π"):
                 n0 = int(n2)
                 resu = f"3,{pi[:n0]}"
                 print(f"{BOLD}{resu}{RESET}\n{BLUE}[{n2} casas decimais de π]{RESET}" )
           else:
               print(red + "ERRØR (insira uma operação valida)" + RESET)
           sleep(3)
           iai = str(input("\nIra proseguir com o número?\n"+ REVERSE + "(s/n)" + RESET + "\n"))
           if(iai == "n"):
              continue
           while(iai == "s"):
               n1 = resu
               op = input(f"\nQual operação iremos utilizar {nome}?\n+\n-\n*\n/\n%\n^\n√(índice)\nπ(casas d.)\n")
               if(op == "√"):
                   print(GREEN + "\nselecione o índice\n" + RESET)
               print(f"{n1} {op}")
               n2 = float(input("Segundo número:\n"))
               i = 0
               while(i != 4):
                 print(GREEN + tudo*" " + "PE\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "NS\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "AN\n")
                 sleep(0.005)
                 tudo += 5
                 print(tudo*" " + "DO\n" + RESET)
                 sleep(0.2)
                 tudo += 5
                 i += 1
               sleep(1)
               if(op == "+"):
                   resu = float(n1 + n2)
                   print(f"R: {resu}\n{BLUE}[{n1} + {n2}]{RESET}")
               elif(op == "-"):
                   resu = float(n1 - n2)
                   print(f"R: {resu}\n{BLUE}[{n1} - {n2}]{RESET}")
               elif(op == "*"):
                   resu = float(n1 * n2)
                   print(f"R: {resu}\n{BLUE}[{n1} × {n2}]{RESET}")
               elif(op == "/"):
                   resu = float(n1 / n2)
                   print(f"R: {resu}\n{BLUE}[{n1} ÷ {n2}]{RESET}")
               elif(op == "%"):
                   porca = n1 / 100
                   resu = float(n2 * porca)
                   print(f"{BLUE}{n1}%{RESET} de {BLUE}{n2}{RESET} equivale á {resu:.2f}")
               elif(op == "^"):
                    resu = float(n1 ** n2)
                    print(f"R: {resu}\n{BLUE}[{n1} ^ {n2}]{RESET}")
               elif(op == "√"):
                     resu = float(n1 ** (1/n2))
                     print(f"R: {resu}\n{BLUE}[i:{n2}]{RESET}\n{BLUE}[√{n1}]{RESET}")
               elif(op == "π"):
                     n0 = int(n2)
                     resu = f"3,{pi[:n0]}"
                     print(f"{BOLD}{resu}{RESET}\n{BLUE}[{n2} casas decimais de π]{RESET}" )
               else:
                   print(red + "ERRØR (insira uma operação valida)" + RESET) 
               sleep(3)
               iai = str(input("\nIra proseguir com o número?\n"+ REVERSE + "(s/n)" + RESET + "\n"))
               if(iai == "s"):   
                  continue
               else:
                  procede = "s"
