---
title: "Knot equivalence—why ambient isotopy?"
slug: knot-equivalence
---

### A not-completely-accurate description
<!--start-->
A couple years ago I participated in a knot theory research project for undergraduates, and I remember learning that the "right notion" of equivalence for knots was ambient isotopy. I didn't know what this meant, but I was told it was equivalent to using Reidemeister moves, which were much easier to work with. 

A week ago I was giving a lay description of knot theory and I think I said something along the lines of, "we want to know what all the different knots are, where we think of two knots as being the same if you can deform one into the other without doing any cutting or passing the knot through itself." Thinking about it later I'm realizing I was actually describing knots up to *isotopy*, and it took me a while to figure out what I was missing. I had never gone back and investigated this question of isotopy vs ambient isotopy before, so that's what I'd like to share here.
<!--end-->

### How do we think about knots, mathematically?

Now, had the person I was talking to pressed me on this, perhaps wondering what it meant to "deform one knot into the other," I would have added the adjective "continuous" to my description somewhere and I might have revealed that we technically think of knots as *functions* into a space rather than subsets of a space so that we can define certain families of functions that transform one knot into another. I didn't get the sense the person I was talking to was actually all that interested in the technical details, but here they are: 

**Definition:** A *knot* is an embedding $K: S^1 \to \R^3$ (or with codomain $S^3$). 

<center><img style="max-width: 700px; width:60%" src="/assets/post_photos/8-17-24-knot-as-embedding.png" height="auto"></center>

**Definition:** An isotopy between two embeddings $g$ and $h$ from $X$ to $Y$ is a continuous map $F: X \times [0,1] \to Y$ such that $F_0 = g(x)$, $F_1 = h(x)$, and $F_t$ is always an embedding. In other words, an isotopy is a homotopy through embeddings.

If we think of the parameter $t \in [0,1]$ as meaning time of some sort and then visualize an isotopy as the image of one knot transforming over time into the image of another knot:

<center><img style="max-width: 700px; width:80%" src="/assets/post_photos/8-17-24-isotopy-example.png" height="auto"></center>

In the first step of the above sequence, we picture the left strand being dragged up and over the rest of the knot, since the condition that $F_t$ always be an embedding means in particular that it's injective—the knot can't pass through itself during this transformation. The fact that an isotopy prevents this makes it seem like a pretty good notion for equivalence. The continuity prevents any cutting, and the embedding requirement prevents passing strands through other strands. What's wrong?

### All (tame) knots are isotopic

Our goal is to translate the intuitive understanding we have from working with rope and string into more precise mathematics, but there's one operation we can't do in real life to simplify knots that isotopy still allows. I used to knit and crochet a lot when I was younger, and when a tangled up bit of yarn had exhausted my patience I was always fighting the urge to grab ends of the tangle and just yank, maybe in the hope it would cause the tangle to simply disappear. This would make the knot I was looking at smaller and harder to untangle, but it never made it go away completely. In the real world, I was unable to shrink my tangles down to a point, and this is a reality a good notion of knot equivalence should capture! The problem with isotopy is that the shrinking process is a continuous one, and it never involves creating any self-intersections, so isotopy is fine with it. Here's a picture of an isotopy between the (right-handed) trefoil and the unknot:

<center><img style="max-width: 700px; width:80%" src="/assets/post_photos/8-17-24-trefoil-unknot-isotopy.png" height="auto"></center>

If you prefer an actual animation with something that can draw accurately in 3d, I've put together a (somewhat inelegant) [Desmos animation](https://www.desmos.com/3d/g0ksmevdia), and you can check through it there to see that all the functions involved really are continuous!

### What to do instead

One of the things you'll notice about the Desmos animation is that the functions I've used are not *smooth*. Requiring isotopies be smooth instead of merely continuous is one possible fix, but we can avoid any differential topology by using *ambient* isotopy. Consider the two embeddings of $S^1$ in $\R^2$ shown below. Say one of them is $g(x) = (\cos(x), 2\sin(x))$ and the other is $h(x) = (2\cos(x), \sin(x))$: 

<center><img style="max-width: 700px; width:60%" src="/assets/post_photos/8-17-24-explicit-params.png" height="auto"></center>

We can picture the first embedding transforming into the second in a few different ways, but I think the easiest isotopy to write down concretely is $F:S^1 \times [0,1] \to \R^2$ given by

$$ F(x,t) = \left( \frac{t + 1}{2} \cos(x), \frac{2 - t}{2} \sin(x) \right). $$

When we have an isotopy like this, we're thinking of the curve moving through the ambient space (in this case $\R^2$) without disturbing the ambient space in any way. Another idea is to think instead about the ambient space itself moving in a continuous way, dragging the curve along with it from some starting point to some ending point. 

**Definition:** If we have embeddings $g$ and $h$ of some space $X$ in some space $Y$, an **ambient isotopy** between $g$ and $h$ is a continuous function $F: Y \times [0,1] \to Y$ such that $F_0$ is the identity on $Y$, $F_1 \circ g = h$, and $F_t$ is always a homeomorphism.

Note here that the condition that $F_0$ be the identity means $F_0 \circ g = g$ and we still have some nice symmetry. The way to read this is that we're distorting the ambient space $Y$ via a continuous family of homeomorphisms so that what was the image of $g$ at time $t = 0$ becomes the image of $h$ at time $t = 1$. 

In our example above if we want $F_1$ to take the first embedding to the second, we need $F_1$ to be a homeomorphism of $\R^2$ that stretches things out in the $x$-direction and compresses things in the $y$-direction by a factor of 2, so $F_1(a,b) = (2a, (1/2)b)$. We also want that $F_0: \R^2 \to \R^2$ is the identity, meaning $F_0(a,b) = (a,b)$. Finally, we want a homotopy between these through homeomorphisms, so we could take 

$$ F_t(a,b) = \left( (t + 1) a, \frac{2 - t}{2} b \right). $$

### Ambient isotopic implies isotopic

We've said already that isotopy itself captures some good physical intuition about when knots should be equivalent, and indeed, we get to keep these with ambient isotopy: if $F: \R^3 \times [0,1] \to \R^3$ is an ambient isotopy between knots $K$ and $K'$, then $F(K(x),t)$ is an isotopy between $K$ and $K'$, which we check as follows: 

- $F(K(x),0)$ is the identity $F(x,0) = \text{Id}_{\R^3}$ composed with $K(x)$, so $F(K(x),0) = K(x)$.
- $F(K(x),1)$ is $K'(x)$ by definition (earlier we wrote this using the notation $F_1 \circ g = h$, now $g = K$ and $h = K'$).
- $F(x,t)$ is always a homeomorphism, so composing this with the embedding $K$ means $F(K(x),t)$ is always an embedding.

$$ $$

So what this tells us is that the existence of an ambient isotopy implies the existence of an isotopy, and we see that ambient isotopy is a stronger notion. Indeed, in our example with embeddings of $S^1$ in $\R^2$, the isotopy we get from the ambient isotopy we defined is exactly the first isotopy we gave. 

### What else can ambient isotopy do?

Isotopy wasn't the right notion of equivalence because it allowed the shrinking of a knotted region to a single point. Ambient isotopy is great because it doesn't allow this! The shrinking of a knotted region identifies points into a single point, which cannot happen when $F_1$ is a homeomorphism, since in particular it is injective. Because this is just a property of $F_1$, I've also seen knot equivalence defined where $K$ is in the same class as $K'$ if there is a homeomorphism $F: \R^3 \to \R^3$ with $F \circ K = K'$. However, this is less common, and ambient isotopy does have an advantage. In real life, mirroring is not an operation we can perform, but it is a valid homeomorphism. Requiring the homeomorphism to be isotopic to the identity ensures it is orientation-preserving, and so taking ambient isotopy fixes this potential issue as well. 

Ambient isotopy best captures what we can do with a physical knot tied in some actual string, so ambient isotopy it is! 






