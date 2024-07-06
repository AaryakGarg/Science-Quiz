password = "quizgame"

a = -1

asd = 1

for i in range(1,4):
    
    p = str(input("Enter the Password :"))
    
    j = 3
    
    a+=1
    
    if p == password:
        print("\nWELCOME\n")
        break

    else:
        print("Please re-enter the password\n")
        print("Chances left :",j-i)

        continue

if a == 3:
    
    print("Try again next time")

else:

    while asd == 1:

        import mysql.connector as mysqc

        myconn = mysqc.connect(password = 'mysql123',host = 'localhost', user = 'root')

        c = myconn.cursor(buffered = True)

        c.execute("create database IF NOT EXISTS Quiz")
        c.execute("use Quiz")
        c.execute("create table IF NOT EXISTS quiz_questions(Question varchar(2000), Op1 varchar(500), Op2 varchar(500), Op3 varchar(500), Op4 varchar(500), Answer int(1), Subject varchar(30))")
        c.execute("use Quiz")
        c.execute("create table IF NOT EXISTS player_details(Name varchar(100),Total_Points int(3))")

        a="INSERT INTO quiz_questions VALUES('Which alloy is used to make clock pendulums?','Mischmetal','Invar','Brass','Manganin',2,'Physics')"
        b="INSERT INTO quiz_questions VALUES('During the First World War, which country signed the Peace Treaty with Germany?','England','USA','Russia','Austria',3,'History')"
        d="INSERT INTO quiz_questions VALUES('What is the correct formula of Angular Momentum?','L=rXp','L=rpc','L=pXrd','L=pr',1,'Physics')"
        e="INSERT INTO quiz_questions VALUES('Which function returns all the keys of a dictionary d ?','d.values()','d.items()','d.keys()','d.codes()',3,'Computers')"
        f="INSERT INTO quiz_questions VALUES('When did United Kingdom declare war on Germany which lead to World War II?','4th April 1939','18th August 1939','28th August 1939','3rd September 1939',4,'History')"
        g="INSERT INTO quiz_questions VALUES('What is the unit of measurement for the universal gravitational constant?','Nm/〖kg〗^2','Nm^2/〖kg〗^2','Nm/kg','Nm^2/kg',2,'Physics')"
        h="INSERT INTO quiz_questions VALUES('Which function is used to find out the length of a string?','len()','ord()','int()','id()',1,'Computers')" 
        i="INSERT INTO quiz_questions VALUES('In which year did America join the Second World War','1939','1940','1941','1942',3,'History')"
        j="INSERT INTO quiz_questions VALUES('Rockets works on the principle of?','Newton’s First Law ','Newton’s SecondD Law','Newton’s Third Law','Archimedes principle',3,'Physics')"
        k="INSERT INTO quiz_questions VALUES('Which module is used for GUI creation in Python?','math','tkinter','time','matplotlib',2,'Computers')"
        l="INSERT INTO quiz_questions VALUES('The immediate cause for the outbreak of the first World War was :','The assassination of Archduke Francis Ferdinand','The imprisonment of Lenin','The ambition of America to dominate the world','The sudden death of Lloyd George',1,'History')"
        m="INSERT INTO quiz_questions VALUES('Tesla is a unit of which quantity?','Magnetic Field','Flux','Electric Field','Moment',1,'Physics')"
        n="INSERT INTO quiz_questions VALUES('What is the value passed in the function call statement called?','Formal Argument','Actual Argument','Final Argument','Initial Argument',2,'Computers')"
        o="INSERT INTO quiz_questions VALUES('Who were the Axis powers in World War-I','Poland + Japan + Germany','Italy + Japan + Britain','Germany + Italy + France','Germany + Italy + Japan',4,'History')"
        p="INSERT INTO quiz_questions VALUES('Doppler’s effect is associated with?','Light','Sound','Current','Heat',2,'Physics')"
        q="INSERT INTO quiz_questions VALUES('Which function returns a value?','Void Function','Keyword Function','Non-Void Function','Positional Function',3,'Computers')"
        r="INSERT INTO quiz_questions VALUES('On which side did Japan fight in the First World War?','None it was neutral','With Germany against United Kingdom','Against Russia on its own','With United Kingdom against Germany',4,'History')"
        s="INSERT INTO quiz_questions VALUES('What is the unit of noise pollution?','Decibel','Decimal','ppm','Hertz',1,'Physics')"
        t="INSERT INTO quiz_questions VALUES('What is the term given to the order of execution of statements of a program in Python?','Flow of control','Order of Program','Flow of execution','Flow of Programming',3,'Computers')"
        u="INSERT INTO quiz_questions VALUES('The last country of Axis powers to surrender during the end of the World War II was','Germany','Japan','Italy','France',2,'History')"
        v="INSERT INTO quiz_questions VALUES('Temperature in Celsius and Fahrenheit are the same at?','32','40','-40','-273',3,'Physics')"
        w="INSERT INTO quiz_questions VALUES('Which keyword allows a global variable to be used in local context?','global','entire','complete','full',1,'Computers')"
        x="INSERT INTO quiz_questions VALUES('Who become the Chancellor of Germany for One Day after the death of Hitler during the Second World War','Hermann Goering','Heinrich Himmler','Rudolf Hess','Joseph Goebbels',4,'History')"
        y="INSERT INTO quiz_questions VALUES('If no index is given to pop() function,which element will it remove?','First','Last','Second','Third',2,'History')"
        z="INSERT INTO quiz_questions VALUES('Where was the republic established in Germany after the First World War?','Munich','Weimer','Berlin','Bavaria',2,'History')"
        a1="INSERT INTO quiz_questions VALUES('The current flowing in one direction is called as?','Alternating Current','Induced Current','Direct Current','Ionic Current',3,'Physics')"
        a2="INSERT INTO quiz_questions VALUES('Which module of Python is used to work with binary files?','time','csv','tkinter','pickle',4,'Computers')"
        a3="INSERT INTO quiz_questions VALUES('When was ancient Rome founded?','776 BC','753 BC','752 BC','742 BC',2,'History')"
        a4="INSERT INTO quiz_questions VALUES('A magnifying glass comprises of a simple…?','Convex Lens','Concave Mirror','Concave Lens','Convex Lens',1,'Physics')"
        a5="INSERT INTO quiz_questions VALUES('Which function of pickle module is used to read a binary file?','dump()','read()','load()','peek()',3,'Computers')"
        b1="INSERT INTO quiz_questions VALUES('When was Bulgaria founded','681','864','917','923',1,'History')"
        b2="INSERT INTO quiz_questions VALUES('Planck constant has the dimension of?','Energy','Momentum','Current','Force',1,'Physics')"
        b3="INSERT INTO quiz_questions VALUES('When was NATO signed?','1949','1990','1948','1950',1,'History')"
        b4="INSERT INTO quiz_questions VALUES('What is the full form of RADAR?','Radio Detecting and Ranging','Radio Device and Ranging','Region Device and Ranging','Region Detection and Ranging',1,'Physics')"
        b5="INSERT INTO quiz_questions VALUES('In which year, Alexander the Great become the king of Macedonia?','336 BC','323 BC','350 BC','200 BC',1,'History')"
        c1="INSERT INTO quiz_questions VALUES('What is the rate of change in displacement over time called?','Acceleration','Speed','Velocity','Momentum',3,'Physics')"
        c2="INSERT INTO quiz_questions VALUES('When was Socrates born?','469 BC','465 BC','460 BC','449 BC',1,'History')"
        c3="INSERT INTO quiz_questions VALUES('Which lens is thick at the middle and thin at the edges?','Convex Lens','Concave Lens','Bi-Concave Lens','Concavo-Convex Lens',1,'Physics')"
        c4="INSERT INTO quiz_questions VALUES('When was Sputnik 1 launched?','1970','1957','1980','1990',2,'History')"
        c5="INSERT INTO quiz_questions VALUES('The Tyndall effect is due to which phenomenon of light?','Scattering','Dispersion','Diffraction','Reflection',1,'Physics')"
        d1="INSERT INTO quiz_questions VALUES('The world’s first drainage system was build by the people of-','Egyptian civilization','Indus Valley civilization','Chinese civilization','Mesopotamian civilization',2,'History')"
        d2="INSERT INTO quiz_questions VALUES('Which of the following doesn’t affect velocity of sound?','Heat','Medium','Pressure','Humidity',4,'Physics')"
        d3="INSERT INTO quiz_questions VALUES('Which of the following group of thinkers influenced Fascism?','Plato Machiavelli and Herbet Spencer','Aristotle St Augustine and T.H Green','Kant Fichte Hegel and Rosenberg','Karl Marx Engels and Lenin',3,'History')"
        d4="INSERT INTO quiz_questions VALUES('What is the unit of viscosity?','Poise','Pascal','Poiseuille','Ampere',3,'Physics')"
        d5="INSERT INTO quiz_questions VALUES('From which language, has the term ‘democracy’ been derived?','Greek','Hebrew','English','Latin',1,'History')"
        e1="INSERT INTO quiz_questions VALUES('What is the frequency of direct current?','50Hz','60Hz','90Hz','0',4,'Physics')"
        e2="INSERT INTO quiz_questions VALUES('Who made the famous statement -Man is born free, but everywhere he is in chains-','John Locke','Mirabeau','Voltaire','Jean Jacques Rousseau',4,'History')"
        e3="INSERT INTO quiz_questions VALUES('Which of the following is used in oven?','X-rays','UV Rays','Microwaves','Radio Waves',3,'Physics')"
        e4="INSERT INTO quiz_questions VALUES('Napoleon-I and the Duke of Wellington fought the famous','Battle of Austerlitz','Battle of Leipzig','Battle of Borodini','Battle of Waterloo',4,'History')"
        e5="INSERT INTO quiz_questions VALUES('Who enunciated the laws of planetary motion?','Nicolaus Copernicus','Johannes Kepler','Issac Newton','Galileo',2,'Physics')"
        f1="INSERT INTO quiz_questions VALUES('Which Mountain’s volcano buried Pompeii city with ash in 79 AD','Mount Pelee','Mount Tambora','Mount Etna','Mount Vesuvius',4,'History')"
        f2="INSERT INTO quiz_questions VALUES('Hydraulic machines work on the principle of?','Newton’s law','Joule’s law','Pascal’s law','Flotation law',3,'Physics')"
        f3="INSERT INTO quiz_questions VALUES('When was the All Red Line inaugurated','1901','1902','1922','1872',2,'History')"
        f4="INSERT INTO quiz_questions VALUES('What is the commercial unit of electrical energy?','kWh','Ampere','Volt','Ohm',1,'Physics')"
        f5="INSERT INTO quiz_questions VALUES('Who was the king during the French Revolution?','Napoleon','Louis XV','Louis XVI','Charles IX',3,'History')"
        g1="INSERT INTO quiz_questions VALUES('What is the refractive index of diamond?','1.44','1.47','1.77','2.42',4,'Physics')"
        g2="INSERT INTO quiz_questions VALUES('Angstrom is a unit of which quantiy?','Mass','Time','Length','Force',3,'Physics')"
        g3="INSERT INTO quiz_questions VALUES('In which of the following rays mesons are found?','Cosmic rays','Gamma rays','X-rays','Laser beams',1,'Physics')"
        g4="INSERT INTO quiz_questions VALUES('In which year did Genghis Khan die?','1209','1219','1227','1232',3,'History')"
        g5="INSERT INTO quiz_questions VALUES('What does Immutable mean?','Cannot be changed','Can be changed','Will be deleted','Cannot be deleted',1,'Computers')"
        h1="INSERT INTO quiz_questions VALUES('Where is a global variable declared?','Inside a function','Outside all functions','Inside an if -Block','Cannot be declared',2,'Computers')"
        h2="INSERT INTO quiz_questions VALUES('Which is a method of searching a value?','Diagonal','Top to Bottom','Structural','Linear',4,'Computers')"
        h3="INSERT INTO quiz_questions VALUES('What in Python contains variables,classes,statements,functions related to a task?','Group','Package','Module','Case',3,'Computers')"
        h4="INSERT INTO quiz_questions VALUES('Which module offers tools for scientific calculations in Python?','tkinter','NumPy','Malplotlib','SciPy',4,'Computers')"
        h5="INSERT INTO quiz_questions VALUES('Partitioning a program into individual components is called-','Functionality','Modularity','Accessibility','Snipping',2,'Computers')"
        i1="INSERT INTO quiz_questions VALUES('What is the extension of a Binary File?','.xlsx','.py','.dat','.csv',3,'Computers')"
        i2="INSERT INTO quiz_questions VALUES('A multiline string is also called-','multistring','lenghtstring','longstring','docstring',4,'Computers')"
        i3="INSERT INTO quiz_questions VALUES('What is the escape sequence for a newline in Python?','\n','','/q','/n',1,'Computers')"
        i4="INSERT INTO quiz_questions VALUES('In file handling what does r+ in file handling mean?','read and write','write and read','read and append','append and read',1,'Computers')"
        i5="INSERT INTO quiz_questions VALUES('We can suppress EOL translation in a text file by giving which argument in open()?','Question Mark','Arrow','tab','newline',4,'Computers')"
        j1="INSERT INTO quiz_questions VALUES('Why is binary search preferred over linear search?','Binary search takes a longer time','Results are more accurate','Binary search is faster','Linear search does not work on lists',3,'Computers')"
        j2="INSERT INTO quiz_questions VALUES('Which of the following is a concise description of a list?','List comprehension','List Shortening','List Slicing','List traversing',1,'Computers')"
        j3="INSERT INTO quiz_questions VALUES('Can stacks be implemented using lists?','Maybe','No','Yes','None of these',3,'Computers')"
        j4="INSERT INTO quiz_questions VALUES('Insertion and deletion operations in a QUEUE is known as','push and pop','enqueue and dequeue','Insert and Delete','None of these',2,'Computers')"
        j5="INSERT INTO quiz_questions VALUES('What is the term given to  insertion in a full queue?','Program will give ERROR','NULL EXCEPTION','UNDERFLOW','OVERFLOW',4,'Computers')"


        c.execute(a)
        c.execute(b)
        c.execute(d)
        c.execute(e)
        c.execute(f)
        c.execute(g)
        c.execute(h)
        c.execute(i)
        c.execute(j)
        c.execute(k)
        c.execute(l)
        c.execute(m)
        c.execute(n)
        c.execute(o)
        c.execute(p)
        c.execute(q)
        c.execute(r)
        c.execute(s)
        c.execute(t)
        c.execute(u)
        c.execute(v)
        c.execute(w)
        c.execute(x)
        c.execute(y)
        c.execute(z)
        c.execute(a1)
        c.execute(a2)
        c.execute(a3)
        c.execute(a4)
        c.execute(a5)
        c.execute(b1)
        c.execute(b2)
        c.execute(b3)
        c.execute(b4)
        c.execute(b5)
        c.execute(c1)
        c.execute(c2)
        c.execute(c3)
        c.execute(c4)
        c.execute(c5)
        c.execute(d1)
        c.execute(d2)
        c.execute(d3)
        c.execute(d4)
        c.execute(d5)
        c.execute(e1)
        c.execute(e2)
        c.execute(e3)
        c.execute(e4)
        c.execute(e5)
        c.execute(f1)
        c.execute(f2)
        c.execute(f3)
        c.execute(f4)
        c.execute(f5)
        c.execute(g1)
        c.execute(g2)
        c.execute(g3)
        c.execute(g4)
        c.execute(g5)
        c.execute(h1)
        c.execute(h2)
        c.execute(h3)
        c.execute(h4)
        c.execute(h5)
        c.execute(i1)
        c.execute(i2)
        c.execute(i3)
        c.execute(i4)
        c.execute(i5)
        c.execute(j1)
        c.execute(j2)
        c.execute(j3)
        c.execute(j4)
        c.execute(j5)

        myconn.commit()

        def Quiz_game(arr):

            global y
            
            global i

            global ans

            print("////////////////////////////////////////////////////////////////////////////////////////////////////",'\n')      
            print("Question Number",i,'is : ',arr[0],"\n")
            print("Option 1 is : " , arr[1],"\n")
            print("Option 2 is : " , arr[2],"\n")
            print("Option 3 is : " , arr[3],"\n")
            print("Option 4 is : " , arr[4],"\n")
            print("Or press 9 to exit the game\n")
            
            ans = int(input("Please enter the option number which you think is correct: "))

            
               
            if ans == 1 or ans== 2 or ans== 3 or ans== 4:
                
                if ans == arr[5]:
                    y+=1
                    print(" \n-->Correct")
                    print(" \n-->1 Point Obtained")
                    print(" \n-->Current Score is : ",y,'\n')
                       
                else:
                    print("\n-->Incorrect")
                    print("\n-->No Points Obtained\n")
                    print("-->Current Score is : ",y," out of",i,'\n')
                    print('The correct answer is option :',arr[5],'\n\n')
         
            elif ans == 9:
                    print("\nThank you for playing, hope you had fun\n")
                    print("Your current score is",y,'\n')
                    

            else:
                print("\n-->Invalid choice\n")
                print("-->No points obtained\n")
               

        y = 0
        int(y)

        print("Press 1 for Administrator mode \n")
        print("Press 2 for Player mode \n")
        print("Press 3 to view learder board \n")
        print("Press 4 to Exit\n")

        k1 = int(input("Please enter your choice here : "))

        if k1 == 4:
            break

        elif k1 == 3:
            
            c.execute("use quiz")
            
            c.execute("select * from player_details order by Total_points desc")
            
            ddta = c.fetchall()
            
            for m1 in ddta:
                
                print(m1, "\n")
            

        elif k1 == 1:
            
            print("Password is required for Administrator access \n")
            
            k2 = int(input("Please enter the Administrator Password \n"))
            
            if k2 == 7090:
                
                print("Press 1 to view all questions \n")
                print("Press 2 to add a new question \n")
                print("Press 3 to delete the database \n")

                k3 = int(input("Enter your choice \n"))

                if k3 == 1:
                    
                    c.execute("use quiz")
                    
                    c.execute("select * from quiz_questions order by subject")

                    data = c.fetchall()
                    
                    for i in data:
                        print(i,"\n")
                    
                elif k3 == 2:

                    st1 = str(input("Enter the question \n"))
                    st2 = str(input("Enter the option 1 \n"))
                    st3 = str(input("Enter the option 2 \n"))
                    st4 = str(input("Enter the option 3 \n"))
                    st5 = str(input("Enter the option 4 \n"))
                    st6 = int(input("Enter the correct option number \n"))
                    st7 = str(input("Enter the Subject \n"))
                    
                    st="INSERT INTO quiz_questions(question,op1,op2,op3,op4,answer,subject)VALUES('{}','{}','{}','{}','{}','{}','{}')".format(st1,st2,st3,st4,st5,st6,st7)
                    
                    c.execute(st)

                    print("The question has been added.")

                else:
                    print("WARNING \n")
                    print("This action cannot be reversed \n")

                    a6 = str(input("Do you still want to delete the database?(y/n)\n"))

                    if a6 == 'y':
                    
                        c.execute("Drop database quiz")
                        print("The database has been deleted\n\n")

                    else:
                        print("Database has not been deleted\n\n")
                        
                    
            else:
                print("Password is invalid")
                    
        else:
            
            nm = str(input("Please enter your name"))
            
            c.execute("Select * from quiz_questions")
     

            print("//////////////////////////////////////////////////////////////////////////////////////////////////////////",'\n')
            print("-->INSTRUCTIONS : ",'\n')
            print("-->All questions are Multiple Choice Questions with 4 options each.\n")
            print("-->The player will get only one try for each question.\n")
            print("-->The player will be asked to give a numerical input the answer for each question.\n")
            print("-->The player will not be given extra chances for incorrectly answered questions\n")
            print("-->Only 1,2,3,4 and 9 are valid choices.\n")
            print("-->Invalid entries will result in no points being obtained for that question.\n")
            print("-->Each question carries 1 point for a total of 70 points.","\n")


            for i in range(1,76):
      
                a = c.fetchone()
            
                Quiz_game(a)

                if ans == 9:

                    aaa = "INSERT INTO player_details(Name,Total_Points)VALUES(%s,%s)"

                    val = [(nm,y)]

                    c.executemany(aaa,val)

                    myconn.commit()

                    break
            

