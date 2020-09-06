# 30 longest substring without repeating characters

# pwwkew 해설 과정

# start 0 index 0 char p used: {p:0} max: 1
# start 0 index 1 char w used {p:0, w:1} max: 2
# start 2 index 2 char w used:{p:0, w:2} max: 2
# start 2 index 3 char k used {p:0, w:2, k:3} max: 2
# start 2 index 4 char e used : {p:0, w:2, k:3, e:4} max: 3
# start 3 index 5 char w used : {p:0, w:2, k:3, e:4} max: 3

# wke answer max_length: 3