% predicate to check if alpha prune is possible.
is_alpha_prune_possible(Alpha,V):- V =< Alpha.

% predicate to check if beta prune is possible.
is_beta_prune_possible(V,Beta):- V >= Beta.

% functions to update alpha and beta.
update_alpha((Alpha,Beta),V,(NewAlpha,NewBeta)):- V > Alpha,  NewAlpha = V, NewBeta = Beta.
update_alpha((Alpha,Beta),V,(NewAlpha,NewBeta)):- V =< Alpha, NewAlpha = Alpha, NewBeta = Beta.

update_beta((Alpha,Beta),V,(NewAlpha,NewBeta)):- V < Beta,  NewBeta = V, NewAlpha = Alpha.
update_beta((Alpha,Beta),V,(NewAlpha,NewBeta)):- V >= Beta, NewBeta = Beta, NewAlpha = Alpha.

% alphabeta helper methods to perform min-max and alpha-beta pruning.
% These methods follow uni-snarf-twiki pattern discussed in the class.
alphabetaHelper(l(X),_,L,X) :- L = [("Leaf Value: ", X)].

alphabetaHelper(maximum([N1]),(Alpha,Beta), L1, Res):-  alphabetaHelper(N1,(Alpha,Beta), L1, Res).
alphabetaHelper(maximum([N1|N2]),(Alpha,Beta),L, Res):-
    alphabetaHelper(N1,(Alpha,Beta), L1, V1),
    is_beta_prune_possible(V1,Beta),
    Res = V1,
    append(L1,[("Max Node Value: ", Res)],L2),
    append(L2,[("Beta Prune: ", N2)],L).

alphabetaHelper(maximum([N1|N2]),(Alpha,Beta), L, Res):-
    alphabetaHelper(N1,(Alpha,Beta),L1, V1),
    not(is_beta_prune_possible(V1,Beta)),
    update_alpha((Alpha,Beta),V1,(NewAlpha,NewBeta)),
    alphabetaHelper(maximum(N2),(NewAlpha,NewBeta), L2, V2),
    Res is max(V1,V2),
    append(L1,L2,LeafNodes),
    append(LeafNodes,[("Max node Value: ", Res)],L).

alphabetaHelper(minimum([N1]),(Alpha,Beta), L1, Res):-  alphabetaHelper(N1,(Alpha,Beta), L1, Res).
alphabetaHelper(minimum([N1|N2]),(Alpha,Beta), L, Res):-
    alphabetaHelper(N1,(Alpha,Beta), L1, V1),
    is_alpha_prune_possible(Alpha,V1),
    Res = V1,
    append(L1,[("Min Node Value: ", Res)],L2),
    append(L2,[("Alpha Prune: ", N2)],L).

alphabetaHelper(minimum([N1|N2]),(Alpha,Beta), L, Res):-
    alphabetaHelper(N1,(Alpha,Beta), L1, V1),
    not(is_alpha_prune_possible(Alpha,V1)),
    update_beta((Alpha,Beta),V1,(NewAlpha,NewBeta)),
    alphabetaHelper(minimum(N2),(NewAlpha,NewBeta), L2, V2),
    Res is min(V1,V2),
    append(L1,L2,LeafNodes),
    append(LeafNodes,[("Min node Value: ", Res)],L).

% Function to trigger alpha-beta logic.
alphabeta(T,V):- alphabetaHelper(T,(-9999999,9999999), L, V), write_results(L).

% logic to write the results to the console.
write_results([]).
write_results([H|T]):- H = (A,B), write(A), writeln(B), write_results(T).

% Testing
tree1(T):- T = maximum(
    [minimum(
	 [maximum(
	      [minimum([l(2),l(12)]),
	       minimum([l(6),l(10)])]),
	  maximum(
	      [minimum([l(8),l(19)]),
	       minimum([l(17),l(21)])])]),
     minimum(
	 [maximum(
	      [minimum([l(5),l(4)]),
	       minimum([l(15),l(9)])]),
	  maximum(
	      [minimum([l(12),l(16)]),
	       minimum([l(2),l(12)])])])]).

tree2(T):- T = maximum(
   [minimum(
  [maximum(
       [minimum([l(5),l(4)]),
        minimum([l(15),l(9)])]),
   maximum(
       [minimum([l(12),l(16)]),
        minimum([l(2),l(12)])])]),
   minimum(
	 [maximum(
	      [minimum([l(2),l(12)]),
	       minimum([l(6),l(10)])]),
	  maximum(
	      [minimum([l(8),l(19)]),
	       minimum([l(17),l(21)])])])]).

tree3(T):- T = maximum(
   [minimum(
	 [maximum(
	      [minimum([l(32),l(12),l(8)]),
	       minimum([l(6),l(10),l(9)]),
        minimum([l(4),l(6),l(7)])]),
	  maximum(
	      [minimum([l(8),l(19),l(7)]),
	       minimum([l(17),l(21),l(10)]),
        minimum([l(4),l(6),l(7)])]),
   maximum(
	      [minimum([l(3),l(4),l(5)]),
	       minimum([l(8),l(9),l(7)]),
        minimum([l(10),l(11),l(12)])])]),
    minimum(
	 [maximum(
	      [minimum([l(5),l(4),l(11)]),
	       minimum([l(15),l(9),l(10)]),
        minimum([l(5),l(4),l(6)])]),
	  maximum(
	      [minimum([l(12),l(16),l(10)]),
	       minimum([l(2),l(12),l(24)]),
        minimum([l(5),l(4),l(6)])]),
   maximum(
	      [minimum([l(1),l(2),l(3)]),
	       minimum([l(3),l(1),l(4)]),
        minimum([l(4),l(6),l(7)])])]),
    minimum(
	 [maximum(
	      [minimum([l(4),l(3),l(1)]),
	       minimum([l(9),l(8),l(11)]),
        minimum([l(10),l(4),l(61)])]),
	  maximum(
	      [minimum([l(13),l(34),l(123)]),
	       minimum([l(3),l(13),l(234)]),
        minimum([l(5),l(0),l(9)])]),
   maximum(
	      [minimum([l(1),l(9),l(3)]),
	       minimum([l(9),l(1),l(5)]),
        minimum([l(4),l(2),l(7)])])])]).

% Testing
% tree1(T), alphabeta(T,V).
% tree2(T), alphabeta(T,V).
% tree3(T), alphabeta(T,V).
