#!/usr/bin/gawk -f
# source: https://opensource.com/article/21/4/gawk-letter-game?utm_campaign=intrel
# only count a-z, ignore A-Z and any other characters

BEGIN { LETTERS = "abcdefghijklmnopqrstuvwxyz" }

{
    len = length($0); for (i = 1; i <= len; i++) {
        c = substr($0, i, 1);
        ltr = index(LETTERS, c);

        if (ltr > 0) {
            ++count[ltr];
        }
    }
}

# print relative frequency of each letter

END {
    min = count[1]; for (ltr = 2; ltr <= 26; ltr++) {
        if (count[ltr] < min) {
            min = count[ltr];
        }
    }

    for (ltr = 1; ltr <= 26; ltr++) {
        print substr(LETTERS, ltr, 1), int(count[ltr] / min);
    }
}