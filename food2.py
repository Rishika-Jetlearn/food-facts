from tkinter import*



def facts(user):
    fa.delete(1.0,END)

    if user=="p":
        fa.insert(END,"The world’s first pizzeria opened in Naples, Italy, in 1738, but pizza didn’t become popular worldwide until after World War II! American soldiers stationed in Italy developed a love for the local pizza and brought their enthusiasm for it back home, sparking its boom in the U.S,then being known worldwide!")
    
    elif user=="c":
        fa.insert(END,"Here’s a cool fact about chips on their own: the world record for the largest serving of chips was set in 2020 in Melbourne, Australia. Weighing over 1.5 tons (or about 3,000 pounds), this mega-portion used thousands of potatoes and took a team of chefs to pull off. Now that’s a serious chip craving!")
    
    else:
        fa.insert(END,"Did you know that in the early 2000s, a burger chain called Burger King launched a promotion called the “Left-Handed Whopper”? They claimed it was designed specifically for left-handed people, with all the ingredients rotated 180 degrees. It was an April Fools' joke, but many people believed it and even requested it! The fun part? They made a whole marketing campaign around it, and it became a legendary prank in the fast food world!Talk about flipping the script on burgers! 🍔🤣")


window=Tk()
window.geometry("600x600")
window.title("Number guessing game")
window. configure(bg="#afedd3")

#buttons
image1=PhotoImage(file="pizza.png")
pizza=Button(window,image=image1,width=62,height=50,command=lambda: facts("p"))
pizza.grid(row=2,column=2,padx=130,pady=50)

image2=PhotoImage(file="chips.png")
chips=Button(window,image=image2,width=62,height=47,command=lambda: facts("c"))
chips.grid(row=3,column=2,padx=130,pady=50)

image3=PhotoImage(file="burger.png")
burger=Button(window,image=image3,width=62,height=62,command=lambda: facts("b"))
burger.grid(row=4,column=2,padx=130,pady=50)


#lables
fa=Text(window,height=6,width=60)
fa.grid(row=5,column=2)




window.mainloop()