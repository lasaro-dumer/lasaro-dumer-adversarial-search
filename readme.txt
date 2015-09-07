/**********************************************************************
 *  Adversarial Search readme.txt template
 **********************************************************************/


Name: Lásaro Curtinaz Dumer
Student ID: 11112375-8


Hours to complete assignment (optional): 15


/**********************************************************************
 *  Explain briefly how you implemented the helper methods for
 * \texttt{get_next_move()}.
 **********************************************************************/
 I started more like the traditional algorithm, using a "result" method to
 calculate a successor for each time, but later switched to a "successors" method,
 like the assignment description, to calculate all successors of a state at once

 The Minimax algorithm itself is divided in  two methods, one to evaluate the "minMove"
 and the other to evaluate the "maxMove"

 There is a "isTerminal" and a "utility" method too, the first one is to tell if a node is a
 terminal state or not, and the latter is to tell the value of a state

/**********************************************************************
 *  Explain briefly how you represented the utility of the end game.
 * Did you use different values for different end configurations?
 **********************************************************************/
 Yes, there is different values for different ends
 If it is a tie, then it will be zero
 If the minimax player wins, then "moves until finish"-10
 If the minimax player losses, then 10-"moves until finish"

/**********************************************************************
 *  Explain briefly how you generated the successor moves.
 **********************************************************************/
 The successors are generated based on the free cells of the current state
 Each successors, i.e. state, will be the following tuple representation

 state[0] = state's current 'board'
 state[1] = number of moves from the start state until this
 state[2] = the action the lead to this state
 state[3] = number of free cells in this state

/**********************************************************************
 *  How often does your player wins when it plays as X against a
 * randomizing player, and how often does it wins when it plays as O?
 **********************************************************************/
 As X my player wins 80% or more, and if it's not a win it will mostly be a tie
 As O my player wins 90% or more, and if it's not a win it will mostly be a tie

/**********************************************************************
 *  If you wanted to solve some other games using variations of minimax
 * (such as the ones seen in class), which ones would you use, and how
 * would you integrate them into this code? Why?
 **********************************************************************/

/**********************************************************************
 *  If you did the extra credit, describe your algorithm briefly and
 *  state the order of growth of the running time (in the worst case)
 *  for \texttt{get_next_move()}.
 **********************************************************************/
 The main difference between it and minimax is that it implements alphabeta pruning,
 cutting off the unnecessary branches
 The alphabeta algorithm is between 20 and 60 times faster than minimax

/**********************************************************************
 *  Known bugs / limitations.
 **********************************************************************/



/**********************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including staff, classmates, and
 *  friends) and attribute them by name.
 **********************************************************************/
Compared some times and correctness with Fábio Delazeri Riffel, without exchange of code, only times and wins/losses rate




/**********************************************************************
 *  Describe any serious problems you encountered.
 **********************************************************************/
I have had serious problems with my wins/losses ratio, had to test and debug the utility do see that it was wrong



/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback
 *  on how much you learned from doing the assignment, and whether
 *  you enjoyed doing it.
 **********************************************************************/
Same history here, no previous semester's code, so starting from zero, and the same thought: It's better this time
