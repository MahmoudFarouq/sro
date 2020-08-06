# Sro automation tools and tutorials.

Silkroad Online(sro) is an MMORPG game that i love, basically it's the only game i've ever loved and i have a great memories playing it back in 2006.

So when I came to play again after almost 10 years tring to revive some really beautiful memories from the past, I just got saddend.

Unfortunatly, good things don't last forever.

The game became full of Bots and you basically just open it, let the bot farm for you and do whatever you want. It also became more greedy and p2p game, to login you need to wait for a long time but if you pay a good price as a subscription you'll get in immediatly.

Moreover, people began to build their own private servers which were sickening, boring, buggy, not genuine and for the most part, it lost its taste.

Search for a good private server? I tried this for long time and when i finally found a good one and played in it for sometime the server owners just shut it down and voila.. go f@ck yourself.

So i thought why not build my own server that will be the exact same from back then but with the new stuff, skills and the good updates?

So after a long time of doubting myself(and i still do) i decided to just start. 
I searched the old forums and could find the 1.188 old server files, client and a clean DB.
This became my starting point, I had to properly set it up and start add things one by one.

But things are so much, weapons, items, degrees, skills, NPCs, Mobs and so much more.

The problem was that to add all this by hand or even using ready queries, the error factor would be really huge and i'll screw things up. Moreover, the tutorials on the old forums are just not complete, i had to open 4 tabs at the same time and read them together to add an npc with all it's required data, and as you might have guessed i made a lot of mistakes because of this inconsistencies. so why not first build and test some automation tools for the task to be handled properly without any human interaction? that would be great right?.

So this is it, This project is(will be) a collection of CLI tools that will allow anyone to just add whatever they want with the error factor as minimum as possible. I'll also Include tutorials for each Command to descripe what exactly does this command do and why did we do it like that, the *explaination* that basically never existed online and made me walk blindly and just copy paste things with Zero understanding.

The project is Incremental, I'll just add things as i go. And hopfully I'll cover a wide range of questions that you might ask when you start to make your own sro private server.

## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run sro cli application

$ sro --help


### run pytest / coverage

$ make test
```
