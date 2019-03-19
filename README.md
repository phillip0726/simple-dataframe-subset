# simple-dataframe-subset
- This code used the python pandas module
- We assume that test1's columns and test2's columns are the same.

# output
- data/test1

|  | A | B | C | D | E | F |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:| 
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 1 | 11 | 12 | 13 | 14 | 15 | 16 |
| 2 | 21 | 22 | 23 | 24 | 25 | 26 |
| 3 | 31 | 32 | 33 | 34 | 35 | 36 |
| 4 | 41 | 42 | 43 | 44 | 45 | 46 |
| 5 | 51 | 52 | 53 | 54 | 55 | 56 |
| 6 | 61 | 62 | 63 | 64 | 65 | 66 |
| 7 | 71 | 72 | 73 | 74 | 75 | 76 |
| 8 | 81 | 82 | 83 | 84 | 85 | 86 |
| 9 | 91 | 92 | 93 | 94 | 95 | 96 |
| 10 | 101 | 102 | 103 | 104 | 105 | 106 |



- data/test2

|  | A | B | C | D | E | F |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:| 
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 1 | 101 | 102 | 103 | 104 | 105 | 106 |
| 2 | 21 | 22 | 23 | 24 | 25 | 26 |
| 3 | 31 | 32 | 33 | 34 | 35 | 36 |
| 4 | 111 | 112 | 113 | 114 | 115 | 116 |
| 5 | 51 | 52 | 53 | 54 | 55 | 56 |
| 6 | 121 | 122 | 123 | 124 | 125 | 126 |
| 7 | 131 | 132 | 133 | 134 | 135 | 136 |
| 8 | 81 | 82 | 83 | 84 | 85 | 86 |
| 9 | 151 | 152 | 153 | 154 | 155 | 156 |
| 10 | 141 | 142 | 143 | 144 | 145 | 146 |
| 11 | 91 | 92 | 93 | 94 | 95 | 96 |


- test2 - test1

|  | A | B | C | D | E | F |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:| 
| 4 | 111 | 112 | 113 | 114 | 115 | 116 |
| 6 | 121 | 122 | 123 | 124 | 125 | 126 |
| 7 | 131 | 132 | 133 | 134 | 135 | 136 |
| 9 | 151 | 152 | 153 | 154 | 155 | 156 |
| 10 | 141 | 142 | 143 | 144 | 145 | 146 |
