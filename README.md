# clltz
Empiric execution of Collatz Conjecture, with the chance of giving n number or going indefinitely.

Collatz Conjecture describes that any given n natural number following this instructions: if its even, n/2; if its odd, 3n+1, will end up in a 4, 2, 1 loop.

$$f(n) = \begin{cases} \frac{n}{2} 
& \text{if } n \equiv 0 \pmod{2}, \\ 3n+1 
& \text{if } n \equiv 1 \pmod{2}. \end{cases}$$
