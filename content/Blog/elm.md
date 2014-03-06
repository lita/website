Title: Working with Elm
Date: 2014-03-05 02:07
Tags: elm, website hacker school
Slug: working-with-elm

Last week, we had Evan Czaplicki as our resident! He is an awesome guy who 
invented Elm, a functional language used for making interactive programs. It has
been awhile since I've done any functional programming. Basically, I've only 
written ghetto Scheme code back in college (if you went to Berkeley, the class 
was CS61A). But I've completely forgotten it. 

Evan gave a great talk for our batch, live coding a Mario game during the 
presentation! You guys have to check it out!

[Mario programmed in Elm][mario]

The talk was enough to get me to try to learn it, even though I 
had no intention on learning a functional programming language. I know this
was a distraction from learning web programming, but it's not like I was binging 
on a TV show... 

Elm is very similar to Haskell, ML, and OCaml. It is a statically-typed, 
functional language. If you don't have Haskell installed, installing Elm 
REALLY sucks right now. Evan is working on making an installer. For now, I 
mostly did my coding on the interactive browser, which compiles the code on Evan's
server.

[Try Elm!][try]

Starting was SOOOoo hard. I just tried writing a linked-list...

```
:::elm
data LinkedList a = Empty | Cons a (LinkedList a)
generateList x = if x == 0 then Empty 
                 else Cons x (generateList (x-1))
main = asText (generateList 10)
```

You have no idea how long this took me to write. Basically, I write an algebraic data type (ADT), which basically says I can be either "Empty" or a two element data with "a" and another LinkedList. Cons is a Lisp thing, that just means it 
constructs two elements. `generateList` just recursively creates a 
LinkedList from `x` to 0.

I knew making any project was going to be death after trying to do this. I decided I try to write a bouncy ball.. How hard could that be. This is what I ended up creating.

[Red Bouncing Ball][firstGist]

I have to admit, I had a lot of help from Evan. I had trouble understanding how 
data was flowing. He made these diagrams:

```
add: Int -> Int -> Int
add a b = a + b
```

At first, these didn't make any sense. However, talking with Evan and reading the [Haskell Introduction][http://www.haskell.org/haskellwiki/Introduction] page definitely helped. First, parenthesis are not needed to pass in arguments. They represent a grouping. So here, `add` takes in two arguments, `a` and `b`. `=` here doesn't mean assignment. It represents a definition of a function.

With functional programming, you have to think about how the data flows through the pipeline rather than saving state through variables. In the `add` method, you can very well give it just one argument. This will just return an incomplete function rather than an `Int`. 

[elm]: http://www.elm-lang.org
[gist]: http://share-elm.com/sprout/53173b34e4b0f7cc0dd4e12b
[firstGist]: http://share-elm.com/sprout/5317940ee4b0f7cc0dd4e16d
[try]: http://elm-lang.org/try
[mario]: http://elm-lang.org/edit/examples/Intermediate/Mario.elm