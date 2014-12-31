# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
string_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

#I am creating a dictionary that will take in each user and the games/friends associated with them. 
#I will run through each sentence and since they each begin with a user name associated them with the correct person becomes much easier. 

def create_data_structure(string_input):
    network={}
    if not string_input:
        return network
    
    lines=string_input.split('.')
    #break the string input into different string by utilizing the period
    
    for word in range(0, len(lines)-1,2):
        userline=lines[word]
        userline=userline.split(' ')
        user=userline[0]
        
        #we split the sentence (string) into individual words and we know that the first word is the user
        
        
        
        friendline=lines[word]
        friendline=friendline.split(' is connected to ')[1]
        friendline=friendline.split(', ')
           
        
        #here the line that lists the user and friends is found via a for loop then broken down
        #into individual strings via split and now can be dissected
        #based on the knowledge of
        #the sentence structure to bring back the appropriate words
        
        gameline=lines[word+1]
        gameline=gameline.split('likes to play ')[1]
        gameline=gameline.split(', ')
        
        
        
        
        # similar construct to the friendline variable but first we need to move the
        #for loop to the appropriate sentence.
        
        
        games=gameline
        friends=friendline
        
        
        
        network[user]={'friends':friends,'games':games}
        
    return network


        #since the string_input's structure is friends sentence then game sentence we can be confident building
        #our network in this fashion even tho hard values are used since each loops finds friends then games
        #and has them attached to the correct user. Otherwise we would need to check the beginning
        #of each sentence to attach them to the correct user.





    
           
           
        
        
            
            
            
           
       
        
    
#create_data_structure(string_input)

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

#purpose of this function is to call the friends of the user using the previously created network

def get_connections(network, user):
    if user in network:
        return network[user]['friends']
    else:
        return None
    




	


# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.

#purpose of this function is to recall the games liked by users using the previously built network

def get_games_liked(network,user):
    if user in network:
        return network[user]['games']
    else:
        return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.

#purpose of this function is to determine if both users are in a network and friends
#if they are not friends we add the connection and update the network

def add_connection(network, user_A, user_B):
    if user_A in network:
        if user_B in network:
            if user_B not in get_connections(network,user_A):
                get_connections(network,user_A).append(user_B)
                return network
            else: return network
        else: return False
    else: return False
    
    #since the arguments state we are only looking for essentially user_B
    #in the friendlist of user_A once we establish they are both users
    #and that connection doesnt exist we simply append the list and return
    #the updated network. Otherwise we return the network unchanged
	

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user]={'friends':[],'games':games}
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.

#This function determines who are friends of friends and if not recalls that

def get_secondary_connections(network, user):
   second=[]
   if get_connections(network,user)==second:
        return second
   if user not in network:
        return None
   else:
       
        for friendy in get_connections(network,user):
            for name in get_connections(network,friendy):
                if name not in second:
                    second.append(name)
                
                    
                    
                
            
            

   return second
        
       
        
       

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.

#This process determines if they have mutual friends by finding friends, comparing,
#then adding that individual to an empty list

def connections_in_common(network, user_A, user_B):
    common=[]
    if user_A not in network or user_B not in network:
        return False
    else:
        for friendy in get_connections(network, user_A):
            if friendy in get_connections(network, user_B):
                common.append(friendy)
                
    return len(common)

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

#This procedure determines the degrees that 2 individuals are seperated and the inidividuals
#between them. It uses recurse to repeat  process of finding friends of friends adding them
#to an empty list then searching that list for the specific individual. It repeats these
#processes until a successful run then returns that path.

def path_to_friend(network,user_A,user_B, friendlist=None):
    
    if user_A not in network or user_B not in network:
            return None
        
    if friendlist is None:
        friendlist=[]
        
    friendlist=friendlist+[user_A]
    if user_B in get_connections(network, user_A):
        return friendlist+[user_B]
    else:
        for friendly in get_connections(network, user_A):
            if friendly not in friendlist:
                friendlist2=path_to_friend(network,friendly,user_B, friendlist)
                if friendlist2:
                    return friendlist2
          
               
	
	return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Find any game to users may have in common. We are assuming they are both in the network.
#If not we want a False signal to be called or if no common likes a blank data set
# To do this we will use a similar procedure to connections_in_common but substituting 
#get_connections with get_games

def games_in_common(network, user_A, user_B):
    common=[]
    if user_A not in network or user_B not in network:
        return False
    else:
        for thegame in get_games_liked(network, user_A):
            if thegame in get_games_liked(network, user_B):
                common.append(thegame)
    return common



