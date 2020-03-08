# upass-spork
i want to have my own little program to save all my passwords!


trying to be more sequre with my passwords, so i tought okay that my be great to have a little python programm.
that would handle all my password,
the initial idea is, encrypt everything so it cant be encoded, encrypt it with the one and only password, we dont use
in this program.

then if the correct password is entered we would load and decrypt everything (or what we need).
when we pass the "username" of that password i would like to have it copied to my control V, already so i can just paste it wherever.
and that is it basically.

maybe add autopass generators as well.


what is done ? :
so far the program let you fill username and password, on with it tries to open the user file,
if it doesnt exist it just generate one.
if it exist and the generated key does not work (means password is wrong!) then do nothing.

when in:
you have the option to quit, load , add
add : lets you to create a new password and encrypt it, add syntax => add name password/random/-r
where random/-r would generate a random 12 character password. (can be even longer)
and where passed anything else like password, would set the text to the password.

load : would load the given password vide the name! syntax : load name
where name is the name of the asked password.




done:
1. login system, type user and password.
2. add, get password.
3. generate random passwords.

4. copy the asked password to clipboard

todo:
1. make a shortcut to create a password when pressed a special combination of keys,
using the window name as the "password name" or something.

2. hopefully make it able to fill password/username for me.

maybes:
add actual gui, windows and stuff.
