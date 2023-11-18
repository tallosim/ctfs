# Scan-chu, I choose you! - Misc

This was a simple challenge which required a little googling. The challenge had a `bro-what.txt` (`level-1.txt`) file which contained the following text:

```txt
pi pi pi pi pi pi pi pi pi pi pika pipi pi pipi pi pi pi pipi pi pi pi pi pi pi pi pipi pi pi pi pi pi pi pi pi pi pi pichu pichu pichu pichu ka chu pipi pipi pipi pipi ka ka ka ka ka ka ka ka ka pikach ...
```

This chiper text was a [Pikalang](https://esolangs.org/wiki/Pikalang) code.

I used [this](https://martin.ingesen.no/Pikalang/) online tool to decode the text. The decoded text was:

```txt
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>---------.++.--.<<++++++++++.-------.>>.++.<<++++++++++.>>--.++.<<--.>>--.<<++.>>.++..<<.---.-------.>>--.++.<<++++++++++.>>--.++.<<--.>>--.<<------- ...
```

This chiper text was a [Brainfuck](https://esolangs.org/wiki/Brainfuck) code.

I used [this](https://www.splitbrain.org/_static/ook/) online tool to decode the text. The decoded text was:

```txt
[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+( ...
```

This chiper text was a [JSFuck](https://jsfuck.com/) code. As somebody from the community pointed out, this can be directly run by a JS interpreter and get the flag, but I took a little longer route to extract the flag.

I used [this](https://enkhee-osiris.github.io/Decoder-JSFuck/) online tool to decode the text. The decoded text was:

```txt
return"\110\113N\173\167\150\157\137is\137as\150\137\153e\164\143\150u\160\175"
```

This was an escaped string. I used a Python print to get back the key.

```python
print("\110\113N\173\167\150\157\137is\137as\150\137\153e\164\143\150u\160\175")
```

The final flag was:

```txt
HKN{who_is_ash_ketchup}
```
