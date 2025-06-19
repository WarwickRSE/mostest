# Hints and 'Solutions' for the quadratic solver

In the case of a quadratic solver which explicitly claims to handle imaginary and repeated
roots, what things can we check? Here are some ideas:

- Known results which you can write out - e.g. by expanding (x-2)(x+2) 
- Ditto for a repeated root
- You could do this for an imaginary root too. Even though there's a higher chance of making a mistake in the expansion, you're unlikely to make the same mistake in the code
- Make sure to check real coefficients as well as integers
- Try and check with big and small values too - for instance take the integer case above and multiply by 10^-6 or by 10^6
- In this case, you can check by back-substitution and thus access the entire possible space of randomly picked coefficients! Since the code claims to handle all cases you don't need to restrict to ones with real roots
- Don't forget to check for coefficients with value 0 (bearing in mind that my code can't handle a=0...)