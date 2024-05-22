---
title: "What is Elliptic Curve Cryptography?"
slug: ecc explainer
date: 2021-07-05T18:07:46-04:00
---

The following is an assignment for a writing class and is aimed at a non-math audience. 

### Elliptic curves

<!--start-->

You might not have heard of elliptic curves before, but odds are you've used them without knowing it to securely pass information back and forth. Elliptic curves are abstract mathematical objects, and in the same way that you probably learned to represent equations like $y = x^2$ or $x^2 + y^2 = 4$ as curves in the $xy$ plane in high school, we can graph elliptic curves. These curves have the form $y^2 = x^3 + ax + b$ where $a$ and $b$ are numbers we can choose. When graphed, they look something like the following: 

<!--end-->

<center><img style="max-width: 700px; width:90%" src="/assets/post_photos/ecc_examples.png" height="auto"></center>

These curves have many interesting properties and mathematicians have studied them for a long time, but what on earth do they have to do with the ciphers and codes used to secure information? You might not be familiar with many ideas from cryptography, the study of ciphers and information security, but if you ever learned about simple ciphers in school, passed codes back and forth with your friends, or even if you've just whispered to someone, you already have some idea of what cryptography is all about. 

### The basic idea of cryptography

You might have heard before of something called a shift cipher, also known as a Caesar cipher, in which someone wanting to encrypt a message simply takes each letter in the message and shifts it by a fixed amount, say, by three letters. In the message “message,” for example, the letter ‘m’ would be shifted by three letters to become ‘p,’ and the letter ‘e’ would be shifted by three letters to become ‘h,’ so the full message becomes “phvvdjh.” In order to decrypt this message, the intended recipient needs to know how much the sender shifted each letter in order to do the reverse.

The shift cipher is very simple, but it manages to capture the fundamental idea of **symmetric** systems in cryptography. In these symmetric cryptosystems, both parties communicating have some kind of shared secret, some information only they know that they can use to encrypt and decrypt messages. One party uses this secret key to turn a message into something that looks like gibberish and sends it to another party with the key. The idea is that anyone other than the intended recipient won't be able to turn the gibberish back into English. This is the motivation behind the simple shift cipher, which isn't secure at all, and it's also the motivation behind very sophisticated and secure ciphers, like the Advanced Encryption Standard (AES) used by governments and businesses all over the world. 

### Asymmetric systems and one-way functions

One potential issue with symmetric systems is this need for a shared secret key---after all, how would two parties without secure means of communication come to agree on a key to use? Suppose two people, Alice and Bob, have begun to suspect that someone is reading their messages and would like to start encrypting their communications using a symmetric cipher like AES. To do this, they need to have a shared secret---a large number that only the two of them know. Now suppose that Alice and Bob live in the same town and would like to meet up at a coffee shop to discuss this large number to use. Unfortunately, they realize that throughout their conversation, some eavesdropper nearby has been taking notes. Very suspicious. How might they have avoided this scenario in which they need to pass this large number back and forth?

One answer comes from **asymmetric** cryptosystems, in which a public key that potentially anyone could access is used in combination with users' private keys. First proposed in the mid 70s, these systems can provide a means for two parties to arrive at a shared key without ever having to exchange any sensitive information over an insecure channel (that is, Alice and Bob never have to share their large number when they meet up at the coffee shop). To do this, asymmetric systems rely on **one-way** functions. These aren’t necessarily functions in the way that $y = x^2$ is a function, but rather, these are mathematical procedures that are relatively easy to perform in one direction, but so difficult to perform in reverse that it would take even the most powerful computers longer than the 14 billion years our universe has existed to do it. This is where elliptic curves come into play--they provide an extremely useful one-way function that is the basis of many efficient and secure algorithms that can solve the problem Alice and Bob encountered trying to agree on keys to use for symmetric systems. Before we can discuss these algorithms, however, we need to learn a little bit about operations on the points of an elliptic curve.

### Adding and multiplying points on an elliptic curve

When we add, we take two numbers, put them together, and get a third number. This is also true of elliptic curve point addition---it is a way of taking two points on a curve and obtaining a third one. An elliptic curve has the form $y^2 = x^3 + ax + b$, and so points on the curve can be thought of as ordered pairs $(x,y)$ satisfying this equation. When we take $x$ and $y$ to come from the real numbers, there is a very nice geometric way to describe point addition, illustrated in Figure 3: 

<center><img style="padding:0px 0px 15px 0px; max-width: 400px; width:80%" src="/assets/post_photos/ecc_addition.png" height="auto"></center> 

Given two points, $P$ and $Q$, we can draw a line through them (the solid line shown in green). Due to a nice property of elliptic curves, this line is guaranteed to hit another point on the curve somewhere, and to figure out where the point $P + Q$ is, we reflect this point of intersection across the $x$-axis (shown with the dashed green line). As shown in the figure, the solid green line hits the curve somewhere below the $x$-axis, and so we define the point $P + Q$ to be the point with the same $x$-coordinate, only above the $x$-axis. Like the more familiar addition of numbers, the order we add points in doesn't matter: $P + Q$ is always the same as $Q + P$.

We can also multiply a point on an elliptic curve by some integer $n$, and we think of the point $nP$ as being the result of adding the point $P$ to itself $n$ times. But here, your alarm bells should be going off: we've defined addition using a line drawn through two *distinct* points $P$ and $Q$---what line should we draw when we're adding $P$ to itself? The answer is that we take the line tangent to $P$, and then use the same procedure from there. The process of finding the point $2P$ from $P$ is shown in Figure 4:

<center><img style="max-width: 420px; width:90%" src="/assets/post_photos/ecc_doubling.png" height=auto></center> 

In order to figure out where the point $nP$ is, we just need to find $2P$, and then add $P$ to it to get $3P$. Then we'll add $P$ again to get $4P$, and we'll continue all the way up to $nP$. As it turns out, multiplying a point $P$ by an integer $n$ is pretty easy for a computer to do. However, if one is given two points $P$ and $Q$, knowing that $Q$ is a multiple of $P$ (that is, $Q = nP$ for some $n$), it is very difficult even for a computer to figure out what $n$ is in a reasonable amount of time. This, at last, is almost our one-way function.

### Elliptic curves over finite fields

The reason this isn't quite a good enough one-way function for practical use is that if we let our point coordinates $x$ and $y$ come from the real numbers, there are going to be infinitely many points on our curve, the same way there are infinitely many numbers on the number line. If we can, we'd like to restrict ourselves to working with $x$ and $y$ that come from the integers, maybe integers no larger than some number $p$. This restriction would mean that there would be finitely many points (which is great news for our computers), and yet, there would still be so many points that it would be practically impossible for someone to guess the answer to our one-way function, assuming we choose $p$ to be fairly large. If in the process of adding or multiplying numbers we get a result greater than or equal to $p$, we simply subtract $p$ from the result until we have a number between $0$ and $p-1$, inclusive.

The set of numbers from $0$ to $p-1$, together with this kind of arithmetic forms an object called a **finite field**, commonly denoted by $\mathbb{F}\_p$. We can think of arithmetic in a finite field as working analogously to how we use clocks. On a clock face, once we reach $12$, we wrap back around and then start counting again at $1$ instead of moving on to $13$. If it is eight o'clock now and we then wait seven hours, it will be three o'clock, and in a finite field $\mathbb{F}\_p$, if we add the elements $p - 2$ and $5$, we get the element $p + 3$. This is too large, so we subtract $p$ (we wrap back around) and end up at $3$.

<center><img style="max-width: 400px; width:90%" src="/assets/post_photos/ecc_finite_field.png" height=auto></center> 

As it turns out, arithmetic in a finite field otherwise functions just like normal, and we can return to elliptic curves. Now we will be considering curves defined by equations of the form $y^2 = x^3 + ax + b$, where the numbers $x$, $y$, $a$, and $b$ are all integers in the range from $0$ to $p-1$ for some prime number $p$, that is, they belong to the finite field $\mathbb{F}\_p$. A downside of restricting ourselves to using the elements of $\mathbb{F}\_p$ is that the nice geometric interpretation of elliptic curve point addition and multiplication no longer works. However, just as an elliptic curve can be represented as both an equation and a graph, there is an algebraic interpretation of point addition that can be derived from the geometric interpretation. We won't get into the equations here (though check out the further reading section if you're interested), but the key point is that they apply equally all cases, whether we use points with coordinates from the real numbers or points with coordinates from $\mathbb{F}\_p$. Once we have a well-defined way to add and multiply points on elliptic curves over finite fields, we're ready to go---the one-way function that we need is still the process of multiplying a point by an integer $n$. It remains easy to do in one direction, but very hard to do in reverse. 

### The Diffie-Hellman key exchange protocol

We are now at long last in a position to understand how elliptic curves over finite fields can give Alice and Bob a way to arrive at a shared key without simply saying it out loud and allowing the eavesdropper to overhear. To do this, Alice and Bob will go ahead an meet at the coffee shop, but this time, instead of agreeing on a large number, they will agree on a curve, a finite field $\mathbb{F}\_p$ to take point coordinates from, a point $P$, and a coordinate, $x$ or $y$. All of this information can be made public (that is, it's totally fine if the eavesdropper hears). Suppose they choose the curve $y^2 = x^3 + 970x + 1$ over the field $\mathbb{F}\_{971}$ along with the point $P = (478, 164)$. Notice that all the numbers that appear here are less than $971$, which means they come from the field $\mathbb{F}\_{971}$.  Suppose they also choose the $x$-coordinate (we'll see what this means in a moment).

Once they have their public information together (curve, field, point, and coordinate), Alice and Bob will each choose an integer to be their private key. As the name suggests, this is the information Alice and Bob need to keep to themselves. Suppose that, after leaving the coffee shop, Alice chooses $a = 13$ and Bob chooses $b = 201$. Using the algebraic version of the point multiplication we described earlier, Alice will find the point $K_A$ and Bob will find the point $K_B$ where 

$$\begin{gather*}
K_A = a \cdot P = 13 \cdot (478, 164) = (105, 846) \\
K_B = b \cdot P = 201 \cdot (478, 164) = (505, 134).
\end{gather*}$$

At their next meeting, Alice and Bob will exchange these points, again without any concern for potential eavesdroppers. After returning home again, Alice can find a new point $K$ by multiplying the point she received from Bob by her secret key, and Bob can find the same point by multiplying the point he received from Alice by his secret key: 

$$\begin{gather*}
a \cdot K_B = 13 \cdot (505, 134) = (551, 591) = K \\
b \cdot K_A = 201 \cdot (105, 846) = (551, 591) = K.
\end{gather*}$$

Now Alice and Bob both know the point $K = a \cdot b \cdot P$. Why does this matter? If you still remember, the whole point of doing this was to arrive at a large number that they can use as their secret key for some symmetric system like AES, and now they have a point $K$. But a point is really nothing but two numbers, an $x$-coordinate and a $y$-coordinate, and at their first meeting when Alice and Bob agreed on a curve, field, and point to use for this process, they also chose the $x$-coordinate, and this is why: it's the last piece of information they needed to agree on to get to a shared secret. Once both Alice and Bob have arrived at the point $K$, they simply begin encrypting their messages using the point's $x$-coordinate, $551$, as their shared key.

When Alice and Bob first met, before they knew about elliptic curves and the Diffie-Hellman key-exchange protocol, an eavesdropper learned what their secret key was. This time, the eavesdropper learned the curve being used, the field being used, the points $P$, $K_A$, and $K_B$, and that Alice and Bob would be using the $x$-coordinate of the point $K$. Crucially, the eavesdropper did not learn the point $K$, or either of the secret keys used to find it. While $K_A$ and $K_B$ are multiples of $P$, figuring out what numbers $P$ was multiplied by (the secret keys) is very difficult---this is why our one-way function is so useful! In order for someone to figure out the shared key Bob and Alice have arrived at, they would need to know someone's secret key, and the only way to know that is to do our one-way function in reverse.

Granted, if Alice and Bob actually used this setup with $p = 971$, their communication wouldn't be very secure. The one-way function only presents difficulties if the number $p$ is large enough, and something with only three digits just doesn't cut it. For an example of a number large enough to be secure, we can look to Bitcoin. Bitcoin uses a system slightly different from the one Alice and Bob used here, but it's still based on elliptic curves, and for a rough idea of how large $p$ ought to be, consider that Bitcoin uses the curve $y^2 = x^3 + 7$ over the field $\mathbb{F}\_p$ where $p = 2^{256} - 2^{32} - 977$, a number with 77 digits.

### Further reading

This procedure in which two parties arrive at a shared key using elliptic curves is just one example of an elliptic curve cryptosystem, and such systems continue to become more widely used. There are also other commonly used asymmetric cryptosystems that rely on one-way functions that aren't quite as difficult as the one-way function elliptic curves have, so to use them, you need numbers much much larger than Bitcoin's $2^{256} - 2^{32} - 977$ and this can slow things down significantly. If you'd like to delve into the math and learn more about why this is the case, check out [Victor Miller's paper](https://link.springer.com/content/pdf/10.1007%2F3-540-39799-X_31.pdf) in which he originally suggested using elliptic curves for cryptography. If you'd like to read more about the history of elliptic curves in general, I recommend the paper  [*Why ellipses are not elliptic curves*](https://www.maa.org/sites/default/files/pdf/upload_library/2/Rice-2013.pdf). For more on cryptography in general, I suggest [Trappe and Washington's text](https://books.google.com/books/about/Introduction_to_Cryptography.html?id=PFDIQgAACAAJ), which includes a chapter on elliptic curves.