
% FACTS
% The Facts that represent our Family are:john and mary are parents of peter and linda.peter and susan are parents of david.linda and james are parents of sarah.john, peter and james are males.mary, susan, linda and sarah are females.

% male is a predicate that is true if the person is male.
male(john).
male(peter).
male(david).
male(james).

% female is a predicate that is true if the person is female.
female(mary).
female(susan).
female(linda).
female(sarah).

% parent(X, Y) is true if X is the parent of Y.
parent(john, peter).
parent(mary, peter).

% parent(X, Y) is true if X is the parent of Y.
parent(john, linda).
parent(mary, linda).

% parent(X, Y) is true if X is the parent of Y.
parent(peter, david).
parent(susan, david).

% parent(X, Y) is true if X is the parent of Y.
parent(linda, sarah).
parent(james, sarah).

% RULES
% father(X, Y) is true if X is the father of Y.
father(X, Y) :-
    male(X),
    parent(X, Y).
    
% mother(X, Y) is true if X is the mother of Y.
mother(X, Y) :-
    female(X),
    parent(X, Y).

% child(X, Y) is true if X is the child of Y.
child(X, Y) :-
    parent(Y, X).

% grandparent(X, Y) is true if X is the grandparent of Y.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% grandchild(X, Y) is true if X is the grandchild of Y.
grandchild(X, Y) :-
   grandparent(Y, X).

% sibling(X, Y) is true if X and Y are siblings.
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
    
% uncle(X, Y) is true if X is the uncle of Y.
uncle(X, Y) :-
    male(X),
    sibling(X, Z),
    parent(Z, Y).

% aunt(X, Y) is true if X is the aunt of Y.
aunt(X, Y) :-
    female(X),
    sibling(X, Z),
    parent(Z, Y).

% cousin(X, Y) is true if X and Y are cousins.
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).