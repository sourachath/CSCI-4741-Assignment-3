# Caesar Cipher

- **Author**: Sourachath Dennis Rojanaphong
- **Class**: CSCI 4741
- **Assignment #**: 03
- **Due Date**: 13 Nov 2023 @ 2359

## Objective
The aim of this assignment is to delve deeper into various cybersecurity concepts and practices. The Caesar Cipher is a type of substitution cipher in which each letter of the plaintext is shifted a specific number of positions down the alphabet. The implementation of the Caesar Cipher is implemented using *Python 3.11.5*.

## Overview
Below is a brief overview of the Caesar Cipher implementation

```
Encryption:
    P = plaintext
    k = key
    e = encrypted_text

    for each character 'c' in 'P':
        if 'c' is an alphabetic character:
            'e' += shift 'c' by 'k' right-positions in the alphabet
    return 'e'
```

```
Decryption:
    C = ciphertext
    k = key
    d = decrypted_text

    for each character 'c' in 'C':
        if 'c' is an alphabetic character:
            'd' += shift 'c' by 'k' left-positions in the alphabet
    return 'd'
```

## Prerequitsites
There are no external libraries or modules implemented.

## Source Files
1. main.py
    - The driver script to run the program
2. caesar.py
    - Contains the Caesar Cipher implementation

## Usage
Execute the following to run the program:
```bash
python main.py
```

You will be prompted with an input prompt asking to select various options. Throughout the usage of the running program, various input prompts will be asked accordingly. Follow the prompts as instructed.

## Case Study Evaluation

### Introduction and Background
***Caesar Cipher*** is one of the simplest and most widely known encryption techniques in cryptography. It is a cipher that uses the substitution method in which each letter in a plaintext is replaced by a letter some fixed number of positions down the alphabet. The method is named so by the famous Julius Caesar, who used it in his private correspondence. The cipher still has uses in modern-day applications such as in the [ROT13](https://en.wikipedia.org/wiki/ROT13) system.

### Security Analysis
Despite its historical significance and simplicity, the cipher is known to possess several security vulnerabilities that hinder its uses for secure communications in modern cryptographic contexts.

One of the primary weaknesses of the Cipher is its susceptibility to [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack). Though the number of shifts can be greater than 25 (one less the total number of alphabetic characters in the case of a standard English alphabet), it is limited to only 25 since a shift of 26 is equivalent to a shift of 0. Thus, the shift resets thereafter 25. An attacker can easily test all possible key combinations to decipher the encrypted text. With only 25 possible shifts, a ciphertext can easily spell out a plaintext.

Additionally, the cipher is highly vulnerable to [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis). It is a cryptographic analysis technique that studies the frequency of letters or groups of letters in a ciphertext. In the case of the English languages, the frequency distribution of letters follows a distinct pattern and attacks can easily leverage this knowledge to decipher the encrypted message by analyzing the frequency of letters and identify common patterns.

Though the cipher has historical significance and educational value, it is limited to security features and susceptibility to various attacks, rendering it inadequate for ensuring confidentiality and integrity of sensitive information in cryptographic applications.

### Advantages
Though the cipher is simplistic in its nature, it is ideal in introducing ideas of cryptographic concepts. It is a straightforward encryption-decryption process involving simple shifts of characters in a plaintext by a fixed number of positions. This is clear in understanding the fundamental principles of substitution ciphers. It requires minimal computations and makes the cipher ideal for lightweight encryption applications, such as in an educational setting or informal communications where risk of sophisticated attacks is low to none.

Given the limitations of the cipher, it necessitates the adoption of more advanced encryption techniques such as symmetric-key/asymmetric-key algorithms like AES and RSA.

### Conclusion and Future Implications
The cipher is mainly emphasized as an educational tool for introducing fundamental cryptographic concepts. The simplicity of the cipher makes it an accessible starting point for learners to understand and grasp the basics of encryption and decryption processes.

Despite its vulnerabilities, the cipher has been used in scenarios where lightweight and easily implementable encryption method is sufficient.

The limitations of the cipher acknowledges its historical significance and educational value, ensuring the security required for modern communication and data protection.
