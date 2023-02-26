# Ten-pin bowling scorer

Ten-pin bowling has a slightly complex scoring system (look it up). The aim here is to write a program that will take user input of the form:

```
^((\d|A){2}[ ]+){9}(\d|A){2}((\d|A)){0,1}$
```

and output a value between 0 and 300 for the score of the game.

Watch out for:
* invalid inputs like "83"; the digits in each pair must sum to <= 0xA.
* The last frame is special and can have three throws in it. The first two digits must sum to <= )xA still, but the third digit can be anything in the range [0x0,0xA].

Some examples of the inputs and corresponding outputs might be

```
=========================================================
input :            00  00  00  00  00  00  00  00  00  00
---------------------------------------------------------
bowling notation : --  --  --  --  --  --  --  --  --  --
cumulative score : 00  00  00  00  00  00  00  00  00  00
---------------------------------------------------------
output : 0
=========================================================

=========================================================
input :            15  91  36  A0  15  91  A0  A0  0A 194
---------------------------------------------------------
bowling notation : 16  9/  39   X  16  9/   X   X  0/ 1/4
cumulative score : 06  19  28  44  50  70  90 110 121 135
---------------------------------------------------------
output : 135
=========================================================

=========================================================
input :            45  26  63  55  44  45  A0  90  11  23
---------------------------------------------------------
bowling notation : 45  26  63  5/  44  45   X  9-  11  23
cumulative score : 09  17  26  40  48  57  76  85  87  92
---------------------------------------------------------
output : 92
=========================================================
```

