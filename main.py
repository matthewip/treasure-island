print('''
*******************************************************************************
                   ____                  
                _.' :  `._               
            .-.'`.  ;   .'`.-.           
   __      / : ___\ ;  /___ ; \      __  
 ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
 :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
      `:-.._J '-.-'L__ `-- ' L_..-;'     
        "-.__ ;  .-"  "-.  : __.-"       
            L ' /.------.\ ' J           
             "-.   "--"   .-"            
            __.l"-:_JL_;-";.__           
         .-j/'.;  ;""""  / .'\"-.        
       .' /:`. "-.:     .-" .';  `.      
    .-"  / ;  "-. "-..-" .-"  :    "-.   
 .+"-.  : :      "-.__.-"      ;-._   \  
 ; \  `.; ;                    : : "+. ; 
 :  ;   ; ;                    : ;  : \: 
 ;  :   ; :                    ;:   ;  : 
: \  ;  :  ;                  : ;  /  :: 
;  ; :   ; :                  ;   :   ;: 
:  :  ;  :  ;                : :  ;  : ; 
;\    :   ; :                ; ;     ; ; 
: `."-;   :  ;              :  ;    /  ; 
 ;    -:   ; :              ;  : .-"   : 
 :\     \  :  ;            : \.-"      : 
  ;`.    \  ; :            ;.'_..--  / ; 
  :  "-.  "-:  ;          :/."      .'  :
   \         \ :          ;/  __        :
    \       .-`.\        /t-""  ":-+.   :
     `.  .-"    `l    __/ /`. :  ; ; \  ;
       \   .-" .-"-.-"  .' .'j \  /   ;/ 
        \ / .-"   /.     .'.' ;_:'    ;  
         :-""-.`./-.'     /    `.___.'   
               \ `t  ._  /  bug          
                "-.t-._:'         
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

first_question = input("You walk for 5 miles when you reach a T-junction. You can either go left or right. Type 'left' or 'right'.\n").lower()
if first_question == "left":
  second_question = input("You turn left, and continue to walk for 10 miles when you reach a dock. You can either swim to a nearby island, or wait for the next boat. Type 'swim' or 'wait'.\n").lower()
  if second_question == 'wait':
    third_question = input("You wait for the next boat which arrives in 30 minutes. You cruise for 3 hours and get off at Kawiki Island. You wander around for a little when you fall into a hole. You have a hard fall and are knocked out. When you regain consciousness, a tall white lion stands before you and says this:\n'You have 3 choices.\nGo through the red door and you will safely be taken back to your homeland, and you will find good treasure there.\nGo through the yellow door, and you will live the rest of your life in service to this island's people.\nGo through the blue door, and you will find the treasure hidden on Kawiki Island.'\nType 'red', 'yellow', or 'blue'.\n").lower()
    if third_question == "red":
      print("You are taken back home in a flying box. You embark on your treasure hunt 4 months later and locate treasure. A week later though, your treasure gets stolen. Game over.")
    elif third_question == "yellow":
      print("You work day and night helping Kawiki's people promoting education, and family unity. Ten years later, you and Kawiki's president invent flying-box technology called AirBox, and attain generational wealth. You win!")
    elif third_question == "blue":
      print("You locate Kawiki Island's treasure. However, in a year, you have spent all the money from the treasure, and you are stranded on Kawiki Island. Game over.")
    else:
      print("The tall white lion punches you and you are left in the hole with no escape. Game over.")
  else:
    print("You swim to the red ship. You get on, and are attacked by pirates, knocked out, and thrown back into sea. Game over.")
else:
  print("You are ran over by a speeding 4x4 Volvo. Game over.")
  
  
