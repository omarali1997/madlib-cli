
import re



def read_template(path):
    try:
        with open(path) as f :
            return f.read()
    except:
        raise FileNotFoundError


def parse_template(s):
    w=re.findall("{(.*?)}",s)
    x=re.sub("{.+?}","{}",s)        
    return x,(tuple)(w)


    



def merge(s,t):
    
    return s.format(*t)

    
def video_game(story):
    print("**welcome to madlibs game**\n**you have to enter some word**")
    d=[]
    with open(story) as f :
        p=parse_template(f.read())
    for i in range(len(p[1])):
        t=input(f"{p[1][i]} ==>  ")
        d.append(t)
      
    h=tuple(d)
    a=merge(p[0],h)

    with open("assets/respons.txt","w") as response:
        response.write(a)
    with open("assets/respons.txt") as response:
        f=response.read()
    print(f)





if __name__=="__main__":
    video_game("assets/story.txt")
