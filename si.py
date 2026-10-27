import sys
def sim_interest(principal,time,rate):
    return (principal*time*rate)/100
if_name_=="_main_":
    p=int(sys.argv[1])
    t=int(sys.argv[2])
    r=int(sys.argv[3])
    print("simple interest:",sim_interest(p,t,r))
    print(sys.argv[0])    git 