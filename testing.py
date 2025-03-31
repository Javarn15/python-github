# this program is for asking a studant if they are going to the ball
print(" time for the school ball")
ball = input("are you planing to go to the school ball? type your awnser as (y or yes) ")
if ball.lower() == "y" or ball.lower() == "yes":
    partner = input("Are you planing to bring an out of school partner?type your answer as  (y or yes) ")
    if partner.lower() == "y" or partner.lower() == "yes":
        print ("make sure you fill in the out of school partner form!")
    else:
        print("make sure you fill in a permissin slip")
else:
    print("you can still watch the students entering the hall at 8pm")
 