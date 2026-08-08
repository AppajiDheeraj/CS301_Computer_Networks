# Socket Programming

Python 3 socket-programming solutions for the ten Week 4 exercises. They use only the Python standard library and default to `127.0.0.1`, so run the server and client in two terminals on the same computer.

## Question-to-file mapping

| # | Exercise | Server | Client | Protocol / port |
| --- | --- | --- | --- | --- |
| 1 | Client sends a string; server converts it to uppercase and returns it. | `q01/server.py` | `q01/client.py` | TCP / 5001 |
| 2 | Client sends two numbers and an operator (`+`, `-`, `*`, `/`); server returns the result. | `q02/server.py` | `q02/client.py` | TCP / 5002 |
| 3 | Client sends an integer; server determines whether it is prime. | `q03/server.py` | `q03/client.py` | UDP / 5003 |
| 4 | Echo server returns each client message until the client sends `exit`. | `q04/server.py` | `q04/client.py` | TCP / 5004 |
| 5 | Client sends a filename; server returns its line, word, and character counts. | `q05/server.py` | `q05/client.py` | TCP / 5005 |
| 6 | Client sends a text message; server displays it with the client's IP address and port. | `q06/server.py` | `q06/client.py` | UDP / 5006 |
| 7 | Server accepts a string and checks whether it is a palindrome. | `q07/server.py` | `q07/client.py` | TCP / 5007 |
| 8 | Transfer a text file from the client to the server. | `q08/server.py` | `q08/client.py` | TCP / 5008 |
| 9 | Client sends a sentence; server returns vowel, consonant, and word counts. | `q09/server.py` | `q09/client.py` | TCP / 5009 |
| 10 | Client sends an integer array; server returns the sorted array. | `q10/server.py` | `q10/client.py` | TCP / 5010 |

## Run an exercise

From this folder, start its server in one terminal, then its client in another:

```bash
cd Socket-Programming
python3 q01/server.py
python3 q01/client.py
```

Repeat with the matching `q02`–`q10` folders. Stop a server with `Ctrl+C`.

For Question 5, enter a filename that exists inside the folder where the server was started (for example `README.md`). Question 8 saves the received content as `received_file.bin` in the server's current folder.

## Check

```bash
python3 test_exercises.py
python3 -m py_compile q*/client.py q*/server.py
```
