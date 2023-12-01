# 🙃 emojilang

emojilang is a toy language comprised only of emojis.

## Syntax

```
# control structures
🤔 - if
🔥 - while

# boolean operators
🌘 - <
🌒 - >
🌖 - <=
🌔 - >=
🌕 - ==
🌑 - !=

# delimiters
🌜 - (
🌛 - )
🛫 - {
🛬 - }

# literals
😁 - true
😢 - false
0️⃣ - 0
1️⃣ - 1
2️⃣ - 2
3️⃣ - 3
4️⃣ - 4
5️⃣ - 5
6️⃣ - 6
7️⃣ - 7
8️⃣ - 8
9️⃣ - 9

# variables and assignment
📌 - assignment
🦁,🐹,🛵,📺,🥨, etc. - variable names

# utilities
📢 - print
🤫 - comment
💤 - sleep
```


## Examples

**Printing a numeric literal**

```
📢🌜1️⃣🌛

> 1
```

**Sleep for seconds**

```
💤🌜1️⃣🌛
```

**Variable assignment**

```
🦁📌3️⃣
📢🌜🦁🌛

> 3
```

**Commenting**

```
🤫 the next line assigns 3️⃣ to 🦁
🦁📌3️⃣
```

**If, and nested if, statements**

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

**Boolean literals**

```
🤔🌜😁🌛 🛫 
    🤫 this should be executed
    📢🌜1️⃣🌛
🛬

🤔🌜😢🌛 🛫 
    🤫 this should not be executed
    📢🌜1️⃣🌛
🛬
```

**Boolean comparisons**

```
🤔🌜1️⃣🌕1️⃣🌛 🛫 
    🤫 this should be executed because 1 is equal to 1
    📢🌜1️⃣🌛
🛬

🤔🌜1️⃣🌑1️⃣🌛 🛫 
    🤫 this should not be executed because 1 is equal to 1
    📢🌜1️⃣🌛
🛬

🤔🌜1️⃣🌒0️⃣🌛 🛫 
    🤫 this should be executed because 1 is greater than 0
    📢🌜1️⃣🌛
🛬
```
**While loop**

```
🔥🌜😁🌛 🛫
    🤫 this should always be executed
    📢🌜1️⃣🌛
    💤🌜3️⃣🌛
🛬
```


## Features
- [ ] mathematical operators
- [x] while loop
- [x] sleep
- [x] if statement
- [x] comments
- [x] boolean operators
- [x] boolean literals
- [x] variables and assignment
- [x] print
- [ ] ifelse statement


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