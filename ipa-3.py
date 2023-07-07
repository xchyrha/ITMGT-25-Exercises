#!/usr/bin/env python
# coding: utf-8

# In[15]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Check if from_member follows to_member
    if from_member in social_graph.get(to_member, {}).get("following", []):
        if to_member in social_graph.get(from_member, {}).get("following", []):
            return "friends"
        return "followed by"

    if to_member in social_graph.get(from_member, {}).get("following", []):
        return "follower"

    return "no relationship"


# In[19]:


#For testing

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

relationship_status("@bongolpoc", "@joaquin", social_graph)


# In[3]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if row == ['X', 'X', 'X'] or row == ['X', 'X', 'X','X'] or row == ['X', 'X', 'X', 'X', 'X'] or row == ['X', 'X', 'X', 'X', 'X', 'X']:
            return "X"
        elif row == ['O', 'O', 'O'] or row == ['O', 'O', 'O', 'O'] or row == ['O', 'O', 'O', 'O', 'O'] or row == ['O', 'O', 'O', 'O','O','O'] :
            return "O"

    for col in range(len(board[0])):
        if all(board[row][col] == 'X' for row in range(len(board))):
            return "X"
        elif all(board[row][col] == 'O' for row in range(len(board))):
            return "O"
            
    if len(board[0])==3:
        if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
            return "X"
        elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
            return "O"
    elif len(board[0])==4:
        if board[0][0] == board[1][1] == board[2][2] == board[3][3]=='X' or board[0][3] == board[1][2] == board[2][1] == board[3][0]=='X':
            return "X"
        elif board[0][0] == board[1][1] == board[2][2] == board[3][3]=='O' or board[0][3] == board[1][2] == board[2][1] == board[3][0]=='O':
            return "O"
    elif len(board[0])==5:
        if board[0][0] == board[1][1] == board[2][2] == board[3][3]==board[4][4]=='X' or board[0][4] == board[1][3] == board[2][2] == board[3][1]==board[4][0]=='X':
            return "X"
        elif board[0][0] == board[1][1] == board[2][2] == board[3][3]==board[4][4]=='O' or board[0][4] == board[1][3] == board[2][2] == board[3][1]==board[4][0]=='O':
            return "O"
    elif len(board[0])==6:
        if board[0][0] == board[1][1] == board[2][2] == board[3][3]==board[4][4]==board[5][5]=='X' or board[0][5] == board[1][4] == board[2][3] == board[3][2]==board[4][1]==board[5][0]=='X':
            return "X"
        elif board[0][0] == board[1][1] == board[2][2] == board[3][3]==board[4][4]==board[5][5]=='O' or board[0][5] == board[1][4] == board[2][3] == board[3][2]==board[4][1]==board[5][0]=='O':
            return "O"

    return "NO WINNER"
# In[21]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    journey =(first_stop, second_stop)
    first_stop=journey[0]
    second_stop=journey[1]
    traveltime=0
    new_map={}
    index_start=0
    index_end=0
   
    counter=0
    for route in route_map.keys():
        counter+=1
        if route[0]==first_stop:
            #find the index
            index_start+=counter
        if route[1]==second_stop:
            index_end+=counter

    if index_start<=index_end:
        routes = list(route_map.items())
        subroute = routes[index_start - 1:index_end]
        new_map.update(subroute)

        for item in new_map.items():
            mins = item[1]["travel_time_mins"]
            traveltime += mins
        return traveltime
   
    elif index_start>index_end:
        routes = list(route_map.items())
        index_end=index_end+len(routes)
        subroute = routes[index_start - 1:len(routes)]
        new_map.update(subroute)
        excess_subroute=routes[0:index_end-len(routes)]
        new_map.update(excess_subroute)
        
        for item in new_map.items():
            mins = item[1]["travel_time_mins"]
            traveltime += mins
            
        return traveltime
