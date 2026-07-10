# Bank System

A small command-line banking app written in Python. You can create an account, log in, and then transfer, withdraw, deposit, or check your balance. Everything gets saved to a local JSON file, so no database setup needed — just run it.

I built this mostly as a way to practice working with file I/O, classes, and basic auth logic in Python. It's not meant to be production-ready (see the "known issues" section below), but it works for messing around with the core banking flow.

## What it does

- Register a new account (name + password)
- Log in with an existing account
- Transfer money to another user
- Withdraw funds
- Deposit funds
- Check your current balance
- Exit cleanly

All account data (name, password, balance) lives in `accounts.json`, which the app reads from and writes to as you use it.

## Project structure

```
.
├── main.py          # entry point — handles the login/register loop and menu
├── account.py        # Account class: registration, login, credential validation
├── services.py        # Services class: transfer, withdraw, deposit, balance, exit
└── accounts.json      # where all the account data is stored
```

## How to run it

You just need Python 3.12+ (it uses some newer f-string syntax internally). No extra dependencies — everything's standard library.

```bash
python3 main.py
```

From there it's all interactive:

1. It'll ask if you already have an account (Y/N).
2. If not, it walks you through registering one.
3. If you do, it asks for your name and password to log in.
4. Once you're in, you get a menu with the options above.

A few of the accounts already in `accounts.json` if you want to try logging in without registering first:

| name    | password  |
|---------|-----------|
| gustavo | Gus@123   |
| ana     | Ana#847   |
| carlos  | Car!2026  |

(There are more in the file — feel free to poke around.)

## Known issues / things to be aware of

I'm keeping this honest since it's a learning project, not a finished product:

- **Passwords are stored in plain text** in `accounts.json`. Don't use this for anything real — there's no hashing or encryption going on here.
- **Newly registered accounts don't get a starting balance.** The registration flow only saves `name` and `password`, so if you create a new account and immediately try to check your balance or deposit/withdraw, it'll break. Logging in with one of the pre-existing accounts avoids this.
- **The "sender" prompt during a transfer is a bit misleading.** It asks for the name of the person you're sending money to, not literally the "sender" — the money always moves out of whoever's currently logged in. Just something to keep in mind when using it.
- There's minimal input validation overall (e.g. typing something that isn't a number when the app expects an amount will crash it).

Contributions / suggestions welcome if you want to build on this.
