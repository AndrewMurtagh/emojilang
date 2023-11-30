# 🙃 emojilang

emojilang is a toy language comprised only of emojis.

## Features
- [ ] boolean operators
- [ ] mathematical operators
- [ ] while loop
- [x] if statement
- [ ] ifelse statement
- [x] comments
- [ ] boolean expression
- [ ] boolean literals
- [x] variables and assignment
- [x] print

## Syntax

```
📌 - assignment
📢 - print
🤫 - comment
🤔 - if
🌤️ - ==
🌜 - (
🌛 - )
🛫 - {
🛬 - }
0️⃣ - 0
1️⃣ - 1
2️⃣ - 2
3️⃣ - 3
4️⃣ - 4
5️⃣ - 5
6️⃣ - 6
7️⃣ - 8
8️⃣ - 8
9️⃣ - 9
🦁,🐹,🛵,📺,🥨, etc. - variable names
```


## Examples

**Print a numeric literal**

```
📢🌜1️⃣🌛

> 1
```

**Variable assignment**

Assign a numeric literal to a variable and print its value:

```
🦁📌3️⃣
📢🌜🦁🌛

> 3
```

**Commenting**

Add single line comments.

```
🤫 the next line assigns 3️⃣ to 🦁
🦁📌3️⃣
```

**If statement**

Nested if statements can be evaluated.

```
🤔🌜1️⃣🌤️1️⃣🌛 🛫 

    🤫 this should be executed
    📢🌜2️⃣🌛

    🤔🌜1️⃣🌤️9️⃣🌛 🛫 

        🤫 this should not be executed
        📢🌜3️⃣🌛
    🛬

🛬
```




## Dependencies
```
pip3 install ply
```

## To run

```
alias emoji='python3 main.py'
emoji
```

## License

[MIT licensed](LICENSE)