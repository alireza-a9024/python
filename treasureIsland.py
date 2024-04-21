print("""   __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
                           ___________
                ___________)%{}%%%%%%/
               /{}%%%%%%%%/%%/%%%%%%/
              /%%\% _---_/ \/%%%%%%/
             /%%%%\/    /()|%%%%%%/
            /%%%%%|()  /+ /%%%%%%/
           /%%%%%%%\ +/HH%%\%%%%/
          /%%%%%%/%HH/_/%%%\%%%/
 ejm97   /%%%%%%/%%\/%%%%%%{}%/
        /%%%%%{}%%%/
       /
      /
     /
    /
   /

treasureisland.ascii.uk
888                                                         d8b        888
888                                                         Y8P        888
888                                                                    888
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b. 888.d8888b 888
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b88888K     888
888   888    88888888.d888888"Y8888b.888  888888    88888888888"Y8888b.888
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.    888     X88888
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 888 88888P'888



                     888
                     888
                     888
 8888b. 88888b.  .d88888
    "88b888 "88bd88" 888
.d888888888  888888  888
888  888888  888Y88b 888
"Y888888888  888 "Y88888



 _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|




  ,d
  88
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88



           88           88                                 88
           ""           88                                 88
                        88                                 88
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8
                                                               """)
print("Welcome to the treasure island.\nYour mission is to find the treasure.")
step_1 = input("There are two paths, Left or right?").lower()
if step_1 == "left":
    step_2 = input("you can swim outside or wait, swim or wait?").lower()
    if step_2 == "wait":
        step_3 = input("you turn around and see three doors, which door? blue red yellow?").lower()
        if step_3 == "yellow":
            print("you won!")
        else:
            print("you lost! the door opened to hell!")
    else:
        print("you lost! sharks are eating you!")
else:
    print("you lost!you fell into a trap!")
